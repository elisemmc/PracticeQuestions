CC=g++
CFLAGS=-I. -std=c++11 
ALL=hellomake euler1 euler2 euler3 euler4 euler5

all: $(ALL)

hellomake: hellomake.o hellofunc.o
	$(CC) -o hellomake hellomake.o hellofunc.o $(CFLAGS)

euler1: euler1main.o euler1func.o
	$(CC) -o euler1 euler1main.o euler1func.o $(CFLAGS)

euler2: euler2main.o euler2func.o
	$(CC) -o euler2 euler2main.o euler2func.o $(CFLAGS)

euler3: euler3main.o euler3func.o
	$(CC) -o euler3 euler3main.o euler3func.o $(CFLAGS)

euler4: euler4main.o euler4func.o
	$(CC) -o euler4 euler4main.o euler4func.o $(CFLAGS)

euler5: euler5main.o euler5func.o
	$(CC) -o euler5 euler5main.o euler5func.o $(CFLAGS)

clean:
	rm *.o $(ALL)