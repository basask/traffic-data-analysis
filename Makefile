CC := gcc
CXX := g++
SRC := ./src
TESTS := ./tests
LIB := ./lib
CFLAGS := -shared -fPIC

TARGET := $(LIB)/traffic.so
ENTRYPOINT := $(SRC)/traffic.cpp

all: build tests

build: $(TARGET)

tests: build
	python -m unittest discover -s $(TESTS) -p '*_test.py'

$(LIB)/%.so: $(SRC)/%.cpp
	$(CXX) -o $@ $(CFLAGS) $^

clean:
	@rm $(TARGET)
