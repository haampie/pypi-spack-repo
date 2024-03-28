# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPhylophlan(PythonPackage):
    # BEGIN VERSIONS
    version("3.1.1", sha256="d607e529d6f2b1789593e49914d830adc395fbde35afd4c600da5f4f5a15cf16", url="https://pypi.org/packages/be/6e/b3a2003bdba99b9f64e3c977a7b409f9c2265c346266bb69bcce972cd81c/PhyloPhlAn-3.1.1-py3-none-any.whl")
    version("3.1", sha256="25ac954fe3985b63d9f39a311dbf2aa7c8d31296b56fe02a9eee519a1ea02e5e", url="https://pypi.org/packages/f7/10/28871121f3a5585227d6a93cd3584f7662189860f04b4f4099384843b10c/PhyloPhlAn-3.1-py3-none-any.whl")
    version("3.0.3", sha256="1c37393742fa2eefb1f7b7829609d0dac03d53dae761c6ab2db13b4c4609cb79", url="https://pypi.org/packages/74/92/0513cefa30ef0f6bef6d7441bf59979213510efdbf875bc877521b5a96e9/PhyloPhlAn-3.0.3-py3-none-any.whl")
    version("3.0.2", sha256="1f5626a920aaed8f0e2ce333326945ea7267a096d7de5cc57dce785079618e16", url="https://pypi.org/packages/61/84/be11873e8749b1c5e5f914a65a23ce41d90204590044129f630516c14420/PhyloPhlAn-3.0.2-py3-none-any.whl")
    version("3.0.1", sha256="dc197f76a3b5a685a5c6c79539dc786dd5c61ca249512c05d0505c938196c1e5", url="https://pypi.org/packages/01/fe/96f17a97e994aa50181256c0a92d2c73674e365cf50628f44712f715a576/PhyloPhlAn-3.0.1-py3-none-any.whl")
    version("3.0.0", sha256="14a2fbfed111fa3f9db90a44913481145b4fb6ba3fd18f2848ba355714c71eba", url="https://pypi.org/packages/bc/f7/c5a8d44a452bf225cb81ed25a248eef9fcd820ba57c4e7ffedbbf75fc8e5/PhyloPhlAn-3.0.0.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-biopython", when="@3.0.1:")
        depends_on("py-dendropy", when="@3.0.1:")
        depends_on("py-matplotlib", when="@3.0.1:")
        depends_on("py-numpy", when="@3.0.1:")
        depends_on("py-pandas", when="@3.0.1:")
        depends_on("py-seaborn", when="@3.0.1:")
    # END DEPENDENCIES

