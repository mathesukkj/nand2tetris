import symbol_table

comp_instructions = {
    "0": "0101010",
    "1": "0111111",
    "-1": "0111010",
    "D": "0001100",
    "A": "0110000",
    "!D": "0001101",
    "!A": "0110001",
    "-D": "0001111",
    "-A": "0110011",
    "D+1": "0011111",
    "A+1": "0110111",
    "D-1": "0001110",
    "A-1": "0110010",
    "D+A": "0000010",
    "D-A": "0010011",
    "A-D": "0000111",
    "D&A": "0000000",
    "D|A": "0010101",
    "M": "1110000",
    "!M": "1110001",
    "-M": "1110011",
    "M+1": "1110111",
    "M-1": "1110010",
    "D+M": "1000010",
    "D-M": "1010011",
    "M-D": "1000111",
    "D&M": "1000000",
    "D|M": "1010101",
}
dest_instructions = {
    "": "000",
    "M": "001",
    "D": "010",
    "MD": "011",
    "A": "100",
    "AM": "101",
    "AD": "110",
    "AMD": "111"
}
jump_instructions = {
    "": "000",
    "JGT": "001",
    "JEQ": "010",
    "JGE": "011",
    "JLT": "100",
    "JNE": "101",
    "JLE": "110",
    "JMP": "111"
}


def translate_mnemonic_into_binary(instruction: str) -> str:
  if instruction.startswith("@"):
    return handle_A_instruction(instruction)

  return handle_C_instruction(instruction)


def handle_A_instruction(instruction: str) -> str:
  address = instruction[1:]

  if not address.isnumeric():
    address = symbol_table.get(address) or symbol_table.create_variable(address)

  address = int(address)
  return f"0{bin(address)[2:].zfill(15)}"


def handle_C_instruction(instruction: str) -> str:
  binary = "111"
  parts = {"dest": "", "comp": "", "jump": ""}

  rest = instruction
  if "=" in instruction:
    parts["dest"], rest = instruction.split("=", 1)
  if ";" in rest:
    parts["comp"], parts["jump"] = rest.split(";", 1)
  else:
    parts["comp"] = rest

  binary = handle_comp(binary, parts["comp"])
  binary = handle_dest(binary, parts["dest"])
  binary = handle_jump(binary, parts["jump"])

  return binary


def handle_comp(binary: str, comp: str) -> str:
  return binary + comp_instructions[comp]


def handle_dest(binary: str, dest: str) -> str:
  return binary + dest_instructions[dest]


def handle_jump(binary: str, jump: str) -> str:
  return binary + jump_instructions[jump]
