#####################################
# ALGORITMO DE GRAHAM               #
#-----------------------------------#
# Josué Galindo                     #
# 2022-04-08                        #
# ###################################

# Funciones para el algoritmo de Graham 
# para el cálculo del cierre convexo 
# de un conjunto de N puntos 

#________ Librerías ______________________________________________________________

from random import randint
from re import I
from matplotlib import pyplot as plt
from math import sqrt

from sqlalchemy import true

#__________________________________________________________________________________
#________ Funciones para quick sort _______________________________________________
def particion(array, start, end, fun_comp):
    """
    función auxiliar del algoritmo de quick sort, encuentra

    Args:
        array (lis): arreglo de objetos a ordenar
        start (int): indice de pricipio de cadena
        end (int): indice de fin de cadena
        fun_comp (function): función boleana que recibe 2 argumentos (los que se van a comparar)
                             indica qué criterio de orden se seguirá   

    Returns:
        (int):indice del corte superior 
    """
    #print(array)
    pivot = array[start]
    #print(pivot)
    low = start + 1
    high = end

    while True:
        while low <= high and fun_comp(array[high], pivot):
            high = high - 1

        while low <= high and not fun_comp(array[low], pivot):
            low = low + 1

        if low <= high:
            array[low], array[high] = array[high], array[low]
        else:
            break

    array[start], array[high] = array[high], array[start]

    return high

def quick_sort(array, start, end, fun_comp):
    if start < end:
        p = particion(array, start, end, fun_comp)
        quick_sort(array, start, p-1, fun_comp)
        quick_sort(array, p+1, end, fun_comp)

## 
#-______Funciones para genar puntos y graficar ___________________________________________

def genera_puntos(n=15,min = 0, max =100):
    """
    Genera una lista de {n} puntos aleatorios (tuplas (x,y))
    con coordenadas enteras entre {min} y {max}
    
    Args:
        n (int, optional): número de puntos. Defaults  15.
        min (int, optional): limite inferior para las coordenadas. Defaults  0.
        max (int, optional): limite superior para las coordenadas. Defaults 100.

    Returns:
        (list): lista de puntos
    """
    return [(randint(min,max),randint(min,max)) for i in range(n)]


def dibuja(S = [(1,1)], Pol = None, etiquetar = False):
    """
    Hace un scatter plot de los puntos suministrados en la lista {S} y
    en caso de dar un Poligono, dibuja las aristas con el orden en que se dan los puntos
    además si etiquetar = True, agrega etiquetas a los vértices del polígino en orden

    Args:
        S (list): lista de puntos (tumplas (x,y)). Defaults [(1,1)]
        Pol (list): lista de vértices de un polígono. Defaults None
    """
    X,Y  = zip(*S)
    plt.scatter(X,Y)
    
    if Pol != None:
        for i in range(len(Pol)):
            plt.plot((Pol[i-1][0],Pol[i][0]),(Pol[i-1][1],Pol[i][1]))
    
    if etiquetar:
        for i, (x,y) in enumerate(Pol):
            plt.annotate(str(i), (x,y)) 

    plt.show()

#____________ Funciones para calculos geométricos _________________________________________________
 
def producto_cruz(A=(1,0),B=(0,0),C =(0,1)):
    #calculamos el producto cruz de 2 vectores> AB y BC
    return ((B[0] - A[0])*(C[1] - A[1])) - ((B[1] - A[1])*(C[0] - A[0])) 

#def pendiente(A=(1,0),B =(0,0)):
#    if A[0] == B[0] :
#        return float('inf')
#    else:
#        #print(1.0*(A[1]-B[1])/(A[0]-B[0]))
#        return 1.0*(A[1]-B[1])/(A[0]-B[0])

def pendiente_ort(A=(1,0),B =(0,0)):
    """
    Recibe 2 puntos (tuplas (x,y)) y calcula la pendiente de una recta perpendicular a este segmento
    Se tienen 3 casos 
    Si las corrdenadas x de los puntos coinciden, la pendiente de la recta perpendicular es 0
    Si las coordenadas y de los puntos coinciden y A.x <= B.x la pendiente de la recta perpendicular es -inf
    Si las coordenadas y de los puntos coinciden y A.x > B.x la pendiente de la recta perpendicular es inf
    En otro caso, se calcula como
     
                -1/m = (A.x-B.x)/(B.y-A.y)      con m la pendiente del segmento AB

    Args:
        A (tuple, optional): primer punto. Defaults to (1,0).
        B (tuple, optional): segundo punto. Defaults to (0,0).

    Returns:
       (float): pendiente de la recta perpendicular al segmento
    """
    
    if A[0] == B[0] :
        return float(0)
    elif A[1]==B[1] and A[0]<=B[0]:
        return -float('inf')
    elif A[1]==B[1] and A[0]>B[0]:
        return float('inf')
    else:
        return 1.0*(A[0]-B[0])/(B[1]-A[1])
       

#def distancia(A,B):
#    #distancia eucludiana entre 2 puntos
#    return sqrt((A[0]-B[0])**2 + (A[1]-B[1])**2) 

def encuentra_minimo(S = [(0,0)],return_elem = False):
    """
    Recibe una lista de puntos 'y' encuentra el punto cuya coordenada 'y' es la menor
    Si 2 o más puntos tienen coordenada 'y' mínima, regresa el punto cuya coordenada x es menor 

    Args:
        S (list, optional): lista de puntos (tuplas (x,y)). Defaults to [(0,0)].
        return_elem (bool, optional): Si es True, regresa el índice y el punto, 
                                      Si es False, regresa sólo el índice 
                                      Defaults to False.

    Returns:
        (tuple): indice y punto (return_elem = True)
        
        (int):indice (return_elem = False)
    """
    min_index = None
    for ind,P in enumerate(S):
        x,y = P
        if min_index == None or y<S[min_index][1]:
            min_index = ind
        if y==S[min_index][1] and x<S[min_index][0]:
            min_index = ind 
    if return_elem:
        return min_index, S[min_index]
    else:
        return min_index
        
    
#________ Algoritmo de graham  ___________________________________________________________________    

def calcula_cierre_convexo(S,show_plot = True):
    """
    Recibe una lista de puntos y calcula su cierre convexo utilizando el algoritmo de Graham
    muestra la gráfca del cierre por Defoult  

    Args:
        S (list): lista de puntos (tuplas (x,y))
        show_plot (bool,optional): Si es True, muestra la gráfica del cierre
                                   Si es False, no la muestra
                                   Defoults to True 

    Returns:
        (list): Lista de vértices del cierre convexo  (tuplas (x,y))
    """
    
    #Primero encontramos el punto con la coordenada x más chica
    p0_idx,p0 = encuentra_minimo(S,return_elem = True)
    
    #Luego, ordenamos los puntos P_i deacuerdo con la pendiente de la recta ortogonal al segmento P_0-P_i
    #Esto garantizará el ordenamiento de los ángulos como se vió en clase 
    S_ord = S.copy() 
    S_ord.pop(p0_idx)
    #print("antes de ordenar >>",S_ord)
        # para ordenar usamos quick sort (O(n log(n)))
    quick_sort(S_ord,0,len(S_ord)-1,lambda p1,p2 : pendiente_ort(p0,p2)<pendiente_ort(p0,p1)) 
    S_ord = [p0]+S_ord #pegamos el punto p0 al principio del arreglo
    #print("ordenados >>",S_ord)
    
    #Comenzamos la pila del cierre convexo con el pinto p0 y el primer punto en orden angular
    CierreConvexo = S_ord[0:2].copy()
    
    for P in S_ord[2:]:    
        #antes de agregar un nuevo punto P a la pila, verificamos que hace un giro en sentido 
        #contrario a las manecillas del reloj (usamos el producto cruz)
        while(producto_cruz(CierreConvexo[-2],CierreConvexo[-1],P)<=0):
            CierreConvexo.pop(-1) #si el giro es al sentido contrario, eliminamos el punto pivote del giro,
                                  #este punto es el último de la pila (porque no hemos añadido al punto P)  
        
        CierreConvexo.append(P) #cuanto ocurre que ya hace un giro en el sentido que se quiere,
                                #lo agregamos y pasamos al siguiente 
    
    print(CierreConvexo)
    
    if show_plot:
        dibuja(S,CierreConvexo,True)  

    return CierreConvexo



