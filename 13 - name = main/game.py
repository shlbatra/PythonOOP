import module1  #Python interpreter reads another source file, sets __name__ for that file and execute the code for that file
#so here also get I am module 1 printed as output. __name__ here for module1 will not be main but module1 -> test if file 
#run directly or via module. 

#from module1 import user #This is same output as import module1 - go through each line of code for module1

print(f"Game File: {__name__}") # output as __main__ -> this file run directly and not imported from another source file

def run():
    print("Game starts")
    
if __name__=='__main__':
    run()  #this function run because game file has run directly. 