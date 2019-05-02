## ---------------------------------------------------------------------------------------------------------------------

from __future__ import division
from datetime import datetime
from interpreter import *

## ---------------------------------------------------------------------------------------------------------------------

class RInterpreter(Interpreter):

## ---------------------------------------------------------------------------------------------------------------------

    def __init__(self, parser, lexer):
        Interpreter.__init__(self, parser, lexer)

## ---------------------------------------------------------------------------------------------------------------------

    def exit(self, reason):
        print_red(reason)
        self.exec_shell()

## ---------------------------------------------------------------------------------------------------------------------

    def exec_shell(self):
        while True:
            try: line = raw_input('R >> ')
            except EOFError: break
            if not line: continue
            self.lexer.lineno = 1
            program = self.parser.parse(str(line))
            if program: self.exec_program(program, show_result=True)

## ---------------------------------------------------------------------------------------------------------------------

    def _clean_return_(self, _list):
        cleanResult = [_val for _val in _list if _val is not None]
        if cleanResult == []:
            return [None]
        else:
            return cleanResult

## ---------------------------------------------------------------------------------------------------------------------
##                                    Funciones que puede usar el usuario
## ---------------------------------------------------------------------------------------------------------------------

    def ejecutar(self, args):
        try:
            filename = self.exec_expression(args[0])
            filename = open(filename[0], 'r').read()
            program = self.parser.parse(filename)
            self.exec_program(program, debug=False, show_result=False)
        except IOError:
            print_red("El archivo no existe")

## ---------------------------------------------------------------------------------------------------------------------

    def retornar(self, args):
        variable = args[0]
        value = self.exec_expression(variable)
        self.push_result(value)
        return value

## ---------------------------------------------------------------------------------------------------------------------

    def ls(self, args):
        print_green("\nTabla de simbolos: \n")
        symbols = self.current_scope().symbols
        for i, j in symbols.items():
            print_purple(i + " : ")
            if type(j[0]) == list:
                print("funcion con " + str(len(j[0])) + " parametros\n")
            else:
                print(self.translate(j) + "\n")

## ---------------------------------------------------------------------------------------------------------------------

    def tokens(self, args):
        print_green("Lista de tokens encontrados: ")
        lexer = self.lexer.clone()
        print("Linea\t\tTipo\t\tValor")
        for tok in lexer:
            sys.stdout.write('%d\t\t%s\t\t%r\n' % (tok.lineno, tok.type, tok.value))

## ---------------------------------------------------------------------------------------------------------------------

    def salir(self, args):
        print_green(str(datetime.now()) + " SALIENDO DE R")
        sys.exit(0)

## ---------------------------------------------------------------------------------------------------------------------

    def alertar(self, args):
        print_red(self.traducir(args))

    def informar(self, args):
        print_blue(self.traducir(args))

    def imprimir(self, args):
        print(self.traducir(args))

    def traducir(self, args):
        string = ""
        for arg in args:
            vect = self.exec_expression(arg)
            if type(vect[0]) == str:
                for i in vect:
                    substring = self.translate_element(i)
                    substring = substring[1:len(substring)-1]
                    string += substring + " "
            else:
                string += self.translate(vect)
        return string

## ---------------------------------------------------------------------------------------------------------------------

    def cadena(self, args):
        try:
            if len(args) != 1:
                self.exit("Funcion cadena() requiere exactamente un parametro.")
            else:
                element = self.exec_expression(args[0])
                result = []
                for i in element:
                    if type(i) != str: result.append(self.translate_element(i))
                    else: result.append(i)
                return result
        except (TypeError, ValueError):
            self.exit("El vector especificado no se puede convertir en un vector de cadenas.")

## ---------------------------------------------------------------------------------------------------------------------

    def vectorAcadena(self, args):

        if len(args) != 1: self.exit("Funcion vectorAcadena() requiere exactamente un parametro.")
        try:
            vector = self.cadena(args)
            if vector == [None]: return [None]
            return [''.join(vector)]

        except (TypeError, ValueError):
                self.exit("Error de tipo en los parametros de funcion vectorAcadena().")

## ---------------------------------------------------------------------------------------------------------------------

    # c(1, 14, 25) = 1 14 25

    def c(self, args):
        result = []
        vals = []
        if len(args) == 0 or not args[0]:
            return [None]

        try:
            strFlag = False
            numFlag = False
            for arg in args:
                val = self.exec_expression(arg)
                if isinstance(val, list):
                    for listVal in val:
                        if isinstance(listVal, str): strFlag = True
                        if str(listVal) != 'True' and str(listVal) != 'False' and listVal != None: numFlag = True
                    vals += val
                else:
                    vals.append(val)
                    if isinstance(val, str): strFlag = True
                    if str(val) != 'True' and str(val) != 'False' and val != None: numFlag = True

            if strFlag:
                for _val in vals:
                    if _val != None: result.append(str(_val))
                if result: return result
                else: return [None]

            if numFlag:
                for val in vals:
                    if val != None: result.append(round(val, 10))
                if result: return result
                else: return [None]

            for boolVal in vals:
                if boolVal != None: result.append(boolVal)
            if result: return result
            else: return [None]

        except TypeError:
            self.exit("Error de tipo en los parametros de funcion c().")

## ---------------------------------------------------------------------------------------------------------------------

    # Funcion encargada de reemplazar un elemento de un vector
    # colocar(vector,posicion, elemento)
    def colocar(self, args):

        if len(args) != 3: self.exit("Funcion colocar() requiere exactamente 3 parametros.")
        try:
            _list = self.exec_expression(args[0])
            if _list == [None]: return [None]
            if not isinstance(_list, list): return [int(_list)]
            pos = int(self.exec_expression(args[1])[0])
            element = self.exec_expression(args[2])
            _list[pos-1] = element[0]
            if type(element[0]) == str:
                tmp = self.cadena([_list])
                for i in range(0, len(tmp)): _list[i] = tmp[i]
            return _list
        except (TypeError, ValueError):
            self.exit("Error de tipo en los parametros de funcion colocar()")
        except IndexError:
            self.exit("Indice fuera de rango en colocar()")

## ---------------------------------------------------------------------------------------------------------------------

    # Funcion encargada de reemplazar un elemento de un arreglo
    # colocar(vector,posicion)
    def eliminar(self, args):

        if len(args) != 2: self.exit("Funcion eliminar() requiere exactamente 2 parametros.")
        try:
            _list = self.exec_expression(args[0])
            if _list == [None]: return [None]
            if not isinstance(_list, list): return [int(_list)]
            pos = int(self.exec_expression(args[1])[0])
            _list.pop(pos - 1)
            return _list if _list else [None]
        except (TypeError, ValueError):
            self.exit("Error de tipo en los parametros de funcion eliminar()")
        except IndexError:
            self.exit("Indice fuera de rango en eliminar()")



## ---------------------------------------------------------------------------------------------------------------------

    # sec(1, 5, 0.5) = 1.0 1.5 2.0 2.5 3.0 3.5 4.0 4.5 5.0
    # sec(start, end, step)

    def sec(self, args):

        if len(args) < 2:
            self.exit("Funcion sec() requiere al menos dos parametros.")
        if len(args) > 3:
            self.exit("Funcion sec() requiere maximo tres parametros.")

        try:
            start = self.exec_expression(args[0])[0]
            if start == [None]: self.exit("Parametro -start- nulo en funcion sec().")
            end = self.exec_expression(args[1])[0]
            if end == [None]: self.exit("Parametro -end- nulo en funcion sec().")

            if len(args) == 3: step = self.exec_expression(args[2])[0]
            else: step = 1 if start < end else -1
            if step == [None]: self.exit("Parametro -step- nulo en funcion sec().")
	    
            step + end + start
            r = start
            result = [round(start,10)]

            if step == 0: self.exit("El valor de salto para sec() no puede ser 0.")
            if start < end:
                if step < 0:
                    self.exit("Error de signo para sec() en el valor de salto.")
                while (r+step) <= end:
                    r += step
                    result.append(round(r,10))
            elif start > end:
                if step > 0:
                    self.exit("Error de signo para sec() en el valor de salto.")
                while (r+step) >= end:
                    r += step
                    result.append(round(r,10))
            else :
                return [start]
            return result

        except (TypeError, ValueError):
            self.exit("Error de tipo en los parametros de funcion sec().")

## ---------------------------------------------------------------------------------------------------------------------

    # rep(1, 5) = 1 1 1 1 1
    # rep(val, times)

    def rep(self, args):

        if len(args) != 2 : self.exit("Funcion rep() requiere exactamente dos argumentos.")
        try:
            val = self.exec_expression(args[0])
            times = self.exec_expression(args[1])[0]

            if times == 0: return [None]
            if not isinstance(times, int): self.exit("Valor invalido para cantidad de repeticiones de rep().")
            if isinstance(val, list): return self._clean_return_(val * times)
            else: return self._clean_return_([val] * times)

        except (TypeError, ValueError):
            self.exit("Error de tipo en los parametros de funcion rep().")

## ---------------------------------------------------------------------------------------------------------------------

    # secuencia(4:5) = 1 2 3 4 1 2 3 4 5
    # secuencia(c(10,5,3))
    # secuencia(lista)

    def secuencia(self, args):

        result = []

        if len(args) == 0: return [None]
        try:
            vals = self.exec_expression(args[0])
            if vals == [None]: self.exit("Parametro nulo en funcion secuencia().")
            for val in vals:
                if val <= 0: self.exit("Funcion secuencia() no acepta valores menores a 1.")
                if isinstance(int(val), int):
                    result += list( range(1, int(val)+1) )
            return self._clean_return_(result)

        except (TypeError, ValueError):
            self.exit("Error de tipo en los parametros de funcion secuencia().")


## ---------------------------------------------------------------------------------------------------------------------

    # length(x) = 7
    # length(lista)

    def largo(self, args):

        if len(args) != 1: self.exit("Funcion largo() requiere exactamente un parametro.")
        try:
            _list = self.exec_expression(args[0])
            if _list == [None]: return [0]
            return [len(_list)]

        except (TypeError, ValueError):
            self.exit("Error de tipo en los parametros de funcion largo().")


## ---------------------------------------------------------------------------------------------------------------------

    def minimo(self, args):

        allElements = []

        if len(args) == 0: self.exit("Funcion minimo() requiere al menos un parametro.")
        try:
            for arg in args:
                val = self.exec_expression(arg)
                if val != None:
                    if isinstance(val, list): allElements += val
                    else: allElements += [val]
            if len(allElements) == 0: self.exit("Parametros nulos o vacios para funcion minimo().")
            return [min(allElements)]

        except (TypeError, ValueError):
            self.exit("Error de tipo en los parametros de funcion minimo().")


## ---------------------------------------------------------------------------------------------------------------------

    def maximo(self, args):

        allElements = []

        if len(args) == 0: self.exit("Funcion maximo() requiere al menos un parametro.")
        try:
            for arg in args:
                val = self.exec_expression(arg)
                if val != None:
                    if isinstance(val, list): allElements += val
                    else: allElements += [val]
            if len(allElements) == 0: self.exit("Parametros nulos o vacios para funcion maximo().")
            return [max(allElements)]

        except (TypeError, ValueError):
            self.exit("Error de tipo en los parametros de funcion maximo().")


## ---------------------------------------------------------------------------------------------------------------------

    def sumatoria(self, args):

        allElements = []

        if len(args) == 0: return [0]
        try:
            for arg in args:
                val = self.exec_expression(arg)
                if val == None: val = 0
                if isinstance(val, list): allElements += val
                else: allElements += [val]
            if len(allElements) == 0: return [0]
            return [round(sum(allElements),10)]

        except (TypeError, ValueError):
            self.exit("Error de tipo en los parametros de funcion sumatoria().")

## ---------------------------------------------------------------------------------------------------------------------

    def promedio(self, args):

        if len(args) == 0: self.exit("Funcion promedio() requiere exactamente un argumento.")
        try:
            vals = self.exec_expression(args[0])
            if vals == [None]: self.exit("Parametro nulo en funcion promedio().")
            return [round(sum(vals)/len(vals),10)]

        except (TypeError, ValueError):
           self.exit("Error de tipo en los parametros de funcion promedio().")

## ---------------------------------------------------------------------------------------------------------------------

    def medio(self, args):

        if len(args) == 0: self.exit("Funcion medio() requiere exactamente un parametro.")
        if len(args) != 1: print_purple("Funcion medio() con mas de un argumento. Se usa el 1ro nada mas.")
        try:
            orig_list = self.exec_expression(args[0])
            if orig_list == [None]: self.exit("Parametro nulo en funcion medio().")
            _list = list(orig_list)
            centro = int(len(_list) / 2)
            _list.sort()
            if len(_list) % 2 == 0: return [ round( (_list[centro-1] + _list[centro])/2, 10) ]
            return [_list[centro]]

        except (TypeError, ValueError):
            self.exit("Error de tipo en los parametros de funcion medio().")

## ---------------------------------------------------------------------------------------------------------------------

    def varianza(self, args):

        if len(args) != 1: self.exit("Funcion varianza() requiere exactamente un parametro.")
        try:
            _list = self.exec_expression(args[0])
            if _list == [None]: self.exit("Parametro nulo en funcion varianza().")
            promed = self.promedio(args)[0]
            listaDifs = []
            for val in _list:
                listaDifs.append((val-promed)*(val-promed))
            return [ round( sum(listaDifs)/(len(_list)-1) ,10) ]

        except (TypeError, ValueError):
            self.exit("Error de tipo en los parametros de funcion varianza().")


## ---------------------------------------------------------------------------------------------------------------------

    def ordenar(self, args):

        if len(args) == 0: self.exit("Funcion ordenar() requiere exactamente un parametro.")
        if len(args) > 2:
            print_purple("Funcion ordenar() con mas de un argumento. Se usa el 1ro nada mas.")
        try:
            _list = self.exec_expression(args[0])
            if _list == [None]: self.exit("Parametro nulo en funcion ordenar().")
            if len(args) == 1:
                _list.sort()
                return _list
            else:
                _asc = self.exec_expression(args[1])[0]
                _list.sort(reverse=_asc)
                return _list

        except (TypeError, ValueError):
            self.exit("Error de tipo en los parametros de funcion ordenar().")

## ---------------------------------------------------------------------------------------------------------------------

    def unicos(self, args):

        if len(args) == 0: self.exit("Funcion unicos() requiere exactamente un parametro.")
        if len(args) != 1: print_purple("Funcion unicos() con mas de un argumento. Se usa el 1ro nada mas.")
        try:
            _list = self.exec_expression(args[0])
            newList = []
            for val in _list:
                if val not in newList: newList.append(val)
            if newList == []: return [None]
            return self._clean_return_(newList)

        except (TypeError, ValueError):
            self.exit("Error de tipo en los parametros de funcion unicos().")


## ---------------------------------------------------------------------------------------------------------------------

    def redondear(self, args):

        if len(args) == 0: self.exit("Funcion redondear() requiere al menos un parametro.")
        if len(args) > 2: self.exit("Funcion redondear() requiere maximos dos parametros.")
        roundVal = 0
        try:
            _list = self.exec_expression(args[0])
            if _list == [None]: self.exit("Funcion redondear() requiere parametros no nulos.")
            if len(args) == 2: roundVal = int(self.exec_expression(args[1])[0])

            result = []
            for val in _list:
                result.append( round(val, roundVal) )

            return result

        except (TypeError, ValueError):
            self.exit("Error de tipo en los parametros de funcion redondear().")


## ---------------------------------------------------------------------------------------------------------------------

    def revertir(self, args):

        if len(args) == 0: self.exit("Funcion revertir() requiere exactamente un parametro.")
        if len(args) != 1: print_purple("Funcion revertir() con mas de un argumento. Se usa el 1ro nada mas.")
        try:
            _list = self.exec_expression(args[0])
            if _list == [None]: return [None]
            if not isinstance(_list, list): return [_list]
            result = list(_list)
            result.reverse()
            return result

        except (TypeError, ValueError):
            self.exit("Error de tipo en los parametros de funcion revertir().")


## ---------------------------------------------------------------------------------------------------------------------

    def absoluto(self, args):

        if len(args) != 1: self.exit("Funcion absoluto() requiere exactamente un parametro.")
        try:
            _list = self.exec_expression(args[0])
            if _list == [None]: return [None]
            if not isinstance(_list, list): return [_list] if _list >= 0 else [-_list]

            result = []
            for val in _list:
                result.append(val if val >= 0 else -val)
            return result if result else [None]

        except (TypeError, ValueError):
            self.exit("Error de tipo en los parametros de funcion absoluto().")

## ---------------------------------------------------------------------------------------------------------------------

    def techo(self, args):

        if len(args) != 1: self.exit("Funcion techo() requiere exactamente un parametro.")
        try:
            _list = self.exec_expression(args[0])
            if _list == [None]: return [None]
            if not isinstance(_list, list): return [_list if _list-int(_list)==0 else round(_list+0.5) ]

            result = []
            for val in _list:
                result.append( val if val-int(val)==0 else round(val+0.5) )
            return result if result else [None]

        except (TypeError, ValueError):
            self.exit("Error de tipo en los parametros de funcion techo().")

## ---------------------------------------------------------------------------------------------------------------------

    def suelo(self, args):

        if len(args) != 1: self.exit("Funcion suelo() requiere exactamente un parametro.")
        try:
            _list = self.exec_expression(args[0])
            if _list == [None]: return [None]
            if not isinstance(_list, list): return [_list if _list - int(_list) == 0 else round(_list - 0.5)]

            result = []
            for val in _list:
                result.append(val if val - int(val) == 0 else round(val - 0.5))
            return result if result else [None]

        except (TypeError, ValueError):
            self.exit("Error de tipo en los parametros de funcion suelo().")

## ---------------------------------------------------------------------------------------------------------------------

    def truncar(self, args):

        if len(args) == 0: self.exit("Funcion truncar() requiere exactamente un parametro.")
        if len(args) != 1: print_purple("Funcion truncar() con mas de un argumento. Se usa el 1ro nada mas.")
        try:
            _list = self.exec_expression(args[0])
            if _list == [None]: return [None]
            if not isinstance(_list, list): return [int(_list)]

            result = []
            for val in _list:
                result.append(int(val))
            return result if result else [None]

        except (TypeError, ValueError):
            self.exit("Error de tipo en los parametros de funcion truncar().")

## ---------------------------------------------------------------------------------------------------------------------
##                                          Funciones de operadores
## ---------------------------------------------------------------------------------------------------------------------

    ## Empareja el tamanho de las listas Ej: [1,2]*[3,4,5,6] = [1,2,1,2]*[3,4,5,6]
    def check_and_match_lists(self, w, z):
        x = w[:]; y = z[:]
        lx = len(x)
        ly = len(y)
        if lx % ly != 0 and ly % lx != 0:
            self.exit("Ninguno de los operandos es multiplo del otro.")
        if lx != ly:
            higher, lower = (x, y) if lx > ly else (y, x)
            lower *= (lx // ly) if lx > ly else (ly // lx)
        return x, y

## ---------------------------------------------------------------------------------------------------------------------

    def exec_bin_op(self, args, function, op):
        try:
            x = self.exec_expression(args[0])
            y = self.exec_expression(args[1])
            w, z = self.check_and_match_lists(x,y)
            return function(w,z)
        except TypeError: self.exit("Tipo de operando no soportado para '"+ op +"'");
        except IndexError: self.exit("Elemento fuera de indice")
        except ZeroDivisionError: self.exit("Division entre 0")

## ---------------------------------------------------------------------------------------------------------------------

    def exec_un_op(self, args, function, op):
        try:
            x = self.exec_expression(args[0])
            return function(x)
        except TypeError: self.exit("Tipo de operando no soportado para '"+ op +"'");

## ---------------------------------------------------------------------------------------------------------------------

    def exec_sum(self, args):
        f = lambda x, y: [x[i] + y[i] for i in range (0, len(x))]
        return self.exec_bin_op(args, f, '+')

## ---------------------------------------------------------------------------------------------------------------------

    def exec_sub(self, args):
        f = lambda x, y: [x[i] - y[i] for i in range(0, len(x))]
        return self.exec_bin_op(args, f, '-')

## ---------------------------------------------------------------------------------------------------------------------

    def exec_mult(self, args):
        f = lambda x, y: [x[i] * y[i] for i in range(0, len(x))]
        return self.exec_bin_op(args, f, '*')

## ---------------------------------------------------------------------------------------------------------------------

    def exec_pow(self, args):
        f = lambda x, y: [x[i] ** y[i] for i in range(0, len(x))]
        return self.exec_bin_op(args, f, '^')

## ---------------------------------------------------------------------------------------------------------------------

    def exec_mod(self, args):
        f = lambda x, y: [x[i] % y[i] for i in range(0, len(x))]
        return self.exec_bin_op(args, f, '%%')

## ---------------------------------------------------------------------------------------------------------------------

    def exec_int_div(self, args):
        f = lambda x, y: [x[i] // y[i] for i in range(0, len(x))]
        return self.exec_bin_op(args, f, '%/%')

## ---------------------------------------------------------------------------------------------------------------------

    def exec_div(self, args):
        f = lambda x, y: [self.exec_div_aux(x[i], y[i]) for i in range(0, len(x))]
        return self.exec_bin_op(args, f, '/')

## ---------------------------------------------------------------------------------------------------------------------

    def exec_div_aux(self, x, y):
        if y == 0:
            if x == 0: return float('nan')
            elif x > 0 : return float('inf')
            else: return float('-inf')
        return x/y

## ---------------------------------------------------------------------------------------------------------------------

    def exec_lt(self, args):
        f = lambda x, y: [x[i] < y[i] for i in range(0, len(x))]
        return self.exec_bin_op(args, f, '<')

## ---------------------------------------------------------------------------------------------------------------------

    def exec_le(self, args):
        f = lambda x, y: [x[i] <= y[i] for i in range(0, len(x))]
        return self.exec_bin_op(args, f, '<=')

## ---------------------------------------------------------------------------------------------------------------------

    def exec_eq(self, args):
        f = lambda x, y: [x[i] == y[i] for i in range(0, len(x))]
        return self.exec_bin_op(args, f, '==')

## ---------------------------------------------------------------------------------------------------------------------

    def exec_ne(self, args):
        f = lambda x, y: [x[i] != y[i] for i in range(0, len(x))]
        return self.exec_bin_op(args, f, '!=')

## ---------------------------------------------------------------------------------------------------------------------

    def exec_ge(self, args):
        f = lambda x, y: [x[i] >= y[i] for i in range(0, len(x))]
        return self.exec_bin_op(args, f, '>=')

## ---------------------------------------------------------------------------------------------------------------------

    def exec_gt(self, args):
        f = lambda x, y: [x[i] > y[i] for i in range(0, len(x))]
        return self.exec_bin_op(args, f, '>')

## ---------------------------------------------------------------------------------------------------------------------

    def exec_and(self, args):
        f = lambda x, y: [bool(x[i]) and bool(y[i]) for i in range(0, len(x))]
        return self.exec_bin_op(args, f, '&')

## ---------------------------------------------------------------------------------------------------------------------

    def exec_or(self, args):
        f = lambda x, y: [bool(x[i]) or bool(y[i]) for i in range(0, len(x))]
        return self.exec_bin_op(args, f, '|')

## ---------------------------------------------------------------------------------------------------------------------

    def exec_bracket(self, args):

        if len(args[1]) > 1:
            print_red("El operador '[' solo tomara en cuenta el primer parametro")

        var = self.exec_expression(args[0])
        index = self.exec_expression(args[1][0])
        typeoflist = type(index[0])

        if typeoflist == float or typeoflist == int:
            if index[0] > 0:
                return self.exec_bracket_case_positive_index(var, index)
            elif index[0] < 0:
                return self.exec_bracket_case_negative_index(var, index)
            else: self.exit("Los indices inician desde (+-) 1")

        elif typeoflist == bool:
            return self.exec_bracket_case_bool_index(var, index)

        else: self.exit("Tipo de parametro no soportado para '['")
        return [None]

## ---------------------------------------------------------------------------------------------------------------------

    def exec_bracket_case_negative_index(self, var, index):
        result = []
        index = [int(index[i] * -1) - 1 for i in range(0, len(index))]
        self.exec_bracket_validation(var, index)
        for i in range(0, len(var)):
            if not index.__contains__(i): result.append(var[i])
        return result if len(result) != 0 else [None]

## ---------------------------------------------------------------------------------------------------------------------

    def exec_bracket_case_positive_index(self, var, index):
        result = []
        index = [int(index[i] - 1) for i in range(0, len(index))]
        self.exec_bracket_validation(var, index)
        for i in range(0, len(var)):
            if index.__contains__(i): result.append(var[i])
        return result if len(result) != 0 else [None]

## ---------------------------------------------------------------------------------------------------------------------

    def exec_bracket_validation(self, var, index):
        for i in index:
            if i < 0: self.exit("El operador [ no puede mezclar indices negativos con positivos")
            elif i > len(var): self.exit("Indice fuera de rango")

## ---------------------------------------------------------------------------------------------------------------------

    def exec_bracket_case_bool_index(self, var, index):
        result = []
        index, var = self.check_and_match_lists(index, var)
        for i in range(0, len(index)):
            if index[i]: result.append(var[i])
        return result if len(result) != 0 else [None]

## ---------------------------------------------------------------------------------------------------------------------

    def exec_d_brack(self, args):
        self.exit("Operador [[ no implementado")
        pass

## ---------------------------------------------------------------------------------------------------------------------

    def exec_and2(self, args):
        f = lambda x, y: [True] if x[0] and y[0] else [False]
        return self.exec_bin_op(args, f, '&&')

## ---------------------------------------------------------------------------------------------------------------------

    def exec_or2(self, args):
        f = lambda x, y: [True] if x[0] and y[0] else [False]
        return self.exec_bin_op(args, f, '||')

## ---------------------------------------------------------------------------------------------------------------------

    def exec_uminus(self, args):
        f = lambda x: [-x[i] for i in range (0, len(x))]
        return self.exec_un_op(args, f, '-')

## ---------------------------------------------------------------------------------------------------------------------

    def exec_uplus(self, args):
        f =  lambda x: [+x[i] for i in range (0, len(x))]
        return self.exec_un_op(args, f, '+')

## ---------------------------------------------------------------------------------------------------------------------

    def exec_not(self, args):
        f =  lambda x: [not x[i] for i in range (0, len(x))]
        return self.exec_un_op(args, f, '!')

## ---------------------------------------------------------------------------------------------------------------------

