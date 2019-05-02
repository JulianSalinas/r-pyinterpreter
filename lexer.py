## ---------------------------------------------------------------------------------------------------------------------

import ply.lex as lex
from util import *
sys.path.insert(0, "../..")

## ---------------------------------------------------------------------------------------------------------------------

literals =  [ '+', '-', '*', '/',
              ':', ';', '!', '[',
              ']', '(', ')', '{',
              '}', ',' ]

## ---------------------------------------------------------------------------------------------------------------------

reserved = {
    'si':'IF', 'sino':'ELSE', 'mientras':'WHILE',
    'para':'FOR', 'en':'IN', 'funcion':'FUNCTION',
    'VERDAD':'TRUE', 'FALSO':'FALSE', 'NULO':'NULL_CONST',
    'Inf':'Inf', 'NeN':'NaN', 'ND':'NA'
}


## ---------------------------------------------------------------------------------------------------------------------

tokens = [
    'REAL', 'INT', 'STR_CONST', 'SYMBOL', 'LEFT_ASSIGN',
    'EQ_ASSIGN', 'RIGHT_ASSIGN', 'LBB', 'GT', 'GE', 'LT',
    'LE', 'EQ', 'NE', 'AND', 'OR', 'AND2', 'OR2', 'NLINE',
    'MOD', 'INT_DIV', 'COMMENT', 'POWER'
]

tokens += reserved.values()

## ---------------------------------------------------------------------------------------------------------------------

t_REAL = r'((\.\d+)|(\d+\.\d+))([eE][-+]?\d+)?'
t_STR_CONST = r'(\"[^\"]*\")|(\'[^\']*\')'
t_INT = r'\d+'
t_MOD = r'%%'
t_INT_DIV = r'%/%'
t_POWER = r'(\^)|(\*\*)'
t_LEFT_ASSIGN = r'<-'
t_EQ_ASSIGN = r'='
t_RIGHT_ASSIGN = r'->'
t_LBB = r'\[\['
t_GT = r'>'
t_GE = r'>='
t_LT = r'<'
t_LE = r'<='
t_EQ = r'=='
t_NE = r'!='
t_AND = r'&'
t_OR = r'\|'
t_AND2 = r'&&'
t_OR2 = r'\|\|'
t_ignore_COMMENT = r'\#.*'
t_ignore = ' \t\r'

## ---------------------------------------------------------------------------------------------------------------------

def t_SYMBOL(t):
    r'(\.|[a-zA-Z_])(\.|[a-zA-Z_0-9])*'
    t.type = reserved.get(t.value, 'SYMBOL')
    return t

## ---------------------------------------------------------------------------------------------------------------------

def t_newline(t):
    r'\n'
    t.lexer.lineno += 1
    t.type = "NLINE"
    return t

## ---------------------------------------------------------------------------------------------------------------------

def t_error(t):
    print_red("Caracter ilegal '" + t.value[0] + "' en la linea " + str(t.lineno))
    t.lexer.skip(1)

## ---------------------------------------------------------------------------------------------------------------------

def RLexer(filename=None, debug=False):
    lexer = lex.lex(debug=debug)
    try:
        if filename:
            lexfile = open(filename, 'r')
            lexfile = lexfile.read()
            lexer.input(lexfile)
    except IOError:
        print_red("No se ha podido abrir el archivo")
    return lexer

## ---------------------------------------------------------------------------------------------------------------------
