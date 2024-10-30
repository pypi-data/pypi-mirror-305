#!/usr/bin/env python3

# Copyright (C) 2023 Zero ASIC

import random
import numpy as np
from pathlib import Path
from argparse import ArgumentParser
from switchboard import SbDut, UmiTxRx, delete_queue, verilator_run
from siliconcompiler.package import path as sc_path
from umi import sumi


def build_testbench(topo="2d"):
    dut = SbDut('testbench', trace=False, default_main=False)

    # Set up inputs
    if topo == '2d':
        dut.input('utils/testbench/testbench_umi2tl_np.v', package='umi')
        print("### Running 2D topology ###")
    # elif topo=='3d':
    #     dut.input('testbench_3d.sv')
    #     dut.input('dut_ebrick_3d.v')
    #     print("### Running 3D topology ###")
    else:
        raise ValueError('Invalid topology')

    dut.input('utils/testbench/testbench_umi2tl_np.cc', package='umi')
    dut.input('utils/testbench/tlmemsim.cpp', package='umi')

    dut.use(sumi)

    # Verilator configuration
    dut.add('tool', 'verilator', 'task', 'compile', 'option', '--coverage')
    header_files_dir = Path(sc_path(dut, 'umi')) / 'utils' / 'testbench'
    dut.set('tool', 'verilator', 'task', 'compile', 'var', 'cflags', f'-I{header_files_dir}')
    dut.set('tool', 'verilator', 'task', 'compile', 'file', 'config', 'utils/testbench/config.vlt', package='umi')
    dut.add('tool', 'verilator', 'task', 'compile', 'option', '-Wall')

    # Settings - enable tracing
    dut.set('tool', 'verilator', 'task', 'compile', 'var', 'trace_type', 'fst')

    # Build simulator
    dut.run()

    return dut.find_result('vexe', step='compile')


def main(topo="2d", vldmode="2", n=100, client2rtl="client2rtl_0.q", rtl2client="rtl2client_0.q"):
    # clean up old queues if present
    delete_queue(client2rtl)
    delete_queue(rtl2client)

    verilator_bin = build_testbench(topo)

    # launch the simulation
    ret_val = verilator_run(verilator_bin, plusargs=['trace', ('valid_mode', vldmode)])

    # instantiate TX and RX queues.  note that these can be instantiated without
    # specifying a URI, in which case the URI can be specified later via the
    # "init" method

    umi = UmiTxRx(client2rtl, rtl2client)

    print("### Starting random test ###")

    n_sent = 0

    while (n_sent < n):
        print(f"Transaction {n_sent}:")
        addr = random.randrange(511)
        length = random.choice([1, 2, 4, 8])

        # FIXME: Align address. Limitation of umi2tl converter. Will be fixed in the next release
        addr = addr & (0xFFFFFFF8 | (8-length))

        data8 = np.random.randint(0, 255, size=length, dtype=np.uint8)
        print(f"umi writing {length} bytes:: data: {data8} to addr: 0x{addr:08x}")
        umi.write(addr, data8, srcaddr=0x0000110000000000)
        print(f"umi reading {length} bytes:: from addr 0x{addr:08x}")
        val8 = umi.read(addr, length, np.uint8, srcaddr=0x0000110000000000)
        print(f"umi Read: {val8}")
        if not (val8 == data8).all():
            print(f"ERROR core read from addr 0x{addr:08x} expected {data8} actual {val8}")
        assert (val8 == data8).all()
        n_sent = n_sent + 1

    ret_val.wait()


if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('--topo', default='2d')
    parser.add_argument('--vldmode', default='2')
    parser.add_argument('-n', type=int, default=10,
                        help='Number of transactions to send during the test.')
    args = parser.parse_args()

    main(topo=args.topo, vldmode=args.vldmode, n=args.n)
