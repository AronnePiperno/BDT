import random


def warmup(a,b):
    a = int(input('insert an integer: '))
    b = int(input('insert an integer: '))
    if a*b > 1000:
        return 'greater than 1000'
    else:
        return a*b

def ex2(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False
        
def fibonacci():
    n = int(input('Insert a number: '))
    liston = [0,1]
    for i in range(2, 100):
        liston.append(liston[i-1] + liston[i-2])
    
    return n in liston

def pantry():
    recipe = {'eggs' : 2, 'flour': 200, 'milk': 100}
    pantry = {'eggs': 12, 'flour': 1000, 'milk': 250, 'apple': 2, 'sugar': 850}
    liston = []
    for k in recipe:
        if k in pantry:
            if pantry[k] > recipe[k]:
                liston.append(pantry[k] // recipe[k])
        else:
            return 0
        
    return min(liston)


def ex5():
    n = int(input('Insert a number: '))
    summy = 0
    for i in range(1,n+1):
        summy += i/(i+1)
    return summy


def ex6():
    
    return_value = random.randint(0,100)
    while return_value % 2 == 0:
        return_value = random.randint(0,100)
    
    return return_value


def ex7(liston):
    for n in range(0, len(liston),2):
        print(liston[n])


print(ex2(21004))

#ex7([3,2,4,5])
#print(pantry())



#print(fibonacci())