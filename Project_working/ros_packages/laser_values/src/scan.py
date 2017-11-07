#!/usr/bin/env python

# ROS python api with lots of handy ROS functions
import rospy

# to be able to subcribe to laser scanner data
from sensor_msgs.msg import LaserScan

#helpfull videos:
# https://www.youtube.com/watch?v=RFNNsDI2b6c
# https://www.youtube.com/watch?v=q3Dn5U3cSWk

def callback(msg):
    print len(msg.ranges) # Should be 720 values
    print 'Value at 0 degrees:'
    print msg.ranges[0]
    print 'Value at 90 degrees:'
    print msg.ranges[360]
    print 'Value at 180 degrees:'
    print msg.ranges[719]

rospy.init_node('scan_values')
#rospy.Subscriber("RosAria/laser/scan", LaserScan, callback)
sub = rospy.Subscriber("RosAria/laser/scan", LaserScan, callback)
rospy.spin()
