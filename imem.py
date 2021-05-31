"""
@Author  : Tianyi Wang
@License : GPL-3.0
@Contact : 2019302443@mail.nwpu.edu.cn
@File    : imem.py
@Time    : 2021/05/31 16:33
@Desc    : An implementation of instruction memory model
"""
import math

from myhdl import block, Signal, instances, always_comb, intbv


@block
def imem(addr):
    dout = Signal(intbv(0, min=-(math.pow(2, 31)), max=(math.pow(2, 31) - 1)))

    imem = [intbv(0, min=-(math.pow(2, 31)), max=(math.pow(2, 31) - 1)) for i in range(1024)]

    @always_comb
    def comb():
        dout.next = imem[addr]

    return instances()
