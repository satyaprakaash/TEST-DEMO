n= int(input("enter n value: "))
def sum_of_squares(n):
    return sum([i**2 for i in range(1, n+1)])

def square_of_sum(n):
    return sum(range(1, n+1)) ** 2

print square_of_sum(n) - sum_of_squares(n)
