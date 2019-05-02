
productoria.pares.mayores <- funcion(x, y){

	# No existe ';' para separar las expresiones en la misma linea
	
    informar("Vector utilizado") imprimir(x)

    filtro.mayores = x > y
    informar("Filtro para mayores a " + cadena(y[1]));
    imprimir(filtro.mayores)

    filtro.pares = x %% 2 == 0
    informar("Filtro utilizado para números pares");
    imprimir(filtro.pares)

    x = x[filtro.mayores & filtro.pares]

    informar("Números que cumplen las condiciones")
    imprimir(x)

    resultado = 1
    para( i en x ) resultado = resultado * i
    retornar(resultado)
}

vector = secuencia(1:10)
resultado = productoria.pares.mayores(vector,5)
informar("Resultado de la productoria!")

## Falta un paréntesis del lada derecho
imprimir(resultado




