# Bitmanipulation Coprocessor Design Verification

The verification environment is set up using [Vyoma's UpTickPro](https://vyomasystems.com) provided for the hackathon.

*Make sure to include the Gitpod id in the screenshot*
![Homepage](https://user-images.githubusercontent.com/84724429/181875766-d7eb2fb8-7533-4c73-8611-de5b3f0a7e28.jpg)
## Verification Environment

The [CoCoTb](https://www.cocotb.org/) based Python test is developed as explained. The test drives inputs to the Design Under Test (Bitmanipulation Coprocessor), which takes in 32-bits input 4 inputs out of which one is instruction based on which operation is performed on other 3 inputs, clock, and gives 33-bit Output *mav_putvalue* and single bit *RDY_mav_putvalue* 

32-bit instruction input has 3 important parts that decide the operation to be performed that are fun_7(7 MSB [31:25]), fun_3(3 bit [17:19]), and operand(7 LSB [6:0])
The assert statement compares the Output to the expected value.
The following error is seen:
```
 assert dut_output == expected_mav_putvalue, error_message
                     AssertionError: Value mismatch DUT = 0x4 does not match MODEL = 0x0
```
## Test Scenario 
### Test one
- func_7 = 0000101
- Combination of func_3 for which functions are defined with possible operands

### Test Two
#### Test Inputs: 
- func_7 = 0100000
- Combination of func_3 for which functions are defined with possible operands

### Test Three
#### Test Inputs: 
- func_7 = 0010000
- Combination of func_3 for which functions are defined with possible operands

### Test Four
#### Test Inputs: 
- func_7 = 0110000
- Combination of func_3 for which functions are defined with possible operands

### Test Five
#### Test Inputs: 
- func_7 = 0100100
- Combination of func_3 for which functions are defined with possible operands

### Test Six
#### Test Inputs: 
- func_7 = 0010100
- Combination of func_3 for which functions are defined with possible operands

### Test Seven
#### Test Inputs: 
- func_7 = 0000101
- Combination of func_3 for which functions are defined with possible operands

### Test Eight
#### Test Inputs: 
- func_7 = 0110100
- Combination of func_3 for which functions are defined with possible operands

For output verification, the provided python model of coprocessor is used, 
as the output mismatches for the above inputs hence design consist of bugs.

![fail_2](https://user-images.githubusercontent.com/84724429/182191209-3ea58ae5-5ebe-46e0-9191-1b2486225cd5.jpg)


## Design Bug
Based on the above test input and analyzing the design, we see the following.

- The function (in tesrt_2) corresponding to func_7 = 0100000, func = 111 and operand = 0110011 doesn't works as expected.
- For the combinations of func_7, func_3, and operand for which the functions are not defined should give output value zero but the model gave non-zero output.
 
## Verification Strategy
- Randomized Testing is implemented for verification, and Testcases are taken in for all the func_7 for which the functions are defined along with func_3 corresponding value of func_7, there were eight 7 bit value of func_7 being used and hence 8 test cases are used.

- Two 7-bit values of the operand ([0110011", 0010011]) was used  in each test case for a specific func_7 with all the func_3 value corresponding to that func_7 value, these two value of operands were taken along with all the possible combinations of remaining bits



