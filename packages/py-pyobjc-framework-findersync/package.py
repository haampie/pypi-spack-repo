# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPyobjcFrameworkFindersync(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("10.2", sha256="11d569492efe74a52883e6086038ca9d5a712a08db828f3ca43c03e756013801", url="https://pypi.org/packages/e6/e7/47529282b26e5c36b81b61465ca486252b43caaa298158287eaed6cd10c3/pyobjc_framework_FinderSync-10.2-py2.py3-none-any.whl")
    version("10.1", sha256="e5a5ff1e7d55edb5208ce04868fcf2f92611053476fbbf8f48daa3064d56deb5", url="https://pypi.org/packages/42/db/bb44f4027ae5b035fda558f7bfe3181e246d0e2bdda22a495363cbebc5b6/pyobjc_framework_FinderSync-10.1-py2.py3-none-any.whl")
    version("10.0", sha256="b2d166fa8af4cd7516fc860c896531bcf9921e5251106c99ac6cd726bf41d020", url="https://pypi.org/packages/08/71/1a0e9c2ed7a962b60ef15e710f8824e08b63b0ed05486884fdd4dad2a5b4/pyobjc_framework_FinderSync-10.0-py2.py3-none-any.whl")
    version("9.2", sha256="b8a2cb4e8ffef487016219bdbc8b01336d6d1e864e0289bab01e74070103ee67", url="https://pypi.org/packages/d5/18/fd51c43a84e11c84f091ae05b65d950121bf2ddc41b46cfa0bf2d4a03a50/pyobjc_framework_FinderSync-9.2-py2.py3-none-any.whl")
    version("9.1.1", sha256="b0be003f6aeacd5604ba5beb98da98b1a07df44d3d5f308b9974d5512d9832e4", url="https://pypi.org/packages/08/c9/dad3e0e0896463cfa90dd4268ad442ae5d09c5698065520409a42c076c56/pyobjc_framework_FinderSync-9.1.1-py2.py3-none-any.whl")
    version("9.1", sha256="9167661a6b5c759652f9a428f9e82cce24a954f72ffe7c89d49a9fb1e67921c3", url="https://pypi.org/packages/ad/17/0b2b0b7faaed363c1cefd69cbf066e438da55236d81469de4f25c7e6189c/pyobjc_framework_FinderSync-9.1-py2.py3-none-any.whl")
    version("9.0.1", sha256="05dad77c6994a89056932f6c876ad87366169a3f8d9136330f71da88317d9f6b", url="https://pypi.org/packages/6e/34/ae8c1eeb69585ced9b25d98bae55bfd78896369de67ef941abaadf4523fd/pyobjc_framework_FinderSync-9.0.1-py2.py3-none-any.whl")
    version("9.0", sha256="9682968a82bc5a5049b90325f25f05c64176f445ea8473dbf0ae4123a386c3f2", url="https://pypi.org/packages/44/66/558f67b9a11bed5b74a0221e882bf39e2040a158e7068f17e67683cbc998/pyobjc_framework_FinderSync-9.0-py2.py3-none-any.whl")
    version("8.5.1", sha256="79dadb2ac8b49c8600b307d066b476b2a2cf7378664988e191b0e5d001a8ff7e", url="https://pypi.org/packages/79/24/5bf12399ba110293d00ee2a5fc236ee1e870a50e86faf9cf68aaf3e2601d/pyobjc_framework_FinderSync-8.5.1-py2.py3-none-any.whl")
    version("8.5", sha256="4b707078362dc9441a8058d8a472f54d2caba344c258408bbf937c1bedbd86de", url="https://pypi.org/packages/38/bb/81900618e91053e74af62a1fe1e21096c9024015c6b8f80a490e48f896c6/pyobjc_framework_FinderSync-8.5-py2.py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-pyobjc-core@10.2:", when="@10.2:")
        depends_on("py-pyobjc-core@10.1:", when="@10.1")
        depends_on("py-pyobjc-core@10:", when="@10:10.0")
        depends_on("py-pyobjc-core@9.2:", when="@9.2:9")
        depends_on("py-pyobjc-core@9.1.1:", when="@9.1.1:9.1")
        depends_on("py-pyobjc-core@9.1:", when="@9.1:9.1.0")
        depends_on("py-pyobjc-core@9.0.1:", when="@9.0.1:9.0")
        depends_on("py-pyobjc-core@9:", when="@9:9.0.0")
        depends_on("py-pyobjc-core@8.5.1:", when="@8.5.1:8")
        depends_on("py-pyobjc-core@8.5:", when="@8.5:8.5.0")
        depends_on("py-pyobjc-framework-cocoa@10.2:", when="@10.2:")
        depends_on("py-pyobjc-framework-cocoa@10.1:", when="@10.1")
        depends_on("py-pyobjc-framework-cocoa@10:", when="@10:10.0")
        depends_on("py-pyobjc-framework-cocoa@9.2:", when="@9.2:9")
        depends_on("py-pyobjc-framework-cocoa@9.1.1:", when="@9.1.1:9.1")
        depends_on("py-pyobjc-framework-cocoa@9.1:", when="@9.1:9.1.0")
        depends_on("py-pyobjc-framework-cocoa@9.0.1:", when="@9.0.1:9.0")
        depends_on("py-pyobjc-framework-cocoa@9:", when="@9:9.0.0")
        depends_on("py-pyobjc-framework-cocoa@8.5.1:", when="@8.5.1:8")
        depends_on("py-pyobjc-framework-cocoa@8.5:", when="@8.5:8.5.0")
    # END DEPENDENCIES

