import sys
import argparse
from autoreviewufzvs import (
    concatenate_xls,
    ordering,
    script_highlight,
    script_highlight_excel,
)


def main():
    # Create the argument parser
    parser = argparse.ArgumentParser(
        description="Autoreview - A package for automating operations on Excel files."
    )
    # Add an argument to specify the module to execute
    parser.add_argument(
        "module",
        type=str,
        help="Name of the module to run. Choose from: concatenate_xls, ordering, script_highlight, script_highlight_excel.",
    )

    # Parse command line arguments
    args = parser.parse_args()

    # Check the specified module and execute it
    if args.module == "concatenate_xls":
        concatenate_xls.main()
    elif args.module == "ordering":
        ordering.main()
    elif args.module == "script_highlight":
        script_highlight.main()
    elif args.module == "script_highlight_excel":
        script_highlight_excel.main()
    else:
        print(f"Unknown module '{args.module}'. Use -h to see available modules.")
        sys.exit(1)


if __name__ == "__main__":
    main()
