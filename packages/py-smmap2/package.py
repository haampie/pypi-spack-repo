##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PySmmap2(PythonPackage):
    version("3.0.1", sha256="0cb6ea470b1ad9a65a02ca7f4c7ae601861f7dd24a43812ca51cfca2892bb524", url="https://pypi.org/packages/3e/11/2dae3df2f19c43e156cce8e02c0080b46821faf816b839a2023ef7b6b84f/smmap2-3.0.1-py3-none-any.whl")
    version("2.0.5", sha256="0555a7bf4df71d1ef4218e4807bbf9b201f910174e6e08af2e138d4e517b4dde", url="https://pypi.org/packages/55/d2/866d45e3a121ee15a1dc013824d58072fd5c7799c9c34d01378eb262ca8f/smmap2-2.0.5-py2.py3-none-any.whl")
    version("2.0.4", sha256="0dd53d991af487f9b22774fa89451358da3607c02b9b886a54736c6a313ece0b", url="https://pypi.org/packages/0f/14/e3112808b727f72df9531fc2f00b84d4966e66001748b6883a21c767e902/smmap2-2.0.4-py2.py3-none-any.whl")
    version("2.0.3", sha256="b78ee0f1f5772d69ff50b1cbdb01b8c6647a8354f02f23b488cf4b2cfc923956", url="https://pypi.org/packages/e3/59/4e22f692e65f5f9271252a8e63f04ce4ad561d4e06192478ee48dfac9611/smmap2-2.0.3-py2.py3-none-any.whl")
    version("2.0.2", sha256="2194d1cead1f618983b8eb749ecccc92f05cc44e1ead24993cf69995ca66d49d", url="https://pypi.org/packages/da/c7/343900b3a0267c8550fbd921967c79e8ca4044b0b3c24e04d2898e937c15/smmap2-2.0.2-py2.py3-none-any.whl")
    version("2.0.1", sha256="2fd9bf96acf84caf80363c2e7178163cda58633fe657f82d0feeed69cf612626", url="https://pypi.org/packages/a2/ce/2aea0d688d58baf60781d4ab9b0ee14b5585929b65355e6c77e9dc42c4c4/smmap2-2.0.1-py2.py3-none-any.whl")
    version("2.0.0", sha256="e648aa5a706e69e12e368db9252901efdca9f4bdbc60f9dee12009a2182f7329", url="https://pypi.org/packages/ed/e9/1623e2979a6886eaa771c5fbfe6633ec82bdc183419497d1c0c9d93c2058/smmap2-2.0.0-py2.py3-none-any.whl")

    with default_args(type="run"):
        depends_on("py-smmap@3.0.1:", when="@3:")

