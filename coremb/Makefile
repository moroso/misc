LINUX_PROGS=coremb.linux coremb.ir.linux

all: $(LINUX_PROGS)

include ../config.mk

CONFIG=Makefile
EXTRA_MBC_OPTS=-l core_portme

coremb.c: coremb.mb $(CONFIG)
	$(MBC) -d --target c -l core_portme:core_portme_linux.mb $< -o $@

coremb.ir.c: coremb.mb $(CONFIG)
	$(MBC) -d --target ir -l core_portme:core_portme_linux.mb $< -o $@

coremb.linux: coremb.c
	gcc -o $@ -O2 -g $<

coremb.ir.linux: coremb.ir.c
	gcc -m32 -o $@ -O2 -g $<

ALL_DEPS=$(LINUX_PROGS:%.linux=%.dep)
-include $(ALL_DEPS)
