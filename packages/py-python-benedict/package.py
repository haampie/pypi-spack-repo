# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPythonBenedict(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("0.33.2", sha256="50a69b601b34d4ad7b67fe94e3266ec05046bc547a4132fe43fd8fbd41aeefaa", url="https://pypi.org/packages/68/5f/e32644b743d33142c6c43af50c86c6a5f535c3b3fa5b50c92aecded37741/python_benedict-0.33.2-py3-none-any.whl")
    version("0.33.1", sha256="8838ebe33ed7508d37472346e67516fcf525ebc717a6f48b37aa00e0b89bc463", url="https://pypi.org/packages/5f/0d/fb82d0840bc705d6e35923287da049a0c3dff9e6039ac829f37cf132f20d/python_benedict-0.33.1-py3-none-any.whl")
    version("0.33.0", sha256="2b6c2ee1edba2794bfe868e66b0eec260df899125b6187a63f486535b8db3dcc", url="https://pypi.org/packages/fc/a0/2f55aaacfb2b818a8e5e348099a62b13a34bb119ad348eebe3da35536287/python_benedict-0.33.0-py3-none-any.whl")
    version("0.32.1", sha256="61272f128ea5046399d261047b33d53e0836c951d9697b23a02d0723f9322e1d", url="https://pypi.org/packages/50/f1/bcb960406e2b669b3e7fdc677756c77584acdd4fb79efda7f17fdd1ef114/python_benedict-0.32.1-py3-none-any.whl")
    version("0.32.0", sha256="46638bc34b527b3deba5fbd267572ba51f907b0b755c95e7e2f9243285c63d54", url="https://pypi.org/packages/26/8c/7990920dadd79744682f4659d61366ed94e6301b3bcddac633fa6bbe1cb9/python_benedict-0.32.0-py3-none-any.whl")
    version("0.31.0", sha256="c1e45d6dab753d1ac7b990cbf2b85701d8dbb1411528916a9c73c3b3270e82e7", url="https://pypi.org/packages/81/6b/dc7923455b5a33b74cfd5291324fa3909d791b7c8bff214332db6af7160c/python_benedict-0.31.0-py3-none-any.whl")
    version("0.30.2", sha256="f167df8ba56979c2e1f80d0449fb35627af05665fca1b1b4ec68a5435ef53898", url="https://pypi.org/packages/bf/2b/c09d34e34d09c72dc8cb7586e46d42739973f96326975f6cdeb0f6f1a6ba/python_benedict-0.30.2-py3-none-any.whl")
    version("0.30.1", sha256="af2587962893ccce35b7fa8b10ab0a3ad583e0b41564d2e9976bcd9ee5963ef8", url="https://pypi.org/packages/5b/d9/74064c53285e0670cab3fe3a2bb404ecafeeeca2ba934ff2e0e454395994/python_benedict-0.30.1-py3-none-any.whl")
    version("0.30.0", sha256="11fc3c6d3e9d0c7a4d87dc4828fb13519cad1744a5b1b9616185c8ace23ce474", url="https://pypi.org/packages/9c/4f/2c5e83c9f178d59ffde24d7f3bc8b71d0e4654e480c5107a977c1ab36ac8/python_benedict-0.30.0-py3-none-any.whl")
    version("0.29.1", sha256="bcfe7f7f80a11890fd48e79d73c26a456d85e7b18892545b62e2fc23cb8693a9", url="https://pypi.org/packages/e0/a0/7c6053ffcee761c1bd37abb10d074f6ec5f79cab373eac629b8a8c31970a/python_benedict-0.29.1-py3-none-any.whl")
    version("0.23.2", sha256="b484901d94eb5b8aabd3e612cf1c504b42a92b6f17506428c60dbf93c3a88c6e", url="https://pypi.org/packages/87/c8/ae31902c3e6f671580e14472ca23d4b19831085999ff34ee00a22f648e84/python_benedict-0.23.2-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-boto3@1.24.89:", when="@0.27:0.28")
        depends_on("py-ftfy@6:", when="@0.25:0.30")
        depends_on("py-ftfy", when="@0.3:0.24")
        depends_on("py-mailchecker@4.1:5", when="@0.25.3:0.30")
        depends_on("py-mailchecker", when="@0.4:0.24")
        depends_on("py-openpyxl@3:", when="@0.26:0.28")
        depends_on("py-phonenumbers@8.12:", when="@0.25:0.30")
        depends_on("py-phonenumbers", when="@0.4:0.24")
        depends_on("py-python-dateutil@2.8:", when="@0.25:0.30")
        depends_on("py-python-dateutil", when="@0.3:0.24")
        depends_on("py-python-fsutil@0.9.3:", when="@0.28.3:")
        depends_on("py-python-fsutil", when="@0.23:0.24")
        depends_on("py-python-slugify@7:", when="@0.30.1:")
        depends_on("py-python-slugify@6.0.1:", when="@0.29:0.30.0")
        depends_on("py-python-slugify", when="@0.3:0.24")
        depends_on("py-pyyaml@6.0:", when="@0.25:0.28")
        depends_on("py-pyyaml", when="@0.5:0.24")
        depends_on("py-requests@2.26:", when="@0.25:")
        depends_on("py-requests", when="@0.5:0.24")
        depends_on("py-six", when="@0.5:0.24")
        depends_on("py-toml@0.10.2:", when="@0.25:0.28")
        depends_on("py-toml", when="@0.5:0.24")
        depends_on("py-xlrd@2:", when="@0.26:0.28")
        depends_on("py-xmltodict@0.12:", when="@0.25:0.28")
        depends_on("py-xmltodict", when="@0.5:0.24")
    # END DEPENDENCIES

