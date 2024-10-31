from indica.readers.read_st40 import ReadST40
import matplotlib.pyplot as plt

equil_reader = ReadST40(11089, tstart=0.04, tend=0.10, dt=0.01,)
equil_reader(["xrcs"], R_shift=-0.2, )

equil_reader.equilibrium.rho[20, 30,].plot()
plt.show()
print()