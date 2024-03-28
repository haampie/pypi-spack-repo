# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyFastprogress(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("1.0.3", sha256="6dfea88f7a4717b0a8d6ee2048beae5dbed369f932a368c5dd9caff34796f7c5", url="https://pypi.org/packages/a7/8f/213223fdee199c55db81e2d0c669f30e8285c5be2526c4ed924de39247da/fastprogress-1.0.3-py3-none-any.whl")
    version("1.0.2", sha256="d00ca857e2e651b08cb4c28f5800e5330d47d2cc50dcc8e0251fa01763c59049", url="https://pypi.org/packages/ef/d3/262caecee633b249afe561722ecad6e51769b4a5c93bfbc912b80db9a5d6/fastprogress-1.0.2-py3-none-any.whl")
    version("1.0.1", sha256="abb43ef7a03aafd14a170bddd7eb457bfb9b24b966ce82cdca83a3246da6cce8", url="https://pypi.org/packages/ca/b1/c1705832649bdcc5a60e312db996bdd203fc1f4bbc02e5fc2ebb1d1973a3/fastprogress-1.0.1-py3-none-any.whl")
    version("1.0.0", sha256="474cd6a6e5b1c29a02383d709bf71f502477d0849bddc6ba5aa80b683f4ad16f", url="https://pypi.org/packages/eb/1f/c61b92d806fbd06ad75d08440efe7f2bd1006ba0b15d086debed49d93cdc/fastprogress-1.0.0-py3-none-any.whl")
    version("0.2.6", sha256="f13593b2b1f33d93377b7e680a31a8f283862118cc6b95dcb6570b9431ea6bae", url="https://pypi.org/packages/fb/21/0705d1ea6193c51157c84ed5eb7c9569d7b3fd9e079806b15f4385415afa/fastprogress-0.2.6-py3-none-any.whl")
    version("0.2.5", sha256="e29260851013b95ddd8d5d179fc92e40cd4e0f879d18da049e5e4731f3338212", url="https://pypi.org/packages/04/bb/d4ccc44ca065a87cabbb257d1b115531e0d8d71a0829ed893d35776c057b/fastprogress-0.2.5-py3-none-any.whl")
    version("0.2.4", sha256="92e12e24700f673020a7184c169e55b6a5d4636806887963c3572621a14d6a9a", url="https://pypi.org/packages/5e/26/6db6f8f976379c04af888bb5d45af64e8b69c5bfb2672a427da2dde89441/fastprogress-0.2.4-py3-none-any.whl")
    version("0.2.3", sha256="8b4d7a6af31bafbe1f17a8e5c29befe514a6d84a920c2d215cb5fac016c8e661", url="https://pypi.org/packages/a3/da/ffd8fe0daf7e679804a32a1e8654ac2988e2ef85937fc1d223e98eee736e/fastprogress-0.2.3-py3-none-any.whl")
    version("0.2.2", sha256="a7837a3339ab49f95b86ba17a8d25b5ebbb6f4f796df7c5964844b74560f8984", url="https://pypi.org/packages/41/67/347d73405b8612e436a4278f577186a8b783fe757df549ba1a82a2986727/fastprogress-0.2.2-py3-none-any.whl")
    version("0.2.1", sha256="48a28d41b57b1842628f87005f13effb78980c1666e3fbe82aaf4f480e3c0616", url="https://pypi.org/packages/84/5b/adef949cf7a8d4f49b30152ea9eb04ad9cf3c0449e8df2ae2e03461a8048/fastprogress-0.2.1-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-numpy", when="@1:1.0.1")
    # END DEPENDENCIES

