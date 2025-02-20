import random
s = 0
for i in range (10):
    s += random.randint(1,100)
print(s)

def greet():
    """
    Simple function printing hello
    :return:
    """
    print("Hello!")
    return 0

greet()

def greet_new(name):
    """
    More complex that takes a name as param
    :param name: name of pers to greet
    :return: None
    """
    print("fuck off", name)

greet_new("John")

def custom_op(x,y):
    """

    :param x:
    :param y:
    :return:
    """
    result = 10*x + y
    return result

print(custom_op(5,8))