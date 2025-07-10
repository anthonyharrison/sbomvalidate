# Copyright (C) 2025 Anthony Harrison
# SPDX-License-Identifier: Apache-2.0

import argparse
import sys
import textwrap
from collections import ChainMap

from lib4sbom.validator import SBOMValidator

from sbomvalidate.version import VERSION

# CLI processing


def main(argv=None):
    argv = argv or sys.argv
    app_name = "sbomvalidate"
    parser = argparse.ArgumentParser(
        prog=app_name,
        description=textwrap.dedent(
            """
            SBOMvalidate validates a SBOM.
            """
        ),
    )
    input_group = parser.add_argument_group("Input")
    input_group.add_argument(
        "-i",
        "--input-file",
        action="store",
        default="",
        help="Name of SBOM file",
    )

    input_group.add_argument(
        "--debug",
        action="store_true",
        default=False,
        help="add debug information",
    )

    parser.add_argument("-V", "--version", action="version", version=VERSION)

    defaults = {
        "input_file": "",
        "debug": False,
    }

    raw_args = parser.parse_args(argv[1:])
    args = {key: value for key, value in vars(raw_args).items() if value}
    args = ChainMap(args, defaults)

    # Validate CLI parameters

    input_file = args["input_file"]

    if input_file == "":
        print("[ERROR] SBOM name must be specified.")
        return -1

    if args["debug"]:
        print("Input file", args["input_file"])

    sbom_validator = SBOMValidator(sbom_type="auto", debug=args["debug"])
    # Load SBOM - will autodetect SBOM type
    valid_sbom = False
    try:
        check = sbom_validator.validate_file(input_file)
        for sbom_type in ["SPDX", "CycloneDX"]:
            if check.get(sbom_type) == "Unknown":
                if args["debug"]:
                    print(
                        f"[INFO] Unable to determine if {input_file} is a valid SBOM: {check}"
                    )
            elif check.get(sbom_type) is False:
                if args["debug"]:
                    print(f"[INFO] {input_file} is not a valid SBOM: {check}")
            elif check.get(sbom_type) is not None:
                if args["debug"]:
                    print(f"[INFO] {input_file} is a valid SBOM: {check}")
                valid_sbom = True

    except FileNotFoundError:
        print(f"[ERROR]{input_file} not found")

    return 0 if valid_sbom else 1


if __name__ == "__main__":
    sys.exit(main())
