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


State = True
laser_line = []
laser_old = [0, 0]
dtlaser = 1.0/10


for x in range(180):
    laser_line.append(x*1.8)
print("on")

coordXY = (lambda x, th: [x*math.cos((1.0*th/180)*math.pi), x*math.sin((1.0*th/180)*math.pi)])



def AVGDistlaser(lista):
    x = 0
    y = 0

    for item in lista:

        x = x + modulo(item[0])
        y = y + modulo(item[1])

    return [x/len(lista), y/len(lista)]


def modulo(x):
    return math.sqrt(x**2)


rospy.init_node('ekf_odometry_publisher')


def callback(odo, laser):

    global laser_old

    vx = odo.twist.twist.linear.x
    th = odo.twist.twist.angular.z
    lasercoordenates = []

    for x in range(85, 95):  # degree laser
        lasercoordenates.append(coordXY(laser.ranges[x], laser_line[x]))

    lasers = AVGDistlaser(lasercoordenates)
    vlasers = [(laser_old[0]-lasers[0])/dtlaser, (laser_old[1]-lasers[1])/dtlaser]
    vlasers = math.sqrt((vlasers[0]**2)+(vlasers[1]**2))
    laser_old = lasers

    rospy.loginfo("vx: {}, Th: {}, VLaser: {}".format(vx, th, vlasers))

# class KalmanFilter(object):
#
#
#     KalmanGain = 0
#     Estimativa = 0
#     ErroDaEstimativa = 0
#
#     def __init__(self, ValorEstimado, ErroDoValorEstimado, ValorMedido, ErroDoValorMedido, ValorEstimadoAnterior, ErroDoValorEstimadoAnterior):
#
#         self.ValorEstimado = ValorEstimado
#         self.ErroDoValorEstimado = ErroDoValorEstimado
#
#         self.ValorMedido = ValorMedido
#         self.ErroDoValorMedido = ErroDoValorMedido
#
#         self.ValorEstimadoAnterior = ValorEstimadoAnterior
#         self.ErroDoValorEstimadoAnterior = ErroDoValorEstimadoAnterior
#
#     # def __kalmangain__ (self):
#
#         self.KalmanGain = self.ErroDoValorEstimado / (self.ErroDoValorEstimado + self.ErroDoValorMedido)
#         self.KalmanGain = np.divide(self.ErroDoValorEstimado, (self.ErroDoValorEstimado + self.ErroDoValorMedido))
#
#     # def __estimativa__(self):
#
#         self.Estimativa = self.ValorEstimado + self.KalmanGain * (self.ValorMedido - self.ValorEstimado)
#
#     # def __errodaestimativa__(self):
#
#         self.ErroDaEstimativa = (1 - self.KalmanGain) * self.ErroDoValorEstimadoAnterior
#
#         State = False
#
#         """
#         Atualiza a função com base nos valores já criados.
#         """
#
#     def update(self, ValorEstimado, ErroDoValorEstimado, ValorMedido, ErroDoValorMedido):
#
#         self.__init__(ValorEstimado, ErroDoValorEstimado, ValorMedido, ErroDoValorMedido, self.Estimativa, self.ErroDaEstimativa)
#
#     def getEstimativa(self):
#
#         return self.Estimativa
#
#     def getErroDaEstimativa(self):
#
#         return self.ErroDaEstimativa


odometry_sub = message_filters.Subscriber('/odom', Odometry)

laser_sub = message_filters.Subscriber('/base_scan_1', LaserScan)

ts = message_filters.TimeSynchronizer([odometry_sub, laser_sub], 50)

ts.registerCallback(callback)
rospy.spin()
