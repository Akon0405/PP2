def square_generator(N):
    for i in range(1,N+1):
        yield i**2

N = int(input("Enter a number:"))
square_gen = square_generator(N)

for i in square_gen:
    print(i,end=' ') 
