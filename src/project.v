`default_nettype none
`timescale 1ns / 1ps

module tt_um_example (
    input  wire [7:0] ui_in,
    output wire [7:0] uo_out,
    input  wire [7:0] uio_in,
    output wire [7:0] uio_out,
    output wire [7:0] uio_oe,
    input  wire ena,
    input  wire clk,
    input  wire rst_n
);

    // Half Adder
    // ui_in[0] = A
    // ui_in[1] = B
    //
    // uo_out[0] = SUM
    // uo_out[1] = CARRY

    assign uo_out[0] = ui_in[0] ^ ui_in[1];  // SUM
    assign uo_out[1] = ui_in[0] & ui_in[1];  // CARRY

    // Unused output pins
    assign uo_out[7:2] = 6'b000000;

    // Bidirectional pins unused
    assign uio_out = 8'b00000000;
    assign uio_oe  = 8'b00000000;

    // Prevent unused-input warnings
    wire _unused;
    assign _unused = ena & clk & rst_n & (|uio_in);

endmodule

`default_nettype wire
