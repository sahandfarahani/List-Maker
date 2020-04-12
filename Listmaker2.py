import os
from os import path
import pdb
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
import codecs

currentaddress=""
addressfinder=""
extensions=""
global thefilename

def findfolders(address,thefile):
    #list of the files in the mother directory
    newstrdir=os.listdir(address)
    theresfolder=0 
    for i in newstrdir:
        newfolder=address+"\\"+i
        if path.isdir(newfolder):
            thefile.write(i+":\r\n")
            newaddress=address+"\\" +i
            theresfolder=1
            #newfiles=os.listdir(newaddress)
            findfiles(newaddress,thefile,theresfolder)
            findfolders(newaddress,thefile)
            
    
def findfiles(address,thefile,theresfolder):
    global extensions
    theresfile=0
    newstrdir=os.listdir(address)
    for i in newstrdir:
        newfile=address+"\\"+i
        if path.isfile(newfile):
            if extensions:
                if path.splitext(i)[1][1:] in (extensions):
                    theresfile=1
                    filename=path.splitext(i)[0]
                    thefile.write(filename+"\r\n")
            else:
                theresfile=1
                filename=path.splitext(i)[0]
                thefile.write(filename+"\r\n")     
        
    if theresfile==1:
        thefile.write("\r\n")
        
def checkifthereisanyfolder(address,thefile,isthereanyfolderhere):
    newstrdir=os.listdir(address)
    for i in newstrdir:
        newfolder=address+"\\"+i
        if path.isdir(newfolder):
            isthereanyfolderhere=1
            break
            
    if isthereanyfolderhere==0:
        for i in newstrdir:
            newfile=address+"\\"+i
            if path.isfile(newfile):
                filename=path.splitext(i)[0]
                thefile.write(filename+"\r\n")
    if isthereanyfolderhere==0:        
        return True
    else:
        return False
            
class App:
    def __init__(self, statWindow):
        self.thetext = StringVar()
        labeltext=ttk.Label(statWindow, text="Enter Extentions (use , to split) :")
        labeltext.pack()
        text=ttk.Entry(statWindow,)
        text.pack()
        text.insert(0,"txt")
        label=ttk.Label(statWindow, text="Enter Address:")
        label.pack()
        addlabel=ttk.Label(statWindow)
        addlabel.pack()
        buttonenteraddress=ttk.Button(statWindow,text="Enter The Address", command=lambda: self.enteraddress(addlabel))
        buttonenteraddress.pack()
        button = ttk.Button(statWindow, text ="Make The File", command=lambda: self.makefiles(text))
        button.pack()
        quitbutton=ttk.Button(statWindow,text="Quit", command=statWindow.destroy)
        quitbutton.pack()
        statWindow.resizable(False,False)
        
    def makefiles(self,exts):
        global currentaddress
        global extensions
        extension=exts.get()
        if extension:
            extensions=extension.split(",")
        #if the address is chosen
        if addressfinder:
            f=codecs.open(addressfinder,"w+","utf-8")
            isthereanyfolder=0
            #check if there is any folder in the root folder
            isthereanyfolder=checkifthereisanyfolder(currentaddress,f,isthereanyfolder)
            if isthereanyfolder==False:
                findfolders(currentaddress,f)
            f.close
        else:
            messagebox.showerror(title="Error",message="You haven't saved your file yet!")
        
    def enteraddress(self,thelabel):
        global currentaddress
        global addressfinder
        addressfinder=filedialog.asksaveasfilename(title="Save file",filetypes = (("text files","*.txt"),("all files","*.*")),defaultextension=".txt")
        (currentaddress,thefilename)=os.path.split(addressfinder)
        thelabel.config(text=addressfinder)
        
def main():
    mainwindow=Tk()
    app = App(mainwindow)
    mainwindow.mainloop()
    
if __name__=="__main__":
    main()
    