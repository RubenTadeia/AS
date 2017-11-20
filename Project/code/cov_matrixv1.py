#!/usr/bin/env python
# coding=utf-8

PKG = 'numpy_tutorial'
import roslib; roslib.load_manifest(PKG)

import rospy
from rospy_tutorials.msg import Floats
from rospy.numpy_msg import numpy_msg

def callback(data):

    rate = rospy.Rate(10)

    global avg_x, avg_y,avg_z,avg_roll,avg_pitch,avg_yaw
    global var_x, var_y,var_z,var_roll,var_pitch,var_yaw, var_xy,var_xz,var_xroll,var_xpitch,var_xyaw,var_yz,var_yroll,var_ypitch,var_yyaw,var_zroll,var_zpitch,var_zyaw,var_rollpitch,var_rollyaw,var_pitchyaw
    global inc_x,inc_y,inc_z,inc_roll,inc_pitch,inc_yaw
    global last_value_x,last_value_y,last_value_z,last_value_roll,last_value_pitch,last_value_yaw


    
    
    print "%s" %str(data.data)
    print "====//===="
    print "teste"
    #print "x=", data.data[1]
    x=data.data[0]
    y=data.data[1]
    z=data.data[2]
    roll=data.data[3]
    pitch=data.data[4]
    yaw=data.data[5]
# get data thats being published in numpy_talker
    rate.sleep()
    time()

    inc_x=incr(x,last_value_x)
    inc_y=incr(y,last_value_y)
    inc_z=incr(z,last_value_z)
    inc_roll=incr(roll,last_value_roll)
    inc_pitch=incr(pitch,last_value_pitch)
    inc_yaw=incr(yaw,last_value_yaw)

    last_value_x=x
    last_value_y=y
    last_value_z=z
    last_value_roll=roll
    last_value_pitch=pitch
    last_value_yaw=yaw
# calculate average value and variances...
    avg_x=media(inc_x,t,avg_x)
    avg_y=media(inc_y,t,avg_y)
    avg_z=media(inc_z,t,avg_z)
    avg_roll=media(inc_roll,t,avg_roll)
    avg_pitch=media(inc_pitch,t,avg_pitch)
    avg_yaw=media(inc_yaw,t,avg_yaw)

    var_x=variance(var_x,avg_x,avg_x,inc_x,inc_x,t)
    var_y=variance(var_y,avg_y,avg_y,inc_y,inc_y,t)
    var_z=variance(var_z,avg_z,avg_z,inc_z,inc_z,t)
    var_roll=variance(var_roll,avg_roll,avg_roll,inc_roll,inc_roll,t)
    var_pitch=variance(var_pitch,avg_pitch,avg_pitch,inc_pitch,inc_pitch,t)
    var_yaw=variance(var_yaw,avg_yaw,avg_yaw,inc_yaw,inc_yaw,t)

    var_xy=variance(var_xy,avg_x,avg_y,inc_x,inc_y,t)
    var_xz=variance(var_xz,avg_x,avg_z,inc_x,inc_z,t)
    var_xroll=variance(var_xroll,avg_x,avg_roll,inc_x,inc_roll,t)
    var_xpitch=variance(var_xpitch,avg_x,avg_pitch,inc_x,inc_pitch,t)
    var_xyaw=variance(var_xyaw,avg_x,avg_yaw,inc_x,inc_yaw,t)
    var_yz=variance(var_yz,avg_y,avg_z,inc_y,inc_z,t)
    var_yroll=variance(var_yroll,avg_y,avg_roll,inc_y,inc_roll,t)
    var_ypitch=variance(var_ypitch,avg_y,avg_pitch,inc_y,inc_pitch,t)
    var_yyaw=variance(var_yyaw,avg_y,avg_yaw,inc_y,inc_yaw,t)
    var_zroll=variance(var_zroll,avg_z,avg_roll,inc_z,inc_roll,t)
    var_zpitch=variance(var_zpitch,avg_z,avg_pitch,inc_z,inc_pitch,t)
    var_zyaw=variance(var_zyaw,avg_z,avg_yaw,inc_z,inc_yaw,t)
    var_rollpitch=variance(var_rollpitch,avg_roll,avg_pitch,inc_roll,inc_pitch,t)
    var_rollyaw=variance(var_rollyaw,avg_roll,avg_yaw,inc_roll,inc_yaw,t)
    var_pitchyaw=variance(var_pitchyaw,avg_pitch,avg_yaw,inc_pitch,inc_yaw,t)

# place data in matrix
    Matrix = [[0 for x in range(6)] for x in range(6)]

    Matrix[0][0]=var_x
    Matrix[1][1]=var_y
    Matrix[2][2]=var_z
    Matrix[3][3]=var_roll
    Matrix[4][4]=var_pitch
    Matrix[5][5]=var_yaw

    Matrix[0][1]=var_xy
    Matrix[1][0]=var_xy
    Matrix[0][2]=var_xz
    Matrix[2][0]=var_xz
    Matrix[0][3]=var_xroll
    Matrix[3][0]=var_xroll
    Matrix[0][4]=var_xpitch
    Matrix[4][0]=var_xpitch
    Matrix[0][5]=var_xyaw
    Matrix[5][0]=var_xyaw

    Matrix[1][2]=var_yz
    Matrix[2][1]=var_yz
    Matrix[1][3]=var_yroll
    Matrix[3][1]=var_yroll
    Matrix[1][4]=var_ypitch
    Matrix[4][1]=var_ypitch
    Matrix[1][5]=var_yyaw
    Matrix[5][1]=var_yyaw

    Matrix[2][3]=var_zroll
    Matrix[3][2]=var_zroll
    Matrix[2][4]=var_zpitch
    Matrix[4][2]=var_zpitch
    Matrix[2][5]=var_zyaw
    Matrix[5][2]=var_zyaw

    Matrix[3][4]=var_rollpitch
    Matrix[4][3]=var_rollpitch
    Matrix[3][5]=var_rollyaw
    Matrix[5][3]=var_rollyaw

    Matrix[4][5]=var_pitchyaw
    Matrix[5][4]=var_pitchyaw

    print "N=", t
    #print "inc_x",inc_x
    #print "avg_x", avg_x
    #print "var_x", var_x

    print "cov:", Matrix



def pl(a):
    

    return a

def time():
# number of "samples"
    global t
    t=t+1


def media(b,t,avg):
# function to calculate average value
    if t<=0:
        t=1

    z=avg*(t-1)
    
    avg=(b+z)/t
    return avg

def incr(b,last_value):
# function to calculate increment
    if last_value==0:
         return 0
    else:
         return b-last_value

def variance(old_var,avg1,avg2,inc1,inc2,t):
# function to calculate variance
    old_avg1=avg1*(t)-inc1
    old_avg2=avg2*(t)-inc2

    var=old_var+((inc1-old_avg1)*(inc2-old_avg2))*((t-1)/float(t))
    var=var/(float(t))

    return abs(var)


def listener():

    global avg_x, avg_y,avg_z,avg_roll,avg_pitch,avg_yaw
    global var_x, var_y,var_z,var_roll,var_pitch,var_yaw, var_xy,var_xz,var_xroll,var_xpitch,var_xyaw,var_yz,var_yroll,var_ypitch,var_yyaw,var_zroll,var_zpitch,var_zyaw,var_rollpitch,var_rollyaw,var_pitchyaw
    global inc_x,inc_y,inc_z,inc_roll,inc_pitch,inc_yaw
    global last_value_x,last_value_y,last_value_z,last_value_roll,last_value_pitch,last_value_yaw
    global var

# initialize variables
    avg=0
    var=0
    
    avg_x=0
    avg_y=0
    avg_z=0
    avg_roll=0
    avg_pitch=0
    avg_yaw=0
    last_value_x=0
    last_value_y=0
    last_value_z=0
    last_value_roll=0
    last_value_pitch=0
    last_value_yaw=0
    inc_x=0
    inc_y=0
    inc_z=0
    inc_roll=0
    inc_pitch=0
    inc_yawvar_x=0
    var_x=0
    var_y=0
    var_z=0
    var_roll=0
    var_pitch=0
    var_yaw=0
    var_xy=0
    var_xz=0
    var_xroll=0
    var_xpitch=0
    var_xyaw=0
    var_yz=0
    var_yroll=0
    var_ypitch=0
    var_yyaw=0
    var_zroll=0
    var_zpitch=0
    var_zyaw=0
    var_rollpitch=0
    var_rollyaw=0
    var_pitchyaw=0


    rospy.init_node('listener')
    rospy.Subscriber("floats",numpy_msg(Floats) , callback)
    rospy.spin()

if __name__ == '__main__':

    t=0
    listener()
