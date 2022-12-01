from tkinter import *
import random
root.config(bg="white")

root = Tk()

root.title("Encapsulation")
root.geometry("500x500")

label_score = Label(root, font= ("Comic",10,"bold"), bg= "white")
label_score.place(relx=0.1,rely=0.2,anchor=W)

label_color = Label(root, font= ("Comic",20,"bold"), bg= "white")
label_color.place(relx=0.5,rely=0.4,anchor=CENTER)

entry_text_color = Entry(root)
entry_text_color.place(relx=0.5,rely=0.6,anchor=CENTER)

class score:
    def __init__(self):
        self.__score = 0
        print("\n","Instructions","/n")
        print("\n","1. You have to type the Text Color of the Word in the space given below that Word","/n")
        print("\n","2. If you guess the correct Text Color, your score will be increased between 1 to 5","/n")
        print("\n","3. If you guess the incorrect Text Color, your score will be decreased between -1 to -5","/n")
    def updategame(self):
        self.text = ["BLUE","PURPLE","ORANGE","PINK","YELLOW","RED"]
        self.random_number_for_text = random.randint(0,5)
        self.color = ["blue","purple","orange","pink","yellow","red"]
        self.random_number_for_color = random.randint(0,5)
        label_name["text"] = self.text[self.random_number_for_text]
        label_name["fg"] = self.color[self.random_number_for_color]
    def get_updatescore(self,entry_text_color):
        self.__updateScore(entry_text_color)
        
        
obj = score()

def get_textcolor():
    text_color = entry_text_color.get()
    obj.get_updatescore(text_color)
    obj.updategame()
    
    entry_text_color.delete(0,END)

btn_check = Button(root,text="Check",relief=FLAT,command=obj1.updategame)
btn.place(relx=0.3,rely=0.8,anchor=CENTER)

btn_start = Button(root,text="Start",relief=FLAT,command=obj1.updategame)
btn.place(relx=0.3,rely=0.8,anchor=CENTER
root.mainloop()