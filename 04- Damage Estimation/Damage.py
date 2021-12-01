import matplotlib.pyplot as plt
import numpy as np


class Damage(object):
    """
    This program calculate the percentage of damage to a structure
    based on its average and max floor accelerations and drifts
    """

    def __init__(self, x=[1, 2, 3], y=[-1, -3, -5], Degree_pol=3):
        self.x = x
        self.y = y
        self.Degree_pol = Degree_pol

    def DMG_calc(self, num=1.5):
        self.num = num
        z = np.polyfit(self.x, self.y, self.Degree_pol)
        f = np.poly1d(z)
        r = f(self.num)
        return [self.num, r]

    def PltCrv(self):
        z = np.polyfit(self.x, self.y, self.Degree_pol)
        f = np.poly1d(z)
        y_new = f(self.x)
        plt.plot(self.x, self.y, "o", self.x, y_new, "--")
        plt.show()


# inputs for three type of system______________________________________________________
fixed = [1.27, 2.6075, 1.67590]
LRB = [0.47, 0.4288, 0.28]
TFP = [0.16, 0.16, 0.13]

L = fixed  # select type out of above
# ___________________________________________________________

floor_acc = L[0]  # 0-3 sec median floor acceleration
Floor_driftM = L[1]  # maximum drift
Floor_drift = L[2]  # Average drift


# Floor acceleration in (g) and corresponding damages
Acc = [0, 0.30, 0.40, 0.60, 1, 1.3, 1.501, 1.502, 1.503, 1.504, 1.505]  # floor Acc
AccD = [0, 1.6, 2.7, 4.2, 10, 14, 16, 16, 16, 16, 16]  # Damage

# Calculate damage
DMG1 = Damage(Acc, AccD, Degree_pol=3)
DMG1.PltCrv()
[Acc_f, damage_f_a] = DMG1.DMG_calc(floor_acc)

# __________________________________________________

print()
print(
    "The associated damage to the floor acc of %.2f g is ------>  %.2f percent of total cost."
    % (Acc_f, damage_f_a)
)


#  Average drift in % __________________________________
Drift = [0, 0.025, 0.050, 0.070, 0.10, 0.13, 0.20, 0.30, 0.5, 0.67, 1, 1.5, 2, 4]

# floor drift
DriftD = [0, 0, 0, 0, 0, 0, 0.50, 1, 1.2, 3.4, 5.9, 11.5, 13, 17]  # Damage in %


DMG2 = Damage(Drift, DriftD, Degree_pol=3)
DMG2.PltCrv()
[value, damage_d_a] = DMG2.DMG_calc(Floor_drift)

print(
    "The associated damge to the story drift of %.2f percent is ------> %.2f percent of total cost."
    % (value, damage_d_a)
)

#  Maximum drift in %
Drift = [0, 0.13, 0.20, 0.30, 1, 2, 3, 5]  # floor drift
DriftD = [0, 0, 0.50, 1, 2, 10, 13.5, 17]  # Damage in %

DMG2 = Damage(Drift, DriftD, Degree_pol=3)
DMG2.PltCrv()
[value, damage_d_m] = DMG2.DMG_calc(Floor_driftM)
print(
    "The associated damage to the story drift of %.2f percent is ------> %.2f percent of total cost."
    % (value, damage_d_m)
)
print()

print("Total damage=", damage_f_a + damage_d_a + damage_d_m)
