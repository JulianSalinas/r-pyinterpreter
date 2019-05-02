
factorial <- funcion(n){
    si (n == 0) retornar(1)
    sino retornar(n * factorial(n-1))
}

factorialsec <- funcion(vector){
    resultado = c()
    para(elemento en vector){
        resultado = c(resultado, factorial(elemento))
    }
    retornar(resultado)
}

informar("Factorial de 10")
imprimir(factorial(10))

informar("Factorial del 1 hasta 10")

## x no está definida en ninguna parte

mientras(x <= 10){
    imprimir(factorial(x))
    x = x + 1
}

# Se está tratando de calcular el factorial de una cadena

factorial("hola")


