#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2024/10/24 14:33
# @Author  : 兵
# @email    : 1747193328@qq.com
import argparse
import logging
import os

import sys
from email.policy import default

sys.path.append('../../')
from NepTrain.core import *
from NepTrain import utils, __version__
import warnings
def check_kpoints_number(value):
    """检查值是否为单个数字或三个数字的字符串"""

    if isinstance(value, str):
        values = value.split(',')

        if len(values) == 3 and all(v.isdigit() for v in values):
            return list(map(int, values))
        elif len(values) == 1 and value.isdigit():
            return [int(value),int(value),int(value)]
        else:
            raise argparse.ArgumentTypeError("参数必须是一个数字或三个用逗号分隔的数字。")
    elif isinstance(value, int):
        return value
    else:
        raise argparse.ArgumentTypeError("参数必须是一个数字或三个用逗号分隔的数字。")

def build_init(subparsers):
    parser_init = subparsers.add_parser(
        "init",
        help="初始化一些文件模板",
    )

    parser_init.add_argument("--queue", "-q",

                             nargs=1,
                             choices=["slurm", "local"],
                             default="local",
                             help="指定下排队方式")
    parser_init.add_argument("-f", "--force", action='store_true',
                             default=False,
                             help="强制覆盖生成模板"
                             )

    parser_init.set_defaults(func=init_template)


def build_perturb(subparsers):
    parser_perturb = subparsers.add_parser(
        "perturb",
        help="生成微扰结构",
    )

    parser_perturb.set_defaults(func=run_perturb)

    parser_perturb.add_argument("model_path",
                             type=str,

                             help="需要计算的结构路径或者结构文件，只支持xyz和vasp格式的文件")
    parser_perturb.add_argument("--num","-n",
                             type=int,
                                default=20,
                             help="每个结构微扰的数量，如果传入一个文件夹，最终生成的数量应该是结构数*num")

    parser_perturb.add_argument("--cell", "-c",
                                dest="cell_pert_fraction",
                                type=float,
                                default=0.03,
                                help="形变比例，比如0.03")
    parser_perturb.add_argument("--rattle_std", "-l",
                                dest="rattle_std",
                                type=float,
                                default=0.06,
                                help="这个是mc的参数，具体说明可参考hiphive。比如0.06")
    parser_perturb.add_argument("--distance", "-d",
                                type=float,
                                dest="min_distance",
                                default=0.1,
                                help="最小原子距离，单位埃")

    parser_perturb.add_argument("--out", "-o",
                             dest="out_file_path",
                             type=str,
                             help="微扰结构的输出文件",
                             default="./perturb.xyz"
                             )
    parser_perturb.add_argument("--append", "-a",
                             dest="append", action='store_true', default=False,
                             help="是否以追加形式写入out_file_path。",

                             )

def build_vasp(subparsers):
    parser_vasp = subparsers.add_parser(
        "vasp",
        help="使用vasp计算单点能",
    )
    parser_vasp.set_defaults(func=run_vasp)

    parser_vasp.add_argument("model_path",
                             type=str,

                             help="需要计算的结构路径或者结构文件，只支持xyz和vasp格式的文件")
    parser_vasp.add_argument("--directory", "-dir",

                             type=str,
                             help="设置VASP计算路径",
                             default="./cache/vasp"
                             )

    parser_vasp.add_argument("--out", "-o",
                             dest="out_file_path",
                             type=str,
                             help="计算结束后的输出文件",
                             default="./vasp_scf.xyz"
                             )

    parser_vasp.add_argument("--append", "-a",
                             dest="append", action='store_true', default=False,
                             help="是否以追加形式写入out_file_path。",

                             )
    parser_vasp.add_argument("--gamma", "-g",
                             dest="use_gamma", action='store_true', default=False,
                             help="默认使用Monkhorst-Pack的k点，设置-g使用Gamma的K点形式。",

                             )
    parser_vasp.add_argument("-n", "-np",
                             dest="n_cpu",
                             default=1,
                             type=int,
                             help="设置CPU核数。")

    parser_vasp.add_argument("--incar",

                             help="直接指定INCAR文件，全局使用这个模板")
    k_group = parser_vasp.add_mutually_exclusive_group(required=False)
    k_group.add_argument("--kspacing", "-kspacing",

                         type=float,
                         help="设置kspacing，将在INCAR中设置这个参数")
    k_group.add_argument("--kpoints", "-k",
                         default=[1, 1, 1],
                         type=check_kpoints_number,
                         help="KPOINTS传入1个或者3个数字（用,连接），将K点设置为（k[0]/a,k[1]/b,k[2]/c）")


def build_nep(subparsers):
    parser_nep = subparsers.add_parser(
        "nep",
        help="使用NEP训练势函数",
    )
    parser_nep.set_defaults(func=run_nep)


    parser_nep.add_argument("--directory", "-dir",

                             type=str,
                             help="设置NEP计算路径",
                             default="./cache/nep"
                             )
    parser_nep.add_argument("--in", "-in",
                            dest="nep_in_path",
                             type=str,
                             help="设置nep.in路径，默认是./nep.in,没有则根据train.xyz生成。",
                             default="./nep.in"
                             )

    parser_nep.add_argument("--train", "-train",
                             dest="train_path",

                             type=str,
                             help="设置train.xyz路径，默认是./train.xyz",
                             default="./train.xyz"
                             )
    parser_nep.add_argument("--test", "-test",
                             dest="test_path",

                             type=str,
                             help="设置test.xyz路径，默认是./test.xyz",
                             default="./test.xyz"
                             )
    parser_nep.add_argument("--nep", "-nep",
                            dest="nep_txt_path",
                             type=str,
                             help="开启预测模式需要势函数,默认是./nep.txt",
                             default="./nep.txt"
                             )
    parser_nep.add_argument("--prediction", "-pred","--pred",

                             action="store_true",
                             help="设置预测模式",
                             default=False
                             )


def main():
    parser = argparse.ArgumentParser(
        description="""
        NepTrain 是一个自动训练NEP势函数的工具""",

    )
    parser.add_argument(
        "-v", "--version", action="version", version=__version__
    )



    subparsers = parser.add_subparsers()


    build_init(subparsers)

    build_perturb(subparsers)
    build_vasp(subparsers)

    build_nep(subparsers)

    try:
        import argcomplete

        argcomplete.autocomplete(parser)
    except ImportError:

        pass


    args = parser.parse_args()

    try:
        _ = args.func
    except AttributeError as exc:
        parser.print_help()
        raise SystemExit("Please specify a command.") from exc
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())
