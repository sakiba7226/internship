import os 
a = input("enter your name:")
print(a)
if not os.path.exists(a):
    os.mkdir(a)