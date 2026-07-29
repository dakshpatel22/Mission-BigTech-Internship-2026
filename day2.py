# # print 0 to 4
# for i in range(5):
#     print(i)

# # print 1 to 5
# for i in range(1,6):
#     print(i)

# # print 1 to 11 odd 
# for i in range(1,12,2):
#     print(i)    

# # print 10 to 1 
# for i in range(10,0,-1):
#     print(i)    

# # print 0 to 10 even
# for i in range(0,11,2):
#     print(i)    

# # print 5 table
# for i in range(1,11):
#     print(f"5 * {i} = {5*i}")    

# # print sum of 1 to 100
# sum = 0
# for i in range(0,101):
#     sum += i
# print(sum)    

# # print sequre of 1 to 50
# for i in range(0,51):
#     print(i*i)

# # print 20 to 1 using while loop
# i = 20 
# while i >= 1:
#     print(i)
#     i -= 1     

# # 9 table using while loop 
# i = 1 
# while i <= 10:
#     print(f"9 * {i} = {i*9}")
#     i += 1

# # number divisible by 5 in 1 to 100 
# i = 1
# while i <= 100:
#     if i % 5 == 0:
#         print(i)
#     i += 1    

# # factorial of number 
# n = int(input("enter the number"))
# result = 1
# i = 1
# while i <= n:
#     result *= i
#     i += 1
# print(result)    

# # table using while 
# n = int(input())
# i = 1
# while i <= 10:
#     print(f"{n} * {i} = {n*i}")
#     i += 1

# # sum of all even numbers of 1 to 22
# sum = 0
# i = 1
# while i <= 22:
#     if i % 2 == 0:
#         sum += i
#     i += 1
# print(sum)        

# pattern making 
for i in range(6,0,-1):
    for j in range(i):
        print("*", end = "")
    print()    

# number pattern
for i in range(1, 6):
    for j in range(1, i+1):
        print(j, end ="")
    print()    
    
# new one 
for i in range(1, 6):
    for j in range(i):
        print(i, end ="")
    print()   

# square pattern
for i in range(1, 6):
    for j in range(5):
        print("*", end ="")
    print()   

