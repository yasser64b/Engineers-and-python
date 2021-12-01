import numpy as np
import matplotlib.pyplot as plt
import os.path


class GenMceDbe(object):
    '''
    This proram takes the design spectrum parameters 
    like SDs, SD1, SMs, SM1, TL and generate DBE and MCE design spectra 
    '''

    def __init__(self, SDs, SD1, SMs, SM1, TL):
        self.SDs = SDs
        self.SD1 = SD1
        self.SMs = SMs
        self.SM1 = SM1
        self.TL = TL

    def GenDBE(self):
        sa = []
        T0 = 0.2 * self.SD1 / self.SDs
        Ts = self.SD1 / self.SDs
        T = np.arange(0, 10, 0.05)
        for t in T:
            if t < T0:
                sa.append(self.SDs * (0.4 + (0.6 * t / T0)))
            elif t < Ts:
                sa.append(self.SDs)
            elif t < self.TL:
                sa.append(self.SD1 / t)
            else:
                sa.append(self.SD1 * self.TL / t ** 2)
        return [T, sa]

    def GenMCE(self):
        sa = []
        T0 = 0.2 * self.SM1 / self.SMs
        Ts = self.SM1 / self.SMs
        T = np.arange(0, 10, 0.05)
        for t in T:
            if t < T0:
                sa.append(self.SMs * (0.4 + (0.6 * t / T0)))
            elif t < Ts:
                sa.append(self.SMs)
            elif t < self.TL:
                sa.append(self.SM1 / t)
            else:
                sa.append(self.SM1 * self.TL / t ** 2)
        return [T, sa]


class save2txt(object):
    def __init__(self, name, matrix, directory):
        self.name = name
        self.matrix = matrix
        self.directory = directory

    def save(self):
        completeName = os.path.join(self.directory, self.name + ".txt")
        f = open(completeName, "w+")
        for i in range(len(self.matrix[0])):
            f.write(
                str("{:.3f}".format(self.matrix[0][i])) 
                + "  "
                + str("{:.4f}".format(self.matrix[1][i])) 
            )
            f.write("\n")
        f.close

# _____________________ INPUTS _____________________________

# Design spectra parameters 

SDs, SD1, SMs, SM1, TL = 0.619, 0.619, 0.93, 0.93, 10
Save2Dir = "C:\\Users\\Yasser B\Dropbox\\Engineers and python\\05- Design Spectrum Genration"

# __________________MCE___________________________
A = GenMceDbe(SDs, SD1, SMs, SM1, TL)
Sig1 = A.GenMCE()
S = save2txt(
    "MCE",
    Sig1,
    Save2Dir,
)

S.save()

#_________________DBE____________________________
Sig2 = A.GenDBE()
D = save2txt(
    "DBE",
    Sig2,
    Save2Dir,
)

D.save()

# ________________plot_____________________________

plt.plot(Sig1[0], Sig1[1],'r', Sig2[0], Sig2[1], 'b')
plt.grid("on", linewidth=0.2)
plt.legend(['MCE', 'DBE'])
plt.title('DBE and MCE spectra', fontsize = 12, color='blue')
plt.xlim([0,TL])
plt.xlabel('Period (sec)')
plt.ylabel('Sa (g)')
plt.savefig('mceDbeSpectrum.png', dpi=300, bbox_inches="tight")
plt.show()
