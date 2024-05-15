from tkinter import *
#import serial
#import time

#serialA=serial.Serial('COM4',9600)
#time.sleep(1)
def JoseVitor():


    root = Tk()
    root.geometry("1000x1000")

    def onled():
        label.destroy()
        labelA.pack()
        #serialA.write(b'a')

    def offled():
        #serialA.write(b'b')
        root.destroy()
        JoseVitor()
        
        
    button=Button(root,text="LED LIGADO")
    button.config(command=onled)
    button.pack()

    buttonA=Button(root,text="LED DESLIGADO")
    buttonA.config(command=offled)
    buttonA.pack()

    photo=PhotoImage(file="offled.png")
    label=Label(image=photo)

    photoA=PhotoImage(file="onled.png")
    labelA=Label(image=photoA)
    label.pack()
    root.mainloop()

JoseVitor()
