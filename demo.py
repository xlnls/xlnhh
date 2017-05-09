#coding=utf-8

import requests
import random
import re
from bs4 import BeautifulSoup

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

class User:
    type = 'user'
    def __init__(self,name,uid):
        self.name = name
        self.uid = uid
    def __repr__(self):
        return "i'm"+" "+self.name+' '+str(self.uid)

class Admin(User):
    type = 'admin'
    def __init__(self, name, uid,group):
        User.__init__(self,name,uid)
        self.group = group
    def __repr__(self):
        return "i'm"+' '+self.name+" "+str(self.uid)+' in '+self.group

u1 = User('user1',101)
print u1

ad1 = Admin('admin1',101,'group1')
print ad1.__repr__()

def demo_random():
   # random.seed(1)
    print 1,random.random()
    print 2,random.randint(0,200)
    print 3,random.choice(range(0,100,10))
    print 4,random.sample(range(0,100),5)
    a=[1,2,3,4,5]
    random.shuffle(a)
    print 5,a
demo_random()


def demo_re():
    str = '123hfjsk ;;  789fjsjf '
    p1 = re.compile('\d+')
    p2 = re.compile('\d')
    print p1.findall(str)
    print p2.findall(str)

    str2 = '<html><h>title</h><body>xxx</body></html>'
    p4 = re.compile('<h>([^<]+)</h>')
    print p4.findall(str2)

    str = 'sdhfj2016-06-13sj'
    p5 = re.compile('\d{4}-\d{2}-\d{2}')
    print p5.findall(str)
demo_re()

print 'ls'