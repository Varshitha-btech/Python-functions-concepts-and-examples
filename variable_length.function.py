def result(name,*marks):
    print("name of student:",name)
    total=sum(marks)
    nc=len(marks)
    cgpa=total/nc
   # print("total marks are :",total)
   # print("total no of coures:",nc)
    print("CGPA is:",cgpa)
result("varsha",80,89,90,98,87)
