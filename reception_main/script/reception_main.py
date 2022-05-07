#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
from std_msgs.msg import Bool

from time import sleep

from simple_push_button.srv import Buttonblink

rospy.init_node('reception_main',anonymous=True)

led_blink = rospy.ServiceProxy( 'buttun_led_blink', Buttonblink )

def cb_human_detect(human_sensor):
    rospy.loginfo("main cb_human_detect")
    if human_sensor.data == True:
        led_blink()


rospy.Subscriber( 'human_detect', Bool,cb_human_detect)

if __name__ == '__main__':

    rate = rospy.Rate(50)

    try:
        while not rospy.is_shutdown():
            #for now 
            rate.sleep()

    except KeyboardInterrupt:
        #pi.write(PIN_SWITCH_LED,pigpio.LOW)
        pass
    finally:
        #pi.write(PIN_SWITCH_LED,pigpio.LOW)
        pass
