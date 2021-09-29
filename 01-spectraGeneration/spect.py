
''''
This code is the computation of 5% damping spectra 
of an acceleration signal for a period of 12 seconds. 

inputs : Acc: acceleration record , dt: time step
'''

import numpy as np

def spect(Acc, dt):  # acc is in in/s2, dt is time step
    """
    This program takes acceleration 
    Time Histories and calculate the spectra for 5% damping
    """
    Tn = 0.05  # start of the spectra 0.05 sec
    zeta = 0.05  # Damping ratio
    u_1 = 0
    Ax = []
    PI = np.pi

    for _ in range(1195):
        wn = 2 * PI / Tn  # natural frequency
        u = [0]

        # the first value of acceleration is used here
        j = 0
        khat = 1 / (dt ** 2) + wn * zeta / (dt)
        a = 1 / (dt ** 2) - wn * zeta / (dt)
        b = (wn ** 2) - 2 / (dt ** 2)
        phat = 386 * Acc[j] - a * u_1 - b * u[j]
        u.append(phat / khat)
        # rest of the acceleration data used here
        for j, accj in enumerate(Acc[1:]):
            phat = 386 * accj - a * u[j] - b * u[j + 1]
            u.append(phat / khat)

        Tn += 0.01
        an = np.multiply((wn ** 2), u)
        Ax.append(max(np.absolute(an)) / 386)

    return Ax
