from myhdl import block, Signal, instances, always_comb, intbv
import math


@block
def imem(addr):
    dout = Signal(intbv(0, min=-(math.pow(2, 31)), max=(math.pow(2, 31) - 1)))

    imem = [intbv(0, min=-(math.pow(2, 31)), max=(math.pow(2, 31) - 1)) for i in range(1024)]

    @always_comb
    def comb():
        dout.next = imem[addr]

    return instances()
