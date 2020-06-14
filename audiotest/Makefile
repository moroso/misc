PROJECT=audiotest
# Place a file called $(AUDIOFILE).wav in this directory.
AUDIOFILE=audio

include ../config.mk

all: $(PROJECT).img

$(AUDIOFILE).wav:
	@echo "Place a sound file called $(AUDIOFILE).wav in this directory."
	@exit 1

%.raw: %.wav
	sox $< -b 16 -c 2 -L -e signed $@

$(PROJECT).img: $(PROJECT).bin $(AUDIOFILE).raw
	truncate $@ --size 0
	dd if=$(PROJECT).bin of=$@
	dd if=$(AUDIOFILE).raw of=$@ bs=512 seek=16

include ../common.mk
