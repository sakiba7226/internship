import os 
p=os.getcwd()
print(p)
os.chdir('D:/')
print(os.getcwd())    

if not os.path.exists("TempDir"):
    os.mkdir('TempDir')
   