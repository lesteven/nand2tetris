// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Mult.asm

// Multiplies R0 and R1 and stores the result in R2.
// (R0, R1, R2 refer to RAM[0], RAM[1], and RAM[2], respectively.)

// Put your code here.

// reset R[2] to zero
    @R2
    M=0

    @R0
    D=M
    @END // if R[0] is zero, skip MULT and go to END
    D;JEQ

    @R1
    D=M
    @END // if R[1] is zero, skip MULT and go to END
    D;JEQ

// multiplication loop
  (MULT)
    @R0
    D=M // grab increment value
    @R2
    M=D+M // increment R[2] by value of R[0]
    
    @R1
    M=M-1 // decrement R[1] by 1
    D=M

    @MULT // loop again if value is greater than 0
    D;JGT 

  (END)
    @END
    0;JMP
