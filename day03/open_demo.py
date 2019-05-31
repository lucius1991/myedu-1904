
def open_like():

    text_io =open ('text.text','w+')
    for i in range(5):
            text_io.write('张雪茹123\n')

def de_oo():
    text_io = open('text.text','r')
    print(text_io.readline())





if __name__ == '__main__':
    de_oo()
