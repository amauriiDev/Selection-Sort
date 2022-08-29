import time
import numpy as np
from mpi4py import MPI
#RANDNUM = 9999
#SIZEMAX = 100
TYPE = 'int32'

comm = MPI.COMM_WORLD
numprocs = comm.Get_size()
rank = comm.Get_rank()

array = None
#localArray = None
valuesArray = None

# size = 0
# randNum = 0
size = 10
randNum = 99

if (rank == 0):
	#txt = input()
	#randNum = int(txt)

	#!array = np.loadtxt("vector.txt", delimiter=",", dtype=TYPE)
	array = np.random.randint(randNum, size=size, dtype=TYPE)
	valuesArray = np.zeros(numprocs, dtype=TYPE)
	minValue = np.zeros(1, dtype=TYPE)
	size = int(len(array) / numprocs)

	arquivo = open("sortedarrayMPI.txt", "w")
	#arquivo.close()
	#!PRINT
	print("Array :\n",array)
(size,randNum) = comm.bcast((size,randNum), root=0)
array = comm.bcast(array, root=0)

#localArray = np.zeros(size, dtype=TYPE)

## DIVIDIR O ARRAY IGUALMENTE ENTRE OS PROCESSOS
#comm.Scatterv(array, localArray, root=0)

#*ALGORITMO SELECTION SORT
# ORDENAR O ARRAY LOCAL
minIndex = size * rank
maxIndex = size * (rank+1)# - 1

for i in range(minIndex,maxIndex):
	minIndex = i
	for j in range(i+1, maxIndex):
		if array[minIndex] > array[j]:
			minIndex = j
	array[i], array[minIndex] = array[minIndex], array[i]

""" 
count = 0
while count < len(array):
	index = 0
	
	# Menor valor na primeira posição
	# Atribui ao vetor de menor valores
	if len(localArray) > 0 :
		firstValue = localArray[0] 
		#localArray = np.delete(localArray, 0)
	else:
		firstValue = randNum+1

	valuesArray = np.array(comm.gather(firstValue, root=0))


	if rank == 0:

		minIndex = 0

		for x in range(len(valuesArray)):
			if valuesArray[minIndex] > valuesArray[x]:
				minIndex = x

		arquivo.write( str(valuesArray[minIndex]) + ",")

	
	index = comm.bcast(minIndex, root=0)
	if rank == index:
		if (len(localArray) > 0):
			localArray = np.delete(localArray, 0)

	count+=1
 """

if rank == 0:
	#!PRINT
	print("ORDENADO!:\n",array)
	arquivo.close()
	print(time.time())