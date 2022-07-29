# See LICENSE.vyoma for details
# SPDX-License-Identifier: CC0-1.0

import cocotb
import random
from cocotb.decorators import coroutine
from cocotb.triggers import Timer, RisingEdge, FallingEdge
from cocotb.result import TestFailure
from cocotb.clock import Clock

# declaring parameters
nickel =1
dime = 2
nickel_dime = 3
dimes_2 = 4
quarter = 5

#Directed Test
@cocotb.test()
async def test_vend(dut):
    clock = Clock(dut.Clk, 2, units="ns")  # Create a 2ns period clock on port clk
    cocotb.start_soon(clock.start())       # Start the clock
 
    # reset
    await FallingEdge(dut.Clk)
    dut.Reset.value = 1
    dut.Coin.value = 0
    await FallingEdge(dut.Clk)  
    dut.Reset.value = 0
    dut.Coin.value = nickel 
    await FallingEdge(dut.Clk)
    dut._log.info(f'input={dut.Coin.value}  DUT = {(dut.vending.value)}')      
    dut.Coin.value = quarter 
    
    await FallingEdge(dut.Clk)
    
    dut._log.info(f'input={dut.Coin.value}  DUT = {(dut.vending.value)}')
    assert dut.vending.value == 1, f"Directed test failed with: input {dut.Coin.value} and output {dut.vending.value}"
    assert dut.change.value == nickel, f"Directed test failed with: input {dut.Coin.value} and output {dut.vending.value}"

#test for chaange return when Machine Reset at non-Reset state
@cocotb.test()
async def test_vend_2(dut):
    clock = Clock(dut.Clk, 2, units="ns")  # Create a 2ns period clock on port clk
    cocotb.start_soon(clock.start())       # Start the clock
    
    #reset
    await FallingEdge(dut.Clk)
    dut.Reset.value = 1
    dut.Coin.value = 0
    await FallingEdge(dut.Clk)  
    dut.Reset.value = 0
    dut.Coin.value = dime
    await FallingEdge(dut.Clk)
    dut._log.info(f'input Coin = {dut.Coin.value}  DUT = {(dut.vending.value)}')      
    dut.Coin.value = nickel 
    await FallingEdge(dut.Clk)
    dut._log.info(f'input Coin = {dut.Coin.value}  DUT = {(dut.vending.value)}')
    dut.Reset.value = 1
    dut.Coin.value = 0
    
    await FallingEdge(dut.Clk)
    dut._log.info(f'input Coin = {dut.Coin.value}  DUT = {(dut.vending.value)}')
    
    assert dut.change.value == nickel_dime,f"Directed test failed with: input {dut.Coin.value}, expected output chamge {(bin(nickel_dime)[2:]).zfill(3)}, output change {dut.change.value}.Didn't got expected output change"

# test for change returned when COin dected in vending state
@cocotb.test()
async def test_vend_3(dut):
    clock = Clock(dut.Clk, 2, units="ns")   # Create a 2ns period clock on port clk
    cocotb.start_soon(clock.start())        # Start the clock

    # reset
    await FallingEdge(dut.Clk)
    dut.Reset.value = 1
    dut.Coin.value = 0
    await FallingEdge(dut.Clk)  
    dut.Reset.value = 0
    dut.Coin.value = dime
    await FallingEdge(dut.Clk)
    dut._log.info(f'input Coin = {dut.Coin.value}  DUT = {(dut.vending.value)}')      
    dut.Coin.value = nickel 
    await FallingEdge(dut.Clk)
    dut._log.info(f'input Coin = {dut.Coin.value}  DUT = {(dut.vending.value)}')
    dut.Coin.value = quarter
    await FallingEdge(dut.Clk)
    dut.Coin.value = dime
    dut._log.info(f'input Coin = {dut.Coin.value}  DUT = {(dut.vending.value)}')
    assert dut.vending.value == 1, f"Directed test failed with: input {dut.Coin.value} and output {dut.vending.value}"
    assert dut.change.value == nickel_dime, f"Directed test failed with: input {dut.Coin.value} and output {dut.vending.value}"
   
    await FallingEdge(dut.Clk)
    dut._log.info(f'input Coin = {dut.Coin.value}  DUT = {(dut.vending.value)}')
    
    assert dut.change.value == dime, f"Directed test failed with: input {dut.Coin.value}, expected output chamge {(bin(nickel)[2:]).zfill(3)}, output change {dut.change.value}.Didn't got expected output change"
