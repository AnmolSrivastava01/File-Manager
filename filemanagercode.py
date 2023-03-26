import os
import shutil
path=input("enter ur path:")
files=os.listdir(path)
for i in files:
    #print(i)
    filename , extension =os.path.splitext(i)
    #print(filename)
    #print(extension)
    extension_1=extension[1:]
    #print(extension_1)
    folder_path=path+"\\"+extension_1
    if os.path.exists(folder_path):
        shutil.move(path+"\\"+i,path+"\\"+extension_1+"\\"+i)
        #print("true")  
    else:
        os.makedirs(folder_path)
        shutil.move(path+"\\"+i, path+"\\"+extension_1+"\\"+i)
            
        #print("false")
    
    
