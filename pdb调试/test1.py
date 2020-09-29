
def getAverage(a,b):
    result = a+b
    print ("result=%d"%result)
    return result
a = 100
b = 200
c = a+b
ret = getAverage(a,b)
print (ret)


'''

l————  list 显示当前的代码
n———— next 向下执行一行代码
c———— continue 继续执行代码
b———— break 添加断点
clear———— 删除断点
s————— step 进入到一个函数
p————print 打印一个变量的值
a————args 打印所有形参数据
q——————退出调试
r———— return 快速执行到函数的最后一行
F:\study>cd pdb调试
F:\study\pdb调试>python -m pdb test1.py
> f:\study\pdb调试\test1.py(5)<module>()
-> def getAverage(a,b):
(Pdb)
Breakpoint 1 at f:\study\pdb调试\test1.py:9
(Pdb) b
Num Type         Disp Enb   Where
1   breakpoint   keep yes   at f:\study\pdb调试\test1.py:9
(Pdb) b 7
Breakpoint 2 at f:\study\pdb调试\test1.py:7
(Pdb) b
Num Type         Disp Enb   Where
1   breakpoint   keep yes   at f:\study\pdb调试\test1.py:9
2   breakpoint   keep yes   at f:\study\pdb调试\test1.py:7
(Pdb) clear 2
Deleted breakpoint 2 at f:\study\pdb调试\test1.py:7
(Pdb) b
Num Type         Disp Enb   Where
1   breakpoint   keep yes   at f:\study\pdb调试\test1.py:9
(Pdb) s
--Call--
> f:\study\pdb调试\test1.py(2)getAverage()
-> def getAverage(a,b):
(Pdb) l
  1
  2  -> def getAverage(a,b):
  3         result = a+b
  4         print ("result=%d"%result)
  5         return result
  6     a = 100
  7     b = 200
  8     c = a+b
  9 B   ret = getAverage(a,b)
 10     print (ret)
 11
(Pdb) p a
100
(Pdb) p b
200
(Pdb) a
a = 100
b = 200
(Pdb)

'''