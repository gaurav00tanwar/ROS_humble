#!/usr/bin/env python3

import rclpy
from rclpy.node import Node

# from std_msgs.msg import String
from std_msgs.msg import Int32

class int_add_pub(Node):
    def __init__(self):
        super().__init__('int_pub')
        self.sum_pub = self.create_publisher(Int32,'topic',10)
        self.timer = self.create_timer(0.5, self.timer_callback)
        self.a = 10
        self.b = 20

    def timer_callback(self):
        msg = Int32()
        msg.data = self.a + self.b
        self.sum_pub.publish(msg)
        self.get_logger().info('Publishing(a+b):"%d" "%d"' %(self.a,self.b))
        self.a+=1
        self.b+=2

def main(args=None):
    rclpy.init(args=args)
    int_pub=int_add_pub()
    rclpy.spin(int_pub)

    int_pub.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

