# Cierre Convexo Graham
J.Galindo 2022-04-08

Implementaciones del curso de Geometría Computacional 


### Descripción
Este proyecto es una implementación del algoritmo de Graham para el cálculo del cierre convexo de un conjunto de puntos dados


## Set up

### Dependencias

Este proyecto se implementó en python 3.8

Utiliza las siguientes librerías:
    random, matplitlib, math y sys 

### Descarga 
El repositorio contiene 3 archivos principales:

#### graham.py 
Este archivo contiene las diferentes funciones utilizadas para el algoritmo 
#### points.py
Un archivo de texto que contiene coordenadas 'x' y 'y' de los puntos de interés
El archivo es modificable, pero para que funcione correctamente, los puntos que se incluyan en el mismo deben estar cáda uno en un renglón, con ambas coordenadas en el mismo renglón separadas por un espacio, comenzando por la coordenada x. 
Ejem:
```
1 2
34 3
23 12
34 56
```

### Ejecición del programa

* Descargar el repositorio
* Modificar el archivo points.txt si se desea
* Ubicarse en la carpeta del repositorio 
* El programa tiene 2 modos de ejecución: 
```
python3 main.py 0
```
En este caso se pide al usuario haber configurado el conjunto de puntos en el archivo de texto, como se describió anteriormente

```
python3 main.py 1
```
En este caso, el programa generará un conjunto de puntos aleatorios con coordenadas enteras entre 1 y 100 y solicitará al usurio ingresar el número de puntos que desea

#### Resultado 
El programa despliega una gráfica que muestra los puntos del conjunto original y su cierre convexo 

![Figure_1](https://user-images.githubusercontent.com/79530376/162401554-36cf629b-4ebf-4345-882b-9c772bf60743.png)
