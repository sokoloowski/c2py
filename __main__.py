import os
import sys
from antlr4 import *
from CLexer import CLexer
from CParser import CParser
from CVisitor import CVisitor


def main(filepath):
    input_stream = FileStream(filepath)
    lexer = CLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = CParser(stream)

    tree = parser.compilationUnit()
    visitor = CVisitor()
    return visitor.visit(tree)

if __name__ == "__main__":
    # Check for filepath argument
    if len(sys.argv) == 1:
        print("Usage: python . <filepath>")
        exit(1)

    # Prepare filepath and filename
    filepath = sys.argv[1]
    filename = filepath[filepath.rfind("/") + 1:]

    # Check if file exists
    if not os.path.isfile(filepath):
        print(f'File "{filepath}" does not exist')
        exit(1)

    # Run lexer and parser
    output = main(filepath)

    # Save output to file
    if not os.path.exists("output"):
        os.makedirs("output")
    note = f"# Generated from {filepath} with C2Py"
    f = open(f"output/{filename}.py", "w")
    f.write(f"{note}\n{output}")
    f.close()
    print(f"Saved output to output/{filename}.py")
