#!/usr/bin/env python3

import rospy, time
from std_msgs.msg import Int32MultiArray
from xycar_msgs.msg import xycar_motor

ultra_msg = None
motor_msg = xycar_motor()

def callback(data):
    global ultra_msg
    ultra_msg = data.data

def drive_go():
    global motor_msg, pub
    motor_msg.speed = -5
    motor_msg.angle = 0
    pub.publish(motor_msg)

def drive_stop():
    global motor_msg, pub
    motor_msg.speed = 0
    motor_msg.angle = 0
    pub.publish(motor_msg)

rospy.init_node('ultra_driver')
rospy.Subscriber("xycar_ultrasonic", Int32MultiArray, callback, queue_size=1)
pub = rospy.Publisher('xycar_motor', xycar_motor, queue_size=1)

time.sleep(2)

while not rospy.is_shutdown():

    if ultra_msg[2] > 0 and ultra_msg[2] < 10:
        drive_stop()
    else:
        drive_go()