from indica.models import Plasma
from indica.readers.read_st40 import ReadST40

if __name__ == "__main__":

    reader = ReadST40(11560, tstart=0.02, dt= 0.01, tend=0.12, )
    reader(["ppts"], R_shift=0.0)


    plasma = Plasma()
    plasma.set_equilibrium(reader.equilibrium)

    # reader(["astra"], R_shift=0.0, revisions={"astra": "RUN613"})