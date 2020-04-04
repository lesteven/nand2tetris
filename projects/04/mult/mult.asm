// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Mult.asm

// Multiplies R0 and R1 and stores the result in R2.
// (R0, R1, R2 refer to RAM[0], RAM[1], and RAM[2], respectively.)

// Put your code here.
    @R0
    D=M
    @inc
    M=D // set RAM[inc] to R[0]

    @R1
    D=M
    @dec
    M=D // set RAM[dec] to R[1]


// reset R[2] to zero
    @0
    D=0
    @R2
    M=D

    @END // if R[1] is zero, set R[2] to 0, skip MULT and go to END
    @R1
    D=M
    D;JEQ

// multiplication loop
  (MULT)
    @inc
    D=M // grab increment value
    @R2
    D=D+M // add increment value to R[2] and store in D Reg
    M=D // set D reg value to R[2]
    
    @dec
    D=M 
    D=D-1 // get RAM[dec] value, store in D Reg and decrease by 1
    M=D // set RAM[dec] to D reg value

    @MULT // loop again if value is greater than 0
    D;JGT 

  (END)
    @END
    0;JMP
