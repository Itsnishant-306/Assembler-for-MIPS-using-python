# Assembler-for-MIPS-using-python
It converts MIPS processor’s instructions into machine code. 

##1. Objective:  
Assembler converts Assembly Language Instructions to Machine 
Language Program. So, our main objective is to generate the machine code for 
the given instructions. 
2. Reason:  
One of our main reasons to select this topic is because this helps us to 
understand how the processes takes place after running the code. It helps us to 
understand how the assembler works at the backend.  
3. Introduction and Theory:  
Assembler: 
It reads a source file containing assembly language program and accompanying 
information (assembler directives or certain bookkeeping details eg. debug 
statements) and in the process of producing the corresponding machine 
language program.  
An essential instrument in the MIPS processor software development cycle 
is the assembler. Programmers write instructions in assembly language, which 
is translated into binary machine code that the processor can comprehend and 
carry out. To accomplish this translation, the assembler carries out a number of 
operations including lexical analysis, syntax parsing, and code generation.  
4. Important Elements:   
Lexer: The lexer reads the assembly code input and extracts tokens, like 
literals, identifiers, and keywords. Python's regular expression feature is used 
to provide effective tokenization.   
Parser: The parser checks the assembly code's syntax in accordance with the 
MIPS instruction set architecture by analyzing the token stream produced by 
the lexer. It builds a parse tree that depicts the program's structure.   
Symbol Table: A mapping between symbolic labels and the memory addresses 
that correspond to them is maintained by the symbol table. It resolves symbolic 
references and gives labels encountered during assembly memory addressing.   
Code Generator: Using the MIPS instruction encoding format as a guide, the 
code generator iterates through the parse tree and creates the binary machine 
code for each instruction. It can handle R-type, I-type, and J-type instructions, 
among other instruction forms. 
