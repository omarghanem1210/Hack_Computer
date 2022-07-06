// Multiplies R0 and R1 and stores the result in R2.
// (R0, R1, R2 refer to RAM[0], RAM[1], and RAM[2], respectively.)
//
// This program only needs to handle arguments that satisfy
// R0 >= 0, R1 >= 0, and R0*R1 < 32768.

// Computes R0 * R1 which can be interpreted as (R0+R0+R0+....) R1 times which implies a loop

@i
M=1
@product
M=0

(LOOP)
// if i > R1 goto stop
@i
D=M
@R1
D=D-M
@STOP
D; JGT
//product = product + R0
@R0
D=M
@product
D=D+M
M=D
@i
M=M+1

@LOOP
0;JMP

(STOP)
//Stores R0*R1 in R2
@product
D=M
@R2
M=D

(END)
@END
0;JMP