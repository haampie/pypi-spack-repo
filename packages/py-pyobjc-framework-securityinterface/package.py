##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPyobjcFrameworkSecurityinterface(PythonPackage):
    version("10.2", sha256="43930539fed05e74f3c692f5ee7848681e7e65c44387af300447514fe8e23ab6", url="https://pypi.org/packages/bf/08/1583580501c6451094619a888764ffa71088de09549872f6dda0c92bbbb2/pyobjc-framework-SecurityInterface-10.2.tar.gz")
    version("10.1", sha256="444a0dc7d50390750c28185b6496ee913011ac886d9e634bfc9a0856372d0a94", url="https://pypi.org/packages/dd/3f/ebb6d6268b6170cc8552f5069a275a9a0e51116b3bd944031c5006f2f65b/pyobjc-framework-SecurityInterface-10.1.tar.gz")
    version("10.0", sha256="fb3e660b7e1e2054597a87237a885ca62212c9889702bd634d34792d84fcc9ab", url="https://pypi.org/packages/54/e1/c38c51f864a5cdd1cdaa47b412562319ff44e944bb24329a502d232a303a/pyobjc-framework-SecurityInterface-10.0.tar.gz")
    version("9.2", sha256="31006ffafc4adc79c4bef7dff600e03944ce654c664c609819c6ef5cddda8d4d", url="https://pypi.org/packages/75/a5/bf3197b9a7ee72f468ed122b9fd0c57af717fd8ddf9426beef021923231a/pyobjc-framework-SecurityInterface-9.2.tar.gz")
    version("9.1.1", sha256="5c2f9795b6da71c5186767d99d3f8a86d68ea03a1e0325204c888ffc10ec32ef", url="https://pypi.org/packages/d9/8b/232b5472e599bc0d55dbbda3026a330f2895545df1c4ca408bda54caa727/pyobjc-framework-SecurityInterface-9.1.1.tar.gz")
    version("9.1", sha256="30e690c2cca3505561ba4a70c40d04099621af3e39dca5ae6d397592c786d018", url="https://pypi.org/packages/f0/17/137bd33df0b0ff9cbffa7562a73fd566e0a5fe90097d21d04ce71cdf8136/pyobjc-framework-SecurityInterface-9.1.tar.gz")
    version("9.0.1", sha256="2971724b3ea089275046dc0ffd1864259cd68e5e2a37da1c02718833e4631e22", url="https://pypi.org/packages/c2/44/212ee04add6a71749f33de9b8b84bb2a4710e503bcbf97347878a485e9ba/pyobjc-framework-SecurityInterface-9.0.1.tar.gz")
    version("9.0", sha256="2545afd56bdb63a55e78b126b9d34696cbf41cda211270fafcec63c99f273aac", url="https://pypi.org/packages/52/17/336a07aefd62e45a991295df914228a649e6dc9b38a62f2cb44c8ba9eca2/pyobjc-framework-SecurityInterface-9.0.tar.gz")
    version("8.5.1", sha256="ed7dfff8e76d3ec1bf445d7d94ad103bf77915594663751d9ea44fe256fde257", url="https://pypi.org/packages/9a/c0/3e3fc4d1422e60b41ea449fd0889251a9f2b23c7532e305801ffb7818b4d/pyobjc-framework-SecurityInterface-8.5.1.tar.gz")
    version("8.5", sha256="a80882df36ba464fbd77d4c037e8a89ed547c302c94a32fee73248dfa4335d01", url="https://pypi.org/packages/58/c2/779a87bbb88e063d9b33ac8ccb5ae2fee84b60c1b0eca67a2490a7e254b1/pyobjc-framework-SecurityInterface-8.5.tar.gz")

    with default_args(type="run"):
        depends_on("py-pyobjc-core@10.2:", when="@10.2:")
        depends_on("py-pyobjc-core@10.1:", when="@10.1")
        depends_on("py-pyobjc-core@10:", when="@10:10.0")
        depends_on("py-pyobjc-framework-cocoa@10.2:", when="@10.2:")
        depends_on("py-pyobjc-framework-cocoa@10.1:", when="@10.1")
        depends_on("py-pyobjc-framework-cocoa@10:", when="@10:10.0")
        depends_on("py-pyobjc-framework-security@10.2:", when="@10.2:")
        depends_on("py-pyobjc-framework-security@10.1:", when="@10.1")
        depends_on("py-pyobjc-framework-security@10:", when="@10:10.0")

