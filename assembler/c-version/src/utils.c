#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char *splitAndGetLastItem(char *string, char *separator) {
  char *splitString = strtok(string, separator);
  char *lastItem = NULL;
  while (splitString != NULL) {
    lastItem = splitString;
    splitString = strtok(NULL, "/");
  }
  return lastItem;
}

char *getOutputFileName(char *inputFileName) {
  char *tmp = malloc(strlen(inputFileName) + 1);
  strcpy(tmp, inputFileName);
  char *baseName = strtok(tmp, ".");

  char *outputFileName = malloc(strlen(baseName) + strlen(".hack") + 1);
  strcpy(outputFileName, baseName);
  strcat(outputFileName, ".hack");

  free(tmp);
  return outputFileName;
}

int logError(char *message) {
  printf("error: %s\n", message);
  return 1;
}