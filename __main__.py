import os
import sys
from antlr4 import *
from CLexer import CLexer
from CVisitor import CVisitor
from CParser import CParser


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
    input_stream = FileStream(filepath)
    lexer = CLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = CParser(stream)
    tree = parser.compilationUnit()
    visitor = CVisitor()
    output = visitor.visit(tree)
    print(output)

    # # Save output to file
    # if not os.path.exists("output"):
    #     os.makedirs("output")
    # f = open(f"output/{filename}.tree", "w")
    # f.write(tree.toStringTree(recog=parser))
    # f.close()
    # print(f"Saved tree to output/{filename}.tree")
