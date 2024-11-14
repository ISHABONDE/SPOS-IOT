import re

# Symbol table class to store labels and addresses
class Symbol:
    def __init__(self, name, address=None):
        self.name = name
        self.address = address

    def __str__(self):
        return f"{self.name}: {self.address}"

# Intermediate code class to hold the instruction and its address
class IntermediateCode:
    def __init__(self, label, opcode, operand, address=None):
        self.label = label
        self.opcode = opcode
        self.operand = operand
        self.address = address

    def __str__(self):
        return f"{self.label} {self.opcode} {self.operand} Address: {self.address if self.address else 'N/A'}"

# Pass-I: First pass - builds symbol table and intermediate code
def pass_1(assembly_code):
    symbol_table = {}
    intermediate_code = []
    address_counter = 100  # Starting address for instructions
    
    for line in assembly_code:
        # Remove comments
        line = re.sub(r";.*", "", line).strip()

        if not line:
            continue  # Skip empty lines

        # Parse label, opcode, and operand
        parts = line.split()
        label = None
        opcode = None
        operand = None
        
        # Check for label
        if ":" in parts[0]:
            label = parts[0][:-1]
            parts = parts[1:]
        
        if len(parts) > 0:
            opcode = parts[0]
        if len(parts) > 1:
            operand = parts[1]

        # Add label to the symbol table if it's not already present
        if label and label not in symbol_table:
            symbol_table[label] = Symbol(label)

        # Create intermediate code with no address yet
        intermediate_code.append(IntermediateCode(label, opcode, operand))
        
        # Update address counter after each instruction
        address_counter += 1

    return symbol_table, intermediate_code
def pass_2(symbol_table, intermediate_code):
    machine_code = []

    for ic in intermediate_code:
        # Ensure ic.address is set correctly, or use a default value (e.g., 0)
        address_str = f"{ic.address:04}" if ic.address is not None else "0000"
        
        # Handle the case where ic.operand might be None
        operand_str = ic.operand if ic.operand else ""
        
        # Append the machine code line to the list
        machine_code.append(f"{address_str} {ic.opcode} {operand_str}")

    # Print the final machine code
    print("\nPass-II Output (Machine Code):")
    for code in machine_code:
        print(code)

    return machine_code



# Main program
def main():
    # Sample assembly code (label, opcode, operand)
    assembly_code = [
        "START: MOV A, B",
        "ADD A, C",
        "SUB B, A",
        "MUL A, D",
        "END: NOP"
    ]
    
    # Pass-I: Build symbol table and intermediate code
    symbol_table, intermediate_code = pass_1(assembly_code)
    
    # Output symbol table and intermediate code (Pass-I output)
    print("Pass-I Output:")
    print("Symbol Table:")
    for symbol in symbol_table.values():
        print(symbol)
    
    print("\nIntermediate Code:")
    for ic in intermediate_code:
        print(ic)

    # Pass-II: Resolve addresses and generate machine code
    machine_code = pass_2(symbol_table, intermediate_code)
    
    # Output machine code (Pass-II output)
    print("\nPass-II Output:")
    for code in machine_code:
        print(code)

if __name__ == "__main__":
    main()
