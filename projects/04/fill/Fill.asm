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
  (LOOP)
    @color    
    M=0
    @24576 // keyboard input
    D=M

    @FILL
    D;JEQ
    @color
    M=-1
    
  (FILL)
    @8192 // 8192 words to fill (includes 0)
    D=A
    @num
    M=D

  (FILLLOOP)
    @SCREEN
    D=A

    @num // grab num and add to pointer
    D=D+M 

    @addr
    M=D
    
    @color
    D=M
    
    @addr
    A=M
    M=D // fill pointer w/ -1

    @num  // decrement num
    M=M-1 
    D=M

    @FILLLOOP
    D;JGE // end of FILL loop

    @LOOP
    0;JMP
