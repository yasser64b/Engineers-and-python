"""Compute and calculate floor spectral acceleration.

Description:
This code take the accelerations txt files (A1, A2)
or one csv file (A.csv) and return 0.05-3 sec spectral value and graph
of 0.05-sec graph.

Have the txt file in the directory before running the code.

"""

import os
import numpy as np
import matplotlib.pyplot as plt
from spectThree import * 


def ThreeSecSpectra (TimeStepSpect, filename=''):
    ''''
    This code take the accelerations txt files (A1, A2) or one csv file (A.csv) and return 0.05-3 sec spectra and graph. 
    Have the txt file in the directory before running the code.  
    '''
    # txt file 
    # A1=np.genfromtxt('A1.txt')
    # A2=np.genfromtxt('A2.txt')
    #  csv file
    A=np.genfromtxt(filename, delimiter=',')
    A1=A[0]
    A2=A[1]

    ax=spectThree(A1,TimeStepSpect)
    ay=spectThree(A2,TimeStepSpect)
    a=np.sqrt(np.sum(np.square([ax,ay]),axis=0))
    return a

fileDir='D:\\EPS\\PROJECTS\\68_Data Center _ Chile\\Sap Model new prop\\out puts\\UB'

files=os.listdir(fileDir)

files_acc=[]
for name in files:
    if 'Acc_floor' in name:
        files_acc.append(name)
        print(name)

TimeStepSpect=0.01


for i in range (len(files_acc)):
    a=ThreeSecSpectra(TimeStepSpect, filename=fileDir+'\\'+files_acc[i])
    ts=np.arange(0,301*TimeStepSpect, TimeStepSpect)
    print('Median 0.05-3 sec =',files_acc[i], "%.2f" % np.median(a[4:]))
    plt.figure(figsize=(7,4))
    p1=plt.plot(ts[4:],a[4:], 'b')
    p2=plt.plot(ts[4:],np.multiply(np.median(a[4:]),np.ones(301-4)), 'r--')
    plt.xlabel('Fundamental Period (sec)')
    plt.ylabel('Spectral Acceleration (g)')
    plt.title(files_acc[i][:-14],fontweight='bold')
    plt.legend((p1[0], p2[0]), ('Time History Response Spectrum', 'Median 0.05-3 sec:'+str("%.2f" % np.median(a[4:]))))
    # plt.title('DBE Floor Spectral Acceleration ', r'$\xi$ =0.05', fontsize=10)
    plt.grid(linewidth=0.15)
    plt.axis([0, 3, 0, 0.4])
    plt.savefig(files_acc[i][:-4]+'.png', dpi=300)
    # plt.show()

