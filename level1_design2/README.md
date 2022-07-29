# Sequence Detector Design Verification

The verification environment is set up using [Vyoma's UpTickPro](https://vyomasystems.com) provided for the hackathon.

*Make sure to include the Gitpod id in the screenshot*
![snap_gitpod](https://user-images.githubusercontent.com/84724429/181510175-e2c15e62-0d13-48c5-8bc6-54cdd5919dcb.jpg)

## Verification Environment

The [CoCoTb](https://www.cocotb.org/) based Python test is developed as explained. The test drives inputs to the Design Under Test (1011 sequence detector module here), which takes in 1-bit input, clock, and give Output *seq_seen* when sequence *1011*
is detected

The assert statement compares the Output to the expected value.
The following error is seen:
```
 assert dut.seq_seen.value == 1, f"Directed test failed with: input {dut.inp_bit.value} and output {dut.seq_seen.value}"
                     AssertionError: Directed test failed with: input 1 and output 0
```
## Test Scenario 
### Test one
- Test Inputs: [0, 1, 1, 0, 1, 1]
- Expected Output: seq_seen = 1
- Observed Output in the DUT dut.seq_seen.value = 1

### Test Two
- Test Inputs: [0, 1, 0, 1, 1, 0, 1, 1]
- Expected Output: seq_seen = 1
- Observed Output in the DUT dut.seq_seen.value = 0

### Test Three
- Test Inputs: [0, 1, 0, 1, 0, 1, 1]
- Expected Output: seq_seen = 1
- Observed Output in the DUT dut.seq_seen.value = 0

Output mismatches for the above inputs hence design consist of bugs.

![failed_2](https://user-images.githubusercontent.com/84724429/181591985-1bfabe91-9838-40a7-9c1c-aa641f84d034.jpg)


## Design Bug
Based on the above test input and analyzing the design, we see the following.
```
SEQ_1:
      begin
        if(inp_bit == 1)
          next_state = IDLE; ====> BUG
        else
          next_state = SEQ_10;
      end          
```
For the design, the logic should be ``next_state = SEQ_1;`` instead of ``next_state = IDLE;`` as in the design code.
- Second bug
```
SEQ_1011:
      begin
        next_state = IDLE;
      end         
```
For the design the logic should include ``next_state = SEQ_1;`` ``if(inp_bit == 1)``
 else ``next_state = SEQ_10;``

- Third bug
```
SEQ_101:
      begin
        if(inp_bit == 1)
          next_state = SEQ_1011;
        else
          next_state = IDLE; ====> BUG
      end       
```
For the design the logic should include ``next_state = SEQ_10;`` insteaded of  ``next_state = IDLE;``
## Design Fix

![fail](https://user-images.githubusercontent.com/84724429/181592618-6d8237b7-39c4-45cc-88c0-b0ad8b119807.jpg)

The updated design is checked in as seq_detect_1011_fix.v

## Verification Strategy
Direct Testing is implemented for verification, and Testcases are taken in which the sequence *1011* appear after the ever possible state in which the designed FSM can exist. 
