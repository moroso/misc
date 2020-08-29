LINUX_PROGS=coremb.linux coremb.ir.linux
OSOROM_PROGS=coremb.osorom

all: $(LINUX_PROGS) $(OSOROM_PROGS)

include ../config.mk

OPT=-O2
CONFIG=Makefile
EXTRA_MBC_OPTS=-l core_portme

GCC_VERSION=$(shell gcc -v 2>&1 | grep 'gcc version' | cut -f3 -d" ")

flags.c.mb: $(CONFIG)
	printf 'const COMPILER_VERSION: *u8 = "ccross, gcc %s";\n' $(GCC_VERSION) > $@
	printf 'const COMPILER_FLAGS: *u8 = "%s";\n' $(OPT) >> $@

flags.ir.mb: $(CONFIG)
	printf 'const COMPILER_VERSION: *u8 = "ircross, gcc %s";\n' $(GCC_VERSION) > $@
	printf 'const COMPILER_FLAGS: *u8 = "%s";\n' $(OPT) >> $@

coremb.c: coremb.mb flags.c.mb $(CONFIG)
	$(MBC) -d --target c -l core_portme:core_portme_linux.mb -l flags:flags.c.mb $< -o $@

coremb.ir.c: coremb.mb flags.ir.mb $(CONFIG)
	$(MBC) -d --target ir -l core_portme:core_portme_linux.mb -l flags:flags.ir.mb $< -o $@

coremb.osorom: coremb.mb $(CONFIG)
	$(MBC) -d --target asm -l core_portme:core_portme_osorom.mb $< -o $@

coremb.linux: coremb.c
	gcc -o $@ $(OPT) -g $<

coremb.ir.linux: coremb.ir.c
	gcc -m32 -o $@ $(OPT) -g $<

ALL_DEPS=$(LINUX_PROGS:%.linux=%.dep) $(OSOROM_PROGS:%.osorom=%.dep)
-include $(ALL_DEPS)
