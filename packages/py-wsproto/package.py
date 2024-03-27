##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyWsproto(PythonPackage):
    version("1.2.0", sha256="b9acddd652b585d75b20477888c56642fdade28bdfd3579aa24a4d2c037dd736", url="https://pypi.org/packages/78/58/e860788190eba3bcce367f74d29c4675466ce8dddfba85f7827588416f01/wsproto-1.2.0-py3-none-any.whl")
    version("1.1.0", sha256="2218cb57952d90b9fca325c0dcfb08c3bda93e8fd8070b0a17f048e2e47a521b", url="https://pypi.org/packages/4b/6e/5f8c3e8418966f50d028e336f0c2c568f8522577183678923609d4d24924/wsproto-1.1.0-py3-none-any.whl")
    version("1.0.0", sha256="d8345d1808dd599b5ffb352c25a367adb6157e664e140dbecba3f9bc007edb9f", url="https://pypi.org/packages/ea/25/0934b1d00f404d75335b144d4396e01998f25db8953bf54b4d6fe65b80ab/wsproto-1.0.0-py3-none-any.whl")
    version("0.15.0", sha256="e3d190a11d9307112ba23bbe60055604949b172143969c8f641318476a9b6f1d", url="https://pypi.org/packages/d5/8b/96575a9a73591ce8e5e519375e30565bf9d299d0ced98a2970c225abedf4/wsproto-0.15.0-py2.py3-none-any.whl")
    version("0.14.1", sha256="2b870f5b5b4a6d23dce080a4ee1cbb119b2378f82593bd6d66ae2cbd72a7c0ad", url="https://pypi.org/packages/6a/e2/d69646c06cc970393e23e7506cb7ec3cec98e1f54ca5c5fac6efc15f67de/wsproto-0.14.1-py2.py3-none-any.whl")
    version("0.14.0", sha256="c7f35e0af250b9f25583b090039eb2159a079fbe71b7daf86cc3ddcd2f3a70b3", url="https://pypi.org/packages/91/0b/d88cabc62f6c85363a57456d2d064dd50746e02c7637cd780c256295dca3/wsproto-0.14.0-py2.py3-none-any.whl")
    version("0.13.0", sha256="c013342d7a9180486713c6c986872e4fe24e18a21ccbece314939d8b58312e0e", url="https://pypi.org/packages/74/18/92f1c6b570ac322d5cfdc9dd10c6ba863b153a38c664d7bc50df719b5815/wsproto-0.13.0-py2.py3-none-any.whl")
    version("0.12.0", sha256="6a51cf18d9de612892b9c1d38a8c1bdadec0cfe15de61cd5c0f09174bf0c7e82", url="https://pypi.org/packages/6b/f8/300c85ce7473a6e81c6aef294b6bb55375720e08974cdec915793eafaf58/wsproto-0.12.0-py2.py3-none-any.whl")
    version("0.11.0", sha256="d2a7f718ab3144ec956a3267d57b5c172f0668827f5803e7d670837b0125b9fa", url="https://pypi.org/packages/1f/bf/a4136bd7950c49f18a7d643f962e307cbed93ca115e0634656d88e02c333/wsproto-0.11.0-py2.py3-none-any.whl")
    version("0.10.0", sha256="cc6a990baec0510f926a9287ae23d031a0ba267474a98e485488244f725900ad", url="https://pypi.org/packages/04/03/a3441f7ce6ea7be9ccae8fa6e1eedfc4bebf6580eb10b8e433a4347c37bc/wsproto-0.10.0.tar.gz")

    with default_args(type="run"):
        depends_on("py-h11@0.9:", when="@1:")
        depends_on("py-h11@0.8.1:", when="@0.14.1:0")
        depends_on("py-h11@0.8.1:0.8", when="@0.12:0.14.0")
        depends_on("py-h11@0.7", when="@0.11")

