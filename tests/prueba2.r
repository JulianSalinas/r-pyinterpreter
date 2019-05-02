# Funcion de Fibonacci de n usando recursion

fib <- funcion(n) {
    si (n < 2) {
        retornar(n)
    }
    sino {
        retornar(fib(n-1) + fib((n-2)))
    }
}

# Calcula un vector con todos los numeros de Fibonacci de n hasta m

fibsec <- funcion(desde, hasta) {
    resultado <- c()
    para(i en desde:hasta){
        c(resultado, fib(i)) -> resultado
    }
    retornar(resultado)
}


informar("Fibonacci de 5")
imprimir(fib(5))


informar("Secuencia de Fibonacci de 1 hasta 8")
x = 1; y <- 8
imprimir(fibsec(x, y))
