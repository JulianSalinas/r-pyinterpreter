## ---------------------------------------------------------------------------------------------------------------------

from parser import *
from rinterpreter import *
from datetime import datetime
sys.path.insert(0, '../..')

## ---------------------------------------------------------------------------------------------------------------------
##                                              Programa principal
## ---------------------------------------------------------------------------------------------------------------------

def R(filename):

    lexer = RLexer(filename)
    parser = RParser(lexer)
    interpreter = RInterpreter(parser, lexer.clone())
	
    if filename:
        program = parser.parse()
        interpreter.exec_program(program)

    interpreter.exec_shell()

## ---------------------------------------------------------------------------------------------------------------------

if __name__ == "__main__":
    print_green(str(datetime.now())+" EJECUTANDO R")
    if len(sys.argv) == 1: R(None)
    elif len(sys.argv) == 2: R(sys.argv[1])

## ---------------------------------------------------------------------------------------------------------------------
