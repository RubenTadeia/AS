#!/usr/bin/env python

import rospy
from nav_msgs.msg import Odometry
from geometry_msgs.msg import Point, Pose, Quaternion, Twist, Vector3

import rosaria
import robot_pose_ekf


# def callbackrosaria():
#     print rosaria


def callback(msg):
    x = msg.pose.pose.position.x
    y = msg.pose.pose.position.y
    rospy.loginfo("x: {}, y: {}".format(x, y))

def main():
    rospy.init_node('location_monitor')
    rospy.Subscriber("/zoeira", Odometry, callback)
    rospy.spin()

if __name__ == '__main__':
    main()



