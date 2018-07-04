from tkinter import Tk, RIGHT, BOTH, RAISED, Label, Entry, messagebox
from tkinter.ttk import Frame, Style, Button
import subprocess
import random
import time

# How much time you want to give yourself
sec = 120

# Allows program to keep nudging every couple minutes
running = True

class Sleep(Frame):
  
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        global running

        '''Creates the window and populates with buttons and input box'''
        self.master.title('Auto Sleep')
        self.style = Style()
        self.style.theme_use('clam')

        frame = Frame(self, relief=RAISED, borderwidth=1)
        frame.pack(fill=BOTH, expand=True)
        self.pack(fill=BOTH, expand=True)

        self.time = Label(frame)
        self.time.pack()

        # Math Problem Display
        self.n1 = random.randint(0, 100)
        self.n2 = random.randint(0, 100)
        problem = Label(frame, text='Solve: {} + {}'.format(self.n1, self.n2))
        problem.pack()

        # Input
        self.userInput = Entry(frame)
        self.userInput.pack()
        
        # Buttons
        closeButton = Button(self, text='Sleep', command=self.goToSleep)
        closeButton.pack(side=RIGHT)
        okButton = Button(self, text='Answer', command=self.readInput)
        okButton.pack(side=RIGHT)

        self.centerWindow()

        self.tick()

    def tick(self):
        '''Timer to sleep'''
        global sec
        sec -= 1
        self.time['text'] = 'Sleeping in {} seconds'.format(sec)
        self.time.after(1000, self.tick)
        if sec <= 0:
            self.goToSleep()

    def readInput(self):
        '''Reads in the user input, if it's the right answer, don't sleep'''
        solution = self.userInput.get()
        
        # Error checking
        try:
            solution = int(solution)
        except ValueError:
            messagebox.showerror('Error', 'Please input a valid integer')
            return

        # Check solution
        if solution == self.n1 + self.n2:
            self.quit()
        else:
            messagebox.showerror('Error', 'Incorrect solution, please try again')

    def goToSleep(self):
        '''Calls window's shutdown function to sleep'''
        global running
        running = False
        subprocess.call(['shutdown', '/h'])
        self.quit()

    def centerWindow(self):
        '''Centers window on the screen'''
        w = 300
        h = 100

        sw = self.master.winfo_screenwidth()
        sh = self.master.winfo_screenheight()
        
        x = (sw - w)/2
        y = (sh - h)/2
        self.master.geometry('%dx%d+%d+%d' % (w, h, x, y))

def main():
    global running
    while True:
        root = Tk()
        app = Sleep()
        r = root.mainloop()
        if running:
            time.sleep(10*60)
        else:
            break

if __name__ == '__main__':
    main()  