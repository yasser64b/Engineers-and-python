
"""
This programe take the analysis results from Th2spectra 
file soterd in a folder togeter with DBE and MCE spectras.
"""

import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


#  Figure limits & properties
xlim = [0, 6]
ylim = [0, 2.5]
grid_lwidth = 0.15
C = ["DeepPink", "Cyan", "blue", "Black"]  # color to plots


#  inputs
saveToDirectory = input("Directory spectra file is stored:")
spectraType = input("Spectra type (1.DBE/MCE, 2.OBE/SSE):")

if spectraType == "1":
    scale = {"DBE": 0.5, "MCE": 0.7}
else:
    scale = {"OBE": 0.5, "SSE": 0.7}

print("Applied scales: ", scale)

#  Read files in the folder
os.chdir(saveToDirectory)
# uploades
spectrum_1 = np.genfromtxt(saveToDirectory + "\\" + list(scale.keys())[0] + ".txt")
spectrum_2 = np.genfromtxt(saveToDirectory + "\\" + list(scale.keys())[1] + ".txt")
Spectrum = {list(scale.keys())[0]: spectrum_1, list(scale.keys())[1]: spectrum_2}

df = pd.read_excel(saveToDirectory + "\\spectra.xlsx")

time = df["Time"]
columns = df.columns[1:-1]
thx_thy_srss = len(columns)

# plot spectrums
for i in range(0, thx_thy_srss, 3):
    for sp in list(scale.keys()):
        scaleSpectra = scale[sp]

        plt.figure(figsize=(10, 5))
        plt.plot(
            time,
            scaleSpectra * df[columns[i + 0]],
            C[0],
            time,
            scaleSpectra * df[columns[i + 1]],
            C[1],
            time,
            scaleSpectra * df[columns[i + 2]],
            C[2],
            Spectrum[sp][:, 0],
            Spectrum[sp][:, 1],
            C[3],
        )

        plt.ylabel("Sa (g)")
        plt.xlabel("Period(sec)")

        plt.title(
            "Acceleration Response Spectra: "
            + columns[i][2:-2]
            + ", "
            + sp
            + " , ζ=0.05 ",
            fontweight="bold",
        )

        plt.grid(linewidth=grid_lwidth)
        plt.legend([columns[i][2:], columns[i + 1][2:], "SRSS", sp + " Spectrum"])
        plt.xlim(xlim)
        plt.ylim(ylim)
        # save images
        plt.savefig(sp + "_" + columns[i][2:-2] + ".png", dpi=300, bbox_inches="tight")


# Plot the Mean spectrum:
for sp in list(scale.keys()):
    scaleSpectra = scale[sp]

    plt.figure(figsize=(10, 5))
    plt.plot(
        time,
        scaleSpectra * df[columns[-1]],
        C[2],
        Spectrum[sp][:, 0],
        Spectrum[sp][:, 1],
        C[3],
    )
    plt.ylabel("Sa (g)")
    plt.xlabel("Period(sec)")
    plt.title(
        sp + " Average Scaled Acceleration Response Spectra ζ=0.05 ",
        fontweight="bold",
    )
    plt.grid(linewidth=grid_lwidth)
    plt.legend(["Mean Spectrum", sp + " Spectrum"])
    plt.xlim(xlim)
    plt.ylim(ylim)
    plt.savefig(sp + "_mean.png", dpi=300, bbox_inches="tight")
    plt.close()

# %%
