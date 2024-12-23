import rclpy
from rclpy.node import Node

from std_msgs.msg import String

import requests
import os
import json
import time

misty_ip = "" # Put Misty IP Address Here
my_ip = "" # Put personal laptop mac's IP Address Here

class MistySubscriber(Node):

    def __init__(self):
        super().__init__('misty_subscriber')
        self.subscription = self.create_subscription(
            String,
            'action',
            self.response,
            1)
        self.subscription  # prevent unused variable warning

        self.publisher = self.create_publisher(String, 'movement', 1)        

        self.misty_ip = misty_ip
        self.my_ip = my_ip

    def response(self, msg):

        self.unresponsive = ["Please go on to the next part", "Please move on to the next message", "Please call the experimenter"]

        if msg.data == "nod":
            self.change_misty_led(0,0,0)
            self.misty_action("head-up-down-nod")

        elif msg.data == "slow_nod":
            self.change_misty_led(0,0,0)
            self.misty_action("head-nod-slow")

        elif msg.data == self.unresponsive[0]:
            self.change_misty_led(0,0,0)
            self.speak(self.unresponsive[0])

        elif msg.data == self.unresponsive[1]:
            self.change_misty_led(0,0,0)
            self.speak(self.unresponsive[1])

        elif msg.data == self.unresponsive[2]:
            self.change_misty_led(0,0,0)
            self.speak(self.unresponsive[2])

        elif msg.data == "bell_sound":
            self.change_misty_led(0,0,0)
            self.play_audiofile("bell_transition.mp3")

        else:
            self.speak(msg.data)

    def misty_action(self, action_name):
        new_name = action_name + '_temp'
        x = requests.post("http://"+self.misty_ip+"/api/actions/start", json={"name": new_name})
        data = x.json()

    def speak(self, params):
        x = requests.post("http://"+self.misty_ip+ "/api/tts/speak", json={"text": params})

    def change_misty_led(self, r, g, b):
        x = requests.post("http://"+self.misty_ip+"/api/led", json={"Red": r, "Green": g, "Blue": b})

    def play_audiofile(self, filename):
        x = requests.post("http://"+self.misty_ip+"/api/audio/play", json={"FileName": 'http://'+self.my_ip+':8000/ros2_ws/src/CCR_Scale/Study3_Code/rapport/'+filename})

def main(args=None):
    rclpy.init(args=args)

    misty_subscriber = MistySubscriber()

    rclpy.spin(misty_subscriber)

    misty_subscriber.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
