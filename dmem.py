"""
@Author  : Tianyi Wang
@License : GPL-3.0
@Contact : 2019302443@mail.nwpu.edu.cn
@File    : dmem.py
@Time    : 2021/05/31 16:33
@Desc    : An implementation of data memory model
"""
import math

from myhdl import block, Signal, instances, always, intbv, bin, always_comb


@block
def dmem(clk, addr, din, be, wren, dout):
    dmem = [Signal(intbv(0, min=-(math.pow(2, 32)), max=(math.pow(2, 32) - 1))) for _ in range(1024)]
    with open("./dmem.txt") as data:
        lines = data.readlines()
        for index, line in enumerate(lines):
            dmem[index] = Signal(intbv(int(line, 2))[32:])

    @always(clk.posedge)
    def write():
        if wren:
            if bin(be) == '1111':
                dmem[addr].next = din
            elif bin(be) == '1100':
                dmem[addr][31:16].next = din[15:0]
            elif bin(be) == '0011':
                dmem[addr][15:0].next = din[15:0]
            elif bin(be) == '1000':
                dmem[addr][31:24].next = din[7:0]
            elif bin(be) == '0100':
                dmem[addr][23:16].next = din[7:0]
            elif bin(be) == '0010':
                dmem[addr][15:8].next = din[7:0]
            elif bin(be) == '0001':
                dmem[addr][7:0].next = din[7:0]

    @always_comb
    def read():
        dout.next = dmem[addr]

    return instances()
