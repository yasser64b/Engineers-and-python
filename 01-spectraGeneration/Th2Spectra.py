"""
This program take gound motion Time histories (THs) in a directory and
save them to excel files
"""

import time
import os
import numpy as np
import pandas as pd
from spect import *


class spect_to_excel(object):

    """
    compute spectra of many time histories (TH) and
    save the to an excel file
    """

    def __init__(self, directory, THx, THy, skip_header):
        self.directory = directory
        self.THx = THx
        self.THy = THy
        self.skip_header = skip_header
        self.datax = np.genfromtxt(
            self.directory + "/" + self.THx, skip_header=self.skip_header
        )
        self.datay = np.genfromtxt(
            self.directory + "/" + self.THy, skip_header=self.skip_header
        )

    def Spectra(self):
        """' calculate the spectral acceleration"""
        spectrum_x = spect(self.datax[:, 1], self.datax[2, 0] - self.datax[1, 0])
        spectrum_y = spect(self.datay[:, 1], self.datay[2, 0] - self.datay[1, 0])
        return [spectrum_x, spectrum_y]


#  Inpute the directory that all you TH files are stored
directory_ths = input("Directory you stored THs: ")
skip_header = int(input("How many lines to skip? (e.g., 5) ="))
save_to_directory = input("Save to  Directory=")
startTime = time.time()


os.chdir(directory_ths)
earthQuakes = os.listdir(directory_ths)
number_of_ths = len(earthQuakes)


# Empty list and DF for result storage
all_spectrums = {}  # store all spectrum and ave
srss_all = []  # Stor srss values
period = np.arange(0.05, 12, 0.01)  # periods
all_spectrums["Time"] = period
os.chdir(save_to_directory)
for i in range(0, number_of_ths, 2):
    THx = earthQuakes[i]
    THy = earthQuakes[i + 1]
    W = spect_to_excel(directory_ths, THx, THy, skip_header)
    [Spectrum_x, Spectrum_y] = W.Spectra()
    SRSS = np.sqrt(np.sum(np.square([Spectrum_x, Spectrum_y]), axis=0))
    srss_all.append(SRSS)

    all_spectrums[THx[:-4]] = Spectrum_x
    all_spectrums[THy[:-4]] = Spectrum_y
    all_spectrums[THy[:-6] + "_SRSS"] = SRSS

all_spectrums["Average of SRSSes"] = np.array(srss_all).mean(axis=0)

spectraDf = pd.DataFrame(all_spectrums)
spectraDf.to_excel("spectra.xlsx", index=False)  # output file


print("Run time: --- %s seconds ---" % (time.time() - startTime))
