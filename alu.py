import math

from myhdl import block, always_comb, Signal, intbv, instances, bin

import ctrl_encode


@block
def alu(a, b, aluop):
    c = Signal(intbv(0, min=-(math.pow(2, 31)), max=(math.pow(2, 31) - 1)))
    compare = Signal(0)

    @always_comb
    def calculate():
        c.next = {bin(ctrl_encode.ALUOp_NOP): lambda: b,
                  bin(ctrl_encode.ALUOp_ADD): lambda: a.signed + b.signed,
                  bin(ctrl_encode.ALUOp_ADDU): lambda: a.unsigned + b.unsigned,
                  bin(ctrl_encode.ALUOp_SUB): lambda: a.signed - b.signed,
                  bin(ctrl_encode.ALUOp_SUBU): lambda: a.unsigned - b.unsigned,
                  bin(ctrl_encode.ALUOp_AND): lambda: a & b,
                  bin(ctrl_encode.ALUOp_OR): lambda: a | b,
                  bin(ctrl_encode.ALUOp_XOR): lambda: a ^ b,
                  bin(ctrl_encode.ALUOp_NOR): lambda: ~(a | b),
                  bin(ctrl_encode.ALUOp_SLL): lambda: b << a[4:0],
                  bin(ctrl_encode.ALUOp_SRL): lambda: b >> a[4:0],
                  bin(ctrl_encode.ALUOp_SLT): lambda: 1 if (a < b) else 0,
                  bin(ctrl_encode.ALUOp_SLTU): lambda: 1 if (a.unsigned < b.unsigned) else 0,
                  bin(ctrl_encode.ALUOp_EQL): lambda: 1 if (a == b) else 0,
                  bin(ctrl_encode.ALUOp_BNE): lambda: 1 if (a != b) else 0,
                  bin(ctrl_encode.ALUOp_GT0): lambda: 1 if (a > 0) else 0,
                  bin(ctrl_encode.ALUOp_GE0): lambda: 1 if (a >= 0) else 0,
                  bin(ctrl_encode.ALUOp_LT0): lambda: 1 if (a < 0) else 0,
                  bin(ctrl_encode.ALUOp_LE0): lambda: 1 if (a <= 0) else 0
                  }.get(bin(aluop), None)()
        if c is None:
            c.next = 0

        compare.next = c[0]

    return instances()
