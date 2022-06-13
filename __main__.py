import os
import argparse
import autopep8
from antlr4 import *
from CLexer import CLexer
from CParser import CParser
from CVisitor import CVisitor


def translate(filepath):
    input_stream = FileStream(filepath)
    lexer = CLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = CParser(stream)

    tree = parser.compilationUnit()
    visitor = CVisitor()
    return visitor.visit(tree)


def main():
    parser = argparse.ArgumentParser(
        prog="C2Py", description="C2Py is a tool to convert C code to Python code.")
    parser.add_argument("path", metavar="path", type=str,
                        nargs=1, help="path to source code in C")
    parser.add_argument("-o", "--output", metavar="dir", type=str,
                        nargs=1, default=["output"], help="specifies the output directory")
    parser.add_argument("-f", "--format", action="store_true",
                        help="format the output using PEP8 code style")

    args = parser.parse_args()

    # Prepare filepath and filename
    filepath = args.path[0].replace("\\", "/")
    filename = filepath[filepath.rfind("/") + 1:]

    # Check if file exists
    if not os.path.isfile(filepath):
        print(f'File "{filepath}" does not exist')
        exit(1)

    # Run lexer and parser
    print("Translating...")
    output = main(filepath)
    if args.format:
        print("Formatting...")
        output = autopep8.fix_code(output)

    # Save output to file
    if not os.path.exists(args.output[0]):
        os.makedirs(args.output[0])
    note = f"# Generated from {filepath} with C2Py"
    f = open(f"{args.output[0]}/{filename}.py", "w")
    f.write(f"{note}\n{output}")
    f.close()
    print(f"Saved translated code to `{args.output[0]}/{filename}.py`")


if __name__ == "__main__":
    main()
