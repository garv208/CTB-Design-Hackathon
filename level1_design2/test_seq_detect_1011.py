# See LICENSE.vyoma for details
# SPDX-License-Identifier: CC0-1.0

import os
import random
from pathlib import Path

import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge, FallingEdge
 

@cocotb.test()
async def test_seq_bug1(dut):
    """Test for seq detection """

    clock = Clock(dut.clk, 10, units="us")  # Create a 10us period clock on port clk
    cocotb.start_soon(clock.start())        # Start the clock

    # test when sequence appear after ist state 
    # reset
    await FallingEdge(dut.clk)
    dut.reset.value = 1
    dut.inp_bit.value = 0
    await FallingEdge(dut.clk)  
    dut.reset.value = 0
    dut.inp_bit.value = 1         # state1
    await FallingEdge(dut.clk)
    dut.inp_bit.value = 1         # state1
    await FallingEdge(dut.clk)
    dut.inp_bit.value = 0        
    await FallingEdge(dut.clk)
    dut.inp_bit.value = 1        
    await FallingEdge(dut.clk)
    dut.inp_bit.value = 1         # state4
    await FallingEdge(dut.clk)
    dut._log.info(f'input={dut.inp_bit.value}  DUT={int(dut.seq_seen.value)}')
    assert dut.seq_seen.value == 1, f"Directed test failed with: expected output {1} and output {dut.seq_seen.value}"
    
    #testing for overlapping
@cocotb.test()
async def test_seq_bug2(dut):

    clock = Clock(dut.clk, 10, units="us")  # Create a 10us period clock on port clk
    cocotb.start_soon(clock.start()) # Start the clock

    await FallingEdge(dut.clk)
    dut.reset.value = 1
    dut.inp_bit.value = 0
    await FallingEdge(dut.clk)  
    dut.reset.value = 0
    dut.inp_bit.value = 1        #state1
    await FallingEdge(dut.clk)
    dut.inp_bit.value = 0      
    await FallingEdge(dut.clk)
    dut.inp_bit.value = 1       
    await FallingEdge(dut.clk)
    dut.inp_bit.value = 1        #state4
    await FallingEdge(dut.clk)       
    dut.inp_bit.value = 0      
    await FallingEdge(dut.clk)
    dut.inp_bit.value = 1       
    await FallingEdge(dut.clk)
    dut.inp_bit.value = 1 
    await FallingEdge(dut.clk)       
    dut._log.info(f'input={dut.inp_bit.value}  DUT={int(dut.seq_seen.value)}')
    assert dut.seq_seen.value == 1, f"Directed test failed with: expected output {1} and output {dut.seq_seen.value}"
# test when sequence appear after 3rd state 
@cocotb.test()
async def test_seq_bug3(dut):
    clock = Clock(dut.clk, 10, units="us")  # Create a 10us period clock on port clk
    cocotb.start_soon(clock.start()) # Start the clock

    await FallingEdge(dut.clk)
    dut.reset.value = 1
    dut.inp_bit.value = 0
    await FallingEdge(dut.clk)  
    dut.reset.value = 0
    dut.inp_bit.value = 1        #state1
    await FallingEdge(dut.clk)
    dut.inp_bit.value = 0      
    await FallingEdge(dut.clk)
    dut.inp_bit.value = 1       
    await FallingEdge(dut.clk)
    dut.inp_bit.value = 0        
    await FallingEdge(dut.clk)       
    dut.inp_bit.value = 1    
    await FallingEdge(dut.clk)
    dut.inp_bit.value = 1        #state4
    await FallingEdge(dut.clk)      
    dut._log.info(f'input={dut.inp_bit.value}  DUT={int(dut.seq_seen.value)}')
    assert dut.seq_seen.value == 1, f"Directed test failed with: expected output {1} and output {dut.seq_seen.value}"
