from src import FileBuilder
from src import logger
from Parser.Parser import Parser
from Parser.Constructions import Constructions
from pprint import pprint
from argparse import ArgumentParser

def parse_arguments(args_parser = ArgumentParser(prog='PLUTO / TRACO Code Parser',
                                                 description='Parsing code from P/T to CUDA')):
    args_parser.add_argument('-i', '--infile', help='input file name', default='Examples/example1.c')
    args_parser.add_argument('-vf', '--valuesfile', help='file that contains variables', default=None)
    args_parser.add_argument('-o', help='output file')

    return args_parser.parse_args()
#

def test_parser(parser=Parser(parse_arguments().infile)):
    print("RESULT OF PARSING: ")
    for x in parser.readfile().instructions:
        if isinstance(x, Constructions):
            pprint(dict(vars(x))['Constr'])
            if x.Constr.instructions:
                print("====inside for===")
                for ins in x.Constr.instructions:
                    if isinstance(ins, Constructions):
                        pprint(dict(vars(ins))['Constr'])
                    else:
                        print(ins)
                print("====end of for===")
        else:
            print(x)

def test_new_examples():
    # Example 1 - loop2.c
    ps = Parser(r'C:\Users\przem\OneDrive\PycharmProjects\S2_SEM1\Projekt\TRACOParser\Examples\loop2\loop2.c',
                r'C:\Users\przem\OneDrive\PycharmProjects\S2_SEM1\Projekt\TRACOParser\Examples\loop2\values.json')

    _ = ps.readfile()
    print(_.instructions)
    print(_.instructions[0].Constr)
    print(_.instructions[0].Constr.instructions[0])
    print(_.instructions[0].Constr.instructions[0].Constr)
    print(_.instructions[0].Constr.instructions[0].Constr.instructions[0].Constr)
    print(_.instructions[0].Constr.instructions[0].Constr.instructions[0].Constr.instructions[0])

    # Example 2
    ps = Parser(r'C:\Users\przem\OneDrive\PycharmProjects\S2_SEM1\Projekt\TRACOParser\Examples\loop2\loop2.c',
                r'C:\Users\przem\OneDrive\PycharmProjects\S2_SEM1\Projekt\TRACOParser\Examples\loop2\values.json')

# test_new_examples()
# test_parser()

# if __name__ == "__main__":
#     file_name = "Examples/example1.c"
#     # readfile() returns a dict('variables', 'instructions')
#     parsing_phrases = Parser(file_name).readfile()
#     filename = 'main'
#     FileBuilder(parsing_phrases, filename)
