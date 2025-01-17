.SILENT:

build:
	gcc -o ./bin/main ./src/main.c  ./src/utils.c

run: build
	./bin/main.exe $(word 2, $(MAKECMDGOALS))

%:
	@: