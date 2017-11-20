#!/usr/bin/env python
import roslib; 
import rospy
import numpy as np

from nav_msgs.msg import Odometry

def odometryCb(msg):

    global xodom1, yodom1, angodom1   
    global xodom2, yodom2, angodom2
    global WL, WR

    global xstate1, ystate1, angstate1
    global xstate2, ystate2, angstate2

    #constantes 
    T=0.1
    L=0.587 
    R=0.109
    delta=0.01

    rate = rospy.Rate(10)  #T=0.1s

    #print msg.pose.pose.position.x

    xodom2=msg.pose.pose.position.x
    yodom2=msg.pose.pose.position.y
    angodom2=msg.pose.pose. #???nav_msg
    rate.sleep()



    WL = (xodom2-xodom1)/(float(T*R*math.cos(angodom1))-(L/(float(T*R*2))*(angodom2-angodom1)  #1ª...

    WR = (angodom2-angodom1)*L/(float(T*R))+WL 

    #update variables
    xodom1=xodom2
    yodom1=yodom2
    angodom1=angodom2
    
    xstate2= xstate1+ ((T*R)/(float(2)))*(WR+WL)*math.cos(angstate1)
    ystate2= ystate1+ ((T*R)/(float(2)))*(WR+WL)*math.sin(angstate1)
    angstate2= angstate1+((T*R)/(float(L))*(WR-WL)
  
	#correçao *
    #calcula matrix P

    A=np.mat([[1, 0, (-T*R*(WR+WL)*math.sin(angstate1))/(float(2))],[0, 1, (T*R*(WR+WL)*math.cos(angstate1))/(float(2))],[0,0,1]])


WQ=np.mat([

[(delta*(WR**2)+delta*(WL**2))*((T*R*math.cos(angstate1)/float(2))**2), 
((T*R/float(2))**2)*math.sin(angstate1)*math.cos(angstate1)*(delta*(WR**2)+delta*(WL**2)),
((T*R)**2)*math.cos(angstate1)*(delta*(WR**2)-delta*(WL**2))/float(2*L)],

[((T*R/float(2))**2)*math.sin(angstate1)*math.cos(angstate1)*(delta*(WR**2)+delta*(WL**2)),
(delta*(WR**2)+delta*(WL**2))*((T*R*math.sin(angstate1)/float(2))**2), 
((T*R)**2)*math.sin(angstate1)*(delta*(WR**2)-delta*(WL**2))/float(2*L)],

[((T*R)**2)*math.cos(angstate1)*(delta*(WR**2)-delta*(WL**2))/float(2*L), 
((T*R)**2)*math.sin(angstate1)*(delta*(WR**2)-delta*(WL**2))/float(2*L),
(delta*(WR**2)+delta*(WL**2))*((T*R/float(L))**2)]

])



#funçao...
def func():

    global xodom1, yodom1, angodom1   #odometria anterior 
    global xodom2, yodom2, angodom2   #odometria atual
    global WL, WR                     #omega left, right

#estados a serem atualizados 
    global xstate1, ystate1, angstate1
    global xstate2, ystate2, angstate2

    xodom1=0
    xodom2=0
    yodom=0
    yodom2=0
    angodom1=0
    angodom2=0
    xstate1=0
    xstate2=0
    ystate1=0
    ystate2=0
    angstate1=0
    angstate2=0
    WL=0
    WR=0



    rospy.init_node('oodometry', anonymous=True) #make node 
    rospy.Subscriber('odom',Odometry,odometryCb)
    rospy.spin()



#!! valor x

if __name__ == "__main__":

    func()



