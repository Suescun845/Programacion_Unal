Proceso Tipo_de_triangulo
	Definir a,b,c Como Entero;
	Escribir "Este programa comprueba si se puede formar un triángulo y que tipo de triangulo se forma, a continuación, coloque la longitud de los lados ";
	Escribir "Ponga el lado a";
	Leer a;
	Escribir "Ponga el lado b";
	leer b;
	Escribir "Ponga el lado c";
	leer c;
	Si a + b > c y c + b > a y c + a > a Entonces
		Si a = b y a = c  Entonces
			Escribir "Se puede formar un triángulo equilátero con lados:", a,",", b,",", c;
		FinSi
		si a= c o b =c o b = a; Entonces
			Escribir "Se puede formar un triángulo Isósceles con lados:", a,",", b,",", c;
		SiNo
			Escribir "Se puede formar un triángulo escaleno con lados:",a,",", b,",", c;
		FinSi
	Sino 
			Escribir   "No se puede formar un tri?ngulo con lados:", a,",", b,",", c;
	FinSi
FinProceso

	

