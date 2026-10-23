def logic_gate(gate, a, b=None):
    if gate == "AND":
        return a & b
    elif gate == "OR":
        return a | b
    elif gate == "NOT":
        return 1 - a
    elif gate == "NAND":
        return 1 - (a & b)
    elif gate == "NOR":
        return 1 - (a | b)
    elif gate == "XOR":
        return a ^ b
    elif gate == "XNOR":
        return 1 - (a ^ b)


print("DIGITAL LOGIC GATE SIMULATOR")
print("AND, OR, NOT, NAND, NOR, XOR, XNOR")

gate = input("Enter gate name: ").upper()
a = int(input("Enter first input (0 or 1): "))

if gate == "NOT":
    result = logic_gate(gate, a)
else:
    b = int(input("Enter second input (0 or 1): "))
    result = logic_gate(gate, a, b)

print("Output:", result)
