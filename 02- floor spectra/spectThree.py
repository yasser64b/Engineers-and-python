
''''
This code is the computation of 5% damping spectra 
of an acceleration signal for a period of 12 seconds. 

inputs : Acc: acceleration record , dt: time step
'''

import numpy as np

def spectThree(Acc, dt):  # acc is in in/s2, dt is time step
    """
    This program takes acceleration 
    Time Histories and calculate the spectra for 5% damping
    for 3 second period
    """
    Tn = 0.05  # start of the spectra 0.05 sec
    zeta = 0.05  # Damping ratio
    u_1 = 0
    Ax = []
    PI = np.pi

    for _ in range (301):
        wn = 2 * PI / Tn  # natural frequency
        u = [0]


        for j , _ in enumerate (Acc):

           if j == 0:
               khat = 1/(dt**2) + wn * zeta/(dt)
               a = 1/(dt**2) -  wn*zeta/(dt)
               b = (wn**2) - 2/(dt**2)
               phat = (Acc[j] - a*u_1 - b*u[j])
               u.append(phat/khat) 

           else:
               phat = Acc[j] - a*u[j-1] - b*u[j]
               u.append(phat/khat)
        Tn += 0.01
        an=np.multiply((wn**2), u)
        Ax.append(max(np.absolute(an))/386)        
    return Ax