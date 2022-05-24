import os
import sys
from antlr4 import *
from c_antlr.CLexer import CLexer
from c_antlr.CListener import CListener
from c_antlr.CParser import CParser


if __name__ == "__main__":
    # Check for filepath argument
    if len(sys.argv) == 1:
        print("Usage: python c2py <filepath>")
        exit(1)

    # Prepare filepath and filename
    filepath = sys.argv[1]
    filename = filepath[filepath.rfind("/") + 1:]

    # Check if file exists
    if not os.path.isfile(filepath):
        print(f'File "{filepath}" does not exist')
        exit(1)

    # Run lexer and parser
    input_stream = FileStream(filepath)
    lexer = CLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = CParser(stream)
    tree = parser.compilationUnit()

    # Save output to file
    if not os.path.exists("output"):
        os.makedirs("output")
    f = open(f"output/{filename}.tree", "w")
    f.write(tree.toStringTree(recog=parser))
    f.close()
    print(f"Saved tree to output/{filename}.tree")
