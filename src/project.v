`default_nettype none

module tt_um_half_adder (
    input  wire [7:0] ui_in,
    output wire [7:0] uo_out,
    input  wire [7:0] uio_in,
    output wire [7:0] uio_out,
    output wire [7:0] uio_oe,
    input  wire       ena,
    input  wire       clk,
    input  wire       rst_n
);

    // Half Adder
    // ui_in[0] = A
    // ui_in[1] = B
    // uo_out[0] = SUM
    // uo_out[1] = CARRY

    assign uo_out[0] = ui_in[0] ^ ui_in[1];
    assign uo_out[1] = ui_in[0] & ui_in[1];

    // Unused outputs
    assign uo_out[7:2] = 6'b000000;

    // Bidirectional pins not used
    assign uio_out = 8'b00000000;
    assign uio_oe  = 8'b00000000;

    // Unused inputs
    wire _unused = &{ena, clk, rst_n, uio_in};

endmodule
