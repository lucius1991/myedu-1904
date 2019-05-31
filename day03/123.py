def list_ok():
    a=22
    b=11
    try:
        assert 3>2
        assert 2<3
        assert a>b
        print('断言成功')

    except:
        print('失败')
if __name__ == '__main__':
    list_ok()