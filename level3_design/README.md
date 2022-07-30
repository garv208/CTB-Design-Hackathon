# Vending Machine Design Verification

The verification environment is set up using [Vyoma's UpTickPro](https://vyomasystems.com) provided for the hackathon.

*Make sure to include the Gitpod id in the screenshot*

![Homepage](https://user-images.githubusercontent.com/84724429/181875766-d7eb2fb8-7533-4c73-8611-de5b3f0a7e28.jpg)


## Verification Environment

The [CoCoTb](https://www.cocotb.org/) based Python test is developed as explained. The test drives inputs to the Design Under Test (Vending Machine), which takes in 3-bit in *Coin* along with reset signal and gives Output *vending* when it detects a sum of 25 cents and gives the remaining amount in Output *change*. Parameters are used for the allowed denominations nickel(001), dime (010), nickel_dime (011), dimes_2(100), a quarter (101)

The assert statement compares the Output to the expected value.
The following error is seen:
```
 assert dut.change.value == dime, f"Directed test failed with: input {dut.Coin.value}, expected output chamge {(bin(nickel)[2:]).zfill(3)}, output change {dut.change.value}.Didn't got expected output change"
                     AssertionError: Directed test failed with: input 010, expected output change 001, output change 000, and didn't get the expected output change
```
## Test Scenario 
### Test one
- Test Inputs: [nickel, quarter]
- Expected Output: vending = 1, change = nickel
- Observed Output in the DUT dut.vending.value = 1, dut.change.value = 001 (nickel)

### Test Two
- Test Inputs: [dime, nickel, reset = 1]
- Expected Output: vending = 0. change = nickel_dime (011)
- Observed Output in the DUT dut.vending.value = 0, dut.change.value = 0

### Test Three
- Test Inputs: [dime, nickel, quarter, dime]
- Expected Output: seq_seen = 0, change = dime(010)
- Observed Output in the DUT dut.vending.value = 0, dut.change.value = 0

Output mismatches for the above inputs in the 2nd and 3rd case; hence design consists of bugs.

![failed_3](https://user-images.githubusercontent.com/84724429/181875806-fb9e1f29-5860-4719-b8e3-ff0fd21113b6.jpg)


## Design Bug
Based on the above test input and analyzing the design, we see the following.

- When the machine is in a non-reset state (states of the machine when the reset signal is zero), and then we apply the reset signal machine enters an *idle* state, but it should also return the amount  that the machine has previously taken before going in *idle*, but it doesn't give any change 

- When the machine detects the required amount of 25 cents and enters the vending state, some denomination may be detected by the machine, and after vending state, when it goes into *idle* the amount seen in the vending state should be returned by *change* output, but the machine doesn't produce the expected change 
## Verification Strategy
Direct Testing is implemented for verification. Test cases are taken in such a way to test the output logic of *vending* and *change* in different situations. when the machine is in different state
