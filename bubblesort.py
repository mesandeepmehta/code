#bubblesort it is a technique to sort an array on numbers;
def bubblesort(a):
  l=len(a)
  for i in range(l-1):
    for j in range(1,l-i-1):
      if a[j]>a[j+1]:
        a[j],a[j+1]=a[j+1],a[j]
      else:
        pass
  return(a)
b=[2,45,42,85,3,6,5,9,2,2,47,5,21,45,654,56,78,58]
c=bubblesort(b)
print(c)  
