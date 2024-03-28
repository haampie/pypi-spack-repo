# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPythonDaemon(PythonPackage):
    # BEGIN VERSIONS
    version("3.0.1", sha256="42bb848a3260a027fa71ad47ecd959e471327cb34da5965962edd5926229f341", url="https://pypi.org/packages/83/7f/feffd97af851e2a837b5ca9bfbe570002c45397734724e4abfd4c62fdd0d/python_daemon-3.0.1-py3-none-any.whl")
    version("3.0.0", sha256="244d97f57567d1a2da53840b4ef59946c9837b7790403d82ac6f846466dd73ec", url="https://pypi.org/packages/ff/33/014116323e7088e76bc4d667a2090a86ded5b228eccdb803c2fe1110f3d9/python_daemon-3.0.0-py3-none-any.whl")
    version("2.3.2", sha256="01d26358598f8c3f5fc6de553e2f3080ffc59cf89102d7ee8098f33c72b3c04c", url="https://pypi.org/packages/89/38/c223036ee8104ae95118d4481b5cacccf4547d7e5b8d1ee1c63d2cd57e5d/python_daemon-2.3.2-py3-none-any.whl")
    version("2.3.1", sha256="4e3bf67784c78aaa55ec001a2f832b464a54c5f9c89c11b311e2416a8c247431", url="https://pypi.org/packages/aa/b0/bc79d8ff019c2583d839e0143b1f91eafd4cfe92f86fb9d378a515dfb612/python_daemon-2.3.1-py2.py3-none-any.whl")
    version("2.3.0", sha256="191c7b67b8f7aac58849abf54e19fe1957ef7290c914210455673028ad454989", url="https://pypi.org/packages/b1/cc/2ab0d910548de45eaaa50d0372387951d9005c356a44c6858db12dc6b2b7/python_daemon-2.3.0-py2.py3-none-any.whl")
    version("2.2.4", sha256="a0d5dc0b435a02c7e0b401e177a7c17c3f4c7b4e22e2d06271122c8fec5f8946", url="https://pypi.org/packages/5a/0c/57f15b1572661877ff1acbe66c2f5be9d999ae5fb128e22933d374f62aa1/python_daemon-2.2.4-py2.py3-none-any.whl")
    version("2.2.3", sha256="1d9a541f74822ac87045163ebd5473f9a7b22ab4031ed28293aba81fdaf6c156", url="https://pypi.org/packages/e6/44/6734382d1beb8704137ec94589e7d173a415f3396e34d020fb6b6271c2ff/python_daemon-2.2.3-py2.py3-none-any.whl")
    version("2.2.2", sha256="e9d97b4680ebee7c3fb91d5d2303311a5465eb38a346a494cbfd9514614f1581", url="https://pypi.org/packages/42/df/f3a68d4ad9bd370a476f84e65ac034de6990c588318274945be063fe9dd0/python_daemon-2.2.2-py2.py3-none-any.whl")
    version("2.2.1", sha256="092f9c37e32a78436464e74fbd04339b1d1109943fb3a48690c967ac63cac4a0", url="https://pypi.org/packages/62/c7/8edb6eac27dd80858c0c84057be77f4916086355b84bf63615fa2473ef99/python_daemon-2.2.1-py2.py3-none-any.whl")
    version("2.2.0", sha256="aca149ebf7e73f10cd554b2df5c95295d49add8666348eff6195053ec307728c", url="https://pypi.org/packages/99/2a/75fe6aa7086e838570f29899f674e7896a42be26d9fff33f90d990e599d2/python-daemon-2.2.0.tar.gz")
    version("2.0.5", sha256="db316a0fcf54b9702caf6ca619b76be25d53f5ee0781baff0bb9e2e0355faf24", url="https://pypi.org/packages/5b/90/b55062dbce72c24ba1c1655b07974b300a66f352800152e6ed21f29b7dc4/python_daemon-2.0.5-py2.py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-docutils", when="@:0,2.2.1:")
        depends_on("py-lockfile@0.10:", when="@:0,2.2.1:")
        depends_on("py-setuptools@62.4:", when="@3.0.1:")
        depends_on("py-setuptools", when="@:0,2.2.1:3.0.0")
    # END DEPENDENCIES

