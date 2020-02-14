open_project -reset negative
set_top negative
add_files     ../negative.cpp    -cflags "-std=c++0x"
add_files -tb ../negative_tb.cpp -cflags "-std=c++0x"

open_solution -reset "solution1"
set_part {xczu3eg-sfva625-1-e} -tool vivado
create_clock -period 10 -name default

# csim_design
csynth_design
# cosim_design
export_design -rtl verilog -format ip_catalog

exit
