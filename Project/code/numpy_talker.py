#!/usr/bin/env python
PKG = 'numpy_tutorial'
import roslib; roslib.load_manifest(PKG)

import rospy
import random
from rospy.numpy_msg import numpy_msg
from rospy_tutorials.msg import Floats

import numpy
def talker():
    pub = rospy.Publisher('floats', numpy_msg(Floats),queue_size=10)
    rospy.init_node('talker', anonymous=True)
    r = rospy.Rate(10) # 10hz

#publish vector with random increments

    a = numpy.array([1.0, 2.1, 3.2, 4.3, 5.4, 6.5], dtype=numpy.float32)


    while not rospy.is_shutdown():
        
        pub.publish(a)
        r.sleep()

        a[0] = a[0] + random.random()
        a[1] = a[1] + random.random()
        a[2] = a[2] + random.random()

        a[3] = a[3] + random.random()
        a[4] = a[4] + random.random()
        a[5] = a[5] + random.random()

if __name__ == '__main__':
    talker()


