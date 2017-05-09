#coding=utf-8

def demo_string():
    stra='hello Qorld'
    print stra.capitalize()
    print stra.replace('hell','hh')
    strb ='  hee   \r\n'
    print 1,strb.lstrip()
    print 2,strb.rstrip()
    str2='hhhh'.join([stra,strb])
    print str2
demo_string()

def demo_operator():
    print 1, 1+2,5/2,5*3
    print 2,True,not True
    print 3,1<2,5>3
    print 4,8>>3
demo_operator()

def demo_infunc():
    print 1,max(2,1),min(5,3)
    print len("111111")
def demo_contolflow():
    score =65
    if score >90:
        print 1,'a'
    else :
        print 2,'c'
    while score<100:
        print score
        score+=10

demo_contolflow()