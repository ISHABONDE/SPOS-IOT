# Data Structures for Pass-I
MNT = []  # Macro Name Table
MDT = []  # Macro Definition Table
intermediate_code = []  # Intermediate code without macro definitions
macro_definitions = {}  # To store macro definitions during Pass-I

# Data Structure to represent a macro entry
class MacroEntry:
    def __init__(self, macro_name, start_line, end_line):
        self.macro_name = macro_name
        self.start_line = start_line
        self.end_line = end_line

# Pass-I: Extract Macro Definitions and Generate Intermediate Code
def pass_1(source_code):
    global MNT, MDT, intermediate_code
    mnt_index = 0
    mdt_index = 0
    inside_macro = False
    macro_name = ""
    macro_lines = []
    for line in source_code:
        if line.startswith("MACRO"):
            # Starting a macro definition
            inside_macro = True
            macro_name = line.split()[1]
            macro_lines = []
        elif line.startswith("MEND"):
            # Ending a macro definition
            inside_macro = False
            MNT.append((macro_name, mnt_index))  # Add to MNT
            MDT.append(macro_lines)  # Add macro definition to MDT
            mnt_index += 1
        elif inside_macro:
            # Collecting macro definition lines
            macro_lines.append(line.strip())
        else:
            # Regular code (non-macro code)
            intermediate_code.append(line.strip())

    # Display the MNT and MDT
    print("Pass-I Output:")
    print("MNT (Macro Name Table):")
    for entry in MNT:
        print(entry)
    print("\nMDT (Macro Definition Table):")
    for entry in MDT:
        for line in entry:
            print(line)
    print("\nIntermediate Code (without macros):")
    for line in intermediate_code:
        print(line)

# Pass-II: Replace Macro Calls with Their Definitions
def pass_2():
    global intermediate_code
    output_code = []
    
    for line in intermediate_code:
        words = line.split()
        if words[0] in dict(MNT):  # If the first word is a macro name
            mnt_index = next(mnt[1] for mnt in MNT if mnt[0] == words[0])
            macro_definition = MDT[mnt_index]
            for macro_line in macro_definition:
                output_code.append(macro_line)
        else:
            # Regular code (not a macro call)
            output_code.append(line)
    
    # Display the final output after macro replacement
    print("\nPass-II Output (Final Code with Macro Expansions):")
    for line in output_code:
        print(line)

# Main function to simulate the two-pass assembler
def main():
    # Sample source code with macro definitions and macro calls
    source_code = [
        "MACRO A", 
        "MOV R1, #5", 
        "ADD R2, R1", 
        "MEND", 
        "MOV R0, #10", 
        "A", 
        "MOV R3, #20"
    ]
    
    # Pass-I: Generate MNT, MDT and Intermediate Code
    pass_1(source_code)
    
    # Pass-II: Replace macro calls with definitions
    pass_2()

# Run the program
if __name__ == "__main__":
    main()
