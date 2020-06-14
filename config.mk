MBC ?= ../../compiler/mbc
MBC_OPTS = --no_prelude --lib lib:../lib/mod.mb --target asm
LIB_FILES = $(shell find ../lib -iname \*.mb) $(shell find ../lib -iname \*.ma)
