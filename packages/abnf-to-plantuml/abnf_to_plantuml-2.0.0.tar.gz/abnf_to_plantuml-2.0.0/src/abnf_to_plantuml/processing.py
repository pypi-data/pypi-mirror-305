import logging
import pathlib
import typing

import abnf
import click
import click_spinner

from abnf_to_plantuml.base import OurRule, Parser, Visitor

logger = logging.getLogger("abnf_to_plantuml")


def process(
    input_path: pathlib.Path, output_path: pathlib.Path, include_std_rules: bool
) -> int:
    """Execute the main processing.

    Args:
        input_path: The path of the file to read from
        output_path: The path of the file to write to (or `stdout` if the path is "-")
        include_std_rules:  include definitions for the RFC 5234 core rules that are used.

    Returns:
        int: 0, if success, 1 if error.

    """

    # We in-line abnf.parser.Rule.from_file and adapt it to be more robust to different
    # line endings.

    text = input_path.read_text(encoding="utf-8")

    # Enforce CRLF line endings
    text = text.replace("\r", "")

    if not text.endswith("\n"):
        text = text + "\n"

    text = text.replace("\n", "\r\n")

    with click_spinner.spinner():
        try:
            node = abnf.parser.ABNFGrammarRule("rulelist").parse_all(text)
            visitor = abnf.parser.ABNFGrammarNodeVisitor(rule_cls=OurRule)
            visitor.visit(node)
        except abnf.ParseError as err:
            text = input_path.read_text()
            line = 1
            for i, symbol in enumerate(text):
                if i == err.start:
                    break

                if symbol == "\n":
                    line += 1

            logging.error(
                f"Parsing error at line {line}: {err}:\n\n"
                f"{text[err.start:err.start + 200]!r};\n"
                "did you make sure that the line endings are stored as CRLF?"
            )
            return 1

        except abnf.GrammarError as err:
            logging.error(f"Failed to interpret the grammar: {err}")
            return 1

        for rule in OurRule.rules():
            if not hasattr(rule, "definition"):
                logging.error(f"Unexpected rule without a definition: {rule.name!r}")
                return 1

        our_rules_string = "OurRule({OurRule.name}) contains:\n"
        for rule in OurRule.rules():
            our_rules_string = our_rules_string + f"{rule} = {rule.definition}\n"
        logger.debug(our_rules_string)

        rules_list = OurRule.rules()

        if include_std_rules:
            collector = CoreRuleCollector()
            for rule in rules_list:
                collector.visit(rule)
            extra_rules = sorted(collector.rules_set, key=lambda r: r.name)
            rules_list.extend(extra_rules)

    click.echo("\33[2K")  # Erase the line with the spinner
    generate_output(output_path, rules_list)

    return 0


class CoreRuleCollector(Visitor[None]):
    """Visitor that collects the RFC 5234 rules that are being referenced."""

    expand_rule: bool = True

    def __init__(self) -> None:
        self.rules_set: set[abnf.Rule] = set()

    def visit_rule(self, rule: abnf.Rule) -> None:
        """Visit a Rule.
        Check if the rule is contained in the core rules, if it is, throw it
        into the set (we only need one each, anyhow), and continue parsing.

        Args:
          rule:  the Rule to process.
        """
        std_rule = abnf.Rule.get(rule.name)
        if std_rule:
            self.rules_set.add(std_rule)
        if self.expand_rule:
            self.expand_rule = False
            self.visit(rule.definition)
            self.expand_rule = True

    def visit_literal(self, literal: abnf.parser.Literal) -> None:
        """Visit a literal.
        We are not interested in Literals, and they have no additional parsable content, so we just do nothing.

        Args:
            literal: The Literal to process
        """

    def visit_option(self, option: abnf.parser.Option) -> None:
        """Visit an optional element.
        We don't care about Options but the content might include rules so we continue visiting.

        Args:
          option:  The Option to process.
        """
        self.visit(option.alternation)

    def visit_repetition(self, repeat: abnf.parser.Repeat, parser: Parser) -> None:
        """Visit a repetition element.
        We do not care about Repetitions but the content might have rules so we visit deeper.

        Args:
          repeat:  the specification of the number of repeats.
          parser:  the contents of the repetition.
        """
        self.visit(parser)

    def visit_concatenation(self, parsers: typing.Iterable[Parser]) -> None:
        """Visit a concatenation element.

        Args:
          parsers: The sequence of elements that should be concatenated
        """
        [self.visit(parser) for parser in parsers]

    def visit_alternation(self, parsers: typing.Iterable[Parser]) -> None:
        """Visit an alternation element.

        Args:
          parsers: The sequence of elements that are alternatives
        """
        [self.visit(parser) for parser in parsers]


class StringmakerVisitor(Visitor[str]):
    """Visitor that generate output string."""

    expand_rule: bool = True

    def visit_rule(self, rule: abnf.Rule) -> str:
        """Visit a rule.
        To avoid infinite recursion when encountering a rule inside a definition,
        we use the expand_rule-flag to specify whether we want the full
        definition or just the name. Before visiting a rule definition, the code
        turns off expansion.  It is up to the user to make it True again.

        Args:
          rule:  the Rule to process.

        Returns:
            str:    Either just the name of the rule or a full expansion with
                    name, equals-sign, and parse of definition, depending on
                    the state of the `expand_rule`-flag.
        """
        # For rules defined in RFC 5234, we check abnf.Rule for the definition
        std_rule = abnf.Rule.get(rule.name)
        if std_rule:
            if self.expand_rule:
                self.expand_rule = False
                result = (
                    f"{std_rule.name} = " + self.visit(std_rule.definition) + ";\r\n"
                )
            else:
                result = f"{std_rule.name}"
        else:
            if self.expand_rule:
                self.expand_rule = False
                result = f"{rule.name} = " + self.visit(rule.definition) + ";\r\n"
            else:
                result = f"{rule.name}"
        return result

    def visit_literal(self, literal: abnf.parser.Literal) -> str:
        """Visit a literal.
        Literals can represent both single characters, strings, and character
        ranges.

        Args:
            literal: The Literal to process

        Returns:
            str:    if the Literal is a simple value, return the value inside quotes,
                    if it is a tuple, return an EBNF special sequence with the
                    tuple values separated by an en-dash.
        """
        if isinstance(literal.value, tuple):
            result = f"?{literal.value[0]}–{literal.value[1]}?"  # noqa: RUF001
        else:
            # string
            # Because the value might contain double quotes, we may need to swap the surrounding quote style.
            if '"' in literal.value:
                result = f"'{literal.value}'"
            else:
                result = f'"{literal.value}"'
        return result

    def visit_option(self, option: abnf.parser.Option) -> str:
        """Visit an optional element.
        An optional element is basically a repetition from 0 to 1 but is
        so common that it has special syntax.

        Args:
          option:  The Option to process.

        Returns:
            str:    The parsed value of the contents surrounded by brackets.
        """
        return f"[{self.visit(option.alternation)}]"

    def visit_repetition(self, repeat: abnf.parser.Repeat, parser: Parser) -> str:
        """Visit a repetition element.
        PlantUML's EBNF variant has no way to express general repetition
        so we need to generate prefix sequences of the minimal length if
        it is greater than 1.

        Args:
          repeat:  the specification of the number of repeats.
          parser:  the contents of the repetition.

        Returns:
            str:    Varies, depending on the range limits:
                    [0, ∞]: parsed contents surrounded by braces;
                    [0, 1]: parsed contents surrounded by brackets;
                    [0, n]: n * [parsed contents];
                    [1, ∞]: parsed contents surrounded by braces and with a minus appended;
                    [1, n]: n * {parsed content}-;
                    [n, n]: n * (parsed content);
                    [n, ∞]: n * (parsed content), {parsed content};
                    [n, m]: n * (parsed content), m-n * [parsed content]
        """
        contents = self.visit(parser)
        result = ""  # Just to ensure that the variable always has a value
        if repeat.min == 0:
            # Zero or more
            if repeat.max is None:
                # Infinite max
                result = "{" + contents + "}"
            elif repeat.max == 1:
                # This is essentially an Option so we can use the same notation
                result = "[" + contents + "]"
            else:
                # Specific max.
                result = f"{repeat.max} * [{contents}]"
        elif repeat.min == 1:
            # One or more
            if repeat.max is None:
                # Infinite max
                result = "{" + contents + "}-"
            else:
                # Specific max, i.e. a specific number of repeats
                result = f"{repeat.max} * {{{contents}}}-"
        else:
            # At least two or more.
            # We begin by generating a specific repetition for the minimum.
            result = f"{repeat.min} * ({contents})"
            if repeat.max is None:
                # Infinite max
                # In this case we follow the minimum with a "zero or more" repetition.
                result = result + ", {" + contents + "}"
            elif repeat.min == repeat.max:
                # An exact number of repeats, we don't need to add anything
                pass
            else:
                # Generic case (i.e. "m to n")
                # Here we need to follow with a "zero to (max-min)" repetition.
                # Let's do a sanity check first.
                if (repeat.max - repeat.min) < 0:
                    raise abnf.GrammarError(
                        "Repeat with negative range found: " + str(repeat)
                    )
                result = result + f", {(repeat.max-repeat.min)} * [{contents}]"
        return result

    def visit_concatenation(self, parsers: typing.Iterable[Parser]) -> str:
        """Visit a concatenation element.

        Args:
          parsers: The sequence of elements that should be concatenated

        Returns:
            str:    the parsed result of each element, with commas in between.
        """
        return ", ".join([self.visit(parser) for parser in parsers])

    def visit_alternation(self, parsers: typing.Iterable[Parser]) -> str:
        """Visit an alternation element.

        Args:
          parsers: The sequence of elements that are alternatives

        Returns:
            str:    the parsed result of each element, with pipe-symbols in between.
        """
        return " | ".join([self.visit(parser) for parser in parsers])


def generate_output(
    output_path: pathlib.Path, rules: typing.Iterable[abnf.Rule]
) -> None:
    """Produces output.

    Args:
      output_path: Where to write the result

    """
    output_generator = StringmakerVisitor()
    result = "'Generated by abnf_to_plantuml.\r\n\r\n@startebnf\r\n"

    for rule in rules:
        output_generator.expand_rule = True
        result = result + output_generator.visit(rule)

    result = result + "@endebnf\r\n"

    with click.open_file(output_path, "w") as f:
        f.write(result)
