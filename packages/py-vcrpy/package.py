# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyVcrpy(PythonPackage):
    # BEGIN VERSIONS
    version("6.0.1", sha256="9e023fee7f892baa0bbda2f7da7c8ac51165c1c6e38ff8688683a12a4bde9278", url="https://pypi.org/packages/bf/59/9fe85bf7af469bdb0ab8416c76cde630cdff6d1790ecb87e5a58f259c89c/vcrpy-6.0.1.tar.gz")
    version("6.0.0", sha256="04fc36b53981b32680d7a860bf4ceca0fbe9948349b2ac7ffd4d8f7324b77006", url="https://pypi.org/packages/49/f8/ae0091e5d3af4f098546a8bf088151af19bc29b70a5cc7da895ebf9b75dd/vcrpy-6.0.0.tar.gz")
    version("5.1.0", sha256="605e7b7a63dcd940db1df3ab2697ca7faf0e835c0852882142bafb19649d599e", url="https://pypi.org/packages/2a/5b/3f70bcb279ad30026cc4f1df0a0491a0205a24dddd88301f396c485de9e7/vcrpy-5.1.0-py2.py3-none-any.whl")
    version("5.0.0", sha256="28b66c87be7678896e9e78fee4f6695e3fb153d5d7e5f635416a33658452bb44", url="https://pypi.org/packages/c6/65/b660368b2c14791ac31c2310cbe2e466b73aadc92908f5523154ee200115/vcrpy-5.0.0-py2.py3-none-any.whl")
    version("4.4.0", sha256="560c9d0d8436ced29223ceefb513c3ac3f2e2a60d51a9830f236a1e63167905a", url="https://pypi.org/packages/e9/eb/4a375b1cea2a3012487bc86b9eda667adb3d541e38419968a5d97c0497ae/vcrpy-4.4.0-py2.py3-none-any.whl")
    version("4.3.1", sha256="35398f1b373f32340f39d735ea45f40d679ace316f3dddf8cbcbc2f120e6d1d0", url="https://pypi.org/packages/2f/d0/11a43916c8c2187685a7143aed5209169e0a484c7c1a061882c4f5d77532/vcrpy-4.3.1-py2.py3-none-any.whl")
    version("4.3.0", sha256="8fbd4be412e8a7f35f623dd61034e6380a1c8dbd0edf6e87277a3289f6e98093", url="https://pypi.org/packages/9f/42/463fb8e4da067708299264c09b3c8ce68051e8e4850df2379dc0f49f6968/vcrpy-4.3.0-py2.py3-none-any.whl")
    version("4.2.1", sha256="efac3e2e0b2af7686f83a266518180af7a048619b2f696e7bad9520f5e2eac09", url="https://pypi.org/packages/8b/c5/f9efe3fea61a844ef1c47c800139d02984442a3a61ab4608fb2a682bc78d/vcrpy-4.2.1-py2.py3-none-any.whl")
    version("4.2.0", sha256="7ec280c8d5385652f1117fe32a200e6676614007d9f946af9f07df1e5f92254c", url="https://pypi.org/packages/49/85/29ddc88eeb16308bf335600bb897d4023e37ebca07dcb92428fda15f1ba2/vcrpy-4.2.0-py2.py3-none-any.whl")
    version("4.1.1", sha256="12c3fcdae7b88ecf11fc0d3e6d77586549d4575a2ceee18e82eee75c1f626162", url="https://pypi.org/packages/6e/62/571e9fa5c2a2c986c001d1be99403a5e800d2e72b905e6b1e951148c75c9/vcrpy-4.1.1-py2.py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-pyyaml", when="@1.13:5")
        depends_on("py-six@1.5:", when="@1.13:5.0")
        depends_on("py-urllib3@:1", when="@4.3.1:5 ^python@:3.9")
        depends_on("py-wrapt", when="@1.13:5")
        depends_on("py-yarl", when="@1.13:5")
    # END DEPENDENCIES

