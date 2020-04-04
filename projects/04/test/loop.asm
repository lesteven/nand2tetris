
    @R0
    D=M // set D reg to value at RAM[0]
  (LOOP)
    @LOOP
    D=D-1 // decrement by 1 until 0
    D;JGT
  (END)
    @END
    0;JMP
