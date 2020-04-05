// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Fill.asm

// Runs an infinite loop that listens to the keyboard input.
// When a key is pressed (any key), the program blackens the screen,
// i.e. writes "black" in every pixel;
// the screen should remain fully black as long as the key is pressed. 
// When no key is pressed, the program clears the screen, i.e. writes
// "white" in every pixel;
// the screen should remain fully clear as long as no key is pressed.

// Put your code here.
    //  @SCREEN
    // M=1
  (LOOP)
    @24576
    D=M

    @LOOP
    D;JEQ
    
  (FILL)
    @8191
    D=A
    @stop
    M=D

  (FILLLOOP)
    @SCREEN
    D=A

    @stop
    A=D+M
    M=-1

    @stop
    M=M-1 
    D=M

    @FILLLOOP
    D;JGE // end of FILL loop

    @LOOP
    0;JMP
