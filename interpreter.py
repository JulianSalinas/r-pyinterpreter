## ---------------------------------------------------------------------------------------------------------------------

from environment import *
import math
from types import NoneType
from os import _exit
sys.path.insert(0, '../..')

## ---------------------------------------------------------------------------------------------------------------------

class Interpreter(Environment):

    def __init__(self, parser, lexer):
        Environment.__init__(self)
        self.parser = parser
        self.lexer = lexer
        self.show_result = False

## ---------------------------------------------------------------------------------------------------------------------

    def exec_program(self, program, debug=False, show_result=False):
        try:
            self.show_result = show_result
            if debug: print_green(str(program))
            result = self.exec_expressions(program[1])
            if result and self.show_result:
                print_green(self.translate(result))
        except ( SystemExit, SystemError, RuntimeError):
            _exit(0)
        except: pass

## ---------------------------------------------------------------------------------------------------------------------

    def exec_expressions(self, exprlist):
        result = None
        for expr in exprlist:
            result = self.exec_expression(expr)
        return result

## ---------------------------------------------------------------------------------------------------------------------

    def exec_expression(self, args):

        if isinstance(args, list): return args

        function = self.lookup(args[0])
        if function: return self.exec_user_function(function, args[1])

        function = self.find_function(args[0])
        if function: return function(args[1])

        self.exit("Funcion '"+ args[0] +"' indefinida")

## ---------------------------------------------------------------------------------------------------------------------

    def exec_symbol(self, arg):
        val = self.lookup(arg)
        if not val:
            self.exit("El simbolo '" + arg + "' no existe en este alcance")
        return val

## ---------------------------------------------------------------------------------------------------------------------

    def exec_user_function(self, function, function_args):
        self.push_scope()
        self.check_arguments_size(function_args, function[0])
        self.link_arguments(function_args, function[0])
        self.exec_expression(function[1])
        self.pop_scope()
        return self.pop_result()

## ---------------------------------------------------------------------------------------------------------------------

    def check_arguments_size(self, function_args, function_params):
        if len(function_args) != len(function_params):
            self.exit("La cantidad de parametros no coincide con la cantidad de argumentos")

## ---------------------------------------------------------------------------------------------------------------------

    def link_arguments(self, function_args, function_params):
        for i in range(0, len(function_params)):
            symbol_name = function_params[i][1]
            arg = self.exec_expression(function_args[i])
            self.define(symbol_name, arg)

## ---------------------------------------------------------------------------------------------------------------------

    def exec_assign(self, args):
        expr = self.exec_expression(args[1])
        self.define(args[0], expr[:])

## ---------------------------------------------------------------------------------------------------------------------

    def exec_if(self, args):
        condition = self.exec_expression(args[0])[0]
        if condition: self.exec_expression(args[1])
        elif args[2]: self.exec_expression(args[2])

## ---------------------------------------------------------------------------------------------------------------------

    def exec_while(self, args):
        while self.exec_expression(args[0])[0]:
            self.exec_expression(args[1])

## ---------------------------------------------------------------------------------------------------------------------

    def exec_for(self, args):
        list_var = self.exec_expression(args[1])
        for i in list_var:
            self.define(args[0][1], [i])
            self.exec_expression(args[2])

## ---------------------------------------------------------------------------------------------------------------------

    def translate(self, var):
        if var: return self.translate_make_string(var)
        else: return 'NULO'

## ---------------------------------------------------------------------------------------------------------------------

    def translate_make_string(self, var):
        result = ""
        for i in range(0, len(var)):
            if i == 0: result += "[" + str(i + 1) + "] "
            elif i % 20 == 0 : result += "\n[" + str(i + 1) + "] "
            result += self.translate_element(var[i]) + " "
        return result

## ---------------------------------------------------------------------------------------------------------------------

    def translate_element(self, element):
        if type(element) == bool: return 'V' if element else 'F'
        elif type(element) == float: return self.translate_element_case_float(element)
        elif type(element) == str: return self.translate_element_case_string(element)
        elif type(element) == NoneType: return 'NULO'
        return str(element)

## ---------------------------------------------------------------------------------------------------------------------

    def translate_element_case_float(self, element):
        if math.isinf(element): return '-Inf' if element < 0 else 'Inf'
        elif math.isnan(element): return 'NeN'
        elif element - int(element) == 0: return str(int(element))
        return str(element)

## ---------------------------------------------------------------------------------------------------------------------

    def translate_element_case_string(self, element):
        if element == 'True': return '\'V\''
        elif element == 'False': return '\'F\''
        elif element == 'None': return '\'NULO\''
        return "'" + element + "'"

## ---------------------------------------------------------------------------------------------------------------------



