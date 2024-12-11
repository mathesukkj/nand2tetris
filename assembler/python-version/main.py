import sys
import parser
import os
import symbol_table


def main():
  input_file_path = sys.argv[1]
  input_file_name = input_file_path.split("/")[-1]

  output_file_name = input_file_name.split(".")[0] + ".hack"
  if os.path.exists(output_file_name):
    os.remove(output_file_name)

  with open(output_file_name, "a") as output_file:
    translate_assembly_file_into_binary_file(input_file_path, output_file)


def translate_assembly_file_into_binary_file(file_path: str, output_file):
  with open(file_path) as file:
    map_labels(file)

    line_number = 0
    for line in file:
      binary = parser.parse_line(line, line_number)
      if binary != "":
        if line_number > 0:
          output_file.write("\n")
        output_file.write(binary)
        line_number += 1


def map_labels(file):
  line_number = 0
  for line in file:
    binary = parser.parse_label(line, line_number)
    if binary != "":
      line_number += 1

  file.seek(0)

if __name__ == "__main__":
  main()
