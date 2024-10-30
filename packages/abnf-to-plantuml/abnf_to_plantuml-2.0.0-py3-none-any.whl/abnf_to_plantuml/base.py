"""Provide base building blocks for the project."""

import abc
from typing import Generic, Iterable, TypeVar, Union

import abnf


class OurRule(abnf.Rule):
    """Represent our ABNF rule list read from a file."""


Parser = Union[
    abnf.Rule,
    abnf.parser.Literal,
    abnf.parser.Concatenation,
    abnf.parser.Option,
    abnf.parser.Alternation,
    abnf.parser.Repetition,
    abnf.parser.Parser,
]

T = TypeVar("T")


class Visitor(Generic[T]):
    """Visit Rules recursively."""

    def visit(self, parser: Parser) -> T:
        """Delegate the visitation of the ``parser``.

        Args:
            parser: The Parser instance to visit.

        """
        if isinstance(parser, abnf.Rule):
            return self.visit_rule(rule=parser)

        elif isinstance(parser, abnf.parser.Literal):
            return self.visit_literal(literal=parser)

        elif isinstance(parser, abnf.parser.Concatenation):
            return self.visit_concatenation(parsers=parser.parsers)

        elif isinstance(parser, abnf.parser.Option):
            return self.visit_option(option=parser)

        elif isinstance(parser, abnf.parser.Alternation):
            return self.visit_alternation(parsers=parser.parsers)

        elif isinstance(parser, abnf.parser.Repetition):
            return self.visit_repetition(repeat=parser.repeat, parser=parser.element)

        else:
            raise NotImplementedError(str(parser))

    @abc.abstractmethod
    def visit_option(self, option: abnf.parser.Option) -> T:
        """
        Visit an option.

        Args:
            option: The Option instance to visit.

        """
        raise NotImplementedError()

    @abc.abstractmethod
    def visit_alternation(self, parsers: Iterable[Parser]) -> T:
        """
        Visit an Alternation.

        Args:
            parsers: The contents of the Alternation visited (i.e. the choices)

        """
        raise NotImplementedError()

    @abc.abstractmethod
    def visit_repetition(self, repeat: abnf.parser.Repeat, parser: Parser) -> T:
        """
        Visit a Repetition.

        Args:
            repeat: A Repeat object with the range of the repetition.
            parser: The contents of the repetition.

        """
        raise NotImplementedError()

    @abc.abstractmethod
    def visit_concatenation(self, parsers: Iterable[Parser]) -> T:
        """
        Visit a Concatenation.

        Args:
            parsers: The sequence of elements that are concatenated.

        """
        raise NotImplementedError()

    @abc.abstractmethod
    def visit_literal(self, literal: abnf.parser.Literal) -> T:
        """
        Visit a Literal element.

        Args:
            literal: The Literal instance to visit.

        """
        raise NotImplementedError()

    @abc.abstractmethod
    def visit_rule(self, rule: abnf.Rule) -> T:
        """
        Visit a Rule.

        Args:
            rule: The Rule to visit.

        """
        raise NotImplementedError()
