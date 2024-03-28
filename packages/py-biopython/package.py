# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyBiopython(PythonPackage):
    # BEGIN VERSIONS
    version("1.83", sha256="78e6bfb78de63034037afd35fe77cb6e0a9e5b62706becf78a7d922b16ed83f7", url="https://pypi.org/packages/cc/d4/3d8848191a7a37187704c382e6dfda4d6a47d05a14cd64f004c55a3cd5a1/biopython-1.83.tar.gz")
    version("1.82", sha256="a9b10d959ae88a9744a91c6ce3601f4c86e7ec41679bc93c29f679218f6167bb", url="https://pypi.org/packages/23/7d/55b8dc4a01bc951b3f6d60acd4eb4617aa22cc5a0d27037972f02e5d3844/biopython-1.82.tar.gz")
    version("1.81", sha256="2cf38112b6d8415ad39d6a611988cd11fb5f33eb09346666a87263beba9614e0", url="https://pypi.org/packages/ad/a4/237edd5f5e5b68d9543c79bcd695ef881e6317fbd0eae1b1e53e694f9d54/biopython-1.81.tar.gz")
    version("1.80", sha256="52805e9af88767e450e2df8113b5bc59e964e2e8a7bb803a83570bdbb51c0e43", url="https://pypi.org/packages/cb/8d/7cd217252797f7088847d667101b490df5644f0ff5202441e444b2b620ba/biopython-1.80.tar.gz")
    version("1.79", sha256="edb07eac99d3b8abd7ba56ff4bedec9263f76dfc3c3f450e7d2e2bcdecf8559b", url="https://pypi.org/packages/28/73/4d61169ce1f15c65ea49af89e534b2089375a44b608cb65062b58ff414de/biopython-1.79.tar.gz")
    version("1.78", sha256="1ee0a0b6c2376680fea6642d5080baa419fd73df104a62d58a8baf7a8bbe4564", url="https://pypi.org/packages/89/c5/7fe326081276f74a4073f6d6b13cfa7a04ba322a3ff1d84027f4773980b8/biopython-1.78.tar.gz")
    version("1.77", sha256="fb1936e9ca9e7af8de1050e84375f23328e04b801063edf0ad73733494d8ec42", url="https://pypi.org/packages/3d/2f/d9df24de05d651c5e686ee8fea3afe3985c03ef9ca02f4cc1e7ea10aa31e/biopython-1.77.tar.gz")
    version("1.76", sha256="3873cb98dad5e28d5e3f2215a012565345a398d3d2c4eebf7cd701757b828c72", url="https://pypi.org/packages/ff/f4/0ce39bebcbb0ff619426f2bbe86e60bc549ace318c5a9113ae480ab2adc7/biopython-1.76.tar.gz")
    version("1.75", sha256="5060e4ef29c2bc214749733634051be5b8d11686c6590fa155c3443dcaa89906", url="https://pypi.org/packages/33/55/becf2b99556588d22b542f3412990bfc79b674e198d9bc58f7bbc333439e/biopython-1.75.tar.gz")
    version("1.74", sha256="25152c1be2c9205bf80901fc49adf2c2efff49f0dddbcf6e6b2ce31dfa6590c0", url="https://pypi.org/packages/8c/ce/380b3ad1d6653bb7b31b51bb3d4fbe9cced3180fe168acfd9f4e932ab12c/biopython-1.74.tar.gz")
    version("1.73", sha256="70c5cc27dc61c23d18bb33b6d38d70edc4b926033aea3b7434737c731c94a5e0", url="https://pypi.org/packages/7a/4a/0d4381a60b6e942c6772b01cfb931196f1a9c33910cc43fbd4faccbd7d9f/biopython-1.73.tar.gz")
    version("1.70", sha256="4a7c5298f03d1a45523f32bae1fffcff323ea9dce007fb1241af092f5ab2e45b", url="https://pypi.org/packages/72/04/73a4bb22fed40eed26c7e1a673ab51778c577afc3d5dd6f1256424a62c35/biopython-1.70.tar.gz")
    version("1.65", sha256="6d591523ba4d07a505978f6e1d7fac57e335d6d62fb5b0bcb8c40bdde5c8998e", url="https://pypi.org/packages/4e/77/8590d61dcda439d83f378106954e748db1a71e565335168a966642133ef8/biopython-1.65.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-numpy", when="@1.82:")
    # END DEPENDENCIES

