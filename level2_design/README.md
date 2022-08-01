# Bitmanipulation Coprocessor Design Verification

The verification environment is set up using [Vyoma's UpTickPro](https://vyomasystems.com) provided for the hackathon.

*Make sure to include the Gitpod id in the screenshot*
![Homepage](https://user-images.githubusercontent.com/84724429/181875766-d7eb2fb8-7533-4c73-8611-de5b3f0a7e28.jpg)
## Verification Environment

The [CoCoTb](https://www.cocotb.org/) based Python test is developed as explained. The test drives inputs to the Design Under Test (Bitmanipulation Coprocessor), which takes in 32-bits input 4 inputs out of which one is instruction based on which operation is performed on other 3 inputs, clock, and gives 33-bit Output *mav_putvalue* and single bit *RDY_mav_putvalue* 

32-bit instruction input has 3 important parts that decide the operation to be performed that are func7(7 MSB [31:25]), func3(3 bit [17:19]), and opcode(7 LSB [6:0])
The assert statement compares the Output to the expected value.
The following error is seen:
```
 assert dut_output == expected_mav_putvalue, error_message
                     AssertionError: Value mismatch DUT = 0x4 does not match MODEL = 0x0
```
## Test Scenario 
### Test one
- func7 = 0000101
- Combination of func3 for which functions are defined with possible opcodes

### Test Two
#### Test Inputs: 
- func7 = 0100000
- Combination of func3 for which functions are defined with possible opcodes

### Test Three
#### Test Inputs: 
- func7 = 0010000
- Combination of func3 for which functions are defined with possible opcodes

### Test Four
#### Test Inputs: 
- func7 = 0110000
- Combination of func3 for which functions are defined with possible opcodes

### Test Five
#### Test Inputs: 
- func7 = 0100100
- Combination of func3 for which functions are defined with possible opcodes

### Test Six
#### Test Inputs: 
- func7 = 0010100
- Combination of func3 for which functions are defined with possible opcodes

### Test Seven
#### Test Inputs: 
- func7 = 0000101
- Combination of func3 for which functions are defined with possible opcodes

### Test Eight
#### Test Inputs: 
- func7 = 0110100
- Combination of func3 for which functions are defined with possible opcodes

For output verification, the provided python model of coprocessor is used, 
as the output mismatches for the above inputs hence design consist of bugs.

![fail_2](https://user-images.githubusercontent.com/84724429/182191209-3ea58ae5-5ebe-46e0-9191-1b2486225cd5.jpg)


## Design Bug
Based on the above test input and analyzing the design, we see the following.

- The function (in tesrt_2) corresponding to func_7 = 0100000, func3 = 111 and opcode = 0110011 doesn't works as expected.
- For the combinations of func7, func3, and operand for which the functions are not defined should give output value zero but the model gave non-zero output.
 
## Verification Strategy
- Randomized Testing is implemented for verification, and Testcases are taken in for all the func7 for which the functions are defined along with func3 corresponding value of func7, there was eight 7 bit values of func7 being used and hence 8 test cases are used.

- Two 7-bit values of the operand ([0110011, 0010011]) was used  in each test case for a specific func7 with all the func3 value corresponding to that func7 value, these two value of operands were taken along with all the possible combinations of remaining bits.

