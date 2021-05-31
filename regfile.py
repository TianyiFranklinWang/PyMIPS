"""
@Author  : Tianyi Wang
@License : GPL-3.0
@Contact : 2019302443@mail.nwpu.edu.cn
@File    : regfile.py
@Time    : 2021/05/31 16:33
@Desc    : An implementation of MIPS register model
"""
import math

from myhdl import block, Signal, instances, always_seq, intbv, always_comb


@block
def regfile(clk, rst, ra, rb, rw, busa, busb, busw, regwr):
    rf = [Signal(intbv(0, min=-(math.pow(2, 31)), max=(math.pow(2, 31) - 1))) for _ in range(32)]

    @always_seq(clk.posedge, reset=rst)
    def write():
        if rst:
            for i in range(32):
                rf[i].next = 0
        if regwr:
            if rw != 0:
                rf[rw].next = busw

    @always_comb
    def read():
        busa.next = 0 if ra == 0 else rf[ra]
        busb.next = 0 if rb == 0 else rf[rb]

    return instances()
