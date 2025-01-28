import rclpy
from rclpy.node import Node

from std_msgs.msg import String

import socket

class SlidesSubscriber(Node):

    def __init__(self):
        # Sets up subscriber
        super().__init__('slides_subscriber')
        self.subscription = self.create_subscription(
            String,
            'slides',
            self.listener_callback,
            1)
        self.subscription

        # Sets up Socket client
        self.server_ip = '' # Put IP Address of personal laptop Mac here
        self.server_port = 4000

        self.server = (self.server_ip, self.server_port)
        self.s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        # self.message = input("->")

    def listener_callback(self, msg):
        self.get_logger().info('I heard: "%s"' % msg.data)
        self.s.sendto(msg.data.encode('utf-8'), self.server)
        self.data, self.addr = self.s.recvfrom(1024)
        self.data = self.data.decode('utf-8')
        self.get_logger().info('I recieved: "%s"' % self.data)

def main(args=None):
    rclpy.init(args=args)
    slides_subscriber = SlidesSubscriber()
    rclpy.spin(slides_subscriber)

    slides_subscriber.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
