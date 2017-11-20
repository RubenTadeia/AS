#!/usr/bin/env python

import rospy
from std_msgs.msg import Float32




def callback(data):
        
    rate = rospy.Rate(10) # 1hz alterar???
    a=data.data

    global avg
    global var

    #print a
    rate.sleep()
    b=pl(a)
    print "dado novo:", b
    time()
    print "N:", t
    avg=media(b,t,avg)
    print "a media e", avg
    var=variance(var,avg,t,b)
    print "a variancia e", var



def pl(a):
    

    return a


def time():
    global t
    #rate2 = rospy.Rate(10)
    #rate2.sleep()
    t=t+1
    
def media(b,t,avg):
    
    z=avg*(t-1)
    
    avg=(b+z)/t
    return avg

    return avg

def variance(var,avg,t,b):
    
    a=(((((var+(avg*avg))*(t-1))+(b*b))/t)-(avg*avg))
    return a

#print data.data
#rospy.loginfo(rospy.get_caller_id() + "teste  %s", data.data)

def listener():

    global avg
    global var

    avg=0
    var=0
    rospy.init_node('listener', anonymous=True)
    rospy.Subscriber("chatter", Float32, callback)
    #print a
#    media(a)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    t=0
    listener()
    
