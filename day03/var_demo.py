avar = '傻瓜'

def c1_avar():
    print(avar)

def c2_avar():
    global avar
    avar='鸡头'
    print(avar)

def c3_aver():
    print(avar)


if __name__ == '__main__':
        c1_avar()
        c2_avar()
        c3_aver()