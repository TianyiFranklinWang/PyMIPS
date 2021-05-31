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
def imem(addr, dout):
    imem = [Signal(intbv(0, min=-(math.pow(2, 32)), max=(math.pow(2, 32) - 1))) for _ in range(1024)]
    with open("./imem.txt") as data:
        lines = data.readlines()
        for index, line in enumerate(lines):
            imem[index] = Signal(intbv(int(line, 16))[32:])

    @always_comb
    def read():
        dout.next = imem[addr]

    return instances()
