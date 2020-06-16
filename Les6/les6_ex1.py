import time
from tkinter import *


class TrafficLight:
    __color = ['red', 'yellow', 'green', 'yellow']

    root = Tk()
    root.title("Светофор")
    root.configure(bg='black')
    root.geometry('135x365')

    canvas = Canvas(root, width=130, height=360, bg="black")
    canvas.grid()

    oval_red = canvas.create_oval(15, 20, 115, 120, fill="white")
    oval_yellow = canvas.create_oval(15, 130, 115, 230, fill="white")
    oval_green = canvas.create_oval(15, 240, 115, 340, fill="white")


    def running(self):
        i = 0
        timeout = 60
        timeout_start = time.time()
        while time.time() < timeout_start + timeout:
            color = TrafficLight.__color[i]
            if color == 'red':
                self.canvas.itemconfig(self.oval_red, fill="red")
                self.canvas.itemconfig(self.oval_yellow, fill="white")
                self.canvas.itemconfig(self.oval_green, fill="white")
                TrafficLight.root.update()
                time.sleep(7)
            elif color == 'yellow':
                self.canvas.itemconfig(self.oval_red, fill="white")
                self.canvas.itemconfig(self.oval_yellow, fill="yellow")
                self.canvas.itemconfig(self.oval_green, fill="white")
                TrafficLight.root.update()
                time.sleep(2)
            elif color == 'green':
                self.canvas.itemconfig(self.oval_red, fill="white")
                self.canvas.itemconfig(self.oval_yellow, fill="white")
                self.canvas.itemconfig(self.oval_green, fill="green")
                TrafficLight.root.update()
                time.sleep(7)
            if i == 3:
                i = 0
            else:
                i += 1


TrafficLight = TrafficLight()
TrafficLight.running()
