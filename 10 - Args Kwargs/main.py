current_year = 2022

def get_age(yob):
    print(current_year - yob)
    
get_age(1988)

#for multiple people 

def get_ages(yob1,yob2,yob3):
    print([current_year - yob1, current_year - yob2, current_year - yob3])
    
get_ages(1988,1990,1994)

#for multiple people using *args -> get iterable parameter, value count not known yet 

def get_ages_args(*args):
    for yob in args:
        print(f'The age for {yob} is {current_year-yob}')
        
get_ages_args(1988,1990,1994)

#**kwargs  -> key worded arguments, not know amount of values receive for parameter and what parameter receive 

def get_ages_kwargs(**kwargs):
    for k,v in kwargs.items():
        print(k,v)

get_ages_kwargs(name='Jim',yob=1996)


