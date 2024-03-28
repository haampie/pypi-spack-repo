# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyIpympl(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("0.9.3", sha256="d113cd55891bafe9b27ef99b6dd111a87beb6bb2ae550c404292272103be8013", url="https://pypi.org/packages/08/5b/83a88a44e5dd185104c400e0ed6cdba50c776a8f494d525298bb09db2e5c/ipympl-0.9.3-py2.py3-none-any.whl")
    version("0.9.2", sha256="655604f0bf6d264cf599766950a5b26e292d107cc23e197503647e75417981cc", url="https://pypi.org/packages/2b/9d/33e2e196ecf80b385260301927bfe238b18af3f92a52e4317be330690663/ipympl-0.9.2-py2.py3-none-any.whl")
    version("0.9.1", sha256="3505b472d412178fd115e255764d1e7e7632d6c82e9de6d62b25438a35374680", url="https://pypi.org/packages/11/e8/75891f584aa1636c6a36974e69baf9425aee57718e2b151e0f6e637204f7/ipympl-0.9.1-py2.py3-none-any.whl")
    version("0.9.0", sha256="1e93b74ffcd16e29b1775fa75246d299c963ee73ec318b9250ad15248b5942ce", url="https://pypi.org/packages/e2/6b/07bbbbbe75f2dfd5d43c2856ac9a1698d8fa1804d38c0c3331edd96106ef/ipympl-0.9.0-py2.py3-none-any.whl")
    version("0.8.8", sha256="86468aeaae8c0a28007d0c7f6dbb85f2b6cb9805167e88d4daa7529562009159", url="https://pypi.org/packages/81/13/12a4761eb01a59e7f185af7b9543a9aef9495c42a5f77d8b8c4d51794f8c/ipympl-0.8.8-py2.py3-none-any.whl")
    version("0.8.7", sha256="11c3d01f0555f855c51a960964e3ab4dff38e6ccd1a4695205fe250341a9eb99", url="https://pypi.org/packages/58/9b/3fc587599c11e9ccb6fb0b806257c8d1ba871d44104302ac42767770ec39/ipympl-0.8.7-py2.py3-none-any.whl")
    version("0.8.6", sha256="3d1504cb80aa0701e2c9da6d1c3c23c998233dbca93061255c7d62a4e7468200", url="https://pypi.org/packages/42/50/b356e63f117122a0590429742574943e12f838ab5279f235059e227de27d/ipympl-0.8.6-py2.py3-none-any.whl")
    version("0.8.5", sha256="120a084d84e6a6a00fc39c73e10345dcd9855efb3fa6e774f3e72057a866715c", url="https://pypi.org/packages/14/7f/0d525e20827abb9c1a3b36594c8fa4d93012cc53e16bd90889c4f6256142/ipympl-0.8.5-py2.py3-none-any.whl")
    version("0.8.4", sha256="2f955c1c04d8e6df883d57866450657040bfc568edeabcace801cbdbaf4d0295", url="https://pypi.org/packages/39/ae/f8ecd43dc18af578cce93bc7eb19f13ebbcfcad12c2f2e32778396934778/ipympl-0.8.4-py2.py3-none-any.whl")
    version("0.8.3", sha256="32ef8adcf6de3674ca50e3aa71cf5036248452647a34e529806e47b2e2d454ba", url="https://pypi.org/packages/5c/b4/68fb4c21c3ad323a01530376aa4401128b918ba1d97b3426c3418af81d71/ipympl-0.8.3-py2.py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-ipykernel@4.7:", when="@0.2:0.8.4")
        depends_on("py-ipython", when="@0.8.6:")
        depends_on("py-ipython@:7", when="@0.8.5")
        depends_on("py-ipython-genutils", when="@0.8.5:")
        depends_on("py-ipywidgets@7.6.0:7", when="@0.8.5:0.9.1")
        depends_on("py-ipywidgets@7.6.0:", when="@0.6:0.8.4,0.9.2:")
        depends_on("py-matplotlib@3.4.0:", when="@0.9:")
        depends_on("py-matplotlib@2.0.0:", when="@0.0.4:0.8")
        depends_on("py-numpy", when="@0.8.5:")
        depends_on("py-pillow", when="@0.8.5:")
        depends_on("py-traitlets", when="@0.8.5:")
    # END DEPENDENCIES

