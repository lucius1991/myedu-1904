def assert_int():
    try:
      assert 3>4
      assert 3==3
      assert 2<5
    except:
        print('断言失败')

def assert_str():
    a='成功'
    b='失败'
    try:
        assert  a in b
        assert '成功'=='成功'
        assert  a not in b
    except:
        print('断言失败')

if __name__ == '__main__':
    #assert_str()
    assert_int()