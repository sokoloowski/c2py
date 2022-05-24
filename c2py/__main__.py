import sys
from antlr4 import *
from c_antlr.CLexer import CLexer
from c_antlr.CListener import CListener
from c_antlr.CParser import CParser


if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("Usage: python c2py <filename>")
        exit(1)

    filepath = sys.argv[1]
    filename = filepath[filepath.rfind("/") + 1:]
    input_stream = FileStream(filepath)
    lexer = CLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = CParser(stream)
    tree = parser.compilationUnit()

    f = open(f"output/{filename}.tree", "w")
    f.write(tree.toStringTree(recog=parser))
    f.close()
    print(f"Saved tree to output/{filename}.tree")
