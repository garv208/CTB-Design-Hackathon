module Vending_Machine(Clk, Reset, Coin, vending, change 
    );
	 input Clk, Reset;
	 input [2:0]Coin;
	 
	 output reg vending;
	 output reg [2:0] change;
	 
	 // Declaring coins as paramters
	 parameter [2:0] nickel =3'b001;
	 parameter [2:0] dime = 3'b010;
	 parameter [2:0] nickel_dime = 3'b011;
	 parameter [2:0] dimes_2 = 3'b100;
	 parameter [2:0] quarter = 3'b101;
	 
	 // Declaring parameters for states
	 parameter [2:0] idle=3'b000;
	 parameter [2:0] FIVE=3'b001;
	 parameter [2:0] TEN=3'b010;
	 parameter [2:0] FIFTEEN=3'b011;
	 parameter [2:0] TWENTY=3'b100;
	 parameter [2:0] TWENTYFIVE=3'b101;
	 
	 reg [2:0]state,next_state;
	 
	 always@(posedge Clk) begin
	 if(Reset) begin
	 state <= idle;
	 vending <= 1'b0;
	 change <= 3'b000;
	 end
	 
	 else begin
	 case(state)
	 idle : begin
	 if(Coin == nickel) next_state = FIVE;
	 else if(Coin == dime) next_state = TEN;
	 else if(Coin == quarter)next_state = TWENTYFIVE;
	 else next_state = state;
	 //
	 change <=3'b0;
	 end
	 //
	 FIVE: begin
	 if(Coin == nickel) next_state = TEN;
	 else if(Coin == dime) next_state = FIFTEEN;
	 else if(Coin == quarter) next_state = TWENTYFIVE;
	 else next_state = state;
	 //
	 if (Coin == quarter) change <= nickel;
	 else change <=3'b0;
	 end
	 //
	 TEN: begin
	 if(Coin == nickel) next_state = FIFTEEN;
	 else if(Coin == dime) next_state = TWENTY;
	 else if(Coin == quarter) next_state = TWENTYFIVE;
	 else next_state = state;
	 //
	 if (Coin== quarter) change <= dime;
	 else change <= 3'b0;
	 end
	 //
	 FIFTEEN: begin
	 if(Coin == nickel) next_state = TWENTY;
	 else if(Coin == dime) next_state = TWENTYFIVE;
	 else if(Coin == quarter) next_state = TWENTYFIVE;
	 else next_state = state;
	 //
	 if (Coin== quarter) change <= nickel_dime;
	 else change <= 3'b0;
	 end
	 //
	 TWENTY: begin
	 if(Coin == nickel) next_state = TWENTYFIVE;
	 else if(Coin == dime) next_state = TWENTYFIVE;
	 else if(Coin == quarter) next_state = TWENTYFIVE;
	 else next_state = state;
	 //
	 if (Coin == dime) change <= nickel; 
	 else if (Coin == quarter) change <= dimes_2; 
	 else change <= 3'b0;
	 end
	 //
	 TWENTYFIVE: begin
	 next_state = idle;
	 change <=3'b0;
	 end
	 endcase
	 state = next_state;
	 end
	 end
	 // output logic 
	 always@(state) begin
	 if(state == TWENTYFIVE) vending <= 1'b1;
	 else vending <= 1'b0;
	 end 
endmodule

