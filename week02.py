# WRITE YOUR CODE HERE

def greet(name):
    print("Hello " + name + ". How are you")

name = [Alex]

my_friends = [Alex, Stormy, Lewis]

for friend in my_friends
    greet(friend)



def solve_quadratic(a: int, b: int, c: int) -> bool:
    d = (b*b) - (4*a*c)
    if d < 0:
        print("No real solutions")
        return False
        #no solutions w integers
    else:
        x1 = (-b - (d**0.5)) / (2*a)
        x2 = (-b + (d**0.5)) / (2*a)
        print (x1, "and ", x2)
        return True
        #solutions when integers

solve_quadratic(1, 5, 1)





