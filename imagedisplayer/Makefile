PROJECT=imagedisplayer
IMAGEFILE=image

include ../config.mk

all: $(PROJECT).img

$(IMAGEFILE).raw:
	@echo "Place a headerless, 640-pixel wide, RGB format image file called $(IMAGEFILE).raw in this directory."
	@exit 1

$(PROJECT).img: $(PROJECT).bin $(IMAGEFILE).raw
	truncate $@ --size 0
	dd if=$(PROJECT).bin of=$@
	dd if=$(IMAGEFILE).raw of=$@ bs=512 seek=100

include ../common.mk
