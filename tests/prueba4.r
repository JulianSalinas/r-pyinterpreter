# Productoria de los números pares mayores que y en una secuencia x

productoria.pares.mayores <- funcion(x, y){
    informar("Vector utilizado"); imprimir(x)

    # Mascara con los numeros mayores a y
    filtro.mayores = x > y
    informar("Filtro para mayores a " + cadena(y[1]));
    imprimir(filtro.mayores)

    # Mascara con los numeros pares
    filtro.pares = x %% 2 == 0
    informar("Filtro utilizado para números pares");
    imprimir(filtro.pares)

    # Secuencia sin los numeros menores o iguales a y, (se redefine x)
    x = x[filtro.mayores & filtro.pares]

    # Numeros del vector que cumplen las condiciones
    informar("Números que cumplen las condiciones")
    imprimir(x)

    # Se efectua la productoria
    resultado = 1
    para( i en x ) resultado = resultado * i
    retornar(resultado)
}

# Vector de prueba
vector = secuencia(1:10)
resultado.forma_1 = productoria.pares.mayores(vector,5)
informar("Resultado de la productoria")
imprimir(resultado.forma_1)
