# CoreMb

Rewrite of the coremark benchmark in Mb.

Each supported platform needs a platform specific core_portme module
that will be provided on the mbc command line.

We provide `core_portme_linux` and `core_portme_osorom`, which runs on
bare-metal osorom.
(Maybe the linux one works on macOS but who gives a shit.)

`make` will build `coremb.linux`, `coremb.ir.linux`, `coremb.osorom`.

It goes without saying that this is *not* coremark and the scores
shouldn't be compared or treated as equivalent.
