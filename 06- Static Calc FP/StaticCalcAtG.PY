class dispFTP(object):
    """
    input the expecting acceleration (g) of pendulum , period of pendulum (sec)
    and the friction (u=3) associated with pendulum damping of 5%.
    """

    def __init__(self, acc=0.4, period=4, u=3):
        self.acc = acc
        self.T = period
        self.u = u

    def disp(self):
        W = 1
        R = 386 * (self.T / (2 * 3.14)) ** 2  # T = 2*pi*sqrt(R/g) --> R = g (T/2*pi)**2
        damping = (self.u * 0.01 * W * 4) / (2 * 3.14 * self.acc * W) # 
        Disp = (self.acc - 0.01 * self.u) * R
        return [R, damping, Disp]


DataCenter = dispFTP(acc=0.4, period=5, u=3)
R, damping, Disp = DataCenter.disp()
print("\n")
print("Results: ")
print(
    """Displacement = {0:.1f} inches
Pendulum radius= {1:.1f} inches
Damping = {2:.2f} """.format(
        Disp, R, damping
    )
)
