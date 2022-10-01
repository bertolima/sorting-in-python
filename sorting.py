def countingSort(lista, n=None, r=None):
  if n is None:  #get size of list
    n = len(lista)
  if r is None:  #get value of max item on the list
    r = max(lista)+1
  ocorrencias = [0] * r        #create a auxliar list to count how numbers appears
  ocorrencias_pred = [0] * r   #create a auxiliar list to count how many times a number appears
  aux = [0] * n                #create a auxiliar list to get the sorted elements of the list

  for i in range(n):
    ocorrencias[lista[i]] +=1  #add +1 to position ocorrencias[i] when we have lista[i] = number and ocorrencias[number]
  
  ocorrencias_pred[0] = 0
  for valor in range(1, r):
    ocorrencias_pred[valor] = ocorrencias_pred[valor-1] + ocorrencias[valor-1]    
  
  for i in range(n):
    valor = lista[i]
    aux[ocorrencias_pred[valor]] = lista[i]
    ocorrencias_pred[valor] +=1

  for i in range(n):
    lista[i] = aux[i]
