import os
import numpy as np
import glob
import cv2
import time

#class BaseMotion:
#
#    def run_threaded(self):
#        return self.frame

class MotDec():
    def __init__(self):
        self.frame = None
        self.x_center = 0.0
        self.y_center = 0.0
        self.ssd_angle = 0.0
        self.throttle = 0.0
        self.cnt = 0
        self.mode = 'user'
    def run(self, img_arr=None, psn_x=None, psn_y=None):
        self.frame = img_arr
        self.x_center = psn_x
        self.y_center = psn_y
        if (self.x_center -320) >= 0:
            self.ssd_angle = min(int((self.x_center - 320)/32)*0.2 , 1)
        else:
            self.ssd_angle = max(-1, int((self.x_center - 320)/32)*0.2)
        
        self.cnt += 1
        if self.cnt == 5:
            print ('Run_Cor: ({:.1f},{:.1f})'.format(self.x_center, self.y_center))
            print ('Steering: {:.1f}'.format(self.ssd_angle))
            self.cnt = 0
#        print ('Run_Cor: ({:.1f},{:.1f})'.format(self.x_center, self.y_center))
#        return self.frame
        return self.frame, self.ssd_angle
    def update(self, img_arr=None, psn_x=None, psn_y=None):
#        self.frame = img_arr
#        self.angle = int((str_ang - 320)/32)*0.2
#        self.x_center = psn_x
#        self.y_center = psn_y
#        print ('Update_Cor: ({:.1f},{:.1f})'.format(self.x_center, self.y_center))
#        return self.frame
        self.x_center = psn_x
        self.y_center = psn_y
        if (self.x_center -320) >= 0:
            self.ssd_angle = min(int((self.x_center - 320)/32)*0.2 , 1)
        else:
            self.ssd_angle = max(-1, int((self.x_center - 320)/32)*0.2)
        
        self.cnt += 1
        if self.cnt == 5:
            print ('Update_Cor: ({:.1f},{:.1f})'.format(self.x_center, self.y_center))
            print ('Steering: {:.1f}'.format(self.ssd_angle))
            self.cnt = 0
    def run_threaded(self, img_arr=None, psn_x=None, psn_y=None):
#        self.x_center = psn_x
#        self.y_center = psn_y
#        print ('Thread_Cor: ({:.1f},{:.1f})'.format(self.x_center, self.y_center))
#        return self.frame
        self.x_center = psn_x
        self.y_center = psn_y
        if (self.x_center -320) >= 0:
            self.ssd_angle = min(int((self.x_center - 320)/32)*0.2 , 1)
        else:
            self.ssd_angle = max(-1, int((self.x_center - 320)/32)*0.2)
        
        self.cnt += 1
        if self.cnt == 5:
            print ('Thread_Cor: ({:.1f},{:.1f})'.format(self.x_center, self.y_center))
            print ('Steering: {:.1f}'.format(self.ssd_angle))
            self.cnt = 0
#        return self.frame