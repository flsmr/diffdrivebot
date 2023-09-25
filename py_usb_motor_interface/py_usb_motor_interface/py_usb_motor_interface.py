# Copyright 2016 Open Source Robotics Foundation, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import serial
import time

import rclpy
from rclpy.node import Node

from std_msgs.msg import String
from geometry_msgs.msg import Twist

class MotorInterface(Node):

    def __init__(self):
        super().__init__('motor_interface')
        # subscribe to teleop topic
        self.subscription = self.create_subscription(
            Twist,
            'cmd_vel',
            self.listener_callback,
            10)
        self.subscription  # prevent unused variable warning
        self.ser = serial.Serial('/dev/ttyUSB0', 115200) # start serial connection TODO: configurable USB port

    def listener_callback(self, msg):
        print('Hi from usbInterface.')
        if msg.linear.x == 0.5 and msg.angular.z == 0.0:
            self.ser.write('<1,-255>'.encode('ascii')+ b'\r\n')
            self.ser.write('<2,-255>'.encode('ascii')+ b'\r\n')
            self.ser.write('<3,255>'.encode('ascii')+ b'\r\n')
            self.ser.write('<4,255>'.encode('ascii')+ b'\r\n')
        elif msg.linear.x == 0.5 and msg.angular.z > 0.0:
            self.ser.write('<1,-255>'.encode('ascii')+ b'\r\n')
            self.ser.write('<2,-255>'.encode('ascii')+ b'\r\n')
            self.ser.write('<3,0>'.encode('ascii')+ b'\r\n')
            self.ser.write('<4,0>'.encode('ascii')+ b'\r\n')
        elif msg.linear.x == 0.5 and msg.angular.z < 0.0:
            self.ser.write('<1,0>'.encode('ascii')+ b'\r\n')
            self.ser.write('<2,0>'.encode('ascii')+ b'\r\n')
            self.ser.write('<3,255>'.encode('ascii')+ b'\r\n')
            self.ser.write('<4,255>'.encode('ascii')+ b'\r\n')
        else:
            self.ser.write('<1,0>'.encode('ascii')+ b'\r\n')
            self.ser.write('<2,0>'.encode('ascii')+ b'\r\n')
            self.ser.write('<3,0>'.encode('ascii')+ b'\r\n')
            self.ser.write('<4,0>'.encode('ascii')+ b'\r\n')

def main(args=None):
    rclpy.init(args=args)

    motor_interface = MotorInterface()

    rclpy.spin(motor_interface)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    motor_interface.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()