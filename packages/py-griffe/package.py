# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyGriffe(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("0.42.1", sha256="7e805e35617601355edcac0d3511cedc1ed0cb1f7645e2d336ae4b05bbae7b3b", url="https://pypi.org/packages/c4/59/a13ea5d6d991c0c9861a09b268e6ead054f3d316a74136aa86874ace7bbd/griffe-0.42.1-py3-none-any.whl")
    version("0.42.0", sha256="384df6b802a60f70e65fdb7e83f5b27e2da869a12eac85b25b55250012dbc263", url="https://pypi.org/packages/32/25/55714a61c5d4462efb69faeb5fed6fdae61c2396f0279c6c640fe85a0a02/griffe-0.42.0-py3-none-any.whl")
    version("0.41.3", sha256="27b4610f1ba6e5d039e9f0a2c97232e13463df75e53cb1833e0679f3377b9de2", url="https://pypi.org/packages/4e/f8/0a768c870a6f436e103d915f3dbb5e9f625a448d8ffd999b30624145b6b7/griffe-0.41.3-py3-none-any.whl")
    version("0.41.2", sha256="a3e1824bc8d5c3190b7e05fbfde36e1e794d9c409c646783a57366c947d7816b", url="https://pypi.org/packages/4d/13/00e38b503d0032d73be4a50074a30ac87b0d6cb842fe76b89d21763d542d/griffe-0.41.2-py3-none-any.whl")
    version("0.41.1", sha256="9b71b82d0177a278467ce362827296957f0ca59ff5437ee41a0d6247aee257fa", url="https://pypi.org/packages/c7/62/dc15d53f547ac0c7fadf5368663d6be7c4101764e5ce3db5bfa1661845bd/griffe-0.41.1-py3-none-any.whl")
    version("0.41.0", sha256="8aa7fc6eb00cb80af9c0198178c6b7110cb59fa2c5187bb13ea25eebbe4dd928", url="https://pypi.org/packages/94/9b/e66c720cb04f6f14ccb15e53374daa2443e86ddccc02b951bc85245dc806/griffe-0.41.0-py3-none-any.whl")
    version("0.40.1", sha256="5b8c023f366fe273e762131fe4bfd141ea56c09b3cb825aa92d06a82681cfd93", url="https://pypi.org/packages/aa/4c/7268d218ee38cb0e07d63fc3fe60fe19dc353f757db3d365f0b5ffba85be/griffe-0.40.1-py3-none-any.whl")
    version("0.40.0", sha256="db1da6d1d8e08cbb20f1a7dee8c09da940540c2d4c1bfa26a9091cf6fc36a9ec", url="https://pypi.org/packages/19/2f/44198bdb4eaff14ce5aaa565bdfabc7661d0ac71f686449813cc5865046d/griffe-0.40.0-py3-none-any.whl")
    version("0.39.1", sha256="6ce4ecffcf0d2f96362c5974b3f7df812da8f8d4cfcc5ebc8202ef72656fc087", url="https://pypi.org/packages/78/a5/24cd31a93408838014a842c8b42817468be7265a7d1efbbd327b750524a6/griffe-0.39.1-py3-none-any.whl")
    version("0.39.0", sha256="b5e2f249d86feaad1d3068b33b1c8c2ecf39cb870bf292f2af3a4311891a4835", url="https://pypi.org/packages/30/8d/3b296acc69a4009eab33ef4665d634c7d11f84f43324179787157ff9b41a/griffe-0.39.0-py3-none-any.whl")
    version("0.22.0", sha256="65c94cba634d6ad397c495b04ed5fd3f06d9b16c4f9f78bd63be9ea34d6b7113", url="https://pypi.org/packages/fe/ad/0b31357c29f9108c51e5ba85cdf989fe45652e4e24883da68be7e2272700/griffe-0.22.0-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-astunparse@1.6:", when="@0.41: ^python@:3.8")
        depends_on("py-colorama@0.4:", when="@0.24:")
    # END DEPENDENCIES

