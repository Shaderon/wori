from tkinter import *
import wordi_functions as f
import goslate
import bing_get as b
import random
from PIL import Image,ImageTk
import time
import queue
import threading
import pickle
import os
from tkinter import ttk
#GLOBAL VARIABLES
global_path="D:/wordi project"
en=pickle.load( open( "en_dict.p", "rb" ) )
de=pickle.load( open( "de_dict.p", "rb" ) )
newe=pickle.load( open( "newe_dict.p", "rb" ) )
image=""
learndict={}
target_language="cs"
language="en"
counter=0
allwords=[]
a=[]
flip=0
binary=0
begin=0
gs=goslate.Goslate()
saveadjstate=DISABLED
sensaveadjstate=DISABLED
#END OF GLOBAL VARIABLES

#IMPORT,QUIT BLOCK
def clear_pickles():
    global en
    global de
    global newe
    en={}
    de={}
    newe={}
    pickle.dump( en, open( "en_dict.p", "wb" ) )
    pickle.dump( de, open( "de_dict.p", "wb" ) )
    pickle.dump( newe, open( "newe_dict.p", "wb" ) )
    return
def places_forget():
    logap.place_forget()
    internetimage.place_forget()
    back.grid_forget()
    forth.grid_forget()
    sentenci.place_forget()
    ask.place_forget()
    yes.place_forget()
    no.place_forget()
    nextsen.place_forget()
    translation.place_forget()
    adjustentry.place_forget()
    saveadjustentry.place_forget()
    senadjustentry.place_forget()
    savesenadjusted.place_forget()
    fin.place_forget()
    opentext.place_forget()
    createfile.place_forget()
    filename.place_forget()
    succes.place_forget()
    failed.place_forget()
    choosebox.place_forget()
    learnit.place_forget()
    showhide.place_forget()
    cor_fal.place_forget()
    correct.place_forget()
    wrong.place_forget()
    nomore.place_forget()
    examination.place_forget()
    return
def polish_less(listi):
    for item in listi:
        if item=="":
            listi.remove(item)
        elif item==" ":
            listi.remove(item)
    
    return listi        
def polish(listi):
    i=0
    j=0
    for sen in listi:
        if sen==[""]:
            listi.remove(sen)
        if i>=len(listi):
            break
        for word in sen:
            if j>=len(listi[i]):
                break
            listi[i][j]=listi[i][j].replace(",","")
            listi[i][j]=listi[i][j].replace("1","")
            listi[i][j]=listi[i][j].replace("2","")
            listi[i][j]=listi[i][j].replace("3","")
            listi[i][j]=listi[i][j].replace("4","")
            listi[i][j]=listi[i][j].replace("5","")
            listi[i][j]=listi[i][j].replace("6","")
            listi[i][j]=listi[i][j].replace("7","")
            listi[i][j]=listi[i][j].replace("8","")
            listi[i][j]=listi[i][j].replace("9","")
            listi[i][j]=listi[i][j].replace("0","")
            listi[i][j]=listi[i][j].replace(",","")
            listi[i][j]=listi[i][j].lower()
            if listi[i][j]=="":
                listi[i].remove(listi[i][j])
            j=j+1
            if j>=len(listi[i]):
                break
        if sen==[""]:
            listi.remove(sen)
        elif sen==[]:
            listi.remove(sen)
        i=i+1
        j=0
    return listi
    

def download():
    for sen in allwords:
        for word in sen:
            if os.path.isfile("D:/wordi project/images/%s"%(word+"1.jpg")):
                pass
            
            else:
                b.getpic(word)

    return           
    
def handle_picture(word):
    global finalimage
    global image
    try:
        image=word+str(random.randrange(1,3))+".jpg"
        imagepath="D:/wordi project/images/%s"%(image)
        finalimage=ImageTk.PhotoImage(Image.open(imagepath))
        internetimage.configure(image=finalimage)
    except:
        print("FAILED")
    return
    
def change_state1(*args):
    if adjusted.get()!="":
        saveadjustentry.config(state="active")
    elif adjusted.get()=="":
        saveadjustentry.config(state="disabled")
        
    return
def change_state2(*args):
    if senadjusted.get()!="":
        savesenadjusted.config(state="active")
    elif senadjusted.get()=="":
        savesenadjusted.config(state="disabled")
    return
def correct_word():
    y=adjusted.get()
    cell.set(y)
    return
def correct_sen():
    y=senadjusted.get()
    translated.set(y)
    return
def change():
    global language
    if language=="en":
        language="de"
    else:
        language="en"
    return
    
def quiti():
    exiti=messagebox.askyesno(title="quit?",message="Are you sure you want to exit Wordi?")
    if exiti:
        gui.destroy()
        return
def openo():
    gui.geometry("840x750+100+100")
    places_forget()
    sentenci.place(x=50,y=100)
    ask.place(x=400,y=80)
    yes.place(x=50,y=140)
    no.place(x=50,y=190)
    nextsen.place(x=400,y=250)
    translation.place(x=50,y=220)
    adjustentry.place(x=50,y=270)
    saveadjustentry.place(x=50,y=240)
    senadjustentry.place(x=350,y=270)
    savesenadjusted.place(x=350,y=240)
    internetimage.place(x=0,y=300)
    main()
    t=threading.Thread(target=download)
    progressbar.place(x=100,y=100)
    progressbar.start()
    progressbar.after(10000, stop_progressbar)
    t.start()
    #time.sleep(10)
    return
def stop_progressbar():
    progressbar.stop()
    progressbar.place_forget()
    initial()
def main():
    try:
        importopen=filedialog.askopenfile(filetypes=[("Text files","*.txt")])
        data=importopen.read()
        global startlanguage
        language=gs.detect(data)
        c=importi(data)
        for sen in a:
            allwords.append(sen.split(" "))
            
        polish(allwords)
        polish(allwords)
        
        
    except:
        pass
    return
def initial():
    global flip
    global now
    try:
        while check_ifin(allwords[counter][flip],en,de,newe)==1:
                counting()
                barier(flip,allwords[counter])
        barier(flip,allwords[counter])
        sentenci.insert(1.0,a[counter])
        now=a[counter].split(" ")
        polish_less(now)
        translated.set(gs.translate(a[counter],target_language,language))
        sentenci.tag_add("mytag","1.%s"%(str(a[counter].index(now[flip],begin))),"1.%s"%(str(int(a[counter].index(now[flip],begin))+int(len(now[flip])))))
        sentenci.tag_config("mytag",foreground="blue",background="red")
        sentenci.configure(state="disabled")
        cell.set(allwords[counter][flip]+"-"+gs.translate(allwords[counter][flip],target_language,language))
        handle_picture(allwords[counter][flip])
    except:
        raise
    
    
    
    return

def importi(data):
    global a
    a=data.split(".")
    return a

def counting():
    global flip
    flip=flip+1
    return
def check_ifin(word,list1,list2,list3):
    if word in list1:
        return 1
    if word in list2:
        return 1
    if word in list3:
        return 1
    
    return 0
def barier(var,listi):
    if var>len(listi)-1:
        alghoritm_next()
    if counter>len(allwords)-1:
        finish()
        return 
    
    return
def finish():
    global en
    global de
    global newe
    global begin
    yes.place_forget()
    no.place_forget()
    nextsen.place_forget()
    ask.place_forget()
    sentenci.place_forget()
    translation.place_forget()
    adjustentry.place_forget()
    saveadjustentry.place_forget()
    senadjustentry.place_forget()
    savesenadjusted.place_forget()
    logap.place(x=140,y=100)
    internetimage.place_forget()
    begin=0
    fin.place(x=250,y=100)
    pickle.dump( en, open( "en_dict.p", "wb" ) )
    pickle.dump( de, open( "de_dict.p", "wb" ) )
    pickle.dump( newe, open( "newe_dict.p", "wb" ) )
    return
def alghoritm_next():
    pickle.dump( en, open( "en_dict.p", "wb" ) )
    pickle.dump( de, open( "de_dict.p", "wb" ) )
    pickle.dump( newe, open( "newe_dict.p", "wb" ) )
    global counter
    if counter>len(allwords)-1:
        finish()
    else:
        global translated
        global flip
        global now
        global begin
        save=open("simpletranslation","a")
        save.write(str(translated.get()+"\n"))
        save.close()
        sentenci.configure(state="normal")
        sentenci.delete(1.0,"1.%s"%(len(a[counter])))
        counter=counter+1
        now=a[counter].split(" ")
        polish_less(now)
        sentenci.insert(1.0,a[counter])
        translated.set(gs.translate(a[counter],target_language,language))
        sentenci.tag_delete("mytag")
        flip=0
        begin=0
        sentenci.tag_add("mytag","1.%s"%(str(a[counter].index(now[flip],begin))),"1.%s"%(str(int(a[counter].index(now[flip],begin))+int(len(now[flip])))))
        sentenci.tag_config("mytag",foreground="blue",background="red")
        sentenci.configure(state="disabled")
    return    
def alghoritm_yes():
    barier(flip,allwords[counter])
    global cell
    global begin
    begin=begin+len(allwords[counter][flip])
    word=allwords[counter][flip]+"-"+gs.translate(allwords[counter][flip],target_language,language)
    if language=="en":
        fh=open("word_libraryEN.txt","a")
        fh.write(str(cell.get())+"\n")
        fh.close()
        en[allwords[counter][flip]]= str(cell.get())[str(cell.get()).index("-")+1:]
    if language=="de":
        deh=open("word_libraryDE.txt","a")
        deh.write(str(cell.get())+"\n")
        deh.close()
        de[allwords[counter][flip]]= str(cell.get())[str(cell.get()).index("-")+1:]
    counting()
        
    try:
        barier(flip,allwords[counter])
        if check_ifin(allwords[counter][flip],en,de,newe)==1:
            while check_ifin(allwords[counter][flip],en,de,newe)==1:
                counting()
                barier(flip,allwords[counter])
            else:
                pass
        sentenci.configure(state="normal")
        sentenci.tag_delete("mytag")
        sentenci.tag_add("mytag","1.%s"%(str(a[counter].index(now[flip],begin))),"1.%s"%(str(int(a[counter].index(now[flip],begin))+int(len(now[flip])))))
        sentenci.tag_config("mytag",foreground="blue",background="red")
        sentenci.configure(state="disabled")    
        cell.set(allwords[counter][flip]+"-"+gs.translate(allwords[counter][flip],target_language,language))
        handle_picture(allwords[counter][flip])
    except:
        raise#print("END")
    return
def alghoritm_no():
    barier(flip,allwords[counter])
    global cell
    global begin
    begin=begin+len(allwords[counter][flip])
    word=allwords[counter][flip]+"-"+gs.translate(allwords[counter][flip],target_language,language)
    new=open("word_libraryNEW.txt","a")
    new.write(str(cell.get())+"\n")
    new.close()
    newe[allwords[counter][flip]]= str(cell.get())[str(cell.get()).index("-")+1:]
    counting()
       
    try:
        barier(flip,allwords[counter])
        if check_ifin(allwords[counter][flip],en,de,newe)==1:
            while check_ifin(allwords[counter][flip],en,de,newe)==1:
                counting()
                barier(flip,allwords[counter])
            else:
                pass
        sentenci.configure(state="normal")
        sentenci.tag_delete("mytag")
        sentenci.tag_add("mytag","1.%s"%(str(a[counter].index(now[flip],begin))),"1.%s"%(str(int(a[counter].index(now[flip],begin))+int(len(now[flip])))))
        sentenci.tag_config("mytag",foreground="blue",background="red")
        sentenci.configure(state="disabled")    
        cell.set(allwords[counter][flip]+"-"+gs.translate(allwords[counter][flip],target_language,language))
        handle_picture(allwords[counter][flip])
    except:
        print("END")
    return 
#END OF IMPORT,QUIT

#LEARN BLOCK
def learno():
    gui.geometry("1000x550+100+100")
    places_forget()
    choosebox.place(x=840,y=0)
    learnit.place(x=840,y=470)
    examination.place(x=840,y=520)
    detect_file()
    logap.place(x=140,y=100)
    return
def detect_file():
    x=0
    for file in os.listdir(global_path):
        if ".wordi" in file:
            choosebox.insert(x,file)
            x=x+1
    return        
def alghoritm_learn():
    global counter
    global myvariables
    counter=0
    ask.place(x=300,y=40)
    showhide.place(x=300,y=90)
    back.grid(row=1,column=0,sticky=W)
    forth.grid(row=1,column=4,sticky=E)
    keywords=list(newe.keys())
    cor_fal.place(x=300,y=120)
    cor_fal.bind("<Return>",checkinput)
    global learndict
    learndict={}
    myvariables=[]
    words=[]
    logap.place_forget()
    file=str(choosebox.get(ACTIVE))
    with open(file,"r") as f:
        r=f.read()
        worde=r.split(".")
        for sen in worde:
            words.append(sen.split(" "))
            polish(words)
        f.close()
    for sen in words:
        for word in sen:
            if word in keywords:
                learndict[word]=newe[word]
    myvariables=list(learndict.keys())
    if counter>=len(myvariables):
        print("No words")
    else:
        cell.set(myvariables[counter])
        translated.set(learndict[myvariables[counter]])
        handle_picture(myvariables[counter])
    return 
def alghoritm_show():
    global binary
    if binary==0:
        showhide["text"]="Hide answer!"
        internetimage.place(x=0,y=200)
        translation.place(x=300,y=60)
        binary=1
        
    elif binary==1:
        showhide["text"]="Show answer!"
        internetimage.place_forget()
        translation.place_forget()
        binary=0
        
    return
def forthin():
    global counter
    nomore.place_forget()
    correct.place_forget()
    wrong.place_forget()
    counter=counter+1
    check_index()
    return
def backin():
    global counter
    nomore.place_forget()
    correct.place_forget()
    wrong.place_forget()
    counter=counter-1
    check_index()
    return
def checkinput(event):
    correct.place_forget()
    wrong.place_forget()
    if enter.get()==learndict[myvariables[counter]]:
        correct.place(x=300,y=250)
    else:
        wrong.place(x=300,y=250)
    return
def check_index():
    global counter
    if counter>=len(myvariables):
        nomore.place(x=300,y=250)
        counter=0
    else:
        cell.set(myvariables[counter])
        translated.set(learndict[myvariables[counter]])
        handle_picture(myvariables[counter])
    return    
def exam_me():
    global counter
    global myvariables
    counter=0
    ask.place(x=300,y=40)
    back.grid(row=1,column=0,sticky=W)
    forth.grid(row=1,column=4,sticky=E)
    keywords=list(newe.keys())
    cor_fal.place(x=300,y=120)
    cor_fal.bind("<Return>",checkinput)
    global learndict
    learndict={}
    myvariables=[]
    words=[]
    logap.place_forget()
    file=str(choosebox.get(ACTIVE))
    with open(file,"r") as f:
        r=f.read()
        worde=r.split(".")
        for sen in worde:
            words.append(sen.split(" "))
            polish(words)
        f.close()
    for sen in words:
        for word in sen:
            if word in keywords:
                learndict[word]=newe[word]
    myvariables=list(learndict.keys())
    if counter>=len(myvariables):
        print("No words")
    else:
        cell.set(myvariables[counter])
        translated.set(learndict[myvariables[counter]])
        handle_picture(myvariables[counter])
    return 
    
#END OF LEARN BLOCK

#OPEN BLOCK
def textigui():
    places_forget()
    opentext.place(x=0,y=30)
    createfile.place(x=0,y=30)
    filename.place(x=150,y=30)
    
    return
def create_wordi():
    alltext=str(opentext.get("1.0",'end-1c'))
    name=str(named.get())+".wordi.txt"
    file = open(name,'a')
    file.write(alltext)
    file.close()
    if os.path.isfile(name):
        succes.place(x=200,y=200)
    else:
        failed.place(x=200,y=200)
    
    
    return
#END OF OPEN BLOCK

#GUI BLOCK   
gui=Tk()
gui.title("Wordi")
gui.geometry("840x550+100+100")
gui.configure(background="white")

wmenu=Menu(gui)

wordimenu=Menu(wmenu, tearoff=0)
wordimenu.add_command(label="learn",command=learno)
wordimenu.add_command(label="import",command=openo)
wordimenu.add_command(label="open",command=textigui)
wordimenu.add_checkbutton(label="deutsch",command=change)
wordimenu.add_command(label="configure",command=f.a)
wmenu.add_cascade(label="Wordi",menu=wordimenu)

wmenu.add_command(label="Stacistics",command=f.a)

aboutmenu=Menu(wmenu, tearoff=0)
aboutmenu.add_command(label="This program",command=f.a)
aboutmenu.add_command(label="About me",command=f.a)
wmenu.add_cascade(label="About", menu=aboutmenu)

wmenu.add_command(label="Help",command=f.a)
wmenu.add_command(label="Quit",command=quiti)

gui.configure(menu=wmenu)
forthi=PhotoImage(file="forth.gif")
backi=PhotoImage(file="back.gif")
textversion=PhotoImage(file="textv.gif")
movieversion=PhotoImage(file="moviev.gif")
importphoto=PhotoImage(file="import_button.gif")
backgroundi=PhotoImage(file="background.gif")
learnphoto=PhotoImage(file="learn_button.gif")
openphoto=PhotoImage(file="open_button.gif")
configurephoto=PhotoImage(file="configure_button.gif")
logo=PhotoImage(file="Wordilogo.gif")
languagephoto=PhotoImage(file="language_button.gif")

background_label=Label(gui,image=backgroundi)
back=Button(gui,image=backi,command=backin,bd=0)#.grid(row=0,column=0)
forth=Button(gui,image=forthi,command=forthin,bd=0)#.grid(row=0,column=1)
textv=Button(gui, image=textversion, command=f.a)#.grid(row=0,column=3,sticky=N)
moviev=Button(gui,image=movieversion, command=f.a)#.grid(row=0,column=5,sticky=N)
import_button=Button(gui,image=importphoto,command=openo,bd=0)
open_button=Button(gui,image=openphoto,bd=0,command=textigui)
learn_button=Button(gui,image=learnphoto,bd=0,command=learno)
configure_button=Button(gui,image=configurephoto,bd=0,command=f.a)
language_button=Button(gui,image=languagephoto,bd=0,command=f.a)
logap=Label(gui,image=logo, bg="#1f1f1f",padx=10,pady=10)



background_label.place(x=0,y=0)
open_button.grid(row=0,column=0)
import_button.grid(row=0,column=1)
logap.place(x=140,y=100)
learn_button.grid(row=0,column=2)
configure_button.grid(row=0,column=3)
language_button.grid(row=0,column=4)










translated=StringVar()
cell=StringVar()
adjusted=StringVar()
senadjusted=StringVar()
named=StringVar()
showor=StringVar()
enter=StringVar()


adjusted.trace("w",change_state1)
senadjusted.trace("w",change_state2)
finalimage=ImageTk.PhotoImage(Image.open("D:/wordi project/Wordilogo.gif"))

sentenci=Text(gui,bg="#1f1f1f",font=("Times", 10, "bold"),fg="white",height=1,width=170)
sentenci.configure(relief=FLAT)
ask=Label(gui,textvariable=cell,bg="#1f1f1f",font=("Times", 14, "bold"),fg="red")
yes=Button(gui,text="YES",command=alghoritm_yes)
no=Button(gui,text="NO",command=alghoritm_no)
nextsen=Button(gui,text="SAVE IT",command=alghoritm_next)
translation=Label(gui,textvariable=translated,bg="#1f1f1f",font=("Times", 10, "bold"),fg="white")
adjustentry=Entry(gui,textvariable=adjusted)
saveadjustentry=Button(gui,text="Correct word translation",command=correct_word,state=saveadjstate)
senadjustentry=Entry(gui,textvariable=senadjusted)
savesenadjusted=Button(gui,text="Correct sentence translation",command=correct_sen,state=sensaveadjstate)
internetimage=Label(gui,image=finalimage,bg="#1f1f1f",width=840,height=500)
fin=Label(gui,text="All words have been imported!",bg="#1f1f1f",font=("Times", 10, "bold"))
opentext=Text(gui,bg="white",width=84,height=150)
createfile=Button(gui,command=create_wordi,text="Create wordi file",font=("Times", 10, "bold"))
filename=Entry(gui,textvariable=named,bg="grey",fg="green")
succes=Label(gui,text="File was succesfuly created!",font=("Times", 20, "bold"),fg="black",bg="white")
failed=Label(gui,text="Failed to create file!(see help)",font=("Times", 20, "bold"),fg="black",bg="white")
choosebox=Listbox(gui,width=50,height=23,font=("Times", 10, "bold"))
learnit=Button(gui,text="Learn!",font=("Times", 12, "bold"),fg="blue",bg="grey",command=alghoritm_learn)
showhide=Button(gui,text="Show answer!",font=("Times", 10, "bold"),command=alghoritm_show)
cor_fal=Entry(gui,textvariable=enter,bg="white",fg="blue")
correct=Label(gui,text="Correct!",font=("Times", 12, "bold"),fg="green")
wrong=Label(gui,text="Wrong!",font=("Times", 12, "bold"),fg="red")
nomore=Label(gui,text="No more words to learn!",font=("Times", 12, "bold"),fg="green",bg="grey")
examination=Button(gui,text="Test",font=("Times", 12, "bold"),fg="blue",bg="grey",command=exam_me)
progressbar=ttk.Progressbar(orient=HORIZONTAL, length=600, mode='determinate')
#END OF GUI BLOCK














gui.mainloop()
