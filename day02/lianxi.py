
#这是一个列表的数据类型,英文是list,也叫数组

alist = ['你好',10,15,20,'world']

#查询
def list_test():

    print(alist[0])
    print(alist[0:1])
    取倒数第三位
    print(alist[6:7])
    print(alist[-3])
    #第5个开始到后面所有
    print(alist[4:])
    print(alist[:4])

#删除
def list_del():
    alist.pop()
    print(alist)
    alist.pop(4)
    a = alist.pop(4)
    print(alist)

#增加
def list_add():
    blist = ['Hello',5,6,7,8]
    # blist.append('world')
    # print(blist)
    clist = ['Blue','Sky']
    blist.extend(clist)
    # blist.append(clist)
    print(blist)

#更改
def list_update():
    dlist = [5,'believe','can fly']
    dlist[0] = 'I'
    dlist[2] = 200
    print(dlist)

#排序
def list_order_by():
    elist = [5,7,3,11,1,2,4]
    elist.sort()
    # elist.sort(reverse=True)
    print(elist)

#去重
def list_distinct():
    flist = [1,1,1,4,5,6,7,7,8]
    flist = set(flist)
    print(flist)
    print(len(flist))


def list_sel():
    print(alist[2])
    print(alist[1:4])

def list_de():
    alist = ['你好', 10, 15, 20, 'world']
    alist.pop(3)
    print(alist)

def list_ad():
    alist = ['你好', 10, 15, 20, 'world']
    alist.append(5)


if __name__ == '__main__':
        # list_test()
        # list_del()
        # list_add()
        # list_update()
        # list_order_by()
        # list_distinct()
        list_sel()
        list_de()