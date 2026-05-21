a = 31
t = type(a)
print(t) # <class 'int'>    

b = 2.5
t = type(b) 
print(t) # <class 'float'>

b = "2.5" # b is now a string
t = float(b) # convert string to float
print(t) # 2.5  


c = "Hello"
t = type(c)     
print(t) # <class 'str'>

d = True
t = type(d)     
print(t) # <class 'bool'>

e = None
t = type(e) 
print(t) # <class 'NoneType'>