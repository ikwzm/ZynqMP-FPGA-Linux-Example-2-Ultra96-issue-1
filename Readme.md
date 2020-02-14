ZynqMP-FPGA-Linux Example (2 issue-1) for Ultra96
=================================================

This repository is to reproduce the phenomenon that was problematic in issue-1 of https://github.com/ikwzm/ZynqMP-FPGA-Linux-Example-2-Ultra96.git
This repository is temporary and may be deleted after a period of publication.

# Requirement

 * Board: Ultra96 or Ultra96-V2
 * OS: ZynqMP-FPGA-Linux ([https://github.com/ikwzm/ZynqMP-FPGA-Linux](https://github.com/ikwzm/ZynqMP-FPGA-Linux)) v2019.1 or v2019.2

# Boot Ultra96 and login fpga user

fpga'password is "fpga".

```console
debian-fpga login: fpga
Password:
fpga@debian-fpga:~$
```

# Download this repository

## Download this repository for v2019.1.1

```console
fpga@debian-fpga:~$ mkdir examples
fpga@debian-fpga:~$ cd examples
fpga@debian-fpga:~/examples$ git clone https://github.com/ikwzm/ZynqMP-FPGA-Linux-Example-2-Ultra96-issue-1 negative
fpga@debian-fpga:~/examples$ cd negative
fpga@debian-fpga:~/examples/negative$ git checkout v2019.1.1
```

# Setup

```console
fpga@debian-fpga:~/examples/negative$ sudo rake install
./dtbocfg.rb --install negative --dts negative.dts
/tmp/dtovly20190813-3825-10ieu96: Warning (unit_address_vs_reg): /[ 5690.102944] fpga_manager fpga0: writing negative.bin to Xilinx ZynqMP FPGA Manager
fragment@2/__overlay__/negative-uio: node has a reg or ranges property, but no unit name
/tmp/dtovly20190813-3825-10ieu96: Warning (avoid_unnecessary_addr_size): /fragment@2: unnecessary #address-cells/#size-cells without "ranges" or child "reg" property
[ 5690.263531] fclkcfg amba_pl@0:fclk0: driver installed.
[ 5690.268718] fclkcfg amba_pl@0:fclk0: device name    : amba_pl@0:fclk0
[ 5690.275190] fclkcfg amba_pl@0:fclk0: clock  name    : pl0_ref
[ 5690.280938] fclkcfg amba_pl@0:fclk0: clock  rate    : 99999999
[ 5690.286790] fclkcfg amba_pl@0:fclk0: clock  enabled : 1
[ 5690.292015] fclkcfg amba_pl@0:fclk0: remove rate    : 1000000
[ 5690.297761] fclkcfg amba_pl@0:fclk0: remove enable  : 0
[ 5690.307330] udmabuf negative-udmabuf4: driver version = 1.4.2
[ 5690.313090] udmabuf negative-udmabuf4: major number   = 239
[ 5690.318668] udmabuf negative-udmabuf4: minor number   = 0
[ 5690.324063] udmabuf negative-udmabuf4: phys address   = 0x0000000070100000
[ 5690.330938] udmabuf negative-udmabuf4: buffer size    = 1048576
[ 5690.336855] udmabuf negative-udmabuf4: dma coherent   = 0
[ 5690.342247] udmabuf amba_pl@0:negative-udmabuf4: driver installed.
[ 5690.350256] udmabuf negative-udmabuf5: driver version = 1.4.2
[ 5690.356083] udmabuf negative-udmabuf5: major number   = 239
[ 5690.361659] udmabuf negative-udmabuf5: minor number   = 1
[ 5690.367060] udmabuf negative-udmabuf5: phys address   = 0x0000000070200000
[ 5690.373929] udmabuf negative-udmabuf5: buffer size    = 1048576
[ 5690.379849] udmabuf negative-udmabuf5: dma coherent   = 0
[ 5690.385248] udmabuf amba_pl@0:negative-udmabuf5: driver installed.
```

# Run negative.py

```console
fpga@debian-fpga:~/examples/negative$ sudo python3 negative.py
[  64591051 3172697395          0          0   76157580   46281898
 1342177280   48498273 3373798755 4290117632]
[0 0 0 0]
total:0.907[msec] setup:0.523[msec] xfer:0.026[msec] cleanup:0.359[msec]
throughput          :10275.810[MByte/sec]
[  64591051 3172697395          0          0   76157580   46281898
 1342177280   48498273 3373798755 4290117632]
[  64591051 3172697395   64591051 3172697395]
```

# Clean up

```console
fpga@debian-fpga:~/examples/negative$ sudo rake uninstall
./dtbocfg.rb --remove negative
[ 6020.769899] udmabuf amba_pl@0:negative-udmabuf5: driver removed.
[ 6020.776671] udmabuf amba_pl@0:negative-udmabuf4: driver removed.
[ 6020.784673] fclkcfg amba_pl@0:fclk0: driver unloaded
```

# Build Bitstream file

## Requirement

* Vivado 2019.1
* Vivado-HLS 2019.1

## Download this repository

```console
shell$ git clone https://github.com/ikwzm/ZynqMP-FPGA-Linux-Example-2-Ultra96-issue-1 
shell$ cd ZynqMP-FPGA-Linux-Example-2-Ultra96-issue-1
shell$ git checkout v2019.1.1
shell$ git submodule init
shell$ git submodule update
```
## Setup Vivado Board File for ultra96v1

This project requires ultra96v1 board file. If there is no ultra96v1 in the board file on Vivado, download it ad follows and install it on Vivado.

```console
shell$ git clone git://github.com/Avnet/bdf
shell$ cp -r bdf/ultra96v1 <Vivado Installed Directory/data/boads/board_files
```

## Run Vivado HLS

```console
vivado% cd hls
vivado% vivado_hls -f run_hls.tcl
```

## Create Vivado Project

```console
vivado% cd project
vivado% vivado -mode batch -source create_project.tcl
```

## Build Bitstream file

```console
vivado% cd project
vivado% vivado -mode batch -source implementation.tcl
vivado% cp project.runs/impl_1/design_1_wrapper.bit ../negative.bit
```

## Convert to Binary file from Bitstream file

```console
vivado% bootgen -image negative.bif -arch zynqmp -w -o negative.bin
```
