
# una funcion simple para calcular potencias con base y exponentes enteros positivos
potenciaPositiva = funcion(base, exponente){
	
	# el subTotal va a ir acumulando las sumas
	subTotal = base
	si (exponente == 1) 
		subTotal = base
	
	sino    # el ciclo for se ejecuta tantas veces como sea el exponente
		para(indice en sec(1,exponente-1)){
			# se genera un vector de valores X X X X, para sumarlos y simular una multiplicacion			
			repeticiones = rep(subTotal, base)
			subTotal = sumatoria(repeticiones) # se almacena el nuevo valor
		}
	
	retornar(subTotal)
}

informar("Resultado de 2^4: ")
imprimir(potenciaPositiva(2,4))

informar("Resultado de 3^5: ")
imprimir(potenciaPositiva(3,5))

informar("Resultado de 5^3: ")
imprimir(potenciaPositiva(5,3))

informar("Resultado de 2^10: ")
imprimir(potenciaPositiva(2,10))

informar("Resultado de 1^15: ")
imprimir(potenciaPositiva(1,15))
