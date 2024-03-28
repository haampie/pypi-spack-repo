# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyAutocfg(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("0.0.8", sha256="7458f8dc2aff67161a31a7d196c3d34002a34907bace58373394cc3a7107ce2a", url="https://pypi.org/packages/95/f9/74e0a42cbc6d871c92288806e7812c7d2628c2a06557930dbab0a17438d2/autocfg-0.0.8-py3-none-any.whl")
    version("0.0.7", sha256="c80709e17b420d6353936b60cd669bd059c4193803812e71a865fc542253bbae", url="https://pypi.org/packages/38/8d/bb4b522c5745bafd4d8b3b577f087089f73a5f4048911a99fe4a17fbda92/autocfg-0.0.7-py3-none-any.whl")
    version("0.0.6", sha256="fba203fa757fd0dc28c6712948fda38c6403d1d54aa04ef370970261021417c2", url="https://pypi.org/packages/94/4d/71221541472d0e45351cf9b11b0c3d55c032b80dcf8bc0763b28791e3dd3/autocfg-0.0.6-py2.py3-none-any.whl")
    version("0.0.5", sha256="6f6b5a7424453afaca69ec3536f188f3f9353410e0b7ba23b00a391dc9d76b1b", url="https://pypi.org/packages/e3/84/0676b0bcbc51c08168e8b71cd91a16dfb128bd23d080e4120e68a5cdf420/autocfg-0.0.5-py2.py3-none-any.whl")
    version("0.0.4", sha256="356c236ce26142c70ae251c17db294528def61f358e5b5b65dd32dde3b349451", url="https://pypi.org/packages/c7/ed/341c971728efcaa15b09722a70354a1221d875a0a97baf2a5e9479d22f11/autocfg-0.0.4-py2.py3-none-any.whl")
    version("0.0.3", sha256="7ee3c77f1e911c3bb1e21a8176ec4170cb0221e41eaceda0c5d17f1374c1732c", url="https://pypi.org/packages/65/f8/a69efed815f7abeca39bedca733a5087771b4d8daf222f4323fe76408c1a/autocfg-0.0.3-py2.py3-none-any.whl")
    version("0.0.2", sha256="341c786b44719de7f01b34bd387fa4cf4b5409521ca76cc649bba30a4afa8da0", url="https://pypi.org/packages/87/1d/05f0dc48b9e637ee617971810cf48e8933684e3377f86e539b4d5a6d9045/autocfg-0.0.2-py3-none-any.whl")
    version("0.0.1", sha256="eff25ac824ddd73524b59fe9725fd0485eae0ed9d1daff33cda60cd311db9fed", url="https://pypi.org/packages/2c/c3/2db281d68d6120c2af1893197756ad804ceb579890bb2c0f52a2c120a367/autocfg-0.0.1-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-pyyaml")
    # END DEPENDENCIES

