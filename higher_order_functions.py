numbers=list(map(int,input("enter the integers with space:",).split()))
squared_numbers=list(map(lambda x:x*x,numbers))
even_numbers=list(filter(lambda x:x%2==0,numbers))
from functools import reduce
total_sum=reduce(lambda x,y:x+y,numbers)
print("original list:",numbers)
print("square numbers:",squared_numbers)
print("even numbers:",even_numbers)
print("total sum:",total_sum)