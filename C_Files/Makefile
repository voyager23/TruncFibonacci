UNAME := $(shell uname)

tfib:
ifeq ($(UNAME),Darwin)
	@echo "Macbook"
	gcc a_dev.c -I/opt/homebrew/include  -L/opt/homebrew/lib  -lgmp -o tfib
else
	@echo "?Linux?
	gcc a_dev.c -lgmp -o tfib
endif
	
isprime:
	gcc isprime.c -lgmp -o isprime
