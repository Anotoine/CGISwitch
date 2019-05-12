# -*- coding: utf-8 -*-
"""Main.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1aRHyCHJQl2QCNTaO_JfX8F9GurSeMcTv
"""

import pandas as pd
import numpy as np
import os, time, pickle
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
import datetime as dt


import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)
pd.set_option('mode.chained_assignment', None)

print("Visca el 22")

print('Hello!')

"""## Com obrir arxius
Primer s'han de carregar des de l'ordenador amb el codi de baix
"""

from google.colab import files
uploaded = files.upload()

"""### Basic dataframes"""

f = 'Switch01_Data.xlsx'
df = pd.read_excel(f)

#Noms de les columnes
df.columns

SturingStand = df.iloc[0:6338, 0:2]

SturingStand.rename(columns = {6338:"Data"})

"""Data Loader for all Switches (must be all 5 loaded and it will return a list of df)"""

for i,file in t(enumerate(f[:2])): #For all the Switches
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

"""### Read and modify dataframes"""

Sw = [0,0,0,0,0]
filename = ['Switch01_Data.xlsx', 'Switch02_Data.xlsx','Switch03_Data.xlsx', 'Switch04_Data.xlsx', 'Switch05_Data.xlsx']

for i in range(5):
  df0 = pd.read_excel(filename[i],sheet_name = 0)
  df1 = pd.read_excel(filename[i],sheet_name = 1)
  df2 = pd.read_excel(filename[i],sheet_name = 2)
  df = pd.concat([df0,df1,df2],axis=1).dropna(axis="columns",how = "all")
  #df.count()
  Sw[i] = df

#Executar aquesta cel·la només si es vol reiniciar totes les particions de les dades en el vector newdf fetes.

numerolleig = 1 #Nombre d'esdeveniments de control de més als que s'accedeix en retallar les dades
midamax = 20000
newdf = [midamax*[0] for i in range(5)]

def get_event_info(swNum,tindex):
  if type(newdf[swNum][tindex]) == int:
    
    newdf2 = []
    aux1 = Sw[swNum]
    aux4 = aux1.iloc[:,0].dropna(axis="index",how="all")
    count_row = aux4.shape[0]
    count_col = aux1.shape[1]

    temps = tindex
    t = aux1['SteeringCommandDate'][temps]
    tnext = aux1['SteeringCommandDate'][temps+1+numerolleig]
    print(type(t),type(tnext))
    print(temps)
    for index in range(int(count_col/2)): #Itera columnes (dades)
      aux2 = aux1.iloc[:,index*2:index*2+2]
      #print(aux2)
      newdf2.append(aux2[(aux2.iloc[:,0]>= t)&(aux2.iloc[:,0]<=tnext)].reset_index(drop=True))

    #print(newdf2)
    newdf[swNum][tindex] = pd.concat(newdf2, axis=1)
  return newdf[swNum][tindex]

event = get_event_info(1,155)
event['SteeringCommandDate'].dropna()

"""### Plot dataframe"""

#Tot aquesta cel·la s'ha d'executar junta si es volen imprimir les 

BouwstenenVariableNames = ['ControlPosition', 'SteeringCommand',
                           'MotorCurrentActive']
ctt = -5

def convertToNumber(dataframe, variableName):
  resultdf = dataframe[variableName]
  
  if (variableName == 'ControlPosition'):
    resultdf.loc[dataframe[variableName] == "Links in controle"] = -1+ctt
    resultdf.loc[dataframe[variableName] == "Rechts in controle"] = 1+ctt
    resultdf.loc[dataframe[variableName] == "Uit controle"] = 0+ctt
    
  if (variableName == 'SteeringCommand'):
    resultdf.loc[dataframe[variableName] == "Sturing Links"] = -1+ctt
    resultdf.loc[dataframe[variableName] == "Sturing Rechts"] = 1+ctt
    resultdf.loc[dataframe[variableName] == "Sturing Onbekend"] = 0+ctt
    
  if (variableName == 'MotorCurrentActive'):
    resultdf.loc[dataframe[variableName] == "Motorstroom Actief"] = 1+ctt
    resultdf.loc[dataframe[variableName] == "Geen Motorstroom"] = 0+ctt
    
def plotColumn(dataframe, variableName, ax):
  timeName = variableName + 'Date'
  if (variableName in BouwstenenVariableNames):
    convertToNumber(dataframe, variableName)

  #print(dataframe[timeName])
  dataframe.plot(drawstyle='steps-post',x=timeName,y=variableName, ax=ax)
  
def plotDataframeColumns(dataframe, variableNames):
  df = dataframe.copy()
  ax = plt.gca()
  for variableName in variableNames:
    timeName = variableName + 'Date'
    #print(timeName)
    #print("Previous", dataframe[timeName])
    plotColumn(df, variableName, ax)
    #print("Future", dataframe[timeName])
    
  plt.xlabel('Time')
  
def plotEventColumns(dataframe, variableNames, passedtime=0.0001, timeshift=0):
  df = dataframe.copy()
  ax = plt.gca()
  shift = 0
  f = (dataframe['SteeringCommandDate'][1] - dataframe['SteeringCommandDate'][0])
  f2 = (dataframe['SteeringCommandDate'][2] - dataframe['SteeringCommandDate'][1])
  total = f + f2
  p1 = f/total
  p2 = f2/total
  print(dataframe['SteeringCommandDate'][0])
  print(dataframe['SteeringCommandDate'][1])
  print(dataframe['SteeringCommandDate'][2])
  for variableName in variableNames:
    plotColumn(df, variableName, ax)
  xmin, xmax, ymin, ymax = plt.axis()
  print(xmin, xmax, ymin, ymax)
  shift = p1*(xmax-xmin)-0.00004
  ax.set_xlim(xmax = min(xmin+passedtime+shift,xmax+shift), xmin = xmin+shift)
  xmin, xmax, ymin, ymax = plt.axis()
  print(xmin, xmax, ymin, ymax)
  plt.xlabel('Time')
  
def plotEvent(swNum, eventNum, columnNames):
  event = get_event_info(swNum-1, eventNum)
  plotEventColumns(event,columnNames)

plotEvent(4,419,['SteeringCommand','ControlPosition','MotorCurrent'])

errors_motor2 = [188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 202,
       254, 255, 419, 420, 421]

"""## Exemple en què primer es dóna l'encesa del motor i després la comanda"""

event['SteeringCommandDate']

event['MotorCurrentDate']

event=get_event_info(0,155)
event['MotorCurrentDate']



import pandas as pd
import numpy as np
import os, time, pickle
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
import datetime as dt


import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)
pd.set_option('mode.chained_assignment', None)

nat = np.datetime64('NaT')

def nat_check(nat):
    return nat == np.datetime64('NaT')

print('Hello!')

from google.colab import files
uploaded = files.upload()

filename = 'Switch02_Data.xlsx'
llistacols1 = [0,1,3,4,6,7,9,10,12,13,15,16,18,19,21,22,24,25,27,28,30,31,33,34,36,37,39,40]
llistacols2 = [0,1,3,4,6,7,9,10,12,13,15,16,18,19,21,22]
df1 = pd.read_excel(filename,sheet_name = 0)
df0 = pd.read_excel(filename,sheet_name = 1,usecols=llistacols1 )
df2 = pd.read_excel(filename,sheet_name = 2,usecols=llistacols2 )
df = pd.concat([df0,df1,df2],axis=1).dropna(axis="columns",how = "all")
df

nom = list(df2.columns.values)
n = nom[3]
n
df2[df2.iloc[:,0]<df2.iloc[6,0]]

#import time
#import datetime




#for element in df2.loc[: , "Controle Links"][:]:
#  if  not(nat_check(element)):
#    s = element
#    temps = time.mktime(datetime.datetime.strptime(s, "%Y-%m-%d").timetuple())
#    print(temps)

noms = ["ControlPosition","ControlPositionDate","SteeringCommand","SteeringCommandDate","MotorCurrentActive","MotorCurrentActiveDate","EnergySurfaceLeft","EnergySurfaceLeftDate","EnergySurfaceRight","EnergySurfaceRightDate","StartPeakLeft","StartPeakLeftDate","StartPeakRight","StartPeakRightDate","MaxTransitionLeft","MaxTransitionLeftDate","MaxTransitionRight","MaxTransitionRightDate","MotorTransitionTimeLeft","MotorTransitionTimeLeftDate","MotorTransitionTimeRight","MotorTransitionTimeRightDate","RelayTransitionTimeRight","RelayTransitionTimeRightDate","RelayTransitionTimeLeft","RelayTransitionTimeLeftDate","TimeEndMotorCurrentControlLeft","TimeEndMotorCurrentControlLeftDate","TimeEndMotorCurrentControlRight","TimeEndMotorCurrentControlRightDate","TimeSteeringMotorCurrentLeft","TimeSteeringMotorCurrentLeftDate","TimeSteeringMotorCurrentRight","TimeSteeringMotorCurrentRightDate","ControlOutTime","ControlOutTimeDate","ControlLeft","ControlLeftDate","ControlRight","ControlRightDate","SteeringRight","SteeringRightDate","SteeringLeft","SteeringLeftDate","MotorCurrent","MotorCurrentDate"]



#Aquest loop necessita 5 datasets (un per cada switch) en un vector de datasets anomenat Sw. 
#Les primeres dues columnes de cada Sw han de ser "ControlPositionDate" i "ControlPosition".
#En la resta de columnes hi ha d'haver primer el temps i llavors la dada. 

#for swnum in range(5):

Sw = [df,df]
swnum = 0
aux1 = Sw[swnum]
aux4 = aux1.iloc[:,0].dropna(axis="index",how="all")
count_row = aux4.shape[0]
count_col = aux1.shape[1]
newdf = []

for temps in range(count_row-1): #Itera temps (files)
  t = str(aux1.iloc[temps,0])
  tnext = str(aux1.iloc[temps+1,0])
  newdf2 = []
  for index in range(int(count_col/2)): #Itera columnes (dades)
    aux2 = aux1.iloc[:,index*2:index*2+2]
    aux3 = aux2.iloc[:,0]#.copy()
    aux3 = aux3.dropna(axis="index",how="all")

#    newdf2.append(aux2[(aux2.iloc[:,0]>= t)&(aux2.iloc[:,0]<tnext)])
    newdf2.append(aux2[(aux2.iloc[:,0]>= t)&(aux2.iloc[:,0]<tnext)].reset_index(drop=True))

  newdf.append(pd.concat(newdf2, axis=1))
  

newdf

Sw = [df,df,df,df,df]

midamax = 20000
newdf = 5*[midamax*[0]]

def get_event_info(swnum,tindex):
  global newdf
  
  newdf2 = []
  
  if type(newdf[swnum][tindex]) == int:
    
    #tindex is index of time
    #for swnum in range(5):

    aux1 = Sw[swnum]
    aux4 = aux1.iloc[:,0].dropna(axis="index",how="all")
    count_row = aux4.shape[0]
    count_col = aux1.shape[1]


    temps = tindex
    t = str(aux1.iloc[temps,0])
    tnext = str(aux1.iloc[temps+1,0])
    print(type(t),type(tnext))
    print(temps)
    for index in range(int(count_col/2)): #Itera columnes (dades)
      aux2 = aux1.iloc[:,index*2:index*2+2]
      aux3 = aux2.iloc[:,0]#.copy()
      aux3 = aux3.dropna(axis="index",how="all")
      newdf2.append(aux2[(aux2.iloc[:,0]>= t)&(aux2.iloc[:,0]<tnext)].reset_index(drop=True))

    print(newdf2)
    newdf[swnum][tindex] = pd.concat(newdf2, axis=1)
  
  return newdf[swnum][tindex]

pd.concat(b,axis=1,ignore_index=True)

c = get_event_info(0,1)

a

c.iloc[:,25]

noms = ["ControlPosition","ControlPositionDate","SteeringCommand","SteeringCommandDate","MotorCurrentActive","MotorCurrentActiveDate","EnergySurfaceLeft","EnergySurfaceLeftDate","EnergySurfaceRight","EnergySurfaceRightDate","StartPeakLeft","StartPeakLeftDate","StartPeakRight","StartPeakRightDate","MaxTransitionLeft","MaxTransitionLeftDate","MaxTransitionRight","MaxTransitionRightDate","MotorTransitionTimeLeft","MotorTransitionTimeLeftDate","MotorTransitionTimeRight","MotorTransitionTimeRightDate","RelayTransitionTimeRight","RelayTransitionTimeRightDate","RelayTransitionTimeLeft","RelayTransitionTimeLeftDate","TimeEndMotorCurrentControlLeft","TimeEndMotorCurrentControlLeftDate","TimeEndMotorCurrentControlRight","TimeEndMotorCurrentControlRightDate","TimeSteeringMotorCurrentLeft","TimeSteeringMotorCurrentLeftDate","TimeSteeringMotorCurrentRight","TimeSteeringMotorCurrentRightDate","ControlOutTime","ControlOutTimeDate","ControlLeft","ControlLeftDate","ControlRight","ControlRightDate","SteeringRight","SteeringRightDate","SteeringLeft","SteeringLeftDate","MotorCurrent","MotorCurrentDate"]



#Aquest loop necessita 5 datasets (un per cada switch) en un vector de datasets anomenat Sw. 
#Les primeres dues columnes de cada Sw han de ser "ControlPositionDate" i "ControlPosition".
#En la resta de columnes hi ha d'haver primer el temps i llavors la dada. 

# index 2 i 3 - steering command
# index 14 i 15 - motor current
#30 i 31 - time tranistion right
#28 i 29 - time transition left

Sw = [df,df]
Sw = [df.iloc[:,[2,3,14,15,28,29,30,31]]]
swnum = 0
aux1 = Sw[swnum]
aux4 = aux1.iloc[:,0].dropna(axis="index",how="all")
count_row = aux4.shape[0]
count_col = aux1.shape[1]
newdf = []

for temps in range(count_row-1): #Itera temps (files)
  t = str(aux1.iloc[temps,0])
  tnext = str(aux1.iloc[temps+1,0])
  newdf2 = []
  print(temps)
  for index in range(int(count_col/2)): #Itera columnes (dades)
#  for index in [2,3,14,15,28,29,30,31]: #Itera columnes (dades)
    index = int(index/2)
    aux2 = aux1.iloc[:,index*2:index*2+2]
    aux3 = aux2.iloc[:,0]#.copy()
    aux3 = aux3.dropna(axis="index",how="all")

    newdf2.append(aux2[(aux2.iloc[:,0]>= t)&(aux2.iloc[:,0]<tnext)].reset_index(drop=True))

  newdf.append(pd.concat(newdf2, axis=1))
  

############################ OBTAIN DATA ########################


import matplotlib
l = np.zeros(200)
lc = np.zeros([count_row-1,200])
for temps in range(count_row-1):

  aux = newdf[temps]
  num_row = aux.shape[0]
  for i in range(num_row):
    
    elem = aux.iloc[i,[5]]
    lc[temps][i] = elem.values.tolist()[0] 
    l[i] = l[i] + lc[temps][i]/count_row 

mse = []
desp = []
lc = np.array(lc)
print(lc[0][1]==lc[1][1])
l = np.array(l)
for temps in range(count_row):

  c = np.correlate(l,lc[temps],'full')
  result = np.argmax(c)
  desp.append(int(result) -lc[temps].size+1)
  mse.append(0)
  for index in list(range(max([desp[temps],0]),min([l.size,desp[temps]+lc[temps].size]))):
    print(lc[temps][index])
    mse[temps] = (lc[temps][index]-l[index-desp[temps]])**2.0 + mse[temps]

import matplotlib
l = np.zeros(200)
lc = np.zeros([count_row-1,200])
for temps in range(count_row-1):

  aux = newdf[temps]
  num_row = aux.shape[0]
#  print(temps,num_row)
  for i in range(num_row):
    
    elem = aux.iloc[i,[5]]
    lc[temps][i] = elem.values.tolist()[0] 
#    print(lc[temps][i])
    l[i] = l[i] + lc[temps][i]/count_row 

#    print(lc[temps][i],temps,i)
mse = []
desp = []
lc = np.array(lc)
print(lc[0][1]==lc[1][1])
l = np.array(l)
for temps in range(count_row):

  c = np.correlate(l,lc[temps],'full')
  result = np.argmax(c)
  desp.append(int(result) -lc[temps].size+1)
#  print(desp)
  mse.append(0)
  for index in list(range(max([desp[temps],0]),min([l.size,desp[temps]+lc[temps].size]))):
    print(lc[temps][index])
    mse[temps] = (lc[temps][index]-l[index-desp[temps]])**2.0 + mse[temps]

plt.plot(range(len(l)),l)

plt.plot(range(count_row),mse)
msearray = np.array(mse)
positions = np.where(msearray > 200)
print(positions)

positions = list(positions)
plt.plot(range(len(l)),lc[419,:])

plt.plot(range(count_row),desp)

def informacio(var_list,swnum):
  Sw = [df,df,df,df,df]
  aux1 = Sw[swnum]
# var_list is the list of variables to be observed
# swnum is the switch to be observed
  idxCtrl = aux1.columns.get_loc("SteeringCommand")
  idxCtrlD = aux1.columns.get_loc("SteeringCommandDate")
  idxEL = aux1.columns.get_loc("EnergySurfaceLeft")
  idxER = aux1.columns.get_loc("EnergySurfaceRight")
  idxT = aux1.columns.get_loc("ControlOutTime")
  idxMaxL = aux1.columns.get_loc("")
  idxMaxR = aux1.columns.get_loc("")
  idxMotorT = aux1.columns.get_loc("")

  Sw = [df.iloc[:,[2,3,14,15,28,29,30,31]]]

  
  aux4 = aux1.iloc[:,0].dropna(axis="index",how="all")
  count_row = aux4.shape[0]
  count_col = aux1.shape[1]
  newdf = []

  for temps in range(count_row-1): #Itera temps (files)
    t = str(aux1.iloc[temps,0])
    tnext = str(aux1.iloc[temps+1,0])
    newdf2 = []
    print(temps)
    for index in range(int(count_col/2)): #Itera columnes (dades)
  #  for index in [2,3,14,15,28,29,30,31]: #Itera columnes (dades)
      index = int(index/2)
      aux2 = aux1.iloc[:,index*2:index*2+2]
      aux3 = aux2.iloc[:,0]
      aux3 = aux3.dropna(axis="index",how="all")

      newdf2.append(aux2[(aux2.iloc[:,0]>= t)&(aux2.iloc[:,0]<tnext)].reset_index(drop=True))

    newdf.append(pd.concat(newdf2, axis=1))


  ############################ OBTAIN DATA ########################

# Averaging and correlating for intensity data
  l = np.zeros(200)
  lc = np.zeros([count_row-1,200])
  for temps in range(count_row-1):

    aux = newdf[temps]
    num_row = aux.shape[0]
    for i in range(num_row):

      elem = aux.iloc[i,[5]]
      lc[temps][i] = elem.values.tolist()[0] 
      l[i] = l[i] + lc[temps][i]/count_row 

  mse = []
  desp = []
  lc = np.array(lc)
  l = np.array(l)
  for temps in range(count_row):

    c = np.correlate(l,lc[temps],'full')
    result = np.argmax(c)
    desp.append(int(result) -lc[temps].size+1)
    mse.append(0)
    for index in list(range(max([desp[temps],0]),min([l.size,desp[temps]+lc[temps].size]))):
      print(lc[temps][index])
      mse[temps] = (lc[temps][index]-l[index-desp[temps]])**2.0 + mse[temps]

#Tot aquesta cel·la s'ha d'executar junta si es volen imprimir les 

BouwstenenVariableNames = ['ControlPosition', 'SteeringCommand',
                           'MotorCurrentActive']
ctt = -5

def convertToNumber(dataframe, variableName):
  resultdf = dataframe[variableName]
  
  if (variableName == 'ControlPosition'):
    resultdf.loc[dataframe[variableName] == "Links in controle"] = -1+ctt
    resultdf.loc[dataframe[variableName] == "Rechts in controle"] = 1+ctt
    resultdf.loc[dataframe[variableName] == "Uit controle"] = 0+ctt
    
  if (variableName == 'SteeringCommand'):
    resultdf.loc[dataframe[variableName] == "Sturing Links"] = -1+ctt
    resultdf.loc[dataframe[variableName] == "Sturing Rechts"] = 1+ctt
    resultdf.loc[dataframe[variableName] == "Sturing Onbekend"] = 0+ctt
    
  if (variableName == 'MotorCurrentActive'):
    resultdf.loc[dataframe[variableName] == "Motorstroom Actief"] = 1+ctt
    resultdf.loc[dataframe[variableName] == "Geen Motorstroom"] = 0+ctt
    
def plotColumn(dataframe, variableName, ax):
  timeName = variableName + 'Date'

  if (variableName in BouwstenenVariableNames):
    convertToNumber(dataframe, variableName)
  v = dataframe[variableName]
  dataframe[variableName] = v/max(v)
  dataframe.plot(drawstyle='steps-post',x=timeName,y=variableName, ax=ax)
  
def plotDataframeColumns(dataframe, variableNames):
  df = dataframe.copy()
  ax = plt.gca()
  for variableName in variableNames:
    timeName = variableName + 'Date'
    plotColumn(df, variableName, ax)
    
  plt.xlabel('Time')
  
def plotEventColumns(dataframe, variableNames, passedtime=0.0001, timeshift=0):
  df = dataframe.copy()
  ax = plt.gca()
  shift = 0
  f = (dataframe['SteeringCommandDate'][1] - dataframe['SteeringCommandDate'][0])
  f2 = (dataframe['SteeringCommandDate'][2] - dataframe['SteeringCommandDate'][1])
  total = f + f2
  p1 = f/total
  p2 = f2/total
  print(dataframe['SteeringCommandDate'][0])
  print(dataframe['SteeringCommandDate'][1])
  print(dataframe['SteeringCommandDate'][2])
  for variableName in variableNames:
    plotColumn(df, variableName, ax)
  xmin, xmax, ymin, ymax = plt.axis()
  print(xmin, xmax, ymin, ymax)
  shift = p1*(xmax-xmin)-0.00004
  ax.set_xlim(xmax = min(xmin+passedtime+shift,xmax+shift), xmin = xmin+shift)
  xmin, xmax, ymin, ymax = plt.axis()
  print(xmin, xmax, ymin, ymax)
  plt.xlabel('Time')
  
def plotEvent(swNum, eventNum, columnNames,passedtime=0.0001):
  event = get_event_info(swNum-1, eventNum-1)
  plotEventColumns(event,columnNames,passedtime=passedtime)

plotDataframeColumns(df,["MotorTransitionTimeLeft"])
plotDataframeColumns(df,["EnergySurfaceLeft"])

plotDataframeColumns(df,["MotorTransitionTimeRight"])
plotDataframeColumns(df,["EnergySurfaceRight"])

#Plot energies
ax = plt.gca()
df.plot(drawstyle='steps-post',x="EnergySurfaceLeftDate",y="EnergySurfaceLeft",ax=ax)

df







