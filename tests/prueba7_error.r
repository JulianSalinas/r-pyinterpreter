estadisticas = funcion(){
	
	# generamos algunos valores de prueba similares
	alturas = c(1.61, 1.77, 1.69, 1.82, 1.69)
	alturas2 = c(1.6, 1.7, 1.6, 1.7, 1.8)

	# calcular la diferencia entre los valores de prueba
	difAlturas = alturas - alturas2
	promdif = promedio(difAlturas	# ERROR - Error de sintaxis, se espera un ')' y se encuentra un '\n'

	# generar los resultados segun los datos de prueba
	prom1 = promedio(alturas)
	prom2 = promedio(alturas2)
	var1 = varianza(alturas)
	var2 = varianza(alturas2)
	retornar( c(prom1,prom2,var1,var2,promdif) )
}

main = funcion(){	
	# imprimimos los resultados obtenidos
	vals = estadisticas()
	informar("Altura promedio en muestra 1:"); imprimir(vals[10]) # ERROR - "vals" tiene como indice maximo el 5.
	informar("Altura promedio en muestra 2:"); imprimir(vals[2])
	informar("Promedio de la diferencia de alturas:"); imprimir(vals[5])
	informar("Diferencia de los promedios de alturas:"); imprimir(vals[1] - vals[2])
	informar("Varianza en muestra 1:"); imprimir(vals[3])
	informar("Varianza en muestra 2:"); imprimir(vals[4])
}

main()

