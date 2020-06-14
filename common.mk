$(PROJECT).bin: $(PROJECT).mb $(LIB_FILES)
	$(MBC) $(MBC_OPTS) $< -o $@
