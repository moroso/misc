# CoreMb

Rewrite of the coremark benchmark in Mb.

Each supported platform needs a platform specific core_portme module
that will be provided on the mbc command line.

Right now we only provide `core_portme_linux`, but it shouldn't be hard to
fix that and support osorom, both on bare metal and with an OS.
(And maybe the linux one works on macOS but who gives a shit.)

`make` will build `coremb.linux` and `coremb.ir.linux`.

It goes without saying that this is *not* coremark and the scores
shouldn't be compared or treated as equivalent.
