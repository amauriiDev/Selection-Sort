import time
import numpy as np
from mpi4py import MPI
#//RANDNUM = 9999
#//SIZEMAX = 4096
TYPE = 'int32'

comm = MPI.COMM_WORLD
numprocs = comm.Get_size()
rank = comm.Get_rank()

array = None
localArray = None
valuesArray = None
size = 0
randNum = 0

if (rank == 0):
	#//randNum = 999
	txt = input()
	randNum = int(txt)

	array = np.loadtxt("vector.txt", delimiter=",", dtype=TYPE)
	#//array = np.random.randint(RANDNUM, size=SIZEMAX, dtype=TYPE)
	size = int(len(array) / numprocs)
	arquivo = open("sortedarrayMPI.txt", "w")

(size,randNum) = comm.bcast((size,randNum), root=0)

valuesArray = np.zeros(numprocs, dtype=TYPE)
localArray = np.zeros(size, dtype=TYPE)

## DIVIDIR O ARRAY IGUALMENTE ENTRE OS PROCESSOS
comm.Scatterv(array, localArray, root=0)

#*ALGORITMO SELECTION SORT
# ORDENAR O ARRAY LOCAL
minIndex = 0#i
for i in range(len(localArray)):
	minIndex = i
	for j in range(i+1, len(localArray)):
		if localArray[minIndex] > localArray[j]:
			minIndex = j
	localArray[i], localArray[minIndex] = localArray[minIndex], localArray[i]

# Executar até o tamanho máximo do arquivo
count = 0
max = size * numprocs
while count < max:
	index = 0
		
	# Menor valor na primeira posição
	# Atribui ao vetor de menor valores
	if len(localArray) > 0:
		firstValue = localArray[0] 
	else:
		firstValue = randNum+1

	valuesArray = comm.gather(firstValue, root=0)

	if rank == 0:
		minIndex = 0
		for x in range(len(valuesArray)):
			if valuesArray[minIndex] > valuesArray[x]:
				minIndex = x

		arquivo.write(str(valuesArray[minIndex]) + ",")


	index = comm.bcast(minIndex, root=0)
	if rank == index:
		localArray = np.delete(localArray, 0)

	count+=1

if rank == 0:
	arquivo.close()
	print(time.time())