from tkinter import *
root=Tk()

root.title("File Manager")
e=Entry(root)
e.insert(0,"")


def file_manager():
    #import modules
    import os,shutil

    #change of directory    
    path=e.get()
    os.chdir(path)

    #iterate through files
    for (path,dir,files) in os.walk(path):
        for file in files:
            #to get extension of files
            ext=file.split(".")[1] 
            #to check either directory exist
            #if exist
            if os.path.exists(path+"/"+ext):
                if file.endswith(ext):
                    #move file to its respective directory
                    shutil.move(file,path+"/"+ext)
            #if doesn't exists
            else:
                #to create directory
                os.system("mkdir "+ext)
                #move file to its respective directory
                shutil.move(file,path+"/"+ext)

e.pack()
myButton=Button(
    root,
    text="Submit",
    command=file_manager)

myButton.pack()
root.mainloop()