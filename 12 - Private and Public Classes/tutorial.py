import main 
from main import NotPrivate
#from main import _Private ##you can still call private class but a message to other programmers to not modify or call it in scope only

test=NotPrivate('tim')
test.display()
test._display() #you can still call private attribute but a message to other programmers to not modify or call it in scope only
