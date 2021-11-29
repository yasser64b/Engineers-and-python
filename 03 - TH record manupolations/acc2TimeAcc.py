"""
This program takes a time history record of one column and add a time column
next to it 
"""

import numpy as np
import os


# records= ['record_1.txt', 'record_2.txt'] # earthquake records in the directory
record_dir = input("Directory of the records:")
records = os.listdir(record_dir)

has_description = int(input('How many lines of description?'))

for i in range(len(records)):

    tx = open(records[i], "r").read()
    
    fistlines = tx.split("\n")[:2]
    acc = tx.split("\n")[2:]

    length = len(acc)
    fistlines = "\n ".join(fistlines)

    dt = tx.split("\n")[0]
    dt = float(dt.split("=")[1][:6])
    file = open("a_" + records[i], "w")
    file.write(fistlines)

    n = 0
    for line in acc:
        if line != "":
            file.write(str(round(n * dt - dt, 4)) + "   " + line + "\n")
            n = n + 1
    file.close()
    #     t=np.arange(0,length*dt,dt)
    #     t_acc=list(zip(t,acc))
    #     print(fistlines, '\n')
    print("dt=:", dt, "\n")
# print(t_acc)
