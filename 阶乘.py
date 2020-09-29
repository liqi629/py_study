

def factorial(n):
    if n ==1:
        print ("函数第%d次被调用（倒计）" % n)
        return 1

    else:
        print ("函数第%d次被调用（倒计）"%n)
        return n * factorial(n-1)

num = int(input('请输入'))
res = factorial(num)
print ("%d的阶乘是：%d"%(num, res))
