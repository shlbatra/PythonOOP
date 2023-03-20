print("I am module 1")

print(f"Module 1 : {__name__}")

user="John"
level=1

if __name__=='__main__':
    print("I run directly")  #this function run because module1 file has run directly. 
else:
    print("I did not run directly") #this function runs when module1 is imported in another file and that file is run directly