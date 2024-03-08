#The starter file.
#
# By --
'''
from words import words as w


word = input('> ')
'''

from words import words as w

def a(w,e):
    for o in range(len(w)):
        for i in w:
            if i in e:
                e = Nstr1(e)-Nstr1(i)
    return e

# The str can't to '-'
#But Nstr1 can!
class Nstr1:
    def __init__(self, arg):
        self.x=arg
    def __sub__(self,other):
        c=self.x.replace(other.x,"")
        return c
        
while 1:
    word = input('> ')
             
    print('Wrong words:',a(w,word))
    
#end
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
