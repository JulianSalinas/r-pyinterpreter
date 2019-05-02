
aBinario <- funcion(n){
	
	r = c()
	# la funcion esta definida para trabajar sobre numeros positivos unicamente
	si (n>0){
		mientras (n!=0){
			# operando de residuo o mod
			si (n%%2 == 0)
				# la funcion de crear lista es una opcion para concatenar
				r = c('0', r)
			sino
				r = c('1', r)
			# se utiliza el operador de division entera de R
			n = n%/%2
		}
	}
	sino
		r = c('0')

	# el resultado de residuos se fue almacenando en un vector
	# por lo que al final se concatenan los valores obtenidos
	retornar(vectorAcadena(r))
}

# ERROR - Error lexico - No se logra reconocer los tokens de la linea siguiente
informar("Binario de 10:); imprimir(aBinario(10)) 
informar("Binario de 1024:"); imprimir(aBinario(1024))
informar("Binario de 255:"); imprimir(aBinario(255))
