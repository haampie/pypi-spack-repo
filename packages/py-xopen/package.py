# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyXopen(PythonPackage):
    # BEGIN VERSIONS
    version("1.6.0", sha256="a23913c5263c1567562a77a15260e5d933ea5ef27d5ce95df7be8f637636fd7c", url="https://pypi.org/packages/14/a5/b990e46d1c3d309e63357cb730797594b5b7071aaa57b8a4c3d30d007c7f/xopen-1.6.0-py3-none-any.whl")
    version("1.1.0", sha256="6e57d7f0598bc589bb230390ef006ab5c9f1127bbc3e8257c82f0539f8ac9436", url="https://pypi.org/packages/fd/4a/8721495b3681c87251711a8fe0c7b0faa3620dee9096fd3458fc1b50b81f/xopen-1.1.0-py2.py3-none-any.whl")
    version("1.0.1", sha256="3120647d15eceb703e3669210126d0a886a78b293ca64490fa25d2fa83f7e8ab", url="https://pypi.org/packages/7d/1b/99e2ab42d187b6b0e2902044e589a8cd526e388aaddc88a2f7856999254c/xopen-1.0.1-py2.py3-none-any.whl")
    version("0.9.0", sha256="b21c42d5eb686edb80b23eaf31c82b4015fce937da7b871fb89326a58b6d1e8a", url="https://pypi.org/packages/ed/b6/0006cf17f5b2f7b45ea3258602d1e0b13c6012841645b664ff4977054cd5/xopen-0.9.0-py2.py3-none-any.whl")
    version("0.8.4", sha256="2947ddd6eb1e63996a6d446eb7e4af1ed05fb603ebe2052929872b7a7c787f47", url="https://pypi.org/packages/73/e9/bc35fd93cb6af3a011e44463db468914448825aa659f7636e836b8488b03/xopen-0.8.4-py2.py3-none-any.whl")
    version("0.8.2", sha256="5755814617a5b7049c9cd90c2ea5f752f7036c5db18bfcec4a5548708aa48d2c", url="https://pypi.org/packages/23/67/d986a15915ae70bdaa3d65abf1460319fcf89e987e6748fe137e03ca14b4/xopen-0.8.2-py2.py3-none-any.whl")
    version("0.5.0", sha256="b097cd25e8afec42b6e1780c1f6315016171b5b6936100cdf307d121e2cbab9f", url="https://pypi.org/packages/c4/3b/52f8a5d32c97e6301ea85419f0fc0eaed5cfaedc6a973990a2908116da31/xopen-0.5.0.tar.gz")
    version("0.1.1", sha256="d1320ca46ed464a59db4c27c7a44caf5e268301e68319f0295d06bf6a9afa6f3", url="https://pypi.org/packages/9a/b7/8906d6b2c4f874c0aacc676709a3d533362ac93bebc4a656c9df19421c9b/xopen-0.1.1.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-isal@0.3:", when="@1.1 platform=linux")

        # marker: platform_python_implementation == "CPython" and (platform_machine == "x86_64" or platform_machine == "AMD64")
        # depends_on("py-isal@1:", when="@1.6:1.7")
    # END DEPENDENCIES

