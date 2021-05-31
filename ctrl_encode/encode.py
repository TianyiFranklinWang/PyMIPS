"""
@Author  : Tianyi Wang
@License : GPL-3.0
@Contact : 2019302443@mail.nwpu.edu.cn
@File    : encode.py
@Time    : 2021/05/31 16:33
@Desc    : Customized control signals
"""
from myhdl import intbv

# NPC control signal
NPC_PLUS4 = intbv(0, min=0, max=4)
NPC_BRANCH = intbv(1, min=0, max=4)
NPC_JUMP = intbv(2, min=0, max=4)

# EXT control signal
EXT_ZERO = intbv(0, min=0, max=4)
EXT_SIGNED = intbv(1, min=0, max=4)
EXT_HIGHPOS = intbv(2, min=0, max=4)

# ALU control signal
ALUOp_NOP = intbv(0, min=0, max=32)
ALUOp_ADDU = intbv(1, min=0, max=32)
ALUOp_ADD = intbv(2, min=0, max=32)
ALUOp_SUBU = intbv(3, min=0, max=32)
ALUOp_SUB = intbv(4, min=0, max=32)
ALUOp_AND = intbv(5, min=0, max=32)
ALUOp_OR = intbv(6, min=0, max=32)
ALUOp_NOR = intbv(7, min=0, max=32)
ALUOp_XOR = intbv(8, min=0, max=32)
ALUOp_SLT = intbv(9, min=0, max=32)
ALUOp_SLTU = intbv(10, min=0, max=32)
ALUOp_EQL = intbv(11, min=0, max=32)
ALUOp_BNE = intbv(12, min=0, max=32)
ALUOp_GT0 = intbv(13, min=0, max=32)
ALUOp_GE0 = intbv(14, min=0, max=32)
ALUOp_LT0 = intbv(15, min=0, max=32)
ALUOp_LE0 = intbv(16, min=0, max=32)
ALUOp_SLL = intbv(17, min=0, max=32)
ALUOp_SRL = intbv(18, min=0, max=32)
ALUOp_SRA = intbv(19, min=0, max=32)

# GPR control signal
GPRSel_RD = intbv(0, min=0, max=4)
GPRSel_RT = intbv(1, min=0, max=4)
GPRSel_31 = intbv(2, min=0, max=4)

# MemtoReg
WDSel_FromALU = intbv(0, min=0, max=4)
WDSel_FromMEM = intbv(1, min=0, max=4)
WDSel_FromPC = intbv(2, min=0, max=4)

# Memory control signal
BE_SB = intbv(0, min=0, max=4)
BE_SH = intbv(1, min=0, max=4)
BE_SW = intbv(2, min=0, max=4)

ME_LB = intbv(0, min=0, max=8)
ME_LBU = intbv(1, min=0, max=8)
ME_LH = intbv(2, min=0, max=8)
ME_LHU = intbv(3, min=0, max=8)
ME_LW = intbv(4, min=0, max=8)
