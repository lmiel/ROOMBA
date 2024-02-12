# ROOMBA
link: https://github.com/lmiel/ROOMBA.git

# ENUNCIADO
Le proponemos realizar un proyecto que consiste en la escritura de un script Python que permite a un robot aspirador calcular la superficie de una habitación y estimar el tiempo de limpieza.

Imaginemos que la habitación que hay que limpiar contiene un mueble debajo del cual no puede meterse el robot, Una de las formas posibles de calcular la superficie que debe limpiar el robot consiste en fragmentar la superficie total en zonas utilizables:<br>
**ZONA - LARGO (cm) - ANCHO (cm)** <br>
Zona 1 - 500 - 150 <br>
Zona 2 - 480 - 101 <br>
Zona 3 - 309 - 480 <br>
Zona 4 - 90 - 220 <br>
Una vez fragmentada, es fácil calcular la superficie total que hay que limpiar añadiendo las superficies de cada zona. Estas superficies se calculan multiplicando el largo por el ancho en cada una de ellas.
# EXPLICACIÓN DEL CÓDIGO
Como solución al programa, he creado tres archivos de código:<br>
- **Canvas**: utilizando tkinter nos permite crear una interfaz gráfica donde vamos a ver la habitación y las zonas. Tiene dos clases; _ _Zona_ _ y _ _Objeto_ _ que tienen funciones para poder calcular su área y dibujar dichos elementos.
- **Limpieza**: este archivo consta con dos funciones; _ _datos_zona_ _,que nos permite calcular el area y el tiempo que tarda el roomba en limpiar y _ _detect_zona_ _ que nos permite sabes cuando el usuario esta dando click a que zona.
- **Main**: aquí es donde se llama a las funciones antes nombradas para que todo el programa tome vida y nos muestre lo que le hayamos metido.
