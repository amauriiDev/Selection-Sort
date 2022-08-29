import time
import numpy as np

TYPE = 'int32'
#//RANDNUM = 9999
#//SIZEMAX = 200
#//array = np.random.randint(RANDNUM, size=SIZEMAX, dtype=TYPE)

def main():
    
    array = np.loadtxt("vector.txt", delimiter=",", dtype=TYPE)
    arquivo = open("sortedarray.txt", "w")

    #*ALGORITMO SELECTION SORT
    for i in range(len(array)):
        minIndex = i
        for j in range(i+1, len(array)):
            if array[minIndex] > array[j]:
                minIndex = j
        array[i], array[minIndex] = array[minIndex], array[i]
        arquivo.write(str(array[i]) + ",")

    arquivo.close()

    print(time.time())
    
main()