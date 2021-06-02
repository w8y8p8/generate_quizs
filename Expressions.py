#encoding=utf-8

'''
Author: Dou Liyou
Program Time: 2018-07-16
Version: 1.0

Script using: 
    produce numbers
'''
import random
import operateDocx


def givenNum(max=100):
    """
    return an random int between 1 and max
    Usage:
        intNum = givenNum()
        intNum = givenNum(88)
    """
    tNum=random.randint(1,max)
    #尾数为0的数排除掉
    while int(list(str(tNum))[-1])==0:
        tNum=random.randint(1,max)
    return tNum
    
def givenNumWithLimit(givenNum,Operator,max):
    """
    受限数字受限规则:
    1. 如果是加法运算,要求必须进位,结果不超过max
    2. 如果是减法运算,要求必须退位,减数不超过max
    """
	#一个操作数为两位数（10-99）
    _t_min=10
    if Operator == '+':
        target_max=max-givenNum
        #目标数字与给定数字计算必须可以进位
        tnum=random.randint(_t_min,target_max)
        #tnum=random.randint(1,target_max)
        while (int(list(str(tnum))[-1])+int(list(str(givenNum))[-1]))<10:
            tnum=random.randint(_t_min,target_max)
            #tnum=random.randint(1,target_max)
            if int(list(str(givenNum))[-1])==0:
                break
        return tnum               
    elif Operator == '-':
    #目标数字可以取最大值,并且满足减法退位的要求,个位数比被减数小
        target_max=max
        tnum=random.randint(_t_min,target_max)
        #tnum=random.randint(givenNum+1,target_max)
        while int(list(str(tnum))[-1])>=int(list(str(givenNum))[-1]):
            tnum=random.randint(_t_min,target_max)
            #tnum=random.randint(givenNum+1,target_max)
            if int(list(str(givenNum))[-1])==0:
                break
        return tnum
    
def plusExpression(num1,num2):
    """
    return a plus expression str
    """
    n=random.randint(0,1)
    if n==0:
        return str(num1)+ " + "+ str(num2)
    elif n==1:
        return str(num2)+ " + "+ str(num1)
    #return str(num1)+ " + "+ str(num2)
    
def minusExpression(num1,num2):
    """
    return a minus expression str
    """
    return str(num1)+" - "+str(num2)

def randMakeExpression(max=99):
    """
    随机生成表达式:
    100以内，加法进位和减法退位算式
    """
    #max=100
	#一个操作数为一位数（1-9）
    aNum=givenNum(9)
    #aNum=givenNum(max)
    n=random.randint(0,1)
    if n==0:
        return minusExpression(givenNumWithLimit(aNum,'-',max),aNum)
    elif n==1:
        return plusExpression(givenNumWithLimit(aNum,'+',max),aNum)
def createExpressions(max=10):
    """
    批量生成算术表达的方法
    """
    Expressions=[]
    #for i in range(max):
    i = 0;
    while len(Expressions) < max:
        i += 1;
        if (i > 100000 ):
            print "len="+str(len(Expressions))
            print "loop too much in createExpressions!"
            exit(1)
        new_exp = randMakeExpression()+" = ";
        if not new_exp in Expressions:
            Expressions.append(new_exp)
    return Expressions


def randPlusMakeExpression(max=99):
    """
    100以内，加法进位算式
    """
    aNum=givenNum(9)
    #aNum=givenNum(max)
    return plusExpression(givenNumWithLimit(aNum,'+',max),aNum)+" = "

def randMinusMakeExpression(max=99):
    """
    100以内，减法退位算式
    """
    aNum=givenNum(9)
    #aNum=givenNum(max)
    return minusExpression(givenNumWithLimit(aNum,'-',max),aNum)+" = "

def createPlusExpressions2(max=100):
    """
    批量生成加法进位算式各max
    """
    Expressions=[]
    i = 0;
    while len(Expressions) < max:
        i += 1;
        if (i > 100000):
            print "len="+str(len(Expressions))
            print "loop too much in createPlusExpressions2!"
            exit(1)
        new_exp = randPlusMakeExpression()
        if not new_exp in Expressions:
            Expressions.append(new_exp)
    return Expressions

def createMinusExpressions2(max=100):
    """
    批量生成加法进位算式各max
    """
    Expressions=[]
    i = 0;
    while len(Expressions) < max:
        i += 1;
        if (i > 100000):
            print "len="+str(len(Expressions))
            print "loop too much in createMinusExpressions2!"
            exit(1)
        new_exp = randMinusMakeExpression()
        if not new_exp in Expressions:
            Expressions.append(new_exp)
    return Expressions

def createExpressions2(max=100):
    """
    批量生成加法进位和减法退位算式各max个，每页50个加法50个减法
    """
    plusExp = createPlusExpressions2(max)
    minusExp = createMinusExpressions2(max)
    random.shuffle(plusExp)
    random.shuffle(minusExp)
    Expressions=[]
    pageExp = []
    for i in range(max):
        pageExp.append(plusExp[i])
        pageExp.append(minusExp[i])
        if len(pageExp) == 100:
            random.shuffle(pageExp)
            Expressions.extend(pageExp)
            pageExp = []

    return Expressions


if __name__=="__main__":
    """
    以下是测试代码,仅用于验证实现方法准确性
    
    print plusExpression(1,2)
    print minusExpression(2,1)
    n=givenNum(100)
    print n
    print givenNumWithLimit(n,'-',100)
    print givenNumWithLimit(n,'+',100)
    print randMakeExpression()
    print createExpressions(100)
    """
    #生成计算式列表--6000个，默认参数是10个
    myExpressions = createExpressions2(400)
    #myExpressions = createExpressions(6000)
    #将列表中计算式保存到word文件中
    #print myExpressions
    operateDocx.saveExpression(myExpressions, 'newQuiz.docx')
    