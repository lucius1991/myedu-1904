abc = 10
#def:声明方法的关键字;int_demo:方法的名字;后面的():是固定写法
def int_demo():

    # 声明一个变量,=号前面是变量名aint,=后面是变量名,int是数据类型
    aint = 5

    # type(aint):获取aint的变量类型,print打印出它的类型
    print(type(aint))

def str_demo():
    astr = '5'

    print(type(astr))

def nihao():
     bint = 10
     print(type(bint))

def hello():
    cstr = '你好'
    print(type(cstr))

def world():
    efloat = 1.5
    print(type(efloat))
    print(abc)

def type_zhuanhuan():
    h = 20
    print(type(h))
    print(type(str(h)))

def type_zhuanhuan1():
    g = '20'
    print(type(g))
    print(type(int(g)))

def difference_join():
    q = 456
    w = 'Hello world'
    e = 'I believe I can fly'
    # print('%s,%s,%s'%(q,w,e))
    # print(str(q)+w+e)
    # print('%s %s. %s. '%(q,w,e))

def add(a,b):
    print(a)
    print(b)
    print(a+b)
    return a+b


#这是一个main方法,可以直接执行,main方法下面不能再有其他方法
if __name__ == '__main__':
    # print('Hello world')

    # int_demo()
    # str_demo()
    # nihao()
    # hello()
    # world()
    # type_zhuanhuan()
    # type_zhuanhuan1()
    # g = difference_join()
    # print(g)
    # f = add(10,15)

    a = 'sdklfjg;kfgslkflssl;kf'
    print(a[0])
    print(a[5:])
    print(a[1:5])
    print(a[-1])
    print(a[-8])
    print(a[::-1])
    print(a[::-2])