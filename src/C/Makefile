all: libremove_duplicates.so.1.0.1 libremove_duplicates.so.1

libremove_duplicates.so.1.0.1: remove_duplicates.c remove_duplicates.h
	gcc -Wall -c -fPIC -g remove_duplicates.c
	gcc -shared -Wl,-soname,libremove_duplicates.so.1 -o libremove_duplicates.so.1.0.1 remove_duplicates.o

libremove_duplicates.so.1: libremove_duplicates.so.1.0.1
	ln -s libremove_duplicates.so.1.0.1 libremove_duplicates.so.1

clean:
	rm -fr libremove_duplicates.so.1.0.1 libremove_duplicates.so.1 remove_duplicates.o *~ 
