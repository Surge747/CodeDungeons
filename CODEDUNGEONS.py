import sys,time,random,pickle,csv,os,shutil
shell=sys.stdout.shell
from tkinter import *

#Initialize
name=""
progress=0
health=100
attack=5
heal=5
img=None
label=None
root=None
D=8
C=5+D

#monsters Data
DL1=["D1","D2","D3","D4",["Guardian",[20,4]],["Ghoul",[5,10]],["Wilter",[15,8]]]
DL2=["C1","C2","C3",["Alien",[20,7]],["Banshee",[23,8]],["Warden",[3,13]]]

# Initialize Questions.txt file
with open("Assets/Questions/Questions.txt", "r", encoding="utf-8") as f:
    Q = f.readlines()
r = [a for a in range(0, len(Q), 2)]
f.close()

#Core functions
def menu():
    global root,img,label
    if root==None:
        root=Tk()
    if label!=None:
        label.destroy()
    img = PhotoImage(file="Assets/Titlescreen.png")
    label = Label(root,image=img)
    label.pack()
    root.update()
    print("""----------Code Dungeons----------
->1. New Game
->2. Load Game
->3. Quit""")
    option=input("Enter your choice : ")
    if option=="1":
        main(0)
    elif option=="2":
        load()
    elif option=="3":
        sys.exit()
    else:
        menu()

def main(p=0):
    global name
    global progress,attack,health,heal
    global root,img,label
    while progress<13:
        if progress==0:
            if root==None:
                root=Tk()
            if label!=None:
                label.destroy()
            img = PhotoImage(file="Assets/Backgrounds/D0.png")
            label = Label(root,image=img)
            label.pack()
            root.update()
            name=input("Enter your name adventurer: ")
            newgame(name)
            st("When the news about random people disappearing in the ancient dungeons of the Kingdom reaches him, the king sends you on a mission to those dungeons to figure out the secrets entrapped within the walls","ERROR")
            st("When you approach the dungeon... you hear a faraway hiss","ERROR")
            st("Your stats")
            stats(name)
        elif progress<7:
            global DL1
            if root==None:
                root=Tk()
            if label!=None:
                label.destroy()
            r=random.choice(DL1)
            DL1.remove(r)
            if r in ["D1","D2","D3","D4"]:
                img = PhotoImage(file="Assets/Backgrounds/{}.png".format(r))
                label = Label(root,image=img)
                label.pack()
                root.update()
                text()
            else:
                battle(r)
        elif progress<13:
            global DL2
            if root==None:
                root=Tk()
            if label!=None:
                label.destroy()
            r=random.choice(DL2)
            DL2.remove(r)
            if r in ["C1","C2","C3"]:
                img = PhotoImage(file="Assets/Backgrounds/{}.png".format(r))
                label = Label(root,image=img)
                label.pack()
                root.update()
                text()
            else:
                battle(r)
        progress+=1
        health+=5
        heal+=4
        attack+=4
        f=open("Player data/{}.txt".format(name),"w")
        f.write(str(attack)+"\n"+str(health)+"\n"+str(progress))
        f.flush()
        f.close()
    else:
        battle(["Python",[50,8]])

def newgame(name=""):
    f=open("Player data/{}.txt".format(name),"w")
    l=[5,100,progress] # Starting Attack Health and progress
    for a in l:
        f.write(str(a))
        f.write("\n")
    f.flush()
    f.close()

def load():
    global progress,name,health,attack
    name=input("Enter username of save file ")
    if os.path.isfile("Player data/{}.txt".format(name)):
        f=open("Player data/{}.txt".format(name))
        data=f.readlines()
        attack=int(data[0].strip())
        health=int(data[1].strip())
        progress=int(data[2].strip())
        main(progress)
    else:
        print ("Save does not exist")
        menu()

def stats(name):
    f=open("Player data/{}.txt".format(name),"r+")
    stats=f.readlines()
    global health,attack  
    attack=int(stats[0])
    health=int(stats[1])
    print("Attack :",stats[0],end="")
    print("Health :",stats[1])

def battle(l=["Monster_name",[0,0]]):
    global name,health,attack,heal,img,label,root
    if root==None:
        root=Tk()
    if label!=None:
        label.destroy()
    img = PhotoImage(file="Assets/Monsters/{}.png".format(l[0]))
    label=Label(root,image=img)
    label.pack()
    root.update()
    heal=5
    st("You encounter a {}".format(l[0]),"hit")
    st("Your stats")
    stats(name)
    M_Health=int(l[1][0])
    M_Attack=int(l[1][1])
    st("{} info".format(l[0]),"COMMENT")
    print("{} Attack :".format(l[0]),M_Attack)
    print("{} Health :".format(l[0]),M_Health)
    while health>0 and M_Health>0:
        option=st("""Enter 1 for attack
      2 for heal\n Enter your choice : ""","hit")
        if option in ["1","2"]:
            if option=="1":
                if question():
                    st("You attack the {}".format(l[0]),"hit")
                    M_Health-=attack
                    st("The {} health is ".format(l[0]),"hit")
                    print(M_Health)
            elif option=="2":
                if question():
                    st("You use your turn to heal yourself!","hit")
                    health+=heal
                    print("Your health now is ",health)
            st("The {} attacks you".format(l[0]),"hit")
            health-=M_Attack
            st("Your Health is ")
            print(health)
        else:
            st("Enter a valid option","ERROR")
            pass
    else:
        if M_Health<=0:
            label.destroy()
            img = PhotoImage(file="Assets/Monsters/{}d.png".format(l[0]))
            label=Label(root,image=img)
            label.pack()
            root.update()
            st("{} was defeated".format(l[0]))
            if l[0]=="Python":
                win()
        else:
            gameover()

def boss():
    global root,label,name
    if root==None:
        root=Tk()
    if label!=None:
        label.destroy()
    img = PhotoImage(file="Assets/Backgrounds/boss.png")
    label = Label(root,image=img)
    label.pack()
    root.update()
    st("The door to the boss room lies before you... you hear the endless sounds of the streams of zeros and ones","ERROR")
    if root==None:
        root=Tk()
    if label!=None:
        label.destroy()
    img = PhotoImage(file="Assets/Monsters/Python.png")
    label=Label(root,image=img)
    label.pack()
    root.update()
    st("Welcome user {}".format(name),"hit")
    st("Or should i say","hit")
    l=os.uname()[1]
    st("{} {}".format(l[0]),n=120)
    st("Good luck",n=80)
    battle(["Python",[50,13]])

def text():
    global progress,D,C
    if progress<D+1:
        l=["Torches akin to frenzied hellfire set ablaze the narrow passageways with a feverish glow, the heat enveloping the every corner of the dungeon","the chirping of invisible crickets echoing against the cold, musty cave rock breaks the piercing silence that filled the voids of the dungeon","The silence piercing through the walls grows louder as they become narrower and the darkness gives way to light from barred openings.","Dust and webs cling to the karst as if in fear of the mysteries that lay undiscovered beyond the sealed doors"]
        st(random.choice(l),"KEYWORD")
    elif progress<C+1:
        l=["the cave glistens in a deadly gloom while a raging tempest sends the cobwebs flying across the limestone walls","Faint sounds of gushing water permeate the frosty air as devilish bats hover around the dripping stalactites lining the decayed ceiling","A bluish glow from the openings that bring in the icy gales illuminates the chains, swords and skeletons strewn across the dungeon floor."]
        st(random.choice(l),"KEYWORD")
    elif progress==C+1:
        st("You feel beyond the door lies a powerful being... ","KEYWORD")
    print()
            
def gameover():
    st("""You forever rome the dungeons for eternity...
------------Gameover------------\n""","ERROR")

def question():
    global Q,r
    a=random.choice(r)
    r.remove(a)
    j=Q[a][1:-1]
    l=j.split("|")
    for i in l:
        print(i)
    inp=input("Enter your choice : ")
    if Q[a+1][:-1] in [inp,inp.capitalize()]:
        st("That was the correct answer!")
        return True
    else:
        Qsprac(l,Q[a+1])
        st("You answered incorrectly")
        print("Answer is",Q[a+1])

def Qsprac(q,a):
    f=open("Practice Questions.txt","a+")
    for i in q:
        f.write(i+"\n")
    f.write("Answer is "+a+"\n")
 
def win():
    global root,label
    if root==None:
        root=Tk()
    if label!=None:
        label.destroy()
    img = PhotoImage(file="Assets/Backgrounds/done.png")
    label=Label(root,image=img)
    label.pack()
    root.update()
    st("We hope you had as much as fun playing as we had while making the code :) ")
    root.destroy()

#Other Functions
def st(t,c="STRING",n=1800,i=True,iC=""): #18000 IS FOR CONVINIENCE OF TESTING... MAKE IT 180
    typing_speed = n #wpm
    for l in t:
        shell.write(l,c)
        time.sleep(random.random()*18.0/typing_speed)
    if i==True:
        a=input("")
        return a
menu()
