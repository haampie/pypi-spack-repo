# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPytestMetadata(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("3.1.1", sha256="c8e0844db684ee1c798cfa38908d20d67d0463ecb6137c72e91f418558dd5f4b", url="https://pypi.org/packages/3e/43/7e7b2ec865caa92f67b8f0e9231a798d102724ca4c0e1f414316be1c1ef2/pytest_metadata-3.1.1-py3-none-any.whl")
    version("3.1.0", sha256="54ce21108708d0f2fdb30c7056ce5789ce052262efff4832892aa92df4a76291", url="https://pypi.org/packages/93/ba/cef0c20e1619795eb1ab60ab3f84688f4681565ad0e3d1adac10e15ee994/pytest_metadata-3.1.0-py3-none-any.whl")
    version("3.0.0", sha256="a17b1e40080401dc23177599208c52228df463db191c1a573ccdffacd885e190", url="https://pypi.org/packages/5c/a0/32d2a73f8428402d3017aec0cbb902ee21b363f421dc111d755c97332904/pytest_metadata-3.0.0-py3-none-any.whl")
    version("2.0.4", sha256="acb739f89fabb3d798c099e9e0c035003062367a441910aaaf2281bc1972ee14", url="https://pypi.org/packages/e1/00/c8175f054e801b5d8135ef2d0d7e4ad508c0af94d81e521431c23cf56e8f/pytest_metadata-2.0.4-py3-none-any.whl")
    version("2.0.3", sha256="7fbb5a09110a7f62060ecad77110c6481e4e3a85e46556605b323fc97c072c7f", url="https://pypi.org/packages/5a/1c/6a3aaeefe562b3b302bc75a4ea895376fd7cad9ff4fbaadb9bc0b535a259/pytest_metadata-2.0.3-py3-none-any.whl")
    version("2.0.2", sha256="39261ee0086f17649b180baf2a8633e1922a4c4b6fcc28a2de7d8127a82541bf", url="https://pypi.org/packages/a3/a9/f6dbb9e03cc3a8e24df9482fc6b5bedafc3774dcb91594b22c1537ef92b6/pytest_metadata-2.0.2-py3-none-any.whl")
    version("2.0.1", sha256="141ba561a17659cda00cf74e7c7cf6103bab4550acad76a46f893339de63b1df", url="https://pypi.org/packages/67/13/ee20734c21daa5009cb6578316cf3122f1924cc856e8a992fafe1919ac7a/pytest_metadata-2.0.1-py3-none-any.whl")
    version("2.0.0", sha256="e25f1a77ed02baf1d83911604247a70d60d7dcb970aa12be38e1ed58d4d38e65", url="https://pypi.org/packages/b8/4d/dff1e45b6a88d95080e523191b472dd3fb3c3af434f125753a1877c39349/pytest_metadata-2.0.0-py3-none-any.whl")
    version("1.11.0", sha256="576055b8336dd4a9006dd2a47615f76f2f8c30ab12b1b1c039d99e834583523f", url="https://pypi.org/packages/e5/12/bfb677aad996cc994efb9c61289a4994d60079587e85155738859fd3b68e/pytest_metadata-1.11.0-py2.py3-none-any.whl")
    version("1.10.0", sha256="fcbcc5781aee450107c620c79c57e50796b6777b82b3c504be9cbc3017201169", url="https://pypi.org/packages/48/4a/9b7cd1743b9b27e482f14440e677869993c4d4ed1c4c80b7cb94efa91ec3/pytest_metadata-1.10.0-py2.py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("python@:3.10", when="@2.0.1")
        depends_on("py-pytest@7.0.0:", when="@3:")
        depends_on("py-pytest@3:7", when="@2.0.1:2")
        depends_on("py-pytest@7.1.1:7", when="@2:2.0.0")
        depends_on("py-pytest@2.9:", when="@1.4:1")
    # END DEPENDENCIES

