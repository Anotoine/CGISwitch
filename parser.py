#Imports

import pandas as pd
import numpy as np
import os, time, pickle
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
import datetime as dt

#Base data and empty declarations
Sw = []

f = ['Switch01_Data.xlsx', 'Switch02_Data.xlsx','Switch03_Data.xlsx', 'Switch04_Data.xlsx', 'Switch05_Data.xlsx']
fsheet = ['Meetdata','Bouwstenen','Samenvattende Waarde']

for i,file in enumerate(f): #For all the Switches
  for filesheet in fsheet: #For each sheet in excel
    #Read the correct data for each sheet
    if filesheet == 'Meetdata':
      #Read data for the da
      Sw_Excel = pd.read_excel(file,sheet_name=filesheet)
    
      #Clean the empty Columns (NaN)
      Sw_Excel = Sw_Excel.dropna(axis = 'columns', how = 'all')
    
      #Extracting all the information and cleaning the NaN
      C_ControlLeft = Sw_Excel.iloc[:,:2].dropna(axis = 'index', how = 'all')
      C_ControlRight = Sw_Excel.iloc[:,2:4].dropna(axis = 'index', how = 'all')
      C_SteeringRight = Sw_Excel.iloc[:,4:6].dropna(axis = 'index', how = 'all')
      C_SteeringLeft = Sw_Excel.iloc[:,6:8].dropna(axis = 'index', how = 'all')
      C_MotorCurrent = Sw_Excel.iloc[:,8:10].dropna(axis = 'index', how = 'all')

    

    elif filesheet == 'Bouwstenen':
      #Read data for the da
      Sw_Excel = pd.read_excel(file,sheet_name=filesheet)
    
      #Clean the empty Columns (NaN)
      Sw_Excel = Sw_Excel.dropna(axis = 'columns', how = 'all')
      
      #Extracting all the information and cleaning the NaN
      C_ControlPosition = Sw_Excel.iloc[:,:2].dropna(axis = 'index', how = 'all')
      C_SteeringCommand = Sw_Excel.iloc[:,2:4].dropna(axis = 'index', how = 'all')
      C_MotorCurrentActive = Sw_Excel.iloc[:,4:6].dropna(axis = 'index', how = 'all')
    
      
    elif filesheet == 'Samenvattende Waarde':
      #Read data for the da
      Sw_Excel = pd.read_excel(file,sheet_name=filesheet)
    
      #Clean the empty Columns (NaN)
      Sw_Excel = Sw_Excel.dropna(axis = 'columns', how = 'all')
      
      #Extracting all the information and cleaning the NaN
      C_EnergySurfaceLeft = Sw_Excel.iloc[:,:2].dropna(axis = 'index', how = 'all')
      C_EnergySurfaceRight = Sw_Excel.iloc[:,2:4].dropna(axis = 'index', how = 'all')
      C_StartPeakLeft = Sw_Excel.iloc[:,4:6].dropna(axis = 'index', how = 'all')
      C_StartPeakRight = Sw_Excel.iloc[:,6:8].dropna(axis = 'index', how = 'all')
      C_MaxTransitionLeft = Sw_Excel.iloc[:,8:10].dropna(axis = 'index', how = 'all')
      C_MaxTransitionRight = Sw_Excel.iloc[:,10:12].dropna(axis = 'index', how = 'all')
      C_MotorTransitionTimeLeft = Sw_Excel.iloc[:,12:14].dropna(axis = 'index', how = 'all')
      C_MotorTransitionTimeRight = Sw_Excel.iloc[:,14:16].dropna(axis = 'index', how = 'all')
      C_RelayTransitionTimeRight = Sw_Excel.iloc[:,16:18].dropna(axis = 'index', how = 'all')
      C_RelayTransitionTimeLeft = Sw_Excel.iloc[:,18:20].dropna(axis = 'index', how = 'all')
      C_TimeEndMotorCurrentControlLeft = Sw_Excel.iloc[:,20:22].dropna(axis = 'index', how = 'all')
      C_TimeEndMotorCurrentControlRight = Sw_Excel.iloc[:,22:24].dropna(axis = 'index', how = 'all')
      C_TimeSteeringMotorCurrentLeft = Sw_Excel.iloc[:,24:26].dropna(axis = 'index', how = 'all')
      C_TimeSteeringMotorCurrentRight = Sw_Excel.iloc[:,26:28].dropna(axis = 'index', how = 'all')
      C_ControlOutTime = Sw_Excel.iloc[:,28:30].dropna(axis = 'index', how = 'all')
      C_SectionOcupationTime = Sw_Excel.iloc[:,30:32].dropna(axis = 'index', how = 'all')
    
    #Creation of the final df
  frames = [C_ControlPosition, C_SteeringCommand, C_MotorCurrentActive, C_ControlLeft, C_ControlRight, C_SteeringRight, C_SteeringLeft, C_MotorCurrent, C_EnergySurfaceLeft, C_EnergySurfaceRight, \
             C_StartPeakLeft, C_StartPeakRight, C_MaxTransitionLeft, C_MaxTransitionRight, C_MotorTransitionTimeLeft, C_MotorTransitionTimeRight, C_RelayTransitionTimeRight, C_RelayTransitionTimeLeft, \
             C_TimeEndMotorCurrentControlLeft, C_TimeEndMotorCurrentControlRight, C_TimeSteeringMotorCurrentLeft, C_TimeSteeringMotorCurrentRight, C_ControlOutTime, C_SectionOcupationTime]
  
  Sw.append(pd.concat(frames, keys = [C_ControlPosition.columns[1], C_SteeringCommand.columns[1], C_MotorCurrentActive.columns[1], C_ControlLeft.columns[1], C_ControlRight.columns[1], C_SteeringRight.columns[1], \
                                    C_SteeringLeft.columns[1], C_MotorCurrent.columns[1], C_EnergySurfaceLeft.columns[1], C_EnergySurfaceRight.columns[1], C_StartPeakLeft.columns[1], C_StartPeakRight.columns[1], \
                                    C_MaxTransitionLeft.columns[1], C_MaxTransitionRight.columns[1], C_MotorTransitionTimeLeft.columns[1], C_MotorTransitionTimeRight.columns[1], C_RelayTransitionTimeRight.columns[1], \
                                    C_RelayTransitionTimeLeft.columns[1], C_TimeEndMotorCurrentControlLeft.columns[1], C_TimeEndMotorCurrentControlRight.columns[1], C_TimeSteeringMotorCurrentLeft.columns[1], \
                                    C_TimeSteeringMotorCurrentRight.columns[1], C_ControlOutTime.columns[1], C_SectionOcupationTime.columns[1]], sort=False))

Sw[0].to_csv('Sw0.csv')
Sw[1].to_csv('Sw1.csv')
Sw[2].to_csv('Sw2.csv')
Sw[3].to_csv('Sw3.csv')
Sw[4].to_csv('Sw4.csv')
