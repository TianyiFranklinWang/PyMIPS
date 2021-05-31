"""
@Author  : Tianyi Wang
@License : GPL-3.0
@Contact : 2019302443@mail.nwpu.edu.cn
@File    : instructions.py
@Time    : 2021/05/31 16:33
@Desc    : Global variables of MIPS instructions
"""
from myhdl import intbv

# OP
INSTR_RTYPE_OP = intbv(0, min=0, max=64)

INSTR_LB_OP = intbv(32, min=0, max=64)
INSTR_LH_OP = intbv(33, min=0, max=64)
INSTR_LBU_OP = intbv(36, min=0, max=64)
INSTR_LHU_OP = intbv(37, min=0, max=64)
INSTR_LW_OP = intbv(35, min=0, max=64)

INSTR_SB_OP = intbv(40, min=0, max=64)
INSTR_SH_OP = intbv(41, min=0, max=64)
INSTR_SW_OP = intbv(43, min=0, max=64)

INSTR_ADDI_OP = intbv(8, min=0, max=64)
INSTR_ADDIU_OP = intbv(9, min=0, max=64)
INSTR_ANDI_OP = intbv(12, min=0, max=64)
INSTR_ORI_OP = intbv(13, min=0, max=64)
INSTR_XORI_OP = intbv(14, min=0, max=64)
INSTR_LUI_OP = intbv(15, min=0, max=64)
INSTR_SLTI_OP = intbv(10, min=0, max=64)
INSTR_SLTIU_OP = intbv(11, min=0, max=64)

INSTR_BEQ_OP = intbv(4, min=0, max=64)
INSTR_BNE_OP = intbv(5, min=0, max=64)
INSTR_BGEZ_OP = intbv(1, min=0, max=64)
INSTR_BGTZ_OP = intbv(7, min=0, max=64)
INSTR_BLEZ_OP = intbv(6, min=0, max=64)
INSTR_BLTZ_OP = intbv(1, min=0, max=64)

INSTR_J_OP = intbv(2, min=0, max=64)
INSTR_JAL_OP = intbv(3, min=0, max=64)

# Funct
INSTR_ADD_FUNCT = intbv(32, min=0, max=64)
INSTR_ADDU_FUNCT = intbv(33, min=0, max=64)
INSTR_SUB_FUNCT = intbv(34, min=0, max=64)
INSTR_SUBU_FUNCT = intbv(35, min=0, max=64)
INSTR_AND_FUNCT = intbv(36, min=0, max=64)
INSTR_NOR_FUNCT = intbv(39, min=0, max=64)
INSTR_OR_FUNCT = intbv(37, min=0, max=64)
INSTR_XOR_FUNCT = intbv(38, min=0, max=64)
INSTR_SLT_FUNCT = intbv(42, min=0, max=64)
INSTR_SLTU_FUNCT = intbv(43, min=0, max=64)
INSTR_SLL_FUNCT = intbv(0, min=0, max=64)
INSTR_SRL_FUNCT = intbv(2, min=0, max=64)
INSTR_SRA_FUNCT = intbv(3, min=0, max=64)
INSTR_SLLV_FUNCT = intbv(4, min=0, max=64)
INSTR_SRLV_FUNCT = intbv(6, min=0, max=64)
INSTR_SRAV_FUNCT = intbv(7, min=0, max=64)
INSTR_JR_FUNCT = intbv(8, min=0, max=64)
INSTR_JALR_FUNCT = intbv(9, min=0, max=64)

INSTR_BGEZ_RT = intbv(1, min=0, max=32)
INSTR_BLTZ_RT = intbv(0, min=0, max=32)
