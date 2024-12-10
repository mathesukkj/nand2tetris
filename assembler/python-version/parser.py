import translator


def parse_line(line: str) -> str:
  instruction = handle_whitespace(line)
  if instruction == "":
    return ""

  return translator.translate_mnemonic_into_binary(instruction)


def handle_whitespace(line: str) -> str:
  line = line.strip()
  if line.startswith("//") or line.isspace():
    return ""

  splitted_line = line.split("//")
  return splitted_line[0]
