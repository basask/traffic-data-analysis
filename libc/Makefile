CC := gcc
CXX := g++
TARGET := traffic.so
ENTRYPOINT := traffic.cpp
CFLAGS := -shared -fPIC

# gcc -o hello.so -shared -fPIC hello.c

# %.so: %.c
# 	$(CC) -o $@ $(CFLAGS) $^

%.so: %.cpp
	$(CXX) -o $@ $(CFLAGS) $^

all: $(TARGET)
