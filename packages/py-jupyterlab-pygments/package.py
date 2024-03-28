# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyJupyterlabPygments(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("0.3.0", sha256="841a89020971da1d8693f1a99997aefc5dc424bb1b251fd6322462a1b8842780", url="https://pypi.org/packages/b1/dd/ead9d8ea85bf202d90cc513b533f9c363121c7792674f78e0d8a854b63b4/jupyterlab_pygments-0.3.0-py3-none-any.whl")
    version("0.2.2", sha256="2405800db07c9f770863bcf8049a529c3dd4d3e28536638bd7c1c01d2748309f", url="https://pypi.org/packages/c0/7e/c3d1df3ae9b41686e664051daedbd70eea2e1d2bd9d9c33e7e1455bc9f96/jupyterlab_pygments-0.2.2-py2.py3-none-any.whl")
    version("0.2.1", sha256="05f8056a18fec9ebef01f705443d81edb16bb03d27371f23c0ae135a85a76029", url="https://pypi.org/packages/de/76/4199f6813ecb6f0a3380c03c2b6a329b64b7efd33553415c77777c00e444/jupyterlab_pygments-0.2.1-py2.py3-none-any.whl")
    version("0.2.0", sha256="8feffeec1799aaaea5b889add289e0c6dd648ea049be800fde814de46bf99f83", url="https://pypi.org/packages/67/cd/a76e40ebd4b312bb7cad1ce8aad6170adc6aca2975375c9eed7fdddb1b05/jupyterlab_pygments-0.2.0-py2.py3-none-any.whl")
    version("0.1.2", sha256="abfb880fd1561987efaefcb2d2ac75145d2a5d0139b1876d5be806e32f630008", url="https://pypi.org/packages/a8/6f/c34288766797193b512c6508f5994b830fb06134fdc4ca8214daba0aa443/jupyterlab_pygments-0.1.2-py2.py3-none-any.whl")
    version("0.1.1", sha256="c9535e5999f29bff90bd0fa423717dcaf247b71fad505d66b17d3217e9021fc5", url="https://pypi.org/packages/1f/4c/905faabb03f56ba92b1b9049436afead02bc09aae7e8f0d1107ebb46b151/jupyterlab_pygments-0.1.1-py2.py3-none-any.whl")
    version("0.1.0", sha256="cc15f2a9850899d108a3c22743a86edcd3b42791a6c88b6e5b558d021d14d065", url="https://pypi.org/packages/d8/4d/579c4613dbc656c07fa424663818f8bddd77ecafe6956497f66cab82b130/jupyterlab_pygments-0.1.0-py2.py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-pygments@2.4.1:", when="@:0.1")
    # END DEPENDENCIES

