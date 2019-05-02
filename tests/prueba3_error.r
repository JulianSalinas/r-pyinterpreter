

informar("Sumatoria de los números enteros múltiplos de 5")

sumatoria.multiplos <- funcion(secuencia.enteros, multiplo.x){

    # Ambos, secuencia.enteros y multiplo.x deben ser vectores numericos de
    # lo contrario no se podrá obtener el módulo y se mostrará error
    
    filtro.multiplos = secuencia.enteros %% multiplo.x == 0
    informar("Filtro usado"); imprimir(filtro.multiplos)
 
 	# Aqui falta un paréntesis 
    multiplos = secuencia.enteros[filtro.multiplos 

    informar("Multiplos de " + cadena(multiplo.x))
    imprimir(multiplos)
    resultado = sumatoria(multiplos)
    retornar(resultado)
}

resultado = sumatoria.multiplos(c("1","2","3","4","5","6","7","8"), 5)
informar("Resultado de la sumatoria")
imprimir(resultado)


