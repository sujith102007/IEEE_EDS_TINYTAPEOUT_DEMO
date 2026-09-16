# SPDX-FileCopyrightText: © 2024 Tiny Tapeout
# SPDX-License-Identifier: Apache-2.0

import cocotb
from cocotb.clock import Clock
from cocotb.triggers import ClockCycles


@cocotb.test()
async def test_project(dut):
    dut._log.info("Start")

    # Set the clock period to 10 us (100 KHz)
    clock = Clock(dut.clk, 10, unit="us")
    cocotb.start_soon(clock.start())

    # Reset
    dut._log.info("Reset")
    dut.ena.value = 1
    dut.ui_in.value = 0
    dut.uio_in.value = 0
    dut.rst_n.value = 0
    await ClockCycles(dut.clk, 10)
    dut.rst_n.value = 1

    dut._log.info("Testing Half Adder Logic")

    # Test Case 1: A=0, B=0 -> Sum=0, Carry=0 (uo_out = 00)
    dut.ui_in.value = 0b00
    await ClockCycles(dut.clk, 1)
    assert dut.uo_out.value == 0b00, f"Failed for 0+0: expected 0, got {dut.uo_out.value}"

    # Test Case 2: A=1, B=0 -> Sum=1, Carry=0 (uo_out = 01)
    dut.ui_in.value = 0b01
    await ClockCycles(dut.clk, 1)
    assert dut.uo_out.value == 0b01, f"Failed for 1+0: expected 1, got {dut.uo_out.value}"

    # Test Case 3: A=0, B=1 -> Sum=1, Carry=0 (uo_out = 01)
    dut.ui_in.value = 0b10
    await ClockCycles(dut.clk, 1)
    assert dut.uo_out.value == 0b01, f"Failed for 0+1: expected 1, got {dut.uo_out.value}"

    # Test Case 4: A=1, B=1 -> Sum=0, Carry=1 (uo_out = 10 -> Decimal 2)
    dut.ui_in.value = 0b11
    await ClockCycles(dut.clk, 1)
    assert dut.uo_out.value == 0b10, f"Failed for 1+1: expected 2, got {dut.uo_out.value}"
