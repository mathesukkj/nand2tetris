// R2 = R0 * R1
@R1
D=M

@n
M=D-1

@i
M=0

(LOOP)
@i
D=M
@n
D=D-M
@END
D;JGT

@R0
D=M

@R2
M=D+M

@i
M=M+1
@LOOP
0;JMP

(END)
@END
0;JMP