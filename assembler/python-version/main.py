import sys
import parser
import os


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
    first_line = True
    for line in file:
      binary = parser.parse_line(line)
      if not first_line:
        output_file.write("\n")
      if binary != "":
        output_file.write(binary)
        first_line = False


if __name__ == "__main__":
  main()
