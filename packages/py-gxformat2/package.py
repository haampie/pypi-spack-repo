##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyGxformat2(PythonPackage):
    version("0.18.0", sha256="c2df058a967a662bae624fc35ec08a25be62debfcc92a21f5adf62ab8b88b360", url="https://pypi.org/packages/a9/35/2634d4a64ff0073c0b40208d9c4596d4b980d619abd99e5181e4e7382af2/gxformat2-0.18.0-py2.py3-none-any.whl")
    version("0.17.0", sha256="bb1ffb69dafb6bb0c0584b48c72323a8e093ddc5d5a43557c359115fc9af86fb", url="https://pypi.org/packages/79/4e/e39dcb26d0423b67d0970098847b2cea4771c75a3eb99a5f23cc67f16235/gxformat2-0.17.0-py2.py3-none-any.whl")
    version("0.16.0", sha256="3501d7f0c2f75efb3a49e0805fd7597db691c2640bce2cdd71d8d263a2607793", url="https://pypi.org/packages/11/3d/88016d9ed55ce46cb89d3d2d14ef9f138ee6520a1d3faaba8c76d718fb6e/gxformat2-0.16.0-py2.py3-none-any.whl")
    version("0.15.0", sha256="e60997d25dc745408b1f4a453fdbaf28d1486de201cb7abf271e261f2d157728", url="https://pypi.org/packages/78/8b/02df4f04df1cbf0b741fdd027580ba7d81300512ffcde99422c0aaec74bb/gxformat2-0.15.0-py2.py3-none-any.whl")
    version("0.14.0", sha256="db174d4ee8b76a02c6ae07c3fee91309349c9b9d85f0617741919693cd9e4b43", url="https://pypi.org/packages/f3/e5/44dd9910f7cd69acace4b31f1902b6d064f34d29e45e17dc75dbc7fe0572/gxformat2-0.14.0-py2.py3-none-any.whl")
    version("0.13.1", sha256="f5125ad5f83425b3b75d69152a1fd34b228b7284004dbaaab408b5bb55cc31fb", url="https://pypi.org/packages/e9/df/a98a4205b349d88e39511ef73878904bbbbe5bc98cc9d82d6c54368fe767/gxformat2-0.13.1-py2.py3-none-any.whl")
    version("0.13.0", sha256="fe04af7779ea31fb90e2c2e080fdedaa16ec6b9abdfcfdf299eb6e972c7265dc", url="https://pypi.org/packages/36/dd/6b1ba733a96eaaa7714b68e01ce5cbd739328c4f50ddc441990256a95a83/gxformat2-0.13.0-py2.py3-none-any.whl")
    version("0.12.0", sha256="b5a6b633c091e9de507e5e7c0eb82df62ce37a0d3a3196d2bbdfc7487951480b", url="https://pypi.org/packages/0d/98/d69a182461dfee272589ba909459d7874ba26f871095962865bf24c0452a/gxformat2-0.12.0-py2.py3-none-any.whl")
    version("0.11.4", sha256="a92426fafe08df7a9dadc657c4971081eb46f74bc34847e3d7c6e0d5a118b1c0", url="https://pypi.org/packages/54/90/d35126e01e5600fb12d70e00014db5697fd9e608e30a3a3a6c74d9daa4e0/gxformat2-0.11.4-py2.py3-none-any.whl")
    version("0.11.3", sha256="cadfa2039db83cfef96e951375cedd73ffcbaff40ade0b4ce3d48c28aec2643b", url="https://pypi.org/packages/8a/1a/107cb496bab5ce23207d0fd320ce4d81588976dd09cc52dbaa82924d659d/gxformat2-0.11.3-py2.py3-none-any.whl")

    with default_args(type="run"):
        depends_on("py-bioblend", when="@:0.1.0.0,0.1.1:")
        depends_on("py-pyyaml", when="@:0.1.0.0,0.1.1:")
        depends_on("py-schema-salad@8.2:", when="@0.17:")
        depends_on("py-six@1.9:", when="@:0.1.0.0,0.1.1:0.15,0.16.0.dev:0.16")

