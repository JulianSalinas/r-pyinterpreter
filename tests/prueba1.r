# Calcula el factorial de n usando recursión

factorial <- funcion(n){
    si (n == 0) retornar(1)
    sino retornar(n * factorial(n-1))
}

# Crea una secuencia de con todos los resultados del
# factorial para un vector

factorialsec <- funcion(vector){
    resultado = c()
    para(elemento en vector){
        resultado = c(resultado, factorial(elemento))
    }
    retornar(resultado)
}

# La funcion informar permite imprimir en azul

informar("Factorial de 10")
imprimir(factorial(10))

# Se imprime el factorial de cada num de 1 hasta 10

informar("Factorial del 1 hasta 10")
x <- 1
mientras(x <= 10){
    imprimir(factorial(x))
    x = x + 1
}

# Imprime la misma secuencia pero esta vez usando la
# funcion con el 'para'
informar("Factorial del 1 hasta el 10 usando la funcion factorialsec")
imprimir(factorialsec(1:10))



