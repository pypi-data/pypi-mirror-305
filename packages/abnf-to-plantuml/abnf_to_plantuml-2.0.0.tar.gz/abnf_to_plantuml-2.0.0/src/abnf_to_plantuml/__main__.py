# SPDX-FileCopyrightText: 2024-present Paul Reinerfelt <Paul.Reinerfelt@gmail.com>
#
# SPDX-License-Identifier: MIT
import sys

if __name__ == "__main__":
    from abnf_to_plantuml.cli import abnf_to_plantuml

    sys.exit(abnf_to_plantuml())
