import translator
import symbol_table


def parse_line(line: str, line_number: int) -> str:
  instruction = handle_whitespace(line)
  if instruction == "":
    return ""

  if "(" in instruction:
    handle_label(instruction, line_number)
    return ""

  return translator.translate_mnemonic_into_binary(instruction)


def handle_whitespace(line: str) -> str:
  line = line.strip()
  if line.startswith("//") or line.isspace():
    return ""

  splitted_line = line.split("//")
  return splitted_line[0]


def parse_label(line: str, line_number: int) -> str:
  instruction = handle_whitespace(line)
  if instruction == "":
    return ""

  if "(" in instruction:
    handle_label(instruction, line_number)
    return ""

  return "not-whitespace"


def handle_label(instruction: str, line_number: int):
  label = instruction.strip().replace("(", "").replace(")", "")
  symbol_table.add(label, str(line_number))
