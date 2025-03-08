# Assembler-for-MIPS-using-python
It converts MIPS processor’s instructions into machine code. 

1. Objective
The primary objective of this project is to generate the machine code for a given set of MIPS assembly instructions. The assembler takes assembly language instructions and converts them into corresponding machine language instructions.

2. Reason
The main motivation for choosing this project is to understand the backend process that occurs when code is executed. It helps us gain insights into how an assembler works and how assembly language is translated into machine code, giving a better understanding of low-level programming.

3. Introduction and Theory
Assembler
An assembler reads a source file containing assembly language programs and additional information (such as assembler directives or debug statements) and generates the corresponding machine language program. It plays a crucial role in the MIPS processor's software development cycle. Programmers write instructions in assembly language, which the assembler converts into binary machine code, which the processor can understand and execute. The assembler performs various tasks including:

Lexical analysis
Syntax parsing
Code generation
4. Important Elements
Lexer: The lexer reads the assembly code input and extracts tokens (like literals, identifiers, and keywords). Python's regular expression module is used for efficient tokenization.

Parser: The parser checks the syntax of the assembly code according to the MIPS instruction set architecture. It analyzes the token stream produced by the lexer and builds a parse tree representing the structure of the program.

Symbol Table: The symbol table maps symbolic labels to the corresponding memory addresses. It resolves symbolic references and provides addresses for labels during assembly.

Code Generator: The code generator generates binary machine code for each instruction. It refers to the MIPS instruction encoding format and supports different instruction types, including:

R-type
I-type
J-type
5. Implementation Approach
Initialization
The code begins by importing the necessary libraries, including re for regular expressions and pandas for data manipulation.
MIPS registers, instructions, functions, and initial data are defined.
Parsing Input
The input MIPS assembly code is provided as a string variable (data).
The code splits the input into lines and removes any empty lines.
Instruction Type Functions
Functions are defined for handling different MIPS instruction types:

itype(): For immediate type instructions.
rtype(): For register type instructions.
jtype(): For jump type instructions.
branchtype(): For branch type instructions.
Processing Symbol and Data Tables
The code parses the input to identify symbols and data declarations.
Symbols are stored in the symbolfinal list, and data is stored in the datauser list.
Assembling Instructions
The assembler handles different types of instructions:

R-type: add, sub, and, or, xor, nor
I-type: lui, addi, andi, ori, xori
Branch-type: bltz, bne, beq
Jump-type: j, jr
Writing Output
The assembled machine code is written to an output file (demofile2.txt) in hexadecimal format.
Symbol Table Editing
The symbol table is updated based on the final addresses of symbols after assembling the instructions.
Output
The final symbol table is printed both before and after the assembly process for reference.
6. Features
Support for MIPS instruction set: The project supports various instruction types, including arithmetic, logical, branch, load-store, and control transfer instructions.

Symbolic Labels: It handles symbolic labels and resolves branch targets during the code generation process.

Error Handling: The assembler provides error handling and reporting for:

Syntax errors
Semantic errors
Invalid instructions
Optimization Techniques: The code includes optimization techniques to improve efficiency and reduce memory footprint.

Tracking Updates: The number of times a variable is updated or a label is used is also tracked during the assembly process.
