# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyFparser(PythonPackage):
    # BEGIN VERSIONS
    version("0.1.4", sha256="11c9c609d398dda48f2c318d4ea13705d2281d791d219455d31a3d000736268e", url="https://pypi.org/packages/4c/59/b92fa6a7c8c1194516ab97993296f384b5c7fe91f54ba6b4feb296512a4e/fparser-0.1.4-py3-none-any.whl")
    version("0.1.3", sha256="1c0adcf7e6b5f36851abb2471bab2be1eb67fd834ea29279e917047ecb7fef6a", url="https://pypi.org/packages/7b/52/7fc658906755e0f58294e3a35d214c04787fc9981c9eaed8ce8058a48940/fparser-0.1.3-py3-none-any.whl")
    version("0.0.16", sha256="166c234b199e2936dcb5c71880b7f561f004e4356c017d5401c38b193f3f3161", url="https://pypi.org/packages/08/90/5e21ee72fba76189b7ed01849e4801a85a6f8e2241b4265e23c3341b0264/fparser-0.0.16-py3-none-any.whl")
    version("0.0.15", sha256="6051ac554d0d258c8828c480c268184cba42d83c864ddcc368df180d2071dff5", url="https://pypi.org/packages/aa/7e/f88cabc7fe9efd9e4c70249e49ccd3e207fed93f6084c420575a675ea791/fparser-0.0.15-py3-none-any.whl")
    version("0.0.14", sha256="2e1cd64949f3371ad2b5f45034c88ac21b236bf52aa2be562d07dd2ab5390df4", url="https://pypi.org/packages/eb/69/b043e2313b05b032ccad6ccfa43f969f09de9aac3fe61d17aa72586b8a73/fparser-0.0.14-py3-none-any.whl")
    version("0.0.13", sha256="ed20aea95dcf93fc6f8018de7e33fefe8d8f5cb0a639074f9578fa1a3cb77f3c", url="https://pypi.org/packages/5b/68/6cf4f5db11e67c9ee058703f77427aa14c1b7f5dbfac907cda4c4e6660bd/fparser-0.0.13-py3-none-any.whl")
    version("0.0.12", sha256="6edee516a59f87eac6b8dbacaa58eb782dd7bc0f99ab1671dda9a9843fa846f9", url="https://pypi.org/packages/05/33/3bb57ea8de26a32cfc1ebc0ae0ee0fea298626f3ec6a65f5414a60f28637/fparser-0.0.12-py3-none-any.whl")
    version("0.0.6", sha256="bf8a419cb528df1bfc24ddd26d63f2ebea6f1e103f1a259d8d3a6c9b1cd53012", url="https://pypi.org/packages/67/41/b9cc791c97fa514ca809afc540c76b21d3adb27e84731a3963626b602215/fparser-0.0.6.tar.gz")
    version("0.0.5", sha256="f3b5b0ac56fd22abed558c0fb0ba4f28edb8de7ef24cfda8ca8996562215822f", url="https://pypi.org/packages/f3/7f/4e14104863f9251581a5cbadf5ccf49d9227f9bb7bde386f9353036e2b47/fparser-0.0.5.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-importlib-metadata", when="@0.1:0.1.3")
        depends_on("py-setuptools-scm", when="@0.1:")
        depends_on("py-six", when="@0.0.9:0.0")
    # END DEPENDENCIES

