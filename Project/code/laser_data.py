#!/usr/bin/env python
import roslib
import rospy
import math
import numpy
import matplotlib.pyplot as plt

from sensor_msgs.msg import LaserScan


def create_lines_map(Map,k,l,cluster_map,Occup_grid):
	Map = Map[550][600]
	Occup_grid = numpy.zeros((550,600))
	for i in range(k,550):
		for j in range(l,600):
			if Map[i][j] == 100:
				Occup_grid[i][j] = 1
				cluster_map = cluster_map + (Map[i][j],)
				#agora ver a vizinhança!?
			while (Map[i+1][j-1] == 100 or Map[i+1][j] == 100 or Map[i+1][j+1] == 100):
				if Map[i+1][j-1] == 100 :
					cluster_map = cluster_map + (Map[i+1][j-1],)
					Occup_grid[i+1][j-1] = 1
					create_lines_map(Map,i+1,j-1,cluster_map,Occup_grid)
				if Map[i+1][j] == 100 :
					cluster_map = cluster_map + (Map[i+1][j],)
					Occup_grid[i+1][j] = 1
					create_lines_map(Map,i+1,j,cluster_map,Occup_grid)
				if Map[i+1][j+1] == 100 :
					cluster_map = cluster_map + (Map[i+1][j+1],)
					Occup_grid[i+1][j+1] = 1
					create_lines_map(Map,i+1,j+1,cluster_map,Occup_grid)
					
			



def compar_rectas(r_robot, psi_robot, matrix):
	#primeiro é necessário criar todas as rectas do mapa
	Occup_matrix = numpy.zeros((550,600))
	cl_row=()
	cl_collum=()
	for i in range(550):
		for j in range(600):
			if matrix[i][j]==100:
				cl_row = cl_row + (
	
	
	#agora comparar as rectas:
	




def laser_rangeCb(msg):
	a = msg.ranges	
	for k in range(0, 180):
		b = msg.angle_min+k*msg.angle_increment 
		print b	

	



def points_calcul(msg):
	point = (range(0,180))
	a = msg.ranges	
	for k in range(0, 180):
		point[k] = (a[k]*math.sin(-(msg.angle_min+k*msg.angle_increment)),
	 	a[k]*math.cos(msg.angle_min+k*msg.angle_increment))
#	print point	

#def create_cluster(point)
	index = 0
	n_min = 4 #numero minimo de elementos de um cluster
	cluster = () 
	cluster = cluster + (point[0],) # por o primeiro ponto do cluster
	for k in range(0, 179):
		dist = math.sqrt(abs( (point[k][0]-point[k+1][0])**2 + (point[k][1]-point[k+1][1])**2))
		if dist < 0.1:
			cluster = cluster + (point[k+1],)
				
				
		else:
		#cluster finalizado, portanto tenho de criar a recta e renicializar o cluster
			if len(cluster) > n_min:
				x_cluster = ()
				y_cluster = ()
				for i in range(len(cluster)):
					x_cluster = x_cluster + (cluster[i][0],)
					y_cluster = y_cluster + (cluster[i][1],)			

				A = numpy.vstack([x_cluster, numpy.ones(len(x_cluster))]).T
				m, b = numpy.linalg.lstsq(	A, y_cluster)[0]
				#y = m*x+b rezar para que isto esteja certo!
				#agora vou ter de transformar a linha y=mx+b em parametros decentes
				U = [0 for x in range(len(x_cluster))],[1 for x in range(len(x_cluster))]
				Y = [0 for x in range(len(y_cluster))]
				for i in range(len(cluster)):
					U[0][i] = x_cluster[i]
					Y[i] = y_cluster[i]
			
				
				X = numpy.matrix(U)
				x4 = numpy.matrix(Y)
				x4 = x4.T
				
				X = X.T
				x1 = (X.T) * X
				x2 = x1.I
				x3 = x2 * X.T
				teta = x3 * x4
				print cluster
				print teta # aqui temos o K e o C
				
				#transformacao dos parametros de teta em r e psi
				sign = numpy.sign(teta[1])
				r = (teta[1]/numpy.sqrt(teta[0]**2 +1)) * sign
				
				psi = numpy.arctan2(sign/numpy.sqrt(teta[0]**2+1), (-teta[0]/numpy.sqrt(teta[0]**2+1))*sign)
				
				#chamada da funcao de comparacao de rectas!
					
			
#inicializacao do novo cluster	
				cluster = ()
				cluster = cluster + (point[k+1],) #por o primeiro
			else:
				cluster = ()
				cluster = cluster + (point[k+1],)

	
			



   
if __name__ == "__main__":
    rospy.init_node('my_range', anonymous=True) #make node 
    #rospy.init.node('myteste', anonymous=True) 			
    #rospy.Subscriber('scan',LaserScan,laser_rangeCb)
    rospy.Subscriber('scan', LaserScan,points_calcul)
    rospy.spin()
