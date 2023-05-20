UNAME := $(shell uname)
SOURCE = b_dev.c

tfib:
ifeq ($(UNAME),Darwin)
	@echo "Macbook"
	gcc $(SOURCE) -I/opt/homebrew/include  -L/opt/homebrew/lib  -lgmp -o tfib
else
	@echo "?Linux?"
	gcc $(SOURCE) -g -lgmp -o tfib
endif
	
isprime:
	gcc isprime.c -lgmp -o isprime
