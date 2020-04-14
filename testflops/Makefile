CC = gcc 

all: mm.1 mm.2 mm.3 mm.4 mm.all mm.5 padding \
  padding.1 padding_pack

mm.1 : mm.1.c 
	$(CC) -O0 -o $@ $<

mm.2 : mm.2.c
	$(CC) -O0 -o $@ $<

mm.3 : mm.3.c
	$(CC) -O0 -o $@ $<

mm.4 : mm.4.c
	$(CC) -O0 -o $@ $<

mm.all : mm.all.c
	$(CC) -O0 -o $@ $<

# il compilatore

mm.5 : mm.5.c
	$(CC) -O3 -mtune=core2 -o $@ $<

padding : padding.c
	$(CC) -O0 -o $@ $<

padding.1 : padding.1.c
	$(CC) -O0 -o $@ $<

padding_pack : padding_pack.c
	$(CC) -O0 -o $@ $<

clean:
	rm -f mm.1 mm.2 mm.3 mm.4 mm.5 mm.all padding padding.1 padding_pack
