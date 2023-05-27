'''
*********************************************************************************
*
*        		===============================================
*           		        CYBORG OPENCV TASK 2
*        		===============================================
*
*
*********************************************************************************
'''

# Author Name:		[]
# Roll No:			[]
# Filename:			task_2_{your name}.py
# Functions:		detect_arena_parameters
# 					[ Comma separated list of functions in this file ]


####################### IMPORT MODULES #######################
   ## You are free to make any changes in this section. ##
##############################################################
import cv2
import numpy as np
##############################################################

def detect_arena_parameters(maze_image):

  Image_hsv    = cv2.cvtColor(maze_image, cv2.COLOR_BGR2HSV)
  img_1        = cv2.imread('Opencv/maze_0.png')
  img_2        = cv2.cvtColor(img_1, cv2.COLOR_BGR2GRAY)
  _, threshold = cv2.threshold(img_2, 200, 255, cv2.THRESH_BINARY)
  contours, _  = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
  #VARIABLES
  Cx    =  0
  Cy    =  0
  node  =  0
  Alpha = 65
  nu    = 48
  #LIST
  Nodes        = []
  Every_node   = []
  Every_STRING = []
  Traffic      = []
  start        = []
  V_Road       = []
  H_Road       = []
  SHOP_1       = []
  SHOP_2       = []
  SHOP_3       = []
  SHOP         = []
  arena_parameters ={"Traffic":[] , "Start":[] ,"Vertical Roads":[],"Horizontal Roads":[],"Shops":[]}
  #NODE DETECTION
  while Cy<= 799:
      while Cx<= 799 :
          #COLOR PICKER
          pixel = maze_image[Cy,Cx]
          Blue  = pixel[0]
          Red   = pixel[2]
          Green = pixel[1]
          #COLOR MATCHER BLUE_NODES
          if Blue==255 and Red==0 and Green==0:
              a    =  chr(Alpha)
              b    =  chr(nu+1)
              string = a + b
              Nodes.append((string,(Cx+6,Cy+6)))
              Every_STRING.append(string)
              Every_node.append((Cx+6,Cy+6))
              Cx=Cx+12
              Alpha=Alpha+1
              node=node+1
              if node==7 or node==14 or node==21 or node==28 or node==35 or node==42 or node==49:
                  nu=nu+1
                  Cy=Cy+12
          #COLOR MATCHER TRAFFIC_LIGHT
          elif Blue==0 and Red==255 and Green==0:
              a=chr(Alpha)
              b=chr(nu+1)
              string = a + b
              Traffic.append(string)
              Every_node.append((Cx+6,Cy+6))
              Every_STRING.append(string)
              Alpha=Alpha+1
              Cx=Cx+12
              node=node+1
              if node==7 or node==14 or node==21 or node==28 or node==35 or node==42 or node==49:
                  nu=nu+1
                  Cy=Cy+12
          #COLOR MATCHER START_POINT
          if Cx==94 and Cy==694:
              a=chr(Alpha)
              b=chr(nu+1)
              string = a + b
              start.append(string)
              Every_node.append((Cx+6,Cy+6))
              Every_STRING.append(string)
              node=node+1
              Alpha=Alpha+1
          Cx=Cx+1 
          string = ""
      Cy=Cy+1
      Alpha=65
      Cx=0
  Cy=0
  Cx=0
  while Cx<49:
      if Cx==6 or Cx==13 or Cx==20 or Cx==27 or Cx==34 or Cx==41 or Cx==48:
          1
      else:
          pixel = maze_image[(int(Every_node[Cx][1]),int(Every_node[Cx][0])+10)]
          Blue = pixel[0]
          Red = pixel[2]
          Green = pixel[1]
          if Blue!=0 or Red!=0 or Green!=0:
             H_Road.append((Every_STRING[Cx],Every_STRING[Cx+1]))
      Cx=Cx+1
  Cx=0
  while Cy<49:
      if Cy==42 or Cy==43 or Cy==44 or Cy==45 or Cy==46 or Cy==47 or Cy==48:
          pass
      else:
          pixel = maze_image[(int(Every_node[Cy][1])+10,int(Every_node[Cy][0]))]
          Blue = pixel[0]
          Red = pixel[2]
          Green = pixel[1]
          if Blue!=0 or Red!=0 or Green!=0:
             V_Road.append((Every_STRING[Cy],Every_STRING[Cy+7]))
      Cy=Cy+1
  Cy=0
  for contour in contours:
      approx = cv2.approxPolyDP(contour, 0.02* cv2.arcLength(contour, True), True)
      cv2.drawContours(img_1, [contour], 0, (0, 0, 255), 5)
      M = cv2.moments(contour)
      x,y,w,h =cv2.boundingRect(approx)
      x_mid=int(x+w/2)
      y_mid=int(y+h/2)
      if len(approx) == 3:
          pixel=img_1[y_mid,x_mid]
          Blue = pixel[0]
          Green= pixel[1]
          Red  = pixel[2]
          if Blue==0 and Green==255 and Red==0:
              if x_mid>=110 and x_mid<=190:
                  SHOP_1.append('SHOP_1')
              if x_mid>=210 and x_mid<=290:
                  SHOP_1.append('SHOP_2')
              if x_mid>=310 and x_mid<=390:
                  SHOP_1.append('SHOP_3')
              if x_mid>=410 and x_mid<=490:
                  SHOP_1.append('SHOP_4')
              if x_mid>=510 and x_mid<=590:
                  SHOP_1.append('SHOP_5')
              if x_mid>=610 and x_mid<=690:
                  SHOP_1.append('SHOP_6')
              SHOP_1.append(("Green_Triangle",(x_mid,y_mid)))
          if Blue==0 and Green==127 and Red==255:
              if x_mid>=110 and x_mid<=190:
                  SHOP_1.append('SHOP_1')
              if x_mid>=210 and x_mid<=290:
                  SHOP_1.append('SHOP_2')
              if x_mid>=310 and x_mid<=390:
                  SHOP_1.append('SHOP_3')
              if x_mid>=410 and x_mid<=490:
                  SHOP_1.append('SHOP_4')
              if x_mid>=510 and x_mid<=590:
                  SHOP_1.append('SHOP_5')
              if x_mid>=610 and x_mid<=690:
                  SHOP_1.append('SHOP_6')
              SHOP_1.append(("Orange_Triangle",(x_mid,y_mid)))
          if Blue==255 and Green==255 and Red==0:
              if x_mid>=110 and x_mid<=190:
                  SHOP_1.append('SHOP_1')
              if x_mid>=210 and x_mid<=290:
                  SHOP_1.append('SHOP_2')
              if x_mid>=310 and x_mid<=390:
                  SHOP_1.append('SHOP_3')
              if x_mid>=410 and x_mid<=490:
                  SHOP_1.append('SHOP_4')
              if x_mid>=510 and x_mid<=590:
                  SHOP_1.append('SHOP_5')
              if x_mid>=610 and x_mid<=690:
                  SHOP_1.append('SHOP_6')
              SHOP_1.append(("Blue_Triangle",(x_mid,y_mid)))
          if Blue==180 and Green==0 and Red==255:
              if x_mid>=110 and x_mid<=190:
                  SHOP_1.append('SHOP_1')
              if x_mid>=210 and x_mid<=290:
                  SHOP_1.append('SHOP_2')
              if x_mid>=310 and x_mid<=390:
                  SHOP_1.append('SHOP_3')
              if x_mid>=410 and x_mid<=490:
                  SHOP_1.append('SHOP_4')
              if x_mid>=510 and x_mid<=590:
                  SHOP_1.append('SHOP_5')
              if x_mid>=610 and x_mid<=690:
                  SHOP_1.append('SHOP_6')
              SHOP_1.append(("Pink_Triangle",(x_mid,y_mid)))
      elif len(approx) == 4:
          pixel=img_1[y_mid,x_mid]
          Blue = pixel[0]
          Green= pixel[1]
          Red  = pixel[2]
          if Blue==0 and Green==255 and Red==0:
              if x_mid>=110 and x_mid<=190:
                  SHOP_2.append('SHOP_1')
              if x_mid>=210 and x_mid<=290:
                  SHOP_2.append('SHOP_2')
              if x_mid>=310 and x_mid<=390:
                  SHOP_2.append('SHOP_3')
              if x_mid>=410 and x_mid<=490:
                  SHOP_2.append('SHOP_4')
              if x_mid>=510 and x_mid<=590:
                  SHOP_2.append('SHOP_5')
              if x_mid>=610 and x_mid<=690:
                  SHOP_2.append('SHOP_6')
              SHOP_2.append(("Green_Rectangle",(x_mid,y_mid)))
          if Blue==0 and Green==127 and Red==255:
              if x_mid>=110 and x_mid<=190:
                  SHOP_2.append('SHOP_1')
              if x_mid>=210 and x_mid<=290:
                  SHOP_2.append('SHOP_2')
              if x_mid>=310 and x_mid<=390:
                  SHOP_2.append('SHOP_3')
              if x_mid>=410 and x_mid<=490:
                  SHOP_2.append('SHOP_4')
              if x_mid>=510 and x_mid<=590:
                  SHOP_2.append('SHOP_5')
              if x_mid>=610 and x_mid<=690:
                  SHOP_2.append('SHOP_6')
              SHOP_2.append(("Orange_Rectangle",(x_mid,y_mid)))
          if Blue==255 and Green==255 and Red==0:
              if x_mid>=110 and x_mid<=190:
                  SHOP_2.append('SHOP_1')
              if x_mid>=210 and x_mid<=290:
                  SHOP_2.append('SHOP_2')
              if x_mid>=310 and x_mid<=390:
                  SHOP_2.append('SHOP_3')
              if x_mid>=410 and x_mid<=490:
                  SHOP_2.append('SHOP_4')
              if x_mid>=510 and x_mid<=590:
                  SHOP_2.append('SHOP_5')
              if x_mid>=610 and x_mid<=690:
                  SHOP_2.append('SHOP_6')
              SHOP_2.append(("Blue_Rectangle",(x_mid,y_mid)))
          if Blue==180 and Green==0 and Red==255:
              if x_mid>=110 and x_mid<=190:
                  SHOP_2.append('SHOP_1')
              if x_mid>=210 and x_mid<=290:
                  SHOP_2.append('SHOP_2')
              if x_mid>=310 and x_mid<=390:
                  SHOP_2.append('SHOP_3')
              if x_mid>=410 and x_mid<=490:
                  SHOP_2.append('SHOP_4')
              if x_mid>=510 and x_mid<=590:
                  SHOP_2.append('SHOP_5')
              if x_mid>=610 and x_mid<=690:
                  SHOP_2.append('SHOP_6')
              SHOP_2.append(("Pink_Rectangle",(x_mid,y_mid)))
      if len(approx)>5:
          pixel=img_1[y_mid,x_mid]
          Blue=pixel[0]
          Green=pixel[1]
          Red=pixel[2]
          if Blue==0 and Green==255 and Red==0:
              if x_mid>=110 and x_mid<=190:
                  SHOP_3.append('SHOP_1')
              if x_mid>=210 and x_mid<=290:
                  SHOP_3.append('SHOP_2')
              if x_mid>=310 and x_mid<=390:
                  SHOP_3.append('SHOP_3')
              if x_mid>=410 and x_mid<=490:
                  SHOP_3.append('SHOP_4')
              if x_mid>=510 and x_mid<=590:
                  SHOP_3.append('SHOP_5')
              if x_mid>=610 and x_mid<=690:
                  SHOP_3.append('SHOP_6')
              SHOP_3.append(("Green_Circle",(x_mid,y_mid)))
          if Blue==0 and Green==127 and Red==255:
              if x_mid>=110 and x_mid<=190:
                  SHOP_3.append('SHOP_1')
              if x_mid>=210 and x_mid<=290:
                  SHOP_3.append('SHOP_2')
              if x_mid>=310 and x_mid<=390:
                  SHOP_3.append('SHOP_3')
              if x_mid>=410 and x_mid<=490:
                  SHOP_3.append('SHOP_4')
              if x_mid>=510 and x_mid<=590:
                  SHOP_3.append('SHOP_5')
              if x_mid>=610 and x_mid<=690:
                  SHOP_3.append('SHOP_6')
              SHOP_3.append(("Orange_Circle",(x_mid,y_mid)))
          if Blue==255 and Green==255 and Red==0:
              if x_mid>=110 and x_mid<=190:
                  SHOP_3.append('SHOP_1')
              if x_mid>=210 and x_mid<=290:
                  SHOP_3.append('SHOP_2')
              if x_mid>=310 and x_mid<=390:
                  SHOP_3.append('SHOP_3')
              if x_mid>=410 and x_mid<=490:
                  SHOP_3.append('SHOP_4')
              if x_mid>=510 and x_mid<=590:
                  SHOP_3.append('SHOP_5')
              if x_mid>=610 and x_mid<=690:
                  SHOP_3.append('SHOP_6')
              SHOP_3.append(("Blue_Circle",(x_mid,y_mid)))
          if Blue==180 and Green==0 and Red==255:
              if x_mid>=110 and x_mid<=190:
                  SHOP_3.append('SHOP_1')
              if x_mid>=210 and x_mid<=290:
                  SHOP_3.append('SHOP_2')
              if x_mid>=310 and x_mid<=390:
                  SHOP_3.append('SHOP_3')
              if x_mid>=410 and x_mid<=490:
                  SHOP_3.append('SHOP_4')
              if x_mid>=510 and x_mid<=590:
                  SHOP_3.append('SHOP_5')
              if x_mid>=610 and x_mid<=690:
                  SHOP_3.append('SHOP_6')
              SHOP_3.append(("Pink_Circle",(x_mid,y_mid)))
  #SHOP NUMBER
  if SHOP_1[0]=='SHOP_1':
      SHOP.append(SHOP_1)
  if SHOP_2[0]=='SHOP_1':
      SHOP.append(SHOP_2)
  if SHOP_3[0]=='SHOP_1':
      SHOP.append(SHOP_3)
  if SHOP_1[0]=='SHOP_2':
      SHOP.append(SHOP_1)
  if SHOP_2[0]=='SHOP_2':
      SHOP.append(SHOP_2)
  if SHOP_3[0]=='SHOP_2':
      SHOP.append(SHOP_3)
  if SHOP_1[0]=='SHOP_3':
      SHOP.append(SHOP_1)
  if SHOP_2[0]=='SHOP_3':
      SHOP.append(SHOP_2)
  if SHOP_3[0]=='SHOP_3':
      SHOP.append(SHOP_3)
  if SHOP_1[0]=='SHOP_4':
      SHOP.append(SHOP_1)
  if SHOP_2[0]=='SHOP_4':
      SHOP.append(SHOP_2)
  if SHOP_3[0]=='SHOP_4':
      SHOP.append(SHOP_3)
  if SHOP_1[0]=='SHOP_5':
      SHOP.append(SHOP_1)
  if SHOP_2[0]=='SHOP_5':
      SHOP.append(SHOP_2)
  if SHOP_3[0]=='SHOP_5':
      SHOP.append(SHOP_3)
  if SHOP_1[0]=='SHOP_6':
      SHOP.append(SHOP_1)
  if SHOP_2[0]=='SHOP_6':
      SHOP.append(SHOP_2)
  if SHOP_3[0]=='SHOP_6':
      SHOP.append(SHOP_3)
  arena_parameters["Traffic"] += Traffic 
  arena_parameters["Start"]   += start
  arena_parameters["Vertical Roads"] += V_Road
  arena_parameters["Horizontal Roads"] += H_Road
  arena_parameters["Shops"] += SHOP
  
  return arena_parameters
