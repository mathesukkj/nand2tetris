#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

#include "../include/parser.h"
#include "../include/translator.h"
#include "../include/utils.h"

int main(int argc, char *argv[]) {
  if (argc < 1) {
    return logError("asm file not provided");
  }

  char *inputFilePath = argv[1];
  char *inputFileName = splitAndGetLastItem(inputFilePath, "/");
  char *outputFileName = getOutputFileName(inputFileName);
  if (access(outputFileName, F_OK) == 0) {
    if (remove(outputFileName) != 0) {
      return logError("couldnt remove preexisting output file");
    }
  }

  FILE *outputFile;
  outputFile = fopen(outputFileName, "w");
  if (outputFile == NULL) {
    return logError("couldnt open output file");
  }

  translateAsmFileIntoBinaryFile(inputFilePath, outputFile);

  return 0;
}

void translateAsmFileIntoBinaryFile(char *inputFilePath, FILE *outputFile) {
  FILE *inputFile;
  inputFile = fopen(inputFilePath, "r");
  mapLabels(inputFile);

  int lineNumber = 0;
  char line[256];
  while (fgets(line, sizeof(line), inputFile)) {
    char *binary = parseLine(line, lineNumber);
    if (binary == "") {
      continue;
    }
    if (lineNumber > 0) {
      fprintf(inputFile, "\n");
    }
    fprintf(inputFile, binary);
    lineNumber++;
  }
}

void mapLabels(FILE *file) {
  int lineNumber = 0;
  char line[256];
  while (fgets(line, sizeof(line), file)) {
    char *binary = parseLabel(line, lineNumber);
    if (binary != "") {
      lineNumber++;
    }
  }

  rewind(file);
}