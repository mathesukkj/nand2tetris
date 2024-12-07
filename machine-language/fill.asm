@KBD
D=A
@screenMemoryEnd
M=D-1

(LOOP)
@SCREEN
D=A
@i
M=D // restart for the loops

@KBD
D=M // get keyboard value
@BLACK
D;JGT // black if kbd pressed
@WHITE
D;JEQ // white if kbd not pressed

@LOOP
0;JMP // go back to the start of the loop

(BLACK)
@i
D=M
@screenMemoryEnd
D=D-M
@LOOP
D;JGT

@SCREEN
D=M
@i
A=D+M
M=-1

@i
M=M+1
@BLACK
0;JMP

(WHITE)
@i
D=M
@screenMemoryEnd
D=D-M
@LOOP
D;JGT

@SCREEN
D=M
@i
A=D+M
M=0

@i
M=M+1
@WHITE
0;JMP