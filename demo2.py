import re;
def demo_re():
    str='123sdak p;;453jglgnajk'
    p1 = re.compile('\W+')
    print p1.findall(str)
demo_re()

def demo():
    print 1
demo()