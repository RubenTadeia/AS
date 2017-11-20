#!/usr/bin/env python
import roslib; 
import rospy
import math
import numpy
import matplotlib.pyplot as plt
import re



def create_lines_map(Map,k,l,cluster_map,Occup_grid):
	i = k
	j = l
	if i < 550:
		if j<600:
			if Map[i][j] == 100:
				if Occup_grid[i][j] == 0:
					Occup_grid[i][j] = 1
					cluster_map = cluster_map + (Map[i][j],)
					#agora ver a vizinhanca!?
					while int(Map[i+1][j-1])==100|int(Map[i+1][j]) == 100|int(Map[i+1][j+1]) == 100:
						if int(Map[i+1][j-1]) == 100:
							cluster_map = cluster_map + (Map[i+1][j-1],)
							Occup_grid[i+1][j-1] = 1
							create_lines_map(Map,i+1,j-1,cluster_map,Occup_grid)
						if Map[i+1][j] == 100:
							cluster_map = cluster_map + (Map[i+1][j],)
							Occup_grid[i+1][j] = 1
							create_lines_map(Map,i+1,j,cluster_map,Occup_grid)
						if Map[i+1][j+1] == 100:
							cluster_map = cluster_map + (Map[i+1][j+1],)
							Occup_grid[i+1][j+1] = 1
							create_lines_map(Map,i+1,j+1,cluster_map,Occup_grid)
				#finalizado um cluster, fazer a recta e armazenar as duas coordenadas	
				else:
				
					x_cluster = ()
					y_cluster = ()
				
					x_cluster = x_cluster + (i,)
					y_cluster = y_cluster + (j,)	
				
					A = numpy.vstack([x_cluster, numpy.ones(len(x_cluster))]).T
					m, b = numpy.linalg.lstsq(A, y_cluster)[0]
					print m
					print b
			#plt.plot(x_cluster, y_cluster, 'o', label='Original data', markersize=10)
			#plt.plot(x_cluster, m*x_cluster + b, 'r', label='Fitted line')
			#plt.legend()
			#plt.show()
	
def versao1(Map,cluster_map,Occup_grid):
	k=0
	root_flag = 0
	pontos_ocupados = ()
	for i in range(550):
		for j in range(600):
			if Map[i][j] == 100:
				pontos_ocupados = pontos_ocupados + ([i,j],)
				k = k+1
				
			
	#print pontos_ocupados
	#5752
	root = pontos_ocupados[0]
	recta = () 
	
	for k in range(1,len(pontos_ocupados)-1):
		dist = math.sqrt(abs( (pontos_ocupados[k][0]-pontos_ocupados[k+1][0])**2 + (pontos_ocupados[k][1]-pontos_ocupados[k+1][1])**2))
		
		if (pontos_ocupados[k][1]-root[1]) != 0:
			alpha = math.atan( (pontos_ocupados[k][0]-root[0])/(pontos_ocupados[k][1]-root[1]))
			vertical = 1
			
		if   (len(recta)<5) :
			recta = recta + (pontos_ocupados[k],)
		print recta	
			
		if dist < 10 & len(recta) >5:
			#comparar o declive da recta ja formada com o declive entre a recta e o ponto pretendente
			#primeiro criar a recta com lsq
		
			x_cluster = ()
			y_cluster = ()
			for i in range(len(recta)):
				x_cluster = x_cluster + (recta[i][0],)
				y_cluster = y_cluster + (recta[i][1],)	
			print x_cluster
							
			A = numpy.vstack([x_cluster, numpy.ones(len(recta))]).T
			m, b = numpy.linalg.lstsq(A, y_cluster)[0]
			print m
		
		
			



def find_root(Map,Occupancy_grid,root_ant):
	root_finded = 0
	i=root_ant[0]
	j=root_ant[1]
	
	while root_finded!=1:

		if int(Map[i][j]) == 100 & int(Occupancy_grid[i][j]) == 0:
			print "a" , int(Occupancy_grid[i][j])
			root = (i,j)
			Occupancy_grid[i][j] = 1
			root_finded = 1
			
			return root
			print "ups"
		else:
			j = j+1
			
			if j == 600:
				if i == 550:
					root_finded =1
					print 'root not finded'
				j = 0
				i = i+1
				
	

def find_root2(Map, Occupancy_grid,root):
	
		
def vert_line(Map, Occupancy_grid,line_points,i,j):	
#a primeira vez que se chama a func o i,j sao as coords da root	
	end_line = 0
	
	while end_line == 0:
	#para a primeira linha
		
		if int(Map[i+1][j-1]) == 100 & int(Occupancy_grid[i+1][j-1]) == 0:
			line_points = line_points + ((i+1,j-1),)
			Occupancy_grid[i+1][j-1] = 1
			i = i+1
			j = j-1
			#print 11
			vert_line(Map, Occupancy_grid,line_points,i,j)
			return line_points	
			
		elif int(Map[i+1][j]) == 100 & int(Occupancy_grid[i+1][j]) == 0:
			line_points = line_points + ((i+1,j),)
			Occupancy_grid[i+1][j] = 1
			i = i+1
			j = j
			#print 12
			vert_line(Map, Occupancy_grid,line_points,i,j)
			return line_points	
			                                                              
		elif int(Map[i+1][j+1]) == 100 & int(Occupancy_grid[i+1][j+1])== 0:
			line_points = line_points + ((i+1,j+1),)
			Occupancy_grid[i+1][j+1] = 1
			i = i+1
			j = j+1
			#print 13
			vert_line(Map, Occupancy_grid,line_points,i,j)
			return line_points
	#	if (int(Map[i+1][j-1]) != 100 | int(Occupancy_grid[i+1][j-1]) == 1)&(int(Map[i+1][j]) != 100 & int(Occupancy_grid[i+1][j]) == 1	)&(int(Map[i+1][j+1]) != 100 | int(Occupancy_grid[i+1][j+1]) == 1):
		#	end_line = 1
	
	#para a segunda linha	
		elif int(Map[i+2][j-1]) == 100 & int(Occupancy_grid[i+2][j-1]) == 0:
			line_points = line_points + ((i+2,j-1),)
			Occupancy_grid[i+2][j-1] = 1
			i = i+2
			j = j-1
			#print 21
			vert_line(Map, Occupancy_grid,line_points,i,j)	
			return line_points
		elif int(Map[i+2][j]) == 100 & int(Occupancy_grid[i+2][j]) == 0:
			line_points = line_points + ((i+2,j),)
			Occupancy_grid[i+2][j] = 1
			i = i+2
			j = j
			#print 22
			vert_line(Map, Occupancy_grid,line_points,i,j)	
			return line_points
		elif int(Map[i+2][j+1]) == 100 & int(Occupancy_grid[i+2][j+1])== 0:
			line_points = line_points + ((i+2,j+1),)
			Occupancy_grid[i+2][j+1] = 1
			i = i+2
			j = j+1
			#print 23
			vert_line(Map, Occupancy_grid,line_points,i,j)	
			return line_points
	#para a terceira linha	
	#	if int(Map[i+3][j-1]) == 100 & int(Occupancy_grid[i+3][j-1]) == 0:
	#		line_points = line_points + ((i+3,j-1),)
	#		Occupancy_grid[i+3][j-1] = 1
	#		i = i+3
	#		j = j-1
	#		print 31
	#		vert_line(Map, Occupancy_grid,line_points,i,j)	
	#	if int(Map[i+3][j]) == 100 & int(Occupancy_grid[i+3][j]) == 0:
	#		line_points = line_points + ((i+3,j),)
	#		Occupancy_grid[i+3][j] = 1
	#		i = i+3
	#		j = j
	#		print 32
	#		vert_line(Map, Occupancy_grid,line_points,i,j)	
	#	if int(Map[i+3][j+1]) == 100 & int(Occupancy_grid[i+3][j+1])== 0:
	#		line_points = line_points + ((i+3,j+1),)
	#		Occupancy_grid[i+3][j+1] = 1
	#		i = i+3
	#		j = j+1
	#		print 33
	#		vert_line(Map, Occupancy_grid,line_points,i,j)	
		
		
	#para a quarta linha	
	#	if int(Map[i+4][j-1]) == 100 & int(Occupancy_grid[i+4][j-1]) == 0:
	#		line_points = line_points + ((i+4,j-1),)
	#		Occupancy_grid[i+4][j-1] = 1
	#		i = i+4
	#		i = j-1
	#		print 41
	#		vert_line(Map, Occupancy_grid,line_points,i,j)	
	#	if int(Map[i+4][j]) == 100 & int(Occupancy_grid[i+4][j]) == 0:
	#		line_points = line_points + ((i+4,j),)
	#		Occupancy_grid[i+4][j] = 1
	#		i = i+4
	#		j = j
	#		print 42
	#		vert_line(Map, Occupancy_grid,line_points,i,j)	
		#if int(Map[i+4][j+1]) == 100 & int(Occupancy_grid[i+4][j+1])== 0:
		#	line_points = line_points + ((i+4,j+1),)
		#	Occupancy_grid[i+4][j+1] = 1
		#	i = i+4
		#	j = j+1
		#	print 43
		#	vert_line(Map, Occupancy_grid,line_points,i,j)	
		
		
		
		
		
		#if (int(Map[i+1][j-1]) != 100 | int(Occupancy_grid[i+1][j-1]) == 1)&(int(Map[i+1][j]) != 100 | int(Occupancy_grid[i+1][j]) == 1	)&(int(Map[i+1][j+1]) != 100 | int(Occupancy_grid[i+1][j+1]) == 1) &(int(Map[i+2][j-1]) != 100 | int(Occupancy_grid[i+2][j-1]) == 1)&(int(Map[i+2][j]) != 100 | int(Occupancy_grid[i+2][j]) == 1)&(int(Map[i+2][j+1]) != 100 | int(Occupancy_grid[i+2][j+1]) == 1):#&(int(Map[i+3][j-1]) != 100 | int(Occupancy_grid[i+3][j-1]) == 1)&(int(Map[i+3][j]) != 100 & int(Occupancy_grid[i+3][j]) == 1)&(int(Map[i+3][j+1]) != 100 | int(Occupancy_grid[i+3][j+1]) == 1)#&	(int(Map[i+4][j-1]) != 100 | int(Occupancy_grid[i+4][j-1]) == 1)&(int(Map[i+4][j]) != 100 & int(Occupancy_grid[i+4][j]) == 1)&(int(Map[i+4][j+1]) != 100 | int(Occupancy_grid[i+4][j+1]) == 1):
		end_line = 1
		
	
	return line_points
			
			
			
			
			
			
			
if __name__ == "__main__":
				
				
	c=600
	l=550
	
	x = numpy.zeros((l, c))
	 
	Occupancy_grid=numpy.zeros((550,600))
	
	
	
	
	with open('/home/vitor/Desktop/map3.txt','r') as f:
		for line in f:
			if line.startswith('data:'):
				b = re.findall(r'\d+', line)

	w=0
	for i in reversed(xrange(l)):
		for j in xrange(c):
			x[i,j] =  b[w]
			w=w+1		
	cluster_rect = ()
	end = 0
	root = (0,0)
	
	while end != 5:
		
		root = find_root(x,Occupancy_grid,root)	
		print root
		print int(x[root[0]][root[1]])	
		line_points = vert_line(x,Occupancy_grid,(root,),root[0],root[1])	
		cluster_rect = cluster_rect + (line_points,)	
		end = end+1
		
		
			
	print cluster_rect			
			
				
				
				
				
				
				
				
				
				
				
			
					
