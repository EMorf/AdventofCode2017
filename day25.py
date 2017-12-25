steps = 12173597 * 2
Z = [None]*steps
mid = 12173597
next = 0

def finalise():
    count = 0
    for i in range(0, steps):
        if Z[i] == 1:
            count = count + 1
    print("We have had", count)

def A():
    global mid
    if(Z[mid] == 0):
        Z[mid] = 1
        mid = mid + 1
        return 2
    else:
        Z[mid] = 0
        mid = mid - 1
        return 3

def B():
    global mid
    if(Z[mid] == 0):
        Z[mid] = 1
        mid = mid - 1
        return 1
    else:
        Z[mid] = 1
        mid = mid + 1
        return 4


def C():
    global mid
    if(Z[mid] == 0):
        Z[mid] = 1
        mid = mid + 1
        return 1
    else:
        Z[mid] = 0
        mid = mid - 1
        return 5


def D():
    global mid
    if(Z[mid] == 0):
        Z[mid] = 1
        mid = mid + 1
        return 1
    else:
        Z[mid] = 0
        mid = mid + 1
    return 2


def E():
    global mid
    if(Z[mid] == 0):
        Z[mid] = 1
        mid = mid - 1
        return 6
    else:
        Z[mid] = 1
        mid = mid - 1
        return 3


def F():
    global mid
    if(Z[mid] == 0):
        Z[mid] = 1
        mid = mid + 1
        return 4
    else:
        Z[mid] = 1
        mid = mid + 1
        return 1


for i in range(0, steps):
    Z[i] = 0

for i in range(0, 12173597):
    if(i == 0):
        next = A()
        continue
    if(next == 1):
        next = A()
        continue
    if(next == 2):
        next = B()
        continue
    if(next == 3):
        next = C()
        continue
    if(next == 4):
        next = D()
        continue
    if(next == 5):
        next = E()
        continue
    if(next == 6):
        next = F()
        continue
finalise()


    
