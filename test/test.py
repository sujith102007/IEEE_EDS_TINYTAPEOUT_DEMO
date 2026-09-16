# SPDX-FileCopyrightText: © 2024 Tiny Tapeout
# SPDX-License-Identifier: Apache-2.0

import cocotb
from cocotb.clock import Clock
from cocotb.triggers import ClockCycles


@cocotb.test()
async def test_project(dut):
    dut._log.info("Start")

    # Start clock
    clock = Clock(dut.clk, 10, unit="us")
    cocotb.start_soon(clock.start())

    # Reset
    dut._log.info("Reset")
    dut.ena.value = 1
    dut.ui_in.value = 0
    dut.uio_in.value = 0
    dut.rst_n.value = 0

    await ClockCycles(dut.clk, 2)
    dut.rst_n.value = 1

    dut._log.info("Testing Half Adder")

    # Test 00: A=0, B=0
    dut.ui_in.value = 0b00000000
    await ClockCycles(dut.clk, 1)

    # SUM = 0, CARRY = 0
    assert dut.uo_out.value & 0x03 == 0b00

    # Test 01: A=0, B=1
    dut.ui_in.value = 0b00000001
    await ClockCycles(dut.clk, 1)

    # SUM = 1, CARRY = 0
    assert dut.uo_out.value & 0x03 == 0b01

    # Test 10: A=1, B=0
    dut.ui_in.value = 0b00000010
    await ClockCycles(dut.clk, 1)

    # SUM = 1, CARRY = 0
    assert dut.uo_out.value & 0x03 == 0b01

    # Test 11: A=1, B=1
    dut.ui_in.value = 0b00000011
    await ClockCycles(dut.clk, 1)

    # SUM = 0, CARRY = 1
    assert dut.uo_out.value & 0x03 == 0b10

    dut._log.info("Half Adder test completed successfully!")
