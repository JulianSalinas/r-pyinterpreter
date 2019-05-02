# Sumatoria de los números enteros múltiplos de x de una secuencia de n hasta m

informar("Sumatoria de los números enteros múltiplos de 5 de la secuencia 1:100")

sumatoria.multiplos <- funcion(secuencia.enteros, multiplo.x){

    # Crea un filtro de los indices que contienen un multiplo de x (vector de booleanos)
    filtro.multiplos = secuencia.enteros %% multiplo.x == 0
    informar("Filtro usado")
    imprimir(filtro.multiplos)

    # Lista de solo aquellos valores donde filtro.multiplo es verdadero
    multiplos = secuencia.enteros[filtro.multiplos]

    # Recordar que los indices inicia desde 1
    informar("Multiplos de ", multiplo.x)
    imprimir(multiplos)

    # Llama a la funcion sumatoria del lenguaje
    resultado = sumatoria(multiplos)

    retornar(resultado)
}

resultado = sumatoria.multiplos(1:100, 5)
informar("Resultado de la sumatoria")
imprimir(resultado)
