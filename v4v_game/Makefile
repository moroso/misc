PROJECT=v4v
AUDIOFILE=audio
SPLASH_IMAGE=splash
GAMEOVER_IMAGE=gameover
EXTRA_MBC_OPTS=--list v4v.lst
include ../config.mk

all: $(PROJECT).img

$(AUDIOFILE).wav:
	@echo "Place a sound file called $(AUDIOFILE).wav in this directory."
	@exit 1

$(AUDIOFILE).raw: $(AUDIOFILE).wav
	sox $< -b 16 -c 2 -L -e signed $@

data.dat: $(SPLASH_IMAGE).raw $(GAMEOVER_IMAGE).raw $(AUDIOFILE).raw pack.py
	python3 pack.py $(SPLASH_IMAGE).raw $(GAMEOVER_IMAGE).raw $(AUDIOFILE).raw > $@

$(PROJECT).img: $(PROJECT).bin data.dat
	truncate $@ --size 0
	dd if=$(PROJECT).bin of=$@
	dd if=data.dat of=$@ bs=512 seek=64

include ../common.mk
