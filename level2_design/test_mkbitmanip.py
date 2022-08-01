# See LICENSE.iitm for details
# See LICENSE.vyoma for details

import random
import sys
import cocotb
from cocotb.decorators import coroutine
from cocotb.triggers import Timer, RisingEdge
from cocotb.result import TestFailure
from cocotb.clock import Clock
from model_mkbitmanip import *

from itertools import product
global ten
global five
#making possible combinations of remaining bits for 32 bit intruction.
ten = (list(product('10', repeat= 10)))
five = (list(product('10', repeat= 5)))


# function that converts tuple to string
def join_tuple_string(ten) -> str:
   return ''.join(ten)
def join_tuple_string(five) -> str:
   return ''.join(five)   

# joining all the tuples
result =list(map(join_tuple_string, ten))
result_2 = list(map(join_tuple_string, five))

# Clock Generation
@cocotb.coroutine
def clock_gen(signal):
    while True:
        signal.value <= 0
        yield Timer(1) 
        signal.value <= 1
        yield Timer(1) 

# Sample Test for possible combinations of input with 0000101 as MSB or func_7 bits
@cocotb.test()
def run_test_1(dut): # clock
    cocotb.fork(clock_gen(dut.CLK))
    fun_3 = [	"001", "011", "010", "100", "101", "110", "111"]
    op_code = ["0110011", "0010011"] #doesn't have 0010011 in fun_3
    Inputs = []
    for next_ten in result:
        for bits_remaing in result_2:
            for fun_3 in fun_3:
                for op in op_code:
                    IN = ("0000101" + next_ten + fun_3 + bits_remaing + op)
                    Inputs.append(IN)

    for inp in Inputs:
        dut.RST_N.value <= 0
        yield Timer(10)
        dut.RST_N.value <= 1
     
        mav_putvalue_src1 = random.randint(0, 8)
        mav_putvalue_src2 = random.randint(0, 8)
        mav_putvalue_src3 = random.randint(0, 8)
        mav_putvalue_instr = int(inp , 2)

        # expected output from the model
        expected_mav_putvalue = bitmanip(mav_putvalue_instr, mav_putvalue_src1, mav_putvalue_src2, mav_putvalue_src3)

        # driving the input transaction
        dut.mav_putvalue_src1.value = mav_putvalue_src1
        dut.mav_putvalue_src2.value = mav_putvalue_src2
        dut.mav_putvalue_src3.value = mav_putvalue_src3
        dut.EN_mav_putvalue.value = 1
        dut.mav_putvalue_instr.value = mav_putvalue_instr
  
        yield Timer(1) 

        # obtaining the output
        dut_output = dut.mav_putvalue.value

        cocotb.log.info(f'EXPECTED OUTPUT={hex(expected_mav_putvalue)}')
        cocotb.log.info(f'DUT OUTPUT={hex(dut_output)}')
        cocotb.log.info(f'putvalue_instr= {(dut.mav_putvalue_instr.value)}')
        
    
        # comparison
        error_message = f'Value mismatch DUT = {hex(dut_output)} does not match MODEL = {hex(expected_mav_putvalue)}'
        assert dut_output == expected_mav_putvalue, error_message
        
# Sample Test for possible combinations of input with 0100000 as MSB or func_7 bits
@cocotb.test()
async def run_test_2(dut):
    cocotb.fork(clock_gen(dut.CLK))
    fun_3 = ["111", "110", "100"]
    op_code = ["0110011", "0010011"] # 0010011 doesn't exist for any func_3
    Inputs_2 = []
    for next_ten in result:
        for fun_3 in fun_3:
            for bits_remaing in result_2:
                for op in op_code:
                    IN = ("0100000" + next_ten + fun_3 + bits_remaing + op)
                    Inputs_2.append(IN)
    
    for inp in Inputs_2:
        dut.RST_N.value <= 0
        await Timer(10)
        dut.RST_N.value <= 1
        mav_putvalue_src1 = random.randint(0, 8)
        mav_putvalue_src2 = random.randint(0, 8)
        mav_putvalue_src3 = random.randint(0, 8)
        mav_putvalue_instr = int(inp , 2)
        # expected output from the model
        expected_mav_putvalue = bitmanip(mav_putvalue_instr, mav_putvalue_src1, mav_putvalue_src2, mav_putvalue_src3)

        # driving the input transaction
        dut.mav_putvalue_src1.value = mav_putvalue_src1
        dut.mav_putvalue_src2.value = mav_putvalue_src2
        dut.mav_putvalue_src3.value = mav_putvalue_src3
        dut.EN_mav_putvalue.value = 1
        dut.mav_putvalue_instr.value = mav_putvalue_instr
  
        await Timer(1) 

        # obtaining the output
        dut_output = dut.mav_putvalue.value

        cocotb.log.info(f'EXPECTED OUTPUT={hex(expected_mav_putvalue)}')
        cocotb.log.info(f'DUT OUTPUT={hex(dut_output)}')
        cocotb.log.info(f'putvalue_instr= {(dut.mav_putvalue_instr.value)}')
        # comparison
        error_message = f'Value mismatch DUT = {hex(dut_output)} does not match MODEL = {hex(expected_mav_putvalue)}'
        assert dut_output == expected_mav_putvalue, error_message
        
# Sample Test for possible combinations of input with 0010000 as MSB or func_7 bits
@cocotb.test()
async def run_test_3(dut):
    cocotb.fork(clock_gen(dut.CLK))
    fun_3 = ["010", "100", "110", "001", "101"]
    op_code = ["0110011", "0010011"]
    Inputs_3 = []
    for next_ten in result:
        for bits_remaing in result_2:
            for fun_3 in fun_3:
                for op in op_code:
                    IN = ("0010000" + next_ten + fun_3 + bits_remaing + op)
                    Inputs_3.append(IN)
    
    for inp in Inputs_3:
        dut.RST_N.value <= 0
        await Timer(10)
        dut.RST_N.value <= 1
 
        mav_putvalue_src1 = random.randint(0, 8)
        mav_putvalue_src2 = random.randint(0, 8)
        mav_putvalue_src3 = random.randint(0, 8)
        mav_putvalue_instr = int(inp , 2)
        # expected output from the model
        expected_mav_putvalue = bitmanip(mav_putvalue_instr, mav_putvalue_src1, mav_putvalue_src2, mav_putvalue_src3)

        # driving the input transaction
        dut.mav_putvalue_src1.value = mav_putvalue_src1
        dut.mav_putvalue_src2.value = mav_putvalue_src2
        dut.mav_putvalue_src3.value = mav_putvalue_src3
        dut.EN_mav_putvalue.value = 1
        dut.mav_putvalue_instr.value = mav_putvalue_instr
  
        await Timer(1) 

        # obtaining the output
        dut_output = dut.mav_putvalue.value

        cocotb.log.info(f'EXPECTED OUTPUT={hex(expected_mav_putvalue)}')
        cocotb.log.info(f'DUT OUTPUT={hex(dut_output)}')
        cocotb.log.info(f'putvalue_instr= {(dut.mav_putvalue_instr.value)}')
        # comparison
        error_message = f'Value mismatch DUT = {hex(dut_output)} does not match MODEL = {hex(expected_mav_putvalue)}'
        assert dut_output == expected_mav_putvalue, error_message
        
# Sample Test for possible combinations of input with 0110000 as MSB or func_7 bits
@cocotb.test()
async def run_test_4(dut):
    cocotb.fork(clock_gen(dut.CLK))
    fun_3 = ["001", "101"] 
    op_code = ["0110011", "0010011"] #doesn't contain 001001
    Inputs_4 = []
    for next_ten in result:
        for bits_remaing in result_2:
            for fun_3 in fun_3:
                for op in op_code:
                    IN = ( "0110000"+ next_ten + fun_3 + bits_remaing + op)
                    Inputs_4.append(IN)
    
    for inp in Inputs_4:
        dut.RST_N.value <= 0
        await Timer(10)
        dut.RST_N.value <= 1
        ######### CTB : Modify the test to expose the bug #############
        #input transaction
        mav_putvalue_src1 = random.randint(0, 8)
        mav_putvalue_src2 = random.randint(0, 8)
        mav_putvalue_src3 = random.randint(0, 8)
        mav_putvalue_instr = int(inp , 2)
        # expected output from the model
        expected_mav_putvalue = bitmanip(mav_putvalue_instr, mav_putvalue_src1, mav_putvalue_src2, mav_putvalue_src3)

        # driving the input transaction
        dut.mav_putvalue_src1.value = mav_putvalue_src1
        dut.mav_putvalue_src2.value = mav_putvalue_src2
        dut.mav_putvalue_src3.value = mav_putvalue_src3
        dut.EN_mav_putvalue.value = 1
        dut.mav_putvalue_instr.value = mav_putvalue_instr
  
        await Timer(1) 

        # obtaining the output
        dut_output = dut.mav_putvalue.value

        cocotb.log.info(f'EXPECTED OUTPUT={hex(expected_mav_putvalue)}')
        cocotb.log.info(f'DUT OUTPUT={hex(dut_output)}')
        cocotb.log.info(f'putvalue_instr= {(dut.mav_putvalue_instr.value)}')
        # comparison
        error_message = f'Value mismatch DUT = {hex(dut_output)} does not match MODEL = {hex(expected_mav_putvalue)}'
        assert dut_output == expected_mav_putvalue, error_message
        
# Sample Test for possible combinations of input with 0100100 as MSB or func_7 bits
@cocotb.test()
async def run_test_5(dut):
    cocotb.fork(clock_gen(dut.CLK))
    fun_3 = ["001", "101", "110", "100", "111"] 
    op_code = ["0110011", "0010011"] #doesn't contain 001001 in some fun_3
    Inputs_5 = []
    for next_ten in result:
        for bits_remaing in result_2:
            for fun_3 in fun_3:
                for op in op_code:
                    IN = ( "0100100"+ next_ten + fun_3 + bits_remaing + op)
                    Inputs_5.append(IN)
    
    for inp in Inputs_5:
        dut.RST_N.value <= 0
        await Timer(10)
        dut.RST_N.value <= 1
       
        mav_putvalue_src1 = random.randint(0, 8)
        mav_putvalue_src2 = random.randint(0, 8)
        mav_putvalue_src3 = random.randint(0, 8)
        mav_putvalue_instr = int(inp , 2)
        # expected output from the model
        expected_mav_putvalue = bitmanip(mav_putvalue_instr, mav_putvalue_src1, mav_putvalue_src2, mav_putvalue_src3)

        # driving the input transaction
        dut.mav_putvalue_src1.value = mav_putvalue_src1
        dut.mav_putvalue_src2.value = mav_putvalue_src2
        dut.mav_putvalue_src3.value = mav_putvalue_src3
        dut.EN_mav_putvalue.value = 1
        dut.mav_putvalue_instr.value = mav_putvalue_instr
  
        await Timer(1) 

        # obtaining the output
        dut_output = dut.mav_putvalue.value

        cocotb.log.info(f'EXPECTED OUTPUT={hex(expected_mav_putvalue)}')
        cocotb.log.info(f'DUT OUTPUT={hex(dut_output)}')
        cocotb.log.info(f'putvalue_instr= {(dut.mav_putvalue_instr.value)}')
        # comparison
        error_message = f'Value mismatch DUT = {hex(dut_output)} does not match MODEL = {hex(expected_mav_putvalue)}'
        assert dut_output == expected_mav_putvalue, error_message
        
# Sample Test for possible combinations of input with 0010100 as MSB or func_7 bits
@cocotb.test()
async def run_test_6(dut):
    cocotb.fork(clock_gen(dut.CLK))
    fun_3 = ["001", "101"] 
    op_code = ["0110011", "001001"] #doesn't contain 001001 #pass without 001001
    Inputs_6 = []
    for next_ten in result:
        for bits_remaing in result_2:
            for fun_3 in fun_3:
                for op in op_code:
                    IN = ( "0010100"+ next_ten + fun_3 + bits_remaing + op)
                    Inputs_6.append(IN)
    
    for inp in Inputs_6:
        dut.RST_N.value <= 0
        await Timer(10)
        dut.RST_N.value <= 1
        ######### CTB : Modify the test to expose the bug #############
        #input transaction
        mav_putvalue_src1 = random.randint(0, 8)
        mav_putvalue_src2 = random.randint(0, 8)
        mav_putvalue_src3 = random.randint(0, 8)
        mav_putvalue_instr = int(inp , 2)
        # expected output from the model
        expected_mav_putvalue = bitmanip(mav_putvalue_instr, mav_putvalue_src1, mav_putvalue_src2, mav_putvalue_src3)

        # driving the input transaction
        dut.mav_putvalue_src1.value = mav_putvalue_src1
        dut.mav_putvalue_src2.value = mav_putvalue_src2
        dut.mav_putvalue_src3.value = mav_putvalue_src3
        dut.EN_mav_putvalue.value = 1
        dut.mav_putvalue_instr.value = mav_putvalue_instr
  
        await Timer(1) 

        # obtaining the output
        dut_output = dut.mav_putvalue.value

        cocotb.log.info(f'EXPECTED OUTPUT={hex(expected_mav_putvalue)}')
        cocotb.log.info(f'DUT OUTPUT={hex(dut_output)}')
        cocotb.log.info(f'putvalue_instr= {(dut.mav_putvalue_instr.value)}')
        # comparison
        error_message = f'Value mismatch DUT = {hex(dut_output)} does not match MODEL = {hex(expected_mav_putvalue)}'
        assert dut_output == expected_mav_putvalue, error_message
        
# Sample Test for possible combinations of input with 0110100 as MSB or func_7 bits
@cocotb.test() #some break issue
async def run_test_7(dut):
    cocotb.fork(clock_gen(dut.CLK))
    fun_3 = ["001", "101"] 
    op_code = ["0110011", "0010011"] #doesn't contain 001001 in all fun_3
    Inputs_7 = []
    for next_ten in result:
        for bits_remaing in result_2:
            for fun_3 in fun_3:
                for op in op_code:
                    IN = ( "0110100"+ next_ten + fun_3 + bits_remaing + op)
                    Inputs_7.append(IN)
    
    for inp in Inputs_7:
        dut.RST_N.value <= 0
        await Timer(10)
        dut.RST_N.value <= 1
        ######### CTB : Modify the test to expose the bug #############
        #input transaction
        mav_putvalue_src1 = random.randint(0, 8)
        mav_putvalue_src2 = random.randint(0, 8)
        mav_putvalue_src3 = random.randint(0, 8)
        mav_putvalue_instr = int(inp , 2)
        # expected output from the model
        expected_mav_putvalue = bitmanip(mav_putvalue_instr, mav_putvalue_src1, mav_putvalue_src2, mav_putvalue_src3)

        # driving the input transaction
        dut.mav_putvalue_src1.value = mav_putvalue_src1
        dut.mav_putvalue_src2.value = mav_putvalue_src2
        dut.mav_putvalue_src3.value = mav_putvalue_src3
        dut.EN_mav_putvalue.value = 1
        dut.mav_putvalue_instr.value = mav_putvalue_instr
  
        await Timer(1) 

        # obtaining the output
        dut_output = dut.mav_putvalue.value

        cocotb.log.info(f'EXPECTED OUTPUT={hex(expected_mav_putvalue)}')
        cocotb.log.info(f'DUT OUTPUT={hex(dut_output)}')
        cocotb.log.info(f'putvalue_instr= {(dut.mav_putvalue_instr.value)}')
        # comparison
        error_message = f'Value mismatch DUT = {hex(dut_output)} does not match MODEL = {hex(expected_mav_putvalue)}'
        assert dut_output == expected_mav_putvalue, error_message

# Sample Test for possible combinations of input with 0000100 as MSB or func_7 bits
@cocotb.test()
async def run_test_8(dut):
    cocotb.fork(clock_gen(dut.CLK))
    fun_3 = ["110", "100", "111", "001", "101"] 
    op_code = [ "0110011", "0010011"] #doesn't contain 001001 in some fun_3
    Inputs_7 = []
    for next_ten in result:
        for bits_remaing in result_2:
            for fun_3 in fun_3:
                for op in op_code:
                    IN = ( "0000100"+ next_ten + fun_3 + bits_remaing + op)
                    Inputs_7.append(IN)
    
    for inp in Inputs_7:
        dut.RST_N.value <= 0
        await Timer(10)
        dut.RST_N.value <= 1
        ######### CTB : Modify the test to expose the bug #############
        #input transaction
        mav_putvalue_src1 = random.randint(0, 8)
        mav_putvalue_src2 = random.randint(0, 8)
        mav_putvalue_src3 = random.randint(0, 8)
        mav_putvalue_instr = int(inp , 2)
        # expected output from the model
        expected_mav_putvalue = bitmanip(mav_putvalue_instr, mav_putvalue_src1, mav_putvalue_src2, mav_putvalue_src3)

        # driving the input transaction
        dut.mav_putvalue_src1.value = mav_putvalue_src1
        dut.mav_putvalue_src2.value = mav_putvalue_src2
        dut.mav_putvalue_src3.value = mav_putvalue_src3
        dut.EN_mav_putvalue.value = 1
        dut.mav_putvalue_instr.value = mav_putvalue_instr
  
        await Timer(1) 

        # obtaining the output
        dut_output = dut.mav_putvalue.value

        cocotb.log.info(f'EXPECTED OUTPUT={hex(expected_mav_putvalue)}')
        cocotb.log.info(f'DUT OUTPUT={hex(dut_output)}')
        cocotb.log.info(f'putvalue_instr= {(dut.mav_putvalue_instr.value)}')
        # comparison
        error_message = f'Value mismatch DUT = {hex(dut_output)} does not match MODEL = {hex(expected_mav_putvalue)}'
        assert dut_output == expected_mav_putvalue, error_message
