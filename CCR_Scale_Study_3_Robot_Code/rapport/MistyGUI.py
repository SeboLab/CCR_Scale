import tkinter as tk

import rclpy
from rclpy.node import Node

from std_msgs.msg import String

class MistyGUI(Node):
    def __init__(self):

        # Creates two publishers. 'action' controls Misty and 'slides' controls the slides.
        super().__init__('misty_publisher')

        self.publisher_action = self.create_publisher(String, 'action', 1)
        self.publisher_slides = self.create_publisher(String, 'slides', 1)

        self.message1 = ["That’s really tough. You must have gone through a very difficult time especially","I’m sorry to hear that about ","It sounds like you’ve been experiencing some tension in your relationship. That can be challenging to navigate"," It sounds like a lot of pressure, especially given the expectations you may be facing","It sounds like you’re experiencing a lot of change right now"]
        self.message2 = ["It’s completely understandable that this situation would make you feel this way, given that"," It’s understandable to be concerned. Relationships are deeply personal and conflicts can really affect you.","It must be tough to feel stressed and overwhelmed, especially when there’s so much at stake","It must be incredibly disheartening to feel this way, especially when it matters so much to you"]
        self.message3 = ["What you’re experiencing can be very difficult to navigate. I hope you get this resolved soon","It’s clear that this situation is weighing heavily on you, but it seems like you are handling it well","It sounds like this is having a significant impact on your life","It sounds frustrating, but I'm sure you will be able to find a solution","It sounds like you gained some really important insights from this experience"]
        self.unresponsive = ["Please go on to the next part", "Please move on to the next message", "Please call the experimenter"]

        # Creates the window for the tkinter interface
        self.root = tk.Tk()
        self.root.geometry("1000x800")
        self.root.title("Misty Interface")

        # Creates a stopwatch at the top of the screen
        # Time variables
        self.time_elapsed = 0
        self.running = False

        self.time_display = tk.Label(self.root, text="0:00", font=("Ariel", 18))
        self.time_display.pack()

        self.timer_frame = tk.Frame(self.root)
        self.timer_frame.pack(padx=10, pady=5)

        self.starttimer_button = tk.Button(self.timer_frame, text="Start", command=self.start)
        self.starttimer_button.grid(row=0, column=0, padx=5, pady=0)

        self.stoptimer_button = tk.Button(self.timer_frame, text="Stop", command=self.stop)
        self.stoptimer_button.grid(row=0, column=2, padx=5, pady=0)

        self.reset_button = tk.Button(self.timer_frame, text="Reset", command=self.reset)
        self.reset_button.grid(row=0, column=3, padx=5, pady=0)

        self.update_time()

        # Buttons to change slides
        self.label = tk.Label(self.root, text="Slides", font=("Ariel",16))
        self.label.pack(padx=20,pady=0)

        self.slide_frame = tk.Frame(self.root)
        self.slide_frame.pack(padx=10, pady=5)

        self.slide_button = tk.Button(self.slide_frame, wraplength=300, text="Blank slide", font=("Ariel",10),command=lambda m="0": self.change_slide(m))
        self.slide_button.grid(row=0,column=1, padx=5, pady=0)

        self.slide1_button = tk.Button(self.slide_frame, wraplength=300, text="Prompt slide", font=("Ariel",10),command=lambda m="1": self.change_slide(m))
        self.slide1_button.grid(row=0,column=2, padx=5, pady=0)

        self.slide2_button = tk.Button(self.slide_frame, wraplength=300, text="Message 1", font=("Ariel",10),command=lambda m="2": self.change_slide(m))
        self.slide2_button.grid(row=0,column=3, padx=5, pady=0)

        self.slide3_button = tk.Button(self.slide_frame, wraplength=300, text="Message 2", font=("Ariel",10),command=lambda m="3": self.change_slide(m))
        self.slide3_button.grid(row=0,column=4, padx=5, pady=0)

        self.slide4_button = tk.Button(self.slide_frame, wraplength=300, text="Message 3", font=("Ariel",10),command=lambda m="4": self.change_slide(m))
        self.slide4_button.grid(row=0,column=5, padx=5, pady=0)

        self.slide4_button = tk.Button(self.slide_frame, wraplength=300, text="Shut down slides", bg="#e52b50",font=("Ariel",10),command=lambda m="700": self.change_slide(m))
        self.slide4_button.grid(row=0,column=6, padx=5, pady=0)

        # Responsive Condition
        self.label = tk.Label(self.root, text="Responsive", font=("Ariel",16))
        self.label.pack(padx=20,pady=0)

        self.topbutton_frame = tk.Frame(self.root)
        self.topbutton_frame.pack(padx=10, pady=0)

        self.bell_button = tk.Button(self.topbutton_frame, wraplength=300, text="Play bell sound", font=("Ariel",10), command=lambda m="bell_sound": self.action(m))
        self.bell_button.grid(row=0, column=0, padx=5, pady=0)

        self.slownod_button = tk.Button(self.topbutton_frame, wraplength=300, text="Slow head nod", font=("Ariel",10), command=lambda m="slow_nod": self.action(m))
        self.slownod_button.grid(row=0, column=1, padx=5, pady=0)

        # text entry box
        self.text_frame = tk.Frame(self.root)
        self.text_frame.pack(padx=10, pady=5)

        self.textbox = tk.Entry(self.text_frame, width=100, font=("Ariel",10))
        self.textbox.grid(row=0, column=0, padx=5, pady=0)

        self.speak_button = tk.Button(self.text_frame, wraplength=300, text="Speak", font=("Ariel",10), command=self.text_box)
        self.speak_button.grid(row=0, column=1, padx=5, pady=0)

        self.erase_button = tk.Button(self.text_frame, wraplength=300, text="Clear", font=("Ariel",10), command=self.text_erase)
        self.erase_button.grid(row=0, column=2, padx=5, pady=0)

        self.buttonframe = tk.Frame(self.root)
        self.buttonframe.columnconfigure(0, weight=1)
        self.buttonframe.columnconfigure(1, weight=1)
        self.buttonframe.columnconfigure(2, weight=1)

        # Message 1
        self.message_label = tk.Label(self.buttonframe, text="Message 1", font=("Ariel",10))
        self.message_label.grid(row=0,column=0,sticky=tk.W+tk.E)

        self.message1a = tk.Button(self.buttonframe, wraplength=300, text=self.message1[0], font=("Ariel",10), bg="yellow",command=lambda m=self.message1[0]: self.speech_button(m))
        self.message1a.grid(row=1,column=0,sticky=tk.W+tk.E)

        self.message1b = tk.Button(self.buttonframe, wraplength=300, text=self.message1[1], font=("Ariel",10), bg="yellow",command=lambda m=self.message1[1]: self.speech_button(m))
        self.message1b.grid(row=2,column=0,sticky=tk.W+tk.E)

        self.message1c = tk.Button(self.buttonframe, wraplength=300, text=self.message1[2], font=("Ariel",10), command=lambda m=self.message1[2]: self.speech_button(m))
        self.message1c.grid(row=3,column=0,sticky=tk.W+tk.E)

        self.message1d = tk.Button(self.buttonframe, wraplength=300, text=self.message1[3], font=("Ariel",10), command=lambda m=self.message1[3]: self.speech_button(m))
        self.message1d.grid(row=4,column=0,sticky=tk.W+tk.E)

        self.message1e = tk.Button(self.buttonframe, wraplength=300, text=self.message1[4], font=("Ariel",10), command=lambda m=self.message1[4]: self.speech_button(m))
        self.message1e.grid(row=5,column=0,sticky=tk.W+tk.E)

        # Message 2
        self.message_label = tk.Label(self.buttonframe, text="Message 2", font=("Ariel",10))
        self.message_label.grid(row=0,column=1,sticky=tk.W+tk.E)

        self.message2a = tk.Button(self.buttonframe, wraplength=300, bg="yellow",text=self.message2[0], font=("Ariel",10), command=lambda m=self.message2[0]: self.speech_button(m))
        self.message2a.grid(row=1,column=1,sticky=tk.W+tk.E)

        self.message2b = tk.Button(self.buttonframe, wraplength=300, text=self.message2[1], font=("Ariel",10), command=lambda m=self.message2[1]: self.speech_button(m))
        self.message2b.grid(row=2,column=1,sticky=tk.W+tk.E)

        self.message2c = tk.Button(self.buttonframe, wraplength=300, text=self.message2[2], font=("Ariel",10), command=lambda m=self.message2[2]: self.speech_button(m))
        self.message2c.grid(row=3,column=1,sticky=tk.W+tk.E)

        self.message2d = tk.Button(self.buttonframe, wraplength=300, text=self.message2[3], font=("Ariel",10), command=lambda m=self.message2[3]: self.speech_button(m))
        self.message2d.grid(row=4,column=1,sticky=tk.W+tk.E)

        # Message 3
        self.message_label = tk.Label(self.buttonframe, text="Message 3", font=("Ariel",10))
        self.message_label.grid(row=0,column=2,sticky=tk.W+tk.E)

        self.message3a = tk.Button(self.buttonframe, wraplength=300, text=self.message3[0], font=("Ariel",10), command=lambda m=self.message3[0]: self.speech_button(m))
        self.message3a.grid(row=1,column=2,sticky=tk.W+tk.E)

        self.message3b = tk.Button(self.buttonframe, wraplength=300, text=self.message3[1], font=("Ariel",10), command=lambda m=self.message3[1]: self.speech_button(m))
        self.message3b.grid(row=2,column=2,sticky=tk.W+tk.E)

        self.message3c = tk.Button(self.buttonframe, wraplength=300, text=self.message3[2], font=("Ariel",10), command=lambda m=self.message3[2]: self.speech_button(m))
        self.message3c.grid(row=3,column=2,sticky=tk.W+tk.E)

        self.message3d = tk.Button(self.buttonframe, wraplength=300, text=self.message3[3], font=("Ariel",10), command=lambda m=self.message3[3]: self.speech_button(m))
        self.message3d.grid(row=4,column=2,sticky=tk.W+tk.E)

        self.message3e = tk.Button(self.buttonframe, wraplength=300, text=self.message3[4], font=("Ariel",10), command=lambda m=self.message3[4]: self.speech_button(m))
        self.message3e.grid(row=5,column=2,sticky=tk.W+tk.E)

        self.buttonframe.pack(fill='x')

        # Unresponsive Condition
        self.label = tk.Label(self.root, text="Unresponsive", font=("Ariel",16))
        self.label.pack(padx=20,pady=0)

        self.bell_button_two = tk.Button(self.root, wraplength=300, text="Play bell sound", font=("Ariel",10), command=lambda m="bell_sound": self.action(m))
        self.bell_button_two.pack(padx=5, pady=0)

        self.buttonframe = tk.Frame(self.root)
        self.buttonframe.columnconfigure(0, weight=1)
        self.buttonframe.columnconfigure(1, weight=1)
        self.buttonframe.columnconfigure(2, weight=1)

        self.message_label = tk.Label(self.buttonframe, text="Message 1", font=("Ariel",10))
        self.message_label.grid(row=0,column=0,sticky=tk.W+tk.E)
        self.unresponsive[0] = tk.Button(self.buttonframe, wraplength=300, text=self.unresponsive[0], font=("Ariel",10), command=lambda m=self.unresponsive[0]: self.action(m))
        self.unresponsive[0].grid(row=1,column=0,sticky=tk.W+tk.E)
        
        self.message_label = tk.Label(self.buttonframe, text="Message 2", font=("Ariel",10))
        self.message_label.grid(row=0,column=1,sticky=tk.W+tk.E)
        self.unresponsive[1] = tk.Button(self.buttonframe, wraplength=300, text=self.unresponsive[1], font=("Ariel",10), command=lambda m=self.unresponsive[1]: self.action(m))
        self.unresponsive[1].grid(row=1,column=1,sticky=tk.W+tk.E)
        
        self.message_label = tk.Label(self.buttonframe, text="Message 3", font=("Ariel",10))
        self.message_label.grid(row=0,column=2,sticky=tk.W+tk.E)
        self.unresponsive[2] = tk.Button(self.buttonframe, wraplength=300, text=self.unresponsive[2], font=("Ariel",10), command=lambda m=self.unresponsive[2]: self.action(m))
        self.unresponsive[2].grid(row=1,column=2,sticky=tk.W+tk.E)

        self.buttonframe.pack(fill='x')

        self.root.mainloop()

    # Publishes preset actions to Misty
    def action(self, phrase):
        msg = String()
        msg.data = phrase
        self.publisher_action.publish(msg)
        # self.get_logger().info('Publishing: "%s"' % msg.data)

        if phrase in ["Please go on to the next part", "Please move on to the next message", "Please call the experimenter"]:
            self.reset()

    # Makes a text button pushed that pops up in the textbox
    def speech_button(self, phrase):
        self.textbox.insert(0, phrase)

    # Tells Misty to say speech from textbox
    def text_box(self):
        msg = String()
        msg.data = self.textbox.get()
        # self.get_logger().info(self.textbox.get())
        self.publisher_action.publish(msg)
        self.textbox.delete(0, tk.END)

        self.reset()

    # Clears the textbox
    def text_erase(self):
        self.textbox.delete(0, tk.END)

    def change_slide(self, slide_number):
        msg = String()
        msg.data = slide_number
        self.publisher_slides.publish(msg)

        self.start()

    # Makes the stopwatch function
    def update_time(self):
        if self.running:
            self.time_elapsed += 1
            self.update_display()
            self.root.after(1000, self.update_time)

    def update_display(self):
        minutes = (self.time_elapsed % 3600) // 60
        seconds = self.time_elapsed % 60
        self.time_display.config(text=f"{minutes:01}:{seconds:02}")

    # Starts stopwatch
    def start(self):
        if not self.running:
            self.running = True
            self.update_time()

    # Stops stopwatch
    def stop(self):
        self.running = False

    # Resets stopwatch
    def reset(self):
        self.running = False
        self.time_elapsed = 0
        self.update_display()

def main(args=None):
    rclpy.init(args=args)

    misty_publisher = MistyGUI()

    rclpy.spin(misty_publisher)
    
    misty_publisher.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
