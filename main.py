import  graham
import sys

def main():
    if sys.argv[1]== '0':
        print("Set de puntos extraidos del archivo points.txt")
        with open('points.txt') as f:
            w, h = [int(x) for x in next(f).split()] # read first line
            S = []
            for line in f: # read rest of lines
                S.append(tuple([int(x) for x in line.split()]))
                    
    else:
        print("Se generaran n puntos aleatoriamente")
        n = input("ingrese valor de n : ")
        S = graham.genera_puntos(int(n))
            
    graham.calcula_cierre_convexo(S)
    return 0

if __name__ == "__main__":
    main()