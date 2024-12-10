This is a HackAssembler, designed to translate Hack assembly programs into executable Hack binary code
The source comes from Xxx.asm
The output is written in Xxx.hack
For this first version, it will assume that Xxx.asm is error-free

Phases:
1: Basic assembler, that translates assembly into binary without symbols
2: Assembler that can add labels to the symbol table
3: Assembler that can translate any assembly program
4: Assembler that can have error-validations