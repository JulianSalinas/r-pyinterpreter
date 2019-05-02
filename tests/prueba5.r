
## Ejemplo, Bubblesort 

ordenamiento.burbuja <- funcion(vector.desordenado){

	# Esto para no alterar el vector desordenado
	x = vector.desordenado
	n = largo(x)

    para(i en 1:(n-1)){
    	para(j en 1:(n-i))
    		si(x[j+1] < x[j]){
    			cambio_1 = x[j]
    			cambio_2 = x[j+1]
    			colocar(x, j+1, cambio_1)
    			colocar(x, j, cambio_2)
    		}
    }
    retornar(x)
}

# La variable vector.desordenado no se altera despues del ordenamiento
vector.desordenado = c(54,26,93,17,2,3,77,31,44,55,20,1,4)
informar("Sin ordenar: ")
imprimir(vector.desordenado)

vector.ordenado = ordenamiento.burbuja(vector.desordenado)
informar("Ordenado: ")
imprimir(vector.ordenado)
















