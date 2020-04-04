// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Mult.asm

// Adds R0 and R1 and stores the result in R2.
// (R0, R1, R2 refer to RAM[0], RAM[1], and RAM[2], respectively.)

// Put your code here.
    @R0
    D=M // sets d register to value at RAM[0]

    @R1
    D=D+M // sets d register to D register current value + RAM[1] value

    @R2
    M=D // sets RAM[2] to d register value

    @R6
    0;JMP
