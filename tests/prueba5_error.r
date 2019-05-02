

ordenamiento.burbuja <- funcion(vector.desordenado){

	
	x = vector.desordenado
	n = largo(x)
	
    para(i en 1:(n-1)){
    	
    	para(j en 1:(n-i))
    		si(x[j+1] < x[j]){
    			cambio_1 = x[j]
    			cambio_2 = x[j+1]
    			
    			# Error semantico al tratar de colocar un valor
				# en un índice mayor al tamaño del vector
				
    			colocar(x, 1000, cambio_1)
    			colocar(x, j, cambio_2)
    		}
    }
    retornar(x)
}

# Notesé que después del 3 sigue una coma en vez de un número,
# Esto no esta mál sintácticamente, pues se toma lo que esta entre las comas como NULO,
# sin embargo, obtendremos un error semántico con la función c()

vector.desordenado = c(54,26,93,17,2,3,,,77,4,31,44,55,20,1,4)
informar("Sin ordenar: ")
imprimir(vector.desordenado)

vector.ordenado = ordenamiento.burbuja(vector.desordenado)
informar("Ordenado: ")
imprimir(vector.ordenado)
















