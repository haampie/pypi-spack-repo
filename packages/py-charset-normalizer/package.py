# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyCharsetNormalizer(PythonPackage):
    # BEGIN VERSIONS
    version("3.3.0", sha256="63563193aec44bce707e0c5ca64ff69fa72ed7cf34ce6e11d5127555756fd2f6", url="https://pypi.org/packages/cf/ac/e89b2f2f75f51e9859979b56d2ec162f7f893221975d244d8d5277aa9489/charset-normalizer-3.3.0.tar.gz")
    version("3.1.0", sha256="34e0a2f9c370eb95597aae63bf85eb5e96826d81e3dcf88b8886012906f509b5", url="https://pypi.org/packages/ff/d7/8d757f8bd45be079d76309248845a04f09619a7b17d6dfc8c9ff6433cac2/charset-normalizer-3.1.0.tar.gz")
    version("2.1.1", sha256="83e9a75d1911279afd89352c68b45348559d1fc0506b054b346651b5e7fee29f", url="https://pypi.org/packages/db/51/a507c856293ab05cdc1db77ff4bc1268ddd39f29e7dc4919aa497f0adbec/charset_normalizer-2.1.1-py3-none-any.whl")
    version("2.0.12", sha256="6881edbebdb17b39b4eaaa821b438bf6eddffb4468cf344f09f89def34a8b1df", url="https://pypi.org/packages/06/b3/24afc8868eba069a7f03650ac750a778862dc34941a4bebeb58706715726/charset_normalizer-2.0.12-py3-none-any.whl")
    version("2.0.7", sha256="f7af805c321bfa1ce6714c51f254e0d5bb5e5834039bc17db7ebe3a4cec9492b", url="https://pypi.org/packages/de/c8/820b1546c68efcbbe3c1b10dd925fbd84a0dda7438bc18db0ef1fa567733/charset_normalizer-2.0.7-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("python@3.7:", when="@3.1:")
    # END DEPENDENCIES

