#!/usr/bin/env python
import rospy
import pyttsx3
from std_msgs.msg import String

class speaker_ros:
    def __init__(self):
        self.engine = pyttsx3.init() 
        #self.rate = engine.getProperty('rate')   # getting details of current speaking rate
        self.engine.setProperty('rate', 180)
        self.sub = rospy.Subscriber("/speak", String, self.speakcall)

    def speakcall(self, text):
        self.engine.say(text)
        self.engine.runAndWait()
        self.engine.stop()

speaker = speaker_ros()