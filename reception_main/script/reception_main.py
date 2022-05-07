#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
from std_msgs.msg import Bool

from time import sleep

import simple_push_button.srv

rospy.init_node('reception_main',anonymous=True)

led_blink = rospy.ServiceProxy( 'buttun_led_blink', simple_push_button.srv.Buttionblink )

def cb_human_detect(data):
    rospy.loginfo("main cb_human_detect")
    led_blink()


rospy.Subscliber( 'human_detect', cb_human_detect)

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
