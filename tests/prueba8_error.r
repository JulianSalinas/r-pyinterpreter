
vectorPrueba = c(1.36, 10.42, -15.12451, -33)

obtenerSoloDecimales1 = funcion(vector){
	
	# utilizamos la funcion truncar para obtener la parte entera de los numeros
	enteros = truncar(vector)

	# eliminamos dicha parte entera con la resta de vectores
	resultado = vector - enteros # ERROR - Error Semantico - La variable no existe
	retornar(resultado)

}

informar("Vector solo de decimales:")
imprimir(obtenerSoloDecimales1(vectorPrueba))

# uso de la funcion de valor absoluto
informar("Vector solo de decimales sin signo:")
imprimir(obtenerSoloDecimales1(absoluto(vectorPrueba)))

# uso de la funcion de redondeo
informar("Vector solo de decimales redondeado a 1 decimal:")
imprimir(obtenerSoloDecimales1(redondear(vectorPrueba, 'error'))) # ERROR - Error Semantico

# uso de la funcion de valor absoluto y de redondeo
informar("Vector solo de decimales redondeado a 3 decimales sin signo:")
imprimir(obtenerSoloDecimales1(absoluto(redondear(vectorPrueba,3))))

