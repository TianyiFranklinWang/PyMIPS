"""
@Author  : Tianyi Wang
@License : GPL-3.0
@Contact : 2019302443@mail.nwpu.edu.cn
@File    : mips.py
@Time    : 2021/05/31 16:33
@Desc    : An implementation of MIPS CPU
"""
from myhdl import block, Signal, intbv, always_comb, always_seq, ConcatSignal, instances

from alu import alu
from ctrl_encode import encode
from instruction import instructions
from regfile import regfile


@block
def mips(clk, rst, imem_addr, imem_dout, dmem_addr, dmem_din, dmem_be, dmem_wren, dmem_dout):
    rw = Signal(intbv(0)[5:])
    rs = Signal(intbv(0)[5:])
    rt = Signal(intbv(0)[5:])
    busa = Signal(intbv(0)[32:])
    busb = Signal(intbv(0)[32:])
    busw = Signal(intbv(0)[32:])
    regwr = Signal(intbv(0)[0])
    U_RF = regfile(clk, rst, rw, rs, rt, busa, busb, busw, regwr)

    alu_b = Signal(intbv(0)[32:])
    aluout = Signal(intbv(0)[32:])
    aluctr = Signal(intbv(0)[5:])
    compare = Signal(intbv(0)[0])
    U_ALU = alu(busa, alu_b, aluout, aluctr, compare)

    opcode = Signal(intbv(0)[6:])
    func = Signal(intbv(0)[6:])
    rd = Signal(intbv(0)[5:])
    imm16 = Signal(intbv(0)[16:])
    imm26 = Signal(intbv(0)[26:])
    pc = Signal(intbv(0)[32:])
    memwr = Signal(intbv(0)[0])

    @always_comb
    def data_path():
        opcode.next = imem_dout[31:26]
        func.next = imem_dout[5:0]
        rs.next = imem_dout[25:21]
        rt.next = imem_dout[20:16]
        rd.next = imem_dout[15:11]
        imm16.next = imem_dout[15:0]
        imm26.next = imem_dout[25:0]
        dmem_addr.next = aluout
        dmem_din.next = busb
        imem_addr.next = pc
        dmem_wren.next = memwr
        dmem_be.next = 15 if memwr == 1 else 0

    imm32 = Signal(intbv(0)[32:])

    @always_seq(clk.posedge, rst)
    def pc():
        if rst:
            pc.next = 0
        else:
            pc.next = pc + 4
            if opcode == instructions.INSTR_BEQ_OP and compare == 1:
                pc.next = pc + 4 + imm32
            if opcode == instructions.INSTR_J_OP:
                pc.next = ConcatSignal(pc[31:28], imm26, Signal(intbv(0)[1:]))

    @always_comb
    def extender():
        imm32.next = ConcatSignal(Signal(intbv(1)[16:] if imm16[15] else intbv(0)[16:]), imm16)
        if opcode == instructions.INSTR_ORI_OP:
            imm32.next = ConcatSignal(Signal(intbv(0)[16:]), imm16)

    alusrc = Signal(intbv(0)[0])
    regdst = Signal(intbv(0)[0])
    memtoreg = Signal(intbv(0)[0])

    @always_comb
    def muxs():
        alu_b.next = imm32 if alusrc else busb
        rw.next = rd if regdst else rt
        busw.next = dmem_dout if memtoreg else aluout

    extop = Signal(intbv(0)[2:])

    @always_comb
    def control():
        regwr.next, regdst.next, extop.next, alusrc.next, aluctr.next, memwr.next, memtoreg.next = Signal(
            intbv(1)[1:]), Signal(intbv(1)[1:]), encode.EXT_ZERO, Signal(intbv(0)[1:]), encode.ALUOp_ADDU, Signal(
            intbv(0)[1:]), Signal(intbv(0)[1:])
        if opcode == instructions.INSTR_RTYPE_OP:
            if func == instructions.INSTR_ADDU_FUNCT:
                regwr.next, regdst.next, extop.next, alusrc.next, aluctr.next, memwr.next, memtoreg.next = Signal(
                    intbv(1)[1:]), Signal(intbv(1)[1:]), encode.EXT_ZERO, Signal(
                    intbv(0)[1:]), encode.ALUOp_ADDU, Signal(
                    intbv(0)[1:]), Signal(intbv(0)[1:])
            elif func == instructions.INSTR_SUBU_FUNCT:
                regwr.next, regdst.next, extop.next, alusrc.next, aluctr.next, memwr.next, memtoreg.next = Signal(
                    intbv(1)[1:]), Signal(intbv(1)[1:]), encode.EXT_ZERO, Signal(
                    intbv(0)[1:]), encode.ALUOp_SUBU, Signal(
                    intbv(0)[1:]), Signal(intbv(0)[1:])
        elif opcode == instructions.INSTR_ORI_OP:
            regwr.next, regdst.next, extop.next, alusrc.next, aluctr.next, memwr.next, memtoreg.next = Signal(
                intbv(1)[1:]), Signal(intbv(0)[1:]), encode.EXT_ZERO, Signal(intbv(1)[1:]), encode.ALUOp_OR, Signal(
                intbv(0)[1:]), Signal(intbv(0)[1:])
        elif opcode == instructions.INSTR_LW_OP:
            regwr.next, regdst.next, extop.next, alusrc.next, aluctr.next, memwr.next, memtoreg.next = Signal(
                intbv(1)[1:]), Signal(intbv(0)[1:]), encode.EXT_ZERO, Signal(intbv(1)[1:]), encode.ALUOp_ADDU, Signal(
                intbv(0)[1:]), Signal(intbv(1)[1:])
        elif opcode == instructions.INSTR_SW_OP:
            regwr.next, regdst.next, extop.next, alusrc.next, aluctr.next, memwr.next, memtoreg.next = Signal(
                intbv(0)[1:]), Signal(intbv(0)[1:]), encode.EXT_ZERO, Signal(intbv(1)[1:]), encode.ALUOp_ADDU, Signal(
                intbv(1)[1:]), Signal(intbv(0)[1:])
        elif opcode == instructions.INSTR_BEQ_OP:
            regwr.next, regdst.next, extop.next, alusrc.next, aluctr.next, memwr.next, memtoreg.next = Signal(
                intbv(0)[1:]), Signal(intbv(0)[1:]), encode.EXT_ZERO, Signal(intbv(1)[1:]), encode.ALUOp_EQL, Signal(
                intbv(0)[1:]), Signal(intbv(0)[1:])
        elif opcode == instructions.INSTR_J_OP:
            regwr.next, regdst.next, extop.next, alusrc.next, aluctr.next, memwr.next, memtoreg.next = Signal(
                intbv(0)[1:]), Signal(intbv(0)[1:]), encode.EXT_ZERO, Signal(intbv(0)[1:]), encode.ALUOp_NOP, Signal(
                intbv(0)[1:]), Signal(intbv(0)[1:])

    return instances()
