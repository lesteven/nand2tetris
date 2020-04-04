
    @23
    D=A // set D reg to A value (23)
  (LOOP)
    @LOOP
    D=D-1 // decrement until 0
    D;JGT
  (END)
    @END
    0;JMP
