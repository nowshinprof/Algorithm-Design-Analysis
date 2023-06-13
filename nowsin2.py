def selection_sort (A) :
    n= len(A) 
    for i in range (n) :
        min_index =i
        for j in  range (i+1, n):
            if A[j] < A[min_index]:
                min_index = j
        tmp =A[i]
        A[i] =A [min_index]
        A[min_index] = tmp
        
A= [2,10,1,50,15]
selection_sort(A)
for i in range (len(A)):
    print(A[i],end=' ')
                
                
        
            
        