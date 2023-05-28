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

def detect_arena_parameters(image):

  img_1        = image
  Image_hsv    = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
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
  SHOP         = []
  FINAL_SHOP   = []
  arena_parameters ={"traffic_signals":[] , "start_node":[] ,"horizontal_roads_under_construction":[],"vertical_roads_under_construction":[],"medicine_packages_present":[]}
  #NODE DETECTION
  while Cy<= 799:
      while Cx<= 799 :
          #COLOR PICKER
          pixel = image[Cy,Cx]
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
          pixel = image[(int(Every_node[Cx][1]),int(Every_node[Cx][0])+10)]
          Blue = pixel[0]
          Red = pixel[2]
          Green = pixel[1]
          if Blue!=0 or Red!=0 or Green!=0:
             main_char=Every_STRING[Cx]+"-"+Every_STRING[Cx+1]
             H_Road.append(main_char)
      Cx=Cx+1
  Cx=0
  while Cy<49:
      if Cy==42 or Cy==43 or Cy==44 or Cy==45 or Cy==46 or Cy==47 or Cy==48:
          pass
      else:
          pixel = image[(int(Every_node[Cy][1])+10,int(Every_node[Cy][0]))]
          Blue = pixel[0]
          Red = pixel[2]
          Green = pixel[1]
          if Blue!=0 or Red!=0 or Green!=0:
             main_char=Every_STRING[Cy]+"-"+Every_STRING[Cy+7]
             V_Road.append(main_char)
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
                  SHOP.append(["Shop_1","Green","Triangle",[x_mid,y_mid+3]])
              if x_mid>=210 and x_mid<=290:
                  SHOP.append(["Shop_2","Green","Triangle",[x_mid,y_mid+3]])
              if x_mid>=310 and x_mid<=390:
                  SHOP.append(["Shop_3","Green","Triangle",[x_mid,y_mid+3]])
              if x_mid>=410 and x_mid<=490:
                  SHOP.append(["Shop_4","Green","Triangle",[x_mid,y_mid+3]])
              if x_mid>=510 and x_mid<=590:
                  SHOP.append(["Shop_5","Green","Triangle",[x_mid,y_mid+3]])
              if x_mid>=610 and x_mid<=690:
                  SHOP.append(["Shop_6","Green","Triangle",[x_mid,y_mid+3]])
          if Blue==0 and Green==127 and Red==255:
              if x_mid>=110 and x_mid<=190:
                  SHOP.append(["Shop_1","Orange","Triangle",[x_mid,y_mid+3]])
              if x_mid>=210 and x_mid<=290:
                  SHOP.append(["Shop_2","Orange","Triangle",[x_mid,y_mid+3]])
              if x_mid>=310 and x_mid<=390:
                  SHOP.append(["Shop_3","Orange","Triangle",[x_mid,y_mid+3]])
              if x_mid>=410 and x_mid<=490:
                  SHOP.append(["Shop_4","Orange","Triangle",[x_mid,y_mid+3]])
              if x_mid>=510 and x_mid<=590:
                  SHOP.append(["Shop_5","Orange","Triangle",[x_mid,y_mid+3]])
              if x_mid>=610 and x_mid<=690:
                  SHOP.append(["Shop_6","Orange","Triangle",[x_mid,y_mid+3]])
          if Blue==255 and Green==255 and Red==0:
              if x_mid>=110 and x_mid<=190:
                  SHOP.append(["Shop_1","Skyblue","Triangle",[x_mid,y_mid+3]])
              if x_mid>=210 and x_mid<=290:
                  SHOP.append(["Shop_2","Skyblue","Triangle",[x_mid,y_mid+3]])
              if x_mid>=310 and x_mid<=390:
                  SHOP.append(["Shop_3","Skyblue","Triangle",[x_mid,y_mid+3]])
              if x_mid>=410 and x_mid<=490:
                  SHOP.append(["Shop_4","Skyblue","Triangle",[x_mid,y_mid+3]])
              if x_mid>=510 and x_mid<=590:
                  SHOP.append(["Shop_5","Skyblue","Triangle",[x_mid,y_mid+3]])
              if x_mid>=610 and x_mid<=690:
                  SHOP.append(["Shop_6","Skyblue","Triangle",[x_mid,y_mid+3]])
          if Blue==180 and Green==0 and Red==255:
              if x_mid>=110 and x_mid<=190:
                  SHOP.append(["Shop_1","Pink","Triangle",[x_mid,y_mid+3]])
              if x_mid>=210 and x_mid<=290:
                  SHOP.append(["Shop_2","Pink","Triangle",[x_mid,y_mid+3]])
              if x_mid>=310 and x_mid<=390:
                  SHOP.append(["Shop_3","Pink","Triangle",[x_mid,y_mid+3]])
              if x_mid>=410 and x_mid<=490:
                  SHOP.append(["Shop_4","Pink","Triangle",[x_mid,y_mid+3]])
              if x_mid>=510 and x_mid<=590:
                  SHOP.append(["Shop_5","Pink","Triangle",[x_mid,y_mid+3]])
              if x_mid>=610 and x_mid<=690:
                  SHOP.append(["Shop_6","Pink","Triangle",[x_mid,y_mid+3]])
      elif len(approx) == 4:
          pixel=img_1[y_mid,x_mid]
          Blue = pixel[0]
          Green= pixel[1]
          Red  = pixel[2]
          if Blue==0 and Green==255 and Red==0:
              if x_mid>=110 and x_mid<=190:
                  SHOP.append(["Shop_1","Green","Square",[x_mid,y_mid]])
              if x_mid>=210 and x_mid<=290:
                  SHOP.append(["Shop_2","Green","Square",[x_mid,y_mid]])
              if x_mid>=310 and x_mid<=390:
                  SHOP.append(["Shop_3","Green","Square",[x_mid,y_mid]])
              if x_mid>=410 and x_mid<=490:
                  SHOP.append(["Shop_4","Green","Square",[x_mid,y_mid]])
              if x_mid>=510 and x_mid<=590:
                  SHOP.append(["Shop_5","Green","Square",[x_mid,y_mid]])
              if x_mid>=610 and x_mid<=690:
                  SHOP.append(["Shop_6","Green","Square",[x_mid,y_mid]])
          if Blue==0 and Green==127 and Red==255:
              if x_mid>=110 and x_mid<=190:
                  SHOP.append(["Shop_1","Orange","Square",[x_mid,y_mid]])
              if x_mid>=210 and x_mid<=290:
                  SHOP.append(["Shop_2","Orange","Square",[x_mid,y_mid]])
              if x_mid>=310 and x_mid<=390:
                  SHOP.append(["Shop_3","Orange","Square",[x_mid,y_mid]])
              if x_mid>=410 and x_mid<=490:
                  SHOP.append(["Shop_4","Orange","Square",[x_mid,y_mid]])
              if x_mid>=510 and x_mid<=590:
                  SHOP.append(["Shop_5","Orange","Square",[x_mid,y_mid]])
              if x_mid>=610 and x_mid<=690:
                  SHOP.append(["Shop_6","Orange","Square",[x_mid,y_mid]])
          if Blue==255 and Green==255 and Red==0:
              if x_mid>=110 and x_mid<=190:
                  SHOP.append(["Shop_1","Skyblue","Square",[x_mid,y_mid]])
              if x_mid>=210 and x_mid<=290:
                  SHOP.append(["Shop_2","Skyblue","Square",[x_mid,y_mid]])
              if x_mid>=310 and x_mid<=390:
                  SHOP.append(["Shop_3","Skyblue","Square",[x_mid,y_mid]])
              if x_mid>=410 and x_mid<=490:
                  SHOP.append(["Shop_4","Skyblue","Square",[x_mid,y_mid]])
              if x_mid>=510 and x_mid<=590:
                  SHOP.append(["Shop_5","Skyblue","Square",[x_mid,y_mid]])
              if x_mid>=610 and x_mid<=690:
                  SHOP.append(["Shop_6","Skyblue","Square",[x_mid,y_mid]])
          if Blue==180 and Green==0 and Red==255:
              if x_mid>=110 and x_mid<=190:
                  SHOP.append(["Shop_1","Pink","Square",[x_mid,y_mid]])
              if x_mid>=210 and x_mid<=290:
                  SHOP.append(["Shop_2","Pink","Square",[x_mid,y_mid]])
              if x_mid>=310 and x_mid<=390:
                  SHOP.append(["Shop_3","Pink","Square",[x_mid,y_mid]])
              if x_mid>=410 and x_mid<=490:
                  SHOP.append(["Shop_4","Pink","Square",[x_mid,y_mid]])
              if x_mid>=510 and x_mid<=590:
                  SHOP.append(["Shop_5","Pink","Square",[x_mid,y_mid]])
              if x_mid>=610 and x_mid<=690:
                  SHOP.append(["Shop_6","Pink","Square",[x_mid,y_mid]])
      if len(approx)>5:
          pixel=img_1[y_mid,x_mid]
          Blue=pixel[0]
          Green=pixel[1]
          Red=pixel[2]
          if Blue==0 and Green==255 and Red==0:
              if x_mid>=110 and x_mid<=190:
                  SHOP.append(["Shop_1","Green","Circle",[x_mid,y_mid]])
              if x_mid>=210 and x_mid<=290:
                  SHOP.append(["Shop_2","Green","Circle",[x_mid,y_mid]])
              if x_mid>=310 and x_mid<=390:
                  SHOP.append(["Shop_3","Green","Circle",[x_mid,y_mid]])
              if x_mid>=410 and x_mid<=490:
                  SHOP.append(["Shop_4","Green","Circle",[x_mid,y_mid]])
              if x_mid>=510 and x_mid<=590:
                  SHOP.append(["Shop_5","Green","Circle",[x_mid,y_mid]])
              if x_mid>=610 and x_mid<=690:
                  SHOP.append(["Shop_6","Green","Circle",[x_mid,y_mid]])
          if Blue==0 and Green==127 and Red==255:
              if x_mid>=110 and x_mid<=190:
                  SHOP.append(["Shop_1","Orange","Circle",[x_mid,y_mid]])
              if x_mid>=210 and x_mid<=290:
                  SHOP.append(["Shop_2","Orange","Circle",[x_mid,y_mid]])
              if x_mid>=310 and x_mid<=390:
                  SHOP.append(["Shop_3","Orange","Circle",[x_mid,y_mid]])
              if x_mid>=410 and x_mid<=490:
                  SHOP.append(["Shop_4","Orange","Circle",[x_mid,y_mid]])
              if x_mid>=510 and x_mid<=590:
                  SHOP.append(["Shop_5","Orange","Circle",[x_mid,y_mid]])
              if x_mid>=610 and x_mid<=690:
                  SHOP.append(["Shop_6","Orange","Circle",[x_mid,y_mid]])
          if Blue==255 and Green==255 and Red==0:
              if x_mid>=110 and x_mid<=190:
                  SHOP.append(["Shop_1","Skyblue","Circle",[x_mid,y_mid]])
              if x_mid>=210 and x_mid<=290:
                  SHOP.append(["Shop_2","Skyblue","Circle",[x_mid,y_mid]])
              if x_mid>=310 and x_mid<=390:
                  SHOP.append(["Shop_3","Skyblue","Circle",[x_mid,y_mid]])
              if x_mid>=410 and x_mid<=490:
                  SHOP.append(["Shop_4","Skyblue","Circle",[x_mid,y_mid]])
              if x_mid>=510 and x_mid<=590:
                  SHOP.append(["Shop_5","Skyblue","Circle",[x_mid,y_mid]])
              if x_mid>=610 and x_mid<=690:
                  SHOP.append(["Shop_6","Skyblue","Circle",[x_mid,y_mid]])
          if Blue==180 and Green==0 and Red==255:
              if x_mid>=110 and x_mid<=190:
                  SHOP.append(["Shop_1","Pink","Circle",[x_mid,y_mid]])
              if x_mid>=210 and x_mid<=290:
                  SHOP.append(["Shop_2","Pink","Circle",[x_mid,y_mid]])
              if x_mid>=310 and x_mid<=390:
                  SHOP.append(["Shop_3","Pink","Circle",[x_mid,y_mid]])
              if x_mid>=410 and x_mid<=490:
                  SHOP.append(["Shop_4","Pink","Circle",[x_mid,y_mid]])
              if x_mid>=510 and x_mid<=590:
                  SHOP.append(["Shop_5","Pink","Circle",[x_mid,y_mid]])
              if x_mid>=610 and x_mid<=690:
                  SHOP.append(["Shop_6","Pink","Circle",[x_mid,y_mid]])
  #FINAL_SHOP
  i=0
  n=0
  q=0
  while i<len(SHOP):
    if SHOP[i][0]=="Shop_1":
        while(n<len(FINAL_SHOP)):
            if SHOP[i][3]>FINAL_SHOP[n][3]:
                q=q+1
            n=n+1
        FINAL_SHOP.insert(q,SHOP[i])
        q=0
        n=0
    i=i+1
  i=0
  n=0
  q=0
  while i<len(SHOP):
    if SHOP[i][0]=="Shop_2":
        while(n<len(FINAL_SHOP)):
            if SHOP[i][3]>FINAL_SHOP[n][3]:
                q=q+1
            n=n+1
        FINAL_SHOP.insert(q,SHOP[i])
        q=0
        n=0
    i=i+1
  i=0
  n=0
  q=0
  while i<len(SHOP):
    if SHOP[i][0]=="Shop_3":
        while(n<len(FINAL_SHOP)):
            if SHOP[i][3]>FINAL_SHOP[n][3]:
                q=q+1
            n=n+1
        FINAL_SHOP.insert(q,SHOP[i])
        q=0
        n=0
    i=i+1
  i=0
  n=0
  q=0
  while i<len(SHOP):
    if SHOP[i][0]=="Shop_4":
        while(n<len(FINAL_SHOP)):
            if SHOP[i][3]>FINAL_SHOP[n][3]:
                q=q+1
            n=n+1
        FINAL_SHOP.insert(q,SHOP[i])
        q=0
        n=0
    i=i+1
  i=0
  n=0
  q=0
  while i<len(SHOP):
    if SHOP[i][0]=="Shop_5":
        while(n<len(FINAL_SHOP)):
            if SHOP[i][3]>FINAL_SHOP[n][3]:
                q=q+1
            n=n+1
        FINAL_SHOP.insert(q,SHOP[i])
        q=0
        n=0
    i=i+1
  i=0
  n=0
  q=0
  while i<len(SHOP):
    if SHOP[i][0]=="Shop_6":
        while(n<len(FINAL_SHOP)):
            if SHOP[i][3]>FINAL_SHOP[n][3]:
                q=q+1
            n=n+1
        FINAL_SHOP.insert(q,SHOP[i])
        q=0
        n=0
    i=i+1
  i=0 
  arena_parameters["traffic_signals"] += Traffic 
  arena_parameters["start_node"]   += start
  arena_parameters["horizontal_roads_under_construction"] += H_Road
  arena_parameters["vertical_roads_under_construction"] += V_Road
  arena_parameters["medicine_packages_present"] += FINAL_SHOP
  
  return arena_parameters
maze_image=cv2.imread('/home/kavi/Desktop/Linux/Cyborg/task_2_executable/test_images/maze_0.png')
a=detect_arena_parameters(maze_image)
