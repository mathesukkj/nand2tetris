symbol_to_address = {
    "R0": "0",
    "R1": "1",
    "R2": "2",
    "R3": "3",
    "R4": "4",
    "R5": "5",
    "R6": "6",
    "R7": "7",
    "R8": "8",
    "R9": "9",
    "R10": "10",
    "R11": "11",
    "R12": "12",
    "R13": "13",
    "R14": "14",
    "R15": "15",
    "SCREEN": "16384",
    "KBD": "24576",
    "SP": "0",
    "LCL": "1",
    "ARG": "2",
    "THIS": "3",
    "THAT": "4"
}

new_variable_addr = 16


def add(key: str, value: str):
  symbol_to_address[key] = value


def get(key: str) -> str | None:
  return symbol_to_address.get(key)


def create_variable(key: str) -> str:
  global new_variable_addr

  add(key, str(new_variable_addr))

  new_variable_addr += 1

  return symbol_to_address[key]
