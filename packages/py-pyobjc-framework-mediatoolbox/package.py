# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPyobjcFrameworkMediatoolbox(PythonPackage):
    # BEGIN VERSIONS
    version("10.2", sha256="614ec0a28c810395274aa1d5348a447f67bae4629a3a8372d14162f38e2fc597", url="https://pypi.org/packages/c8/c9/7f17e8424a36c82b7a320ad9ac8699c8956c5d0c8fbb40b557d6506d62d9/pyobjc-framework-MediaToolbox-10.2.tar.gz")
    version("10.1", sha256="56906cd90e1f969656db1fecd5874c6345e160044f54596c288fb0ffdb35cdc5", url="https://pypi.org/packages/e6/93/2294f46dc139f170dfbc413b50c2f3e4b03533e017c8e9dd4a2c33bad3bf/pyobjc-framework-MediaToolbox-10.1.tar.gz")
    version("10.0", sha256="8bd24724b26a0bdcdec7e078261d8777018c9ec275b553dd8e1372afc60778d1", url="https://pypi.org/packages/ba/de/df7b3306d51e6f21b17de460eb39eca2925e2c9ca1005b8c09544ceb1b0a/pyobjc-framework-MediaToolbox-10.0.tar.gz")
    version("9.2", sha256="9b21e9159ee372859ea48b34af39f646016834b37dc8eb35b5b7dafdd2f49831", url="https://pypi.org/packages/e0/03/12e97b39e7603fe66840a72891818354ea680e33045fbf261bdbd2a65413/pyobjc-framework-MediaToolbox-9.2.tar.gz")
    version("9.1.1", sha256="00741730ec1db8e1632e096b66324bd9a0ceaf485fdbb5fec1b1ddecce16a09f", url="https://pypi.org/packages/46/53/fd2b44befdf827e639c46c2e4195e7c3ca55dfad3db16ecfa61228edad58/pyobjc-framework-MediaToolbox-9.1.1.tar.gz")
    version("9.1", sha256="73ca9dae5ba97e27ccdcad941b440960e763d2adf3d8e58e571dd1c26beebbcf", url="https://pypi.org/packages/cb/a7/030d60287ea9d417250d09e4a7857dc7cdbbb36461d4b99788c8a1f0bb47/pyobjc-framework-MediaToolbox-9.1.tar.gz")
    version("9.0.1", sha256="7a6e32e9b3d6e641a982ad7ab00b6b750ea8c1033927d0ba4042c9a0eb2ae9f2", url="https://pypi.org/packages/b1/da/41686fb2300e2898ef2d6e0aa23b0f95617360ea515c5e79295508b9c202/pyobjc-framework-MediaToolbox-9.0.1.tar.gz")
    version("9.0", sha256="baee7dbc81afa85f8202335811d12c89937f06defc9b59848e8b8471c034f8f7", url="https://pypi.org/packages/ec/a4/a0f4fa67b3a9590d70ca1de8a8e7716d15818fbbba2f10df5f613f1ad529/pyobjc-framework-MediaToolbox-9.0.tar.gz")
    version("8.5.1", sha256="88da2e33cbddd95d7bba56948465dd53b3b0e6b8164248b86a8e93cc0900b691", url="https://pypi.org/packages/b6/7c/e71180e5c351ce8c0749147332b93e60331566d5a4d78e16228351c78606/pyobjc-framework-MediaToolbox-8.5.1.tar.gz")
    version("8.5", sha256="46d777892de00abc492adcbbb59752780f838ecde3ec168de618a95db50eaa0f", url="https://pypi.org/packages/d8/f8/0d22728b45378f7e832cb5895fdfbd50b1513d51ddfe9625d624f8a39d38/pyobjc-framework-MediaToolbox-8.5.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-pyobjc-core@10.2:", when="@10.2:")
        depends_on("py-pyobjc-core@10.1:", when="@10.1")
        depends_on("py-pyobjc-core@10:", when="@10:10.0")
        depends_on("py-pyobjc-framework-cocoa@10.2:", when="@10.2:")
        depends_on("py-pyobjc-framework-cocoa@10.1:", when="@10.1")
        depends_on("py-pyobjc-framework-cocoa@10:", when="@10:10.0")
    # END DEPENDENCIES

