# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPythonEngineio(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("4.9.0", sha256="979859bff770725b75e60353d7ae53b397e8b517d05ba76733b404a3dcca3e4c", url="https://pypi.org/packages/fe/e5/03fa8e76c718e1dd7fb5b74e9ce816ae0e08734080b1e98dbafbcf2fc8ba/python_engineio-4.9.0-py3-none-any.whl")
    version("4.8.2", sha256="a357f0aba275c311b66f22181472ed5b174bbc541742eea1d16feae2fa1afabd", url="https://pypi.org/packages/4f/ca/b14136484c9a10230abbf44a89041ccd2c696d0cb425e53f48ca0de0d1e7/python_engineio-4.8.2-py3-none-any.whl")
    version("4.8.1", sha256="70a7700ec68e6a1e0f40eb34533f47dfbd0418a87746a60a54d2ff3b4179be25", url="https://pypi.org/packages/bd/4d/34a3c91e55158822ac0f870025e930aac300b2ef11beb15e48662a449ebf/python_engineio-4.8.1-py3-none-any.whl")
    version("4.8.0", sha256="6055ce35b7f32b70641d53846faf76e06f2af0107a714cedb2750595c69ade43", url="https://pypi.org/packages/8b/89/70ebee15c1ef37d3a5408dbb03e57aa226dc6f1921735ed8cd59ac2a0136/python_engineio-4.8.0-py3-none-any.whl")
    version("4.7.1", sha256="52499e8ab94fea1a6525ffe872fe7028d04b575799c5fa8e2cf7880e032de42e", url="https://pypi.org/packages/b3/69/1e5985404fdc7873cef612ae7451ba5d3c00b2daa0aa1d9a4f6a5265532a/python_engineio-4.7.1-py3-none-any.whl")
    version("4.7.0", sha256="23b05b768d61c281104d8c69e069cea356b2e60aa982f718cdf1731719ce2803", url="https://pypi.org/packages/a7/66/039c705061d2f501fb837e7a0ee7bb1987560c3a14025d23c7ec7425de7b/python_engineio-4.7.0-py3-none-any.whl")
    version("4.6.1", sha256="eed1ffa9b003104b92c7760de5ac43d074abce28fd28a511d5268da82bfb8644", url="https://pypi.org/packages/cf/e1/90b9f0a86fd285270a3fc030c734109ef7365fc8596a0d1ab62ff2d1e527/python_engineio-4.6.1-py3-none-any.whl")
    version("4.6.0", sha256="e3dbf1b95a6782730cba1654fa90a008d7b0081ae95394254341868f876de23c", url="https://pypi.org/packages/1a/de/1274d4c978c6b22d31715223247ad2c33019586bff67aada3ddcfa808f29/python_engineio-4.6.0-py3-none-any.whl")
    version("4.5.1", sha256="67a675569f3e9bb274a8077f3c2068a8fe79cbfcb111cf31ca27b968484fe6c7", url="https://pypi.org/packages/c1/b5/e555067d8dd44b5bccbd17f1ca4fdadd2e4defbb0022a296030d76293d25/python_engineio-4.5.1-py3-none-any.whl")
    version("4.5.0", sha256="7abaa5ca57428955c319e693106aa39f303ca6f426bdcafd3b80d3329659be63", url="https://pypi.org/packages/bb/d9/e519fedb3b8eea075cb64d078e21c6eed75a1be85e44ec3442296c1b5f69/python_engineio-4.5.0-py3-none-any.whl")
    version("2.0.2", sha256="ab79f81a193ca1d9d4df213080fd818bb7ff8cd342f3a405e7302bf7fcfe3eae", url="https://pypi.org/packages/c3/5a/316c1d956e229a9d5a80db842261922ea95a073d91d1402951c66bad7963/python_engineio-2.0.2-py2.py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-simple-websocket@0.10:", when="@4.7.1:")
    # END DEPENDENCIES

