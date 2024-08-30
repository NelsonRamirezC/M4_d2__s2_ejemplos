# instalar multipledispatch
from multipledispatch import dispatch
#importante, en consola instalar previamente el módulo con comando pip install multipledispatch

@dispatch(int,int)
def product(first,second):
 result = first*second
 print("primera:", result)
 
@dispatch(int,int,int)
def product(first,second,third):
 result = first * second * third
 print("segunda:", result)
 
@dispatch(float,float,float)
def product(first,second,third):
 result = first * second * third
 print("tercera: ", result)

# haciendo uso de la primera función
product(5, 3) # 8

# haciendo uso de la segunda función
product(2,3,2) # 7

# haciendo uso de la tercera función
product(2.2,3.4,2.3) # 17.204