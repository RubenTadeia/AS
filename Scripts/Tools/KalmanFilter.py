# coding=utf-8
import numpy as np
import message_filters

import rospy
import tf
from nav_msgs.msg import Odometry
from geometry_msgs.msg import Point, Pose, Quaternion, Twist, Vector3
from sensor_msgs.msg import LaserScan
import math

# Esse codigo é nosso, só o comentario do commit que foi automatico (igual do ultimo).
# The Error from Laser is 30 mm
# we gonna use the Kalman Filter to improve quality from

"""
-------------------  -------------------  ------------------- 
-------------------   Goblal Utilities    ------------------- 
-------------------  -------------------  -------------------
"""

State = True
laser_line = []
laser_old = [0, 0]
dtlaser = 1.0/10

rospy.init_node('ekf_odometry_publisher')
odom_pub = rospy.Publisher("EFF_Odom", Odometry, queue_size=50)
odom_broadcaster = tf.TransformBroadcaster()

current_time = rospy.Time.now()
last_time = rospy.Time.now()

r = rospy.Rate(10)

for x in range(180):
    laser_line.append(x*1.8)
# print("on")

coordXY = (lambda x, th: [x*math.cos((1.0*th/180)*math.pi), x*math.sin((1.0*th/180)*math.pi)])
# print("on1")


"""
-------------------     Functions       -------------------
"""

def AVGDistlaser(lista):
    x = 0
    y = 0

    for item in lista:

        x = x + modulo(item[0])
        y = y + modulo(item[1])

    return [x/len(lista), y/len(lista)]


def modulo(x):
    return math.sqrt(x**2)




# print("on2")
"""
-------------------  -------------------  ------------------- 
-------------------      Loop of EKF      ------------------- 
-------------------  -------------------  -------------------
"""
numstates = 5
dt = 1.0/10.0  # Sample Rate of the Measurements is 50Hz
dtLASER = 1.0/10.0  # Sample Rate of Laser is 50Hz
# ## Initial Uncertainty $P_0$
P = np.diag([1000.0, 1000.0, 1000.0, 1000.0, 1000.0])
sLaser = 5*dt  # assume 8.8m/s2 as maximum acceleration, forcing the vehicle
sCourse = 0.1*dt  # assume 0.1rad/s as maximum turn rate for the vehicle
sVelocity = 5*dt  # assume 8.8m/s2 as maximum acceleration, forcing the vehicle
sYaw = 1.0*dt  # assume 1.0rad/s2 as the maximum turn rate acceleration for the vehicle

Q = np.diag([sLaser**2, sLaser**2, sCourse**2, sVelocity**2, sYaw**2])


varLASER = 0.3  # Standard Deviation of LASER Measurement
varspeed = 1.0  # Variance of the speed measurement
varyaw = 0.1  # Variance of the yawrate measurement
R = np.matrix([[varLASER**2, 0.0, 0.0, 0.0, 0.0],
               [0.0, varLASER**2, 0.0, 0.0, 0.0],
               [0.0, 0.0, varyaw*varspeed, 0.0, 0.0],
               [0.0, 0.0, 0.0, varspeed**2, 0.0],
               [0.0, 0.0, 0.0, 0.0, varyaw**2]])

I = np.eye(numstates)

# ## Initial State
P = np.diag([1000.0, 1000.0, 1000.0, 1000.0, 1000.0])

# Matrix(x,y,th,Velocity,Algular Rate)
x = np.matrix([[0, 0, np.pi/2, 0, 0]]).T

# Preallocation for Plotting
x0 = []
x1 = []
x2 = []
x3 = []
x4 = []
x5 = []
Zx = []
Zy = []
Px = []
Py = []
Pdx = []
Pdy = []
Pddx = []
Pddy = []
Kx = []
Ky = []
Kdx = []
Kdy = []
Kddx = []
dstate = []

Z = None

#
# def savestates(x, Z, P, K):
#     x0.append(float(x[0]))
#     x1.append(float(x[1]))
#     x2.append(float(x[2]))
#     x3.append(float(x[3]))
#     x4.append(float(x[4]))
#     Zx.append(float(Z[0]))
#     Zy.append(float(Z[1]))
#     Px.append(float(P[0, 0]))
#     Py.append(float(P[1, 1]))
#     Pdx.append(float(P[2, 2]))
#     Pdy.append(float(P[3, 3]))
#     Pddx.append(float(P[4, 4]))
#     Kx.append(float(K[0, 0]))
#     Ky.append(float(K[1, 0]))
#     Kdx.append(float(K[2, 0]))
#     Kdy.append(float(K[3, 0]))
#     Kddx.append(float(K[4, 0]))

# -------------------      END EKF GLOBAL   -------------------#
# print("on-on")
def callback(odo, laser):

    global laser_old
    global x
    global Z
    global P


    vx = odo.twist.twist.linear.x
    th = odo.twist.twist.angular.z
    lasercoordenates = []

    for x_laser in range(85, 95):  # degree laser
        lasercoordenates.append(coordXY(laser.ranges[x_laser], laser_line[x_laser]))

    lasers = AVGDistlaser(lasercoordenates)
    vlasers = [(laser_old[0]-lasers[0])/dtlaser, (laser_old[1]-lasers[1])/dtlaser]
    vlasers = math.sqrt((vlasers[0]**2)+(vlasers[1]**2))

    if (vlasers > vx*2) or (th != 0) or (vlasers < vx/2):  # filter of non sense valors
        vlasers = 0.0

    laser_old = lasers

    # rospy.loginfo("vx: {}, Th: {}, VLaser: {}".format(vx, th, vlasers))

    """
    -------------------  -------------------  ------------------- 
    -------------------          EKF          ------------------- 
    -------------------  -------------------  -------------------
    """

    # Time Update (Prediction)
    # ========================
    # Project the state ahead
    # see "Dynamic Matrix"
    if np.abs(odo.twist.twist.angular.z) < 0.0001: # Driving straight
        # print x
        x[0] = x[0] + x[3]*dt * np.cos(x[2])
        x[1] = x[1] + x[3]*dt * np.sin(x[2])
        x[2] = x[2]
        x[3] = x[3]
        x[4] = 0.0000001 # avoid numerical issues in Jacobians
        dstate.append(0)
    else: # otherwise
        x[0] = x[0] + (x[3]/x[4]) * (np.sin(x[4]*dt+x[2]) - np.sin(x[2]))
        x[1] = x[1] + (x[3]/x[4]) * (-np.cos(x[4]*dt+x[2]) + np.cos(x[2]))
        x[2] = (x[2] + x[4]*dt + np.pi) % (2.0*np.pi) - np.pi
        x[3] = x[3]
        x[4] = x[4]
        dstate.append(1)

    # Calculate the Jacobian of the Dynamic Matrix A
    # see "Calculate the Jacobian of the Dynamic Matrix with respect to the state vector"
    a13 = float((x[3]/x[4]) * (np.cos(x[4]*dt+x[2]) - np.cos(x[2])))
    a14 = float((1.0/x[4]) * (np.sin(x[4]*dt+x[2]) - np.sin(x[2])))
    a15 = float((dt*x[3]/x[4])*np.cos(x[4]*dt+x[2]) - (x[3]/x[4]**2)*(np.sin(x[4]*dt+x[2]) - np.sin(x[2])))
    a23 = float((x[3]/x[4]) * (np.sin(x[4]*dt+x[2]) - np.sin(x[2])))
    a24 = float((1.0/x[4]) * (-np.cos(x[4]*dt+x[2]) + np.cos(x[2])))
    a25 = float((dt*x[3]/x[4])*np.sin(x[4]*dt+x[2]) - (x[3]/x[4]**2)*(-np.cos(x[4]*dt+x[2]) + np.cos(x[2])))

    JA = np.matrix([[1.0, 0.0, a13, a14, a15],
                    [0.0, 1.0, a23, a24, a25],
                    [0.0, 0.0, 1.0, 0.0, dt],
                    [0.0, 0.0, 0.0, 1.0, 0.0],
                    [0.0, 0.0, 0.0, 0.0, 1.0]])


    # Project the error covariance ahead
    P = JA * P * JA.T + Q

    # Measurement Update (Correction)
    # ===============================
    # Measurement Function
    hx = np.matrix([[float(x[0])],
                    [float(x[1])],
                    [float(x[2])],
                    [float(x[3])],
                    [float(x[4])]])

    JH = np.matrix([[1.0, 0.0, 0.0, 0.0, 0.0],
                    [0.0, 1.0, 0.0, 0.0, 0.0],
                    [0.0, 0.0, 1.0, 0.0, 0.0],
                    [0.0, 0.0, 0.0, 1.0, 0.0],
                    [0.0, 0.0, 0.0, 0.0, 1.0]])

    S = JH*P*JH.T + R
    K = (P*JH.T) * np.linalg.inv(S)

    # Update the estimate via
    measurements = np.array([odo.pose.pose.position.x, odo.pose.pose.position.y, 1, odo.twist.twist.linear.x, odo.twist.twist.angular.z])
    Z = measurements.reshape(JH.shape[0], 1)
    y = Z - (hx)                        # Innovation or Residual
    x = x + (K*y)

    # Update the error covariance
    P = (I - (K*JH))*P

    """
    -------------------  -------------------  ------------------- 
    -------------------  Publish our Topic    ------------------- 
    -------------------  -------------------  -------------------
    """

    global last_time

    Vector_EKF = x

    current_time = rospy.Time.now()

    ekf_x = Vector_EKF[0]
    ekf_y = Vector_EKF[1]
    speed = Vector_EKF[3]
    yawrate = Vector_EKF[4]

    odom_quat = tf.transformations.quaternion_from_euler(0, 0, th)

    odom_broadcaster.sendTransform(
        (ekf_x, ekf_y, 0.),
        odom_quat,
        current_time,
        "base_link",
        "odom"
    )

    odom = Odometry()
    odom.header.stamp = current_time
    odom.header.frame_id = "odom"

    # Debug

    # print float(ekf_x)
    # print float(ekf_y)

    odom.pose.pose = Pose(Point(ekf_x, ekf_y, 0.), Quaternion(*odom_quat))

    odom.child_frame_id = "base_link"
    odom.twist.twist = Twist(Vector3(speed * math.cos(yawrate), speed * math.sin(yawrate), 0), Vector3(0, 0, yawrate))
    odom_pub.publish(odom)

    last_time = current_time
    # r.sleep()


"""
-------------------  -------------------  ------------------- 
------------------- Config of Subscriber  ------------------- 
-------------------  -------------------  -------------------
"""


odometry_sub = message_filters.Subscriber('/odom', Odometry)

laser_sub = message_filters.Subscriber('/base_scan_1', LaserScan)

ts = message_filters.TimeSynchronizer([odometry_sub, laser_sub], 10)

ts.registerCallback(callback)
rospy.spin()
