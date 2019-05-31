
def for_deom():
    for i in range(10):
        print("like you")
        print(i)

def for_deom3():
    for i in range(10,20):
        print("like you")
        print(i)

def for_deom1():
    for i in range(2,10,6):
        print(i)
    for i in range(12,7,-2):
        print(i)

def for_list():
    alist=['开','心','1',2,3 ]
   #1
    for i in alist:
        print(i)
    #2
    for i in range(len(alist)):
        print(alist[i])


def for_for():
    for i in range(3):
        print("猪头")
        for j in range(6):
            print('你好',end=",")
        print('\n')

def list_list():
    for i in range(2):
        print("开县")
        for l in range(3):
            print('宝贝',end=',')
        print('\n')

def bb_bb():
    for i in range(6):
        print(i)
        if i ==2:
            break
#break 终止所有循环
#continue停止本次循环,直接进行下一次
    for i in range(3):
        if i ==2:
            continue


if __name__ == '__main__':
    #for_deom()
    #for_deom3()
    #for_deom1()
   #$ for_list()
    #for_for()
    bb_bb()