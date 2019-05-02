
factorialIterativo <- funcion(numero){
	
	si (numero < 1){
		imprimir("No hay factorial de negativos.")
		retornar(-1)
	}
	sino {
		resultado = 1
		# genera los numeros desde el 1 hasta el factorial a calcular
		factores <- sec(1, numero, 1)

		# multiplica los numeros del vector de factores
		para(factor en factores){
			resultado <- resultado * factor
		}
		retornar(resultado)
	}
}

imprimir("Factorial de 4:")
imprimir(factorialIterativo(4))

imprimir("Factorial de 5:")
imprimir(factorialIterativo(5))

imprimir("Factorial de 50:")
imprimir(factorialIterativo(50))



