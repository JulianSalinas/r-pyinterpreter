
fib <- funcion(n) {
    si (n < 2) {
        retornar(n)
    }
    sino {
        retornar(fib(n-1) + fib((n-2)))
    }
}

fibsec <- funcion(desde, hasta) {
    resultado <- c()
    para(i en desde:hasta) 
        c(resultado, fib(i)) -> resultado
    
    retornar(resultado)
}


informar("Fibonacci de 5")

## Notesé que la función se llama fib y no fibonacci

imprimir(fib(5)) 


informar("Secuencia de Fibonacci de 1 hasta 8")
x = 1; y <- 8

## La función fibsec debería de recibir dos parámetros

imprimir(fibsec(x))



