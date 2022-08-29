import subprocess as sp
import numpy as np
import time

TYPE = 'int32'

def main():
    randNum = input("Valores aleatorios ate (ex:999): ")    #string
    sizeMax = int(input("Quantidade de valores total: "))   #int


    numProcess = 1
    file = open("vector.txt", "w")
    for i in range(sizeMax):

        if i != (sizeMax -1):
            file.write(str(np.random.randint(int(randNum),dtype=TYPE)) +",")
        else:
            file.write(str(np.random.randint(int(randNum),dtype= TYPE)))

    file.close()


    for x in range(5, 1, -1):
        if sizeMax % x == 0:
            print(f"-----Inicio----\n{sizeMax} eh divisivel por: {x}")
            numProcess = x
            break

    if numProcess == 1:
        print("Numero primo! Executando com 1 processo")
    else:
        print(f"MPI sera executado com {numProcess} processos!\n")
    
    procedureProgram = ["python", "selectionSort.py"]
    mpiProgram = ["mpiexec", "/np", str(numProcess), "python", "selectionSort_MPI.py"]
    tempProcedure = 0
    tempMPI = 0

    #PROCEDURAL
    print("Executando Selection Sort Procedural...")
    inicio = time.time()
    p = sp.Popen(procedureProgram, stdout= sp.PIPE, text = True)
    output = p.communicate()
    tempProcedure = float(output[0]) - inicio
    #!PRINT
    print("Tempo gasto: ",tempProcedure)

    # MPI
    print("Executando Selection Sort com MPI...")
    inicio = time.time()
    #//mpiProgram = ["mpiexec", "/np", "8", "python", "selectionSort_MPI.py"]
    p = sp.Popen(mpiProgram, stdin= sp.PIPE, stdout= sp.PIPE, text = True)
    output = p.communicate(randNum)
    tempMPI = float(output[0]) - inicio
    
    #!PRINT
    print("Tempo gasto: ",tempMPI)
    print(f'\nSpeedup: {tempProcedure / tempMPI}')


if __name__ == "__main__":
    main()