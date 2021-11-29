import os
import time

"""
THis program take the time history record nad update the txt file's name 
per information provided inside the ground motion record file 
"""


# Directory=input('Directory to be read=')
# DirectoryFiles=os.listdir(Directory)

# print('Total Number of files=', len(DirectoryFiles))

# ListFormat=input('Do you need the files in List format? y/n ?')
# if ListFormat=='y':
#     print('\n'+'In a matrix format:')
#     print('Files=',DirectoryFiles)
# else:
#     print('Name of the files=')
#     for i in DirectoryFiles:
#         print(i)


def nameUpdate(Directory=""):
    os.chdir(Directory)
    # name=[]
    for i in range(10000):
        DirectoryFiles = os.listdir(Directory)
        for txt in DirectoryFiles:
            f = open(txt, "r")
            namef = f.readline()
            # name.append(namef.split(' ')[-1][:-1])
            namef = namef.split(":")[-1][1:-1]
            f.close()
            if txt != namef:
                os.rename(txt, namef)
        print(str(i) + " round done")
        time.sleep(1)
        # print(name)
        # for t,n in zip(DirectoryFiles,name):
        #     if t != n:
        #         os.rename(t, n)


def nameUpdate2(Directory=""):
    # l1=len('Time Series matched accelerogram: ')
    # l2=len('M_Chichi_E.txt')
    os.chdir(Directory)
    # name=[]
    for i in range(1000):
        DirectoryFiles = os.listdir(Directory)
        for txt in DirectoryFiles:
            # f=open(txt, 'r')
            # namef=f.readline()
            # name.append(namef.split(' ')[-1][:-1])
            name = txt.split("_")[2:]
            namef = "-".join(name)
            # f.close()
            # if txt != namef:
            os.rename(txt, namef[:-4])
        print(str(i) + " round done")
        time.sleep(1)
        # print(name)
        # for t,n in zip(DirectoryFiles,name):
        #     if t != n:
        #         os.rename(t, n)


Dir = "D:\\EPS\\PROJECTS\\83-Diamante Mexico project\\Matched Received TH"
nameUpdate(Directory=Dir)
