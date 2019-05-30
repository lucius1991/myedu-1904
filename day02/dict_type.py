import json

#字典,被{}抱起来,里面是键值对,:前面是K,:后面是value,多个键值对用逗号分隔开.字典是无序的,没有索引,只能用K查找value,K不能重复
adict = {'username':'admin','password':'123456'}

def dict_sel():
    print(adict['username'])

def dict_update():
    adict['username'] = 'Hello'
    print(adict)

def dict_del():
    adict.pop('username')
    print(adict)
#参数类型入参排序中,元组排倒数第二,字典排最后
def dict_add():
    adict['age'] = 25
    print(adict)
    bdict = {'list':[1,2,3],'tuple':(1,2,3)}
    adict.update(bdict)
    print(adict)
    cdict = {'type':'int','sex':'male'}
    ddict = dict(adict,**cdict)
    print(ddict)

def dict_zhuanhuan():
    print(type(adict))
    str_dict = json.dumps(adict)
    print(type(str_dict))

    dict_str = '{"username":"admin","password":"123456"}'
    print(type(dict_str))
    liu = json.loads(dict_str)
    print(type(liu))

#新建一个字典
bdict = {'age':25,'sex':'male'}

def dict_1():
    #访问一个值
    print(bdict['age'])
    #更改一个值
    bdict['age'] =26
    #添加一个键值对
    bdict['Hi'] = 'Blue Sky'
    #删除一个值
    bdict.pop('sex')
    print(bdict)
    #新建一个字典合并
    cdict = {'Hello':'World'}
    bdict.update(cdict)
    print(bdict)



if __name__ == '__main__':
    # dict_sel()
    # dict_update()
    # dict_del()
    # dict_add()
    # dict_zhuanhuan()
    dict_1()