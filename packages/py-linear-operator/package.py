##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyLinearOperator(PythonPackage):
    version("0.5.2", sha256="26defe85e3c924f24d49117bf78afaf0207f6847877903309dc9bf40a46d08a7", url="https://pypi.org/packages/4e/3b/c86ec0c226763a2a199b370f50309ef58c0d8c1555e6a278bd053263881f/linear_operator-0.5.2-py3-none-any.whl")
    version("0.5.1", sha256="3d40ea5c93a230c8800df80993e49ecc7ec44e63081f80dde2bb0e2a082cb5b1", url="https://pypi.org/packages/b1/09/f05028540be70995435c57b71a96250d1257d6e9aafe848981baa4427a2a/linear_operator-0.5.1-py3-none-any.whl")
    version("0.5.0", sha256="15c9194ea904c69132399d30b5cee4e9e86bdf7eb6a164c6213822cf9571af85", url="https://pypi.org/packages/53/d3/b2e64d95f22b8966df4ae05eb498e43afb06ed59a5a356900458d9abecef/linear_operator-0.5.0-py3-none-any.whl")
    version("0.4.0", sha256="55f120f4e3102eaf017f04af911949536beec9009d6a35c26b775637aa4fe026", url="https://pypi.org/packages/4e/60/770e7e7fabbada728a47ad5d83e98a608dcbd6aa2ed361085bcfc1fc97b0/linear_operator-0.4.0-py3-none-any.whl")
    version("0.3.0", sha256="262b1028ed3cd1ae70d79a3a29b0210301576d9e426a68b8767acdd4abb116a6", url="https://pypi.org/packages/3b/c3/d8cad67ed11f8a270c318b1eae726b4c8fa17df33108811b4e79bc2f438c/linear_operator-0.3.0-py3-none-any.whl")
    version("0.2.0", sha256="14c687de5aad42e16eed5c0712285e8dd497b5a3b1d8ce7bb71f6b5acb15290f", url="https://pypi.org/packages/57/ae/d5062fbbfe447142d5a6ba8ae96a1c237d1997668ed714f5a4ef4bdcb421/linear_operator-0.2.0-py3-none-any.whl")
    version("0.1.1", sha256="55472043408959f04c8eb6153bc68a487b141b8c1f2fdb84afcdf6c2e04e01f0", url="https://pypi.org/packages/e6/3c/a2cbf56429c4e370cdcd76155fc1068d21a812c67655244f0776a27697c7/linear_operator-0.1.1-py3-none-any.whl")

    with default_args(type="run"):
        depends_on("py-jaxtyping@0.2.9:", when="@0.5:")
        depends_on("py-scipy")
        depends_on("py-torch@1.11:")
        depends_on("py-typeguard@2.13.3:2", when="@0.5:")

