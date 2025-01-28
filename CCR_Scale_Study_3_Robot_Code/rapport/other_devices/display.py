from tkinter import *
import csv

def loop():
    global current_question

    # Reads the current value from the displaynumber.csv file to determine which slide to show
    # If the program is not working, it is likely because this value is set to 700. Just change the value to a number between 0 and 4, inclusive.
    with open('displaynumber.csv',newline='') as file:
        reader = csv.reader(file, delimiter=',',quotechar='"')
        for row in reader:
            read_value = row[0]

            # Ignores values that are not 0-4 or 700
            if read_value == "0" or read_value == "1" or read_value == "2" or read_value == "3" or read_value == "4"or read_value == "700":
                current_question = int(row[0])
    
    if current_question != 700:
        lbl = Label(win, text=question_prompts[current_question],font=("Ariel",45), fg="white",bg="black")
        lbl.place(relx=0.5, rely=0.5, anchor='center')
    
    # Quits when the number in the csv is 700
    else:
        win.destroy()
    
    # Creates an invisible exit button
    exit_button = Button(win, text=" ", font=("Ariel",1), bd=0, highlightthickness=0,bg="black",command=end_fullscreen)
    exit_button.place(x=700,y=0) 

    # After 500 ms, check for the value again
    win.after(500,loop)

current_question = 1
question_prompts = [
    "                                                                                                          \n                                                                                                        \n                                                                                  ",
    "Choose one current problem, concern, or \n stressor you are facing in your life",
    "Discuss the circumstances surrounding \n the concern",
    "Discuss how you feel and what you think \nabout the concern",
    "Share any other details or issues that \n you think are important, such as the \n implications of this event for your life"
]

# Responds to the exit button to close the window
def end_fullscreen():
    win.destroy()

win = Tk()
win.title("Prompts")

# Makes the window fullscreen and prevents you from accessing the computer
win.attributes('-fullscreen',True)

# Creates a smaller window that does not lock you out of the computer
# win.geometry("1500x500")

# Makes the backgroun black
win.configure(bg="black")

loop()
mainloop()

