"""
@Author  : Tianyi Wang
@License : GPL-3.0
@Contact : 2019302443@mail.nwpu.edu.cn
@File    : clock.py
@Time    : 2021/05/31 16:33
@Desc    : An implementation of CPU clock
"""
from myhdl import block, always, delay


@block
def clock(clk):
    @always(delay(10))
    def clck():
        clk.next = not clk

    return clck
