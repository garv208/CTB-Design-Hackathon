# Multiplexer Design Verification

The verification environment is set up using [Vyoma's UpTickPro](https://vyomasystems.com) provided for the hackathon.

*Make sure to include the Gitpod id in the screenshot*
![snap_gitpod](https://user-images.githubusercontent.com/84724429/181510175-e2c15e62-0d13-48c5-8bc6-54cdd5919dcb.jpg)
## Verification Environment

The [CoCoTb](https://www.cocotb.org/) based Python test is developed as explained. The test drives inputs to the Design Under Test (mux module here), which takes in 31 2-bits inputs, clock, and 5-bits selection line and gives 2-bits Output *out*. 

The assert statement compares the mux's Output to the expected value.
The following error is seen:
```
assert dut.out.value == input[i], f"Randomised test failed with: Selction {dut.sel.value} and corrsponding inputline {bin(input[1])[2:]} and output {dut.out.value}"
                      AssertionError: Randomised test failed with: Selection 01100,inputline 10 and output 00
```
## Test Scenario
- Test Inputs: sel = 12, in12 = 2
- Expected Output: out = 2
- Observed Output in the DUT dut. out = 0

Output mismatches for the above inputs proving that there is a design bug

## Design Bug
Based on the above test input and analyzing the design, we see the following.

```
 5'b01101: out = inp12; ====> BUG
 5'b01101: out = inp13;             
```
For the design, the logic should be ``5'b01100: out = inp12`` instead of ``5'b01101: out = inp12`` as in the design code.
Updating the design and re-running the test.

![fali_2](https://user-images.githubusercontent.com/84724429/181506783-f0f6ff93-3333-4233-aee3-e8796e96da02.jpg)

The design failed because of the absence of assigning of input port *inp30*  to ouput port with the slection logic ``5'b01111: out = inp30;``

## Design Fix
![Pass](https://user-images.githubusercontent.com/84724429/181507824-16b694fc-9026-4561-9719-84654f7ce07b.jpg)

The updated design is checked in as mux_fix.v

## Verification Strategy
Randomized Testing is implemented for verification, and random 3-bit values are assigned to the inputs (inp0 to inp30).
Then for different values of the selection line, the Output is checked.
