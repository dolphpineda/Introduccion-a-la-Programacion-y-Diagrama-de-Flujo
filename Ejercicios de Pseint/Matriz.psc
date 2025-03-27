Algoritmo Matriz
	Definir calificaciones Como Real
	Dimension calificaciones[3,3]
	
	//asignar valores a las matriz
	calificaciones[1,1]=9.5
	calificaciones[1,2]=8.5
	calificaciones[1,3]=7.5
	calificaciones[2,1]=6.5
	calificaciones[2,2]=5.5
	calificaciones[2,3]=4.5
	calificaciones[3,1]=3.5
	calificaciones[3,2]=2.5
	calificaciones[3,3]=1.5
	
	Escribir "calificacion en la fila, Columna", calificaciones[3,3]
	
	//rrecorer la matriz con ciclo for
	para i=1 hasta 3 Hacer
		para j=1 hasta 3 Hacer
			Escribir "calificacion [",i,",",j,"]:", calificaciones[i,j]
			
		FinPara
	FinPara
	
	
FinAlgoritmo
