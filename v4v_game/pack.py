import sys
import os
import struct

def write_char(c):
    sys.stdout.buffer.write(struct.pack("b", c))

def blocks(i):
    return ((i-1) // 512) + 1

def write_int(i):
    sys.stdout.buffer.write(struct.pack("<I", i))

def pad(length_so_far):
    remaining = (512 - (length_so_far % 512)) % 512
    for _ in range(remaining):
        write_char(0)

files = sys.argv[1:]

block_offs = 1 # the first block is the metadata block

for f in files:
    fsize = os.stat(f).st_size
    fblocks = blocks(fsize)
    write_int(block_offs)
    write_int(fsize)
    block_offs += fblocks
write_int(block_offs)
write_int(0)

pad(8 * (len(files) + 1))

for f in files:
    fh = open(f, "rb")
    sys.stdout.buffer.write(fh.read())
    pad(os.stat(f).st_size)
