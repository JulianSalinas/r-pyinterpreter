## ---------------------------------------------------------------------------------------------------------------------

from util import *
from symtab import *
sys.path.insert(0, '../..')

## ---------------------------------------------------------------------------------------------------------------------

class Environment(object):

## ---------------------------------------------------------------------------------------------------------------------

    def __init__(self):
        self.return_stack = []
        self.return_flag = False
        self.global_symtab = SymbolTable(None)
        self.scopes_stack = [self.global_symtab]

## ---------------------------------------------------------------------------------------------------------------------

    def current_scope(self):
        last_scope = len(self.scopes_stack) - 1
        return self.scopes_stack[last_scope]

## ---------------------------------------------------------------------------------------------------------------------

    def push_scope(self):
        new_scope = SymbolTable(self.current_scope())
        for key, value in self.current_scope().symbols.items():
            new_scope.symbols[key] = value
        self.scopes_stack.append(new_scope)

## ---------------------------------------------------------------------------------------------------------------------

    def pop_scope(self):
        pop = self.scopes_stack.pop()
        scope = self.current_scope().symbols
        for key, value in pop.symbols.items():
            if not scope.__contains__(key): scope[key] = value
        return scope

## ---------------------------------------------------------------------------------------------------------------------

    def push_result(self, result):
        self.return_flag = True
        self.return_stack.append(result)

## ---------------------------------------------------------------------------------------------------------------------

    def pop_result(self):
        if self.return_flag:
            self.return_flag = False
            return self.return_stack.pop()

## ---------------------------------------------------------------------------------------------------------------------

    def define(self, name, content):
        scope = self.current_scope()
        return scope.define(name, content)

## ---------------------------------------------------------------------------------------------------------------------

    def lookup(self, name):
        scope = self.current_scope()
        return scope.lookup(name)

## ---------------------------------------------------------------------------------------------------------------------

    def find_function(self, function_name):
        functions = dir(self)
        if functions.__contains__(function_name):
            return getattr(self, function_name)
        return None

## ---------------------------------------------------------------------------------------------------------------------

    def exit(self, reason):
        print_red(reason)
        sys.exit(1)

## ---------------------------------------------------------------------------------------------------------------------