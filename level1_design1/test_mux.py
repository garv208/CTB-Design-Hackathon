# See LICENSE.vyoma for details

import cocotb
from cocotb.triggers import Timer
import random

#test for design 
@cocotb.test()
async def test_mux(dut):
    """Test for mux """
    #genrating random 3-bit inputs for input port of mux 
    for i in range(31):  #checking output for each possible value of selectionline 
            in0 = random.randint(0, 3)
            in1 = random.randint(0, 3)
            in2 = random.randint(0, 3)
            in3 = random.randint(0, 3)
            in4 = random.randint(0, 3)
            in5 = random.randint(0, 3)
            in6 = random.randint(0, 3)
            in7 = random.randint(0, 3)
            in8 = random.randint(0, 3)
            in9 = random.randint(0, 3)
            in10 = random.randint(0, 3)
            in11 = random.randint(0, 3)
            in12 = random.randint(0, 3)
            in13= random.randint(0, 3)
            in14= random.randint(0, 3)
            in15= random.randint(0, 3)
            in16= random.randint(0, 3)
            in17= random.randint(0, 3)
            in18 = random.randint(0, 3)
            in19 = random.randint(0, 3)
            in20 = random.randint(0, 3)
            in21 = random.randint(0, 3)
            in22 = random.randint(0, 3)
            in23 = random.randint(0, 3)
            in24 = random.randint(0, 3)
            in25 = random.randint(0, 3)
            in26 = random.randint(0, 3)
            in27 = random.randint(0, 3)
            in28 = random.randint(0, 3)
            in29 = random.randint(0, 3)
            in30 = random.randint(0, 3)

            input = [in0, in1, in2, in3, in4, in5, in6, in7, in8, 
            in9, in10, in11, in12, in13, in14, in15, in16, in17,
            in18, in19, in20, in21, in22, in23, in24, in25, in26,
            in27, in28, in29, in30]
            
            # mapping the value to the input ports
            dut.inp0.value = in0
            dut.inp1.value = in1
            dut.inp2.value = in2
            dut.inp3.value = in3
            dut.inp4.value = in4
            dut.inp5.value = in5
            dut.inp6.value = in6
            dut.inp7.value = in7
            dut.inp8.value = in8
            dut.inp9.value = in9
            dut.inp10.value = in10
            dut.inp11.value = in11
            dut.inp12.value = in12
            dut.inp13.value = in13
            dut.inp14.value = in14
            dut.inp15.value = in15
            dut.inp16.value = in16
            dut.inp17.value = in17
            dut.inp18.value = in18
            dut.inp19.value = in19
            dut.inp20.value = in20
            dut.inp21.value = in21
            dut.inp22.value = in22
            dut.inp23.value = in23
            dut.inp24.value = in24
            dut.inp25.value = in25
            dut.inp26.value = in26
            dut.inp27.value = in27
            dut.inp28.value = in28
            dut.inp29.value = in29
            dut.inp30.value = in30
            dut.sel.value = i

            await Timer(2, units='ns')
            dut._log.info(f'Selection={i} model={int(input[i])} DUT={int(dut.out.value)}')
            assert dut.out.value == input[i], f"Randomised test failed with: Selction {dut.sel.value},inputline {(bin(input[1])[2:])} and output {dut.out.value}"
