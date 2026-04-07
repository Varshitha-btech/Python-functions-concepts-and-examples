def find_max(numbers):
    return max(numbers)
def find_min(numbers):
    return min(numbers)
def find_sum(numbers):
    return sum(numbers)
def apply_transformation(numbers,func):
    return list(map(func,numbers))
numbers=list(map(int,input("enter the numbers by using space:",).split()))
maximum=find_max(numbers)
minimum=find_min(numbers)
total=find_sum(numbers)
doubled_numbers=apply_transformation(numbers,lambda x:x*2)
print("Original list:",numbers)
print("Maximum:",maximum)
print("Minimum:",minimum)
print("Sum:",total)
print("Doubled list:",doubled_numbers)

