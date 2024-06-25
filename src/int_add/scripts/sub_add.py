#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32

class MySubscriber(Node):
    def __init__(self):
        super().__init__('my_subscriber')  
        self.subscription = self.create_subscription(
            Int32, 
            'topic',  
            self.listener_callback,  
            10)  
        self.subscription  

    def listener_callback(self, msg):
        self.get_logger().info('Result(a+b): "%s"' % msg.data)  

def main(args=None):
    rclpy.init(args=args)  
    my_subscriber = MySubscriber()  
    rclpy.spin(my_subscriber) 

    my_subscriber.destroy_node() 
    rclpy.shutdown()  

if __name__ == '__main__':
    main()