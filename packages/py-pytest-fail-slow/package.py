##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPytestFailSlow(PythonPackage):
    version("0.5.0", sha256="e5c8b388d20c5ed06bedb90bc33c5af9f5767c11e5d5d04169c0155dce5a9d5f", url="https://pypi.org/packages/02/be/5ae7ad60612ab291721ce875c2de907b18f895cf00db989bd7333e7b948a/pytest_fail_slow-0.5.0-py3-none-any.whl")
    version("0.4.0", sha256="83a83492b9e5bcb4b3b19d86e8c5159a15edfec44098fe64d2a82507ca546ac0", url="https://pypi.org/packages/2a/8b/0525fa75a1b8ad7fe2fa296fdbf7754c3778e55b8642cc310b894c33da11/pytest_fail_slow-0.4.0-py3-none-any.whl")
    version("0.3.0", sha256="bf8b57a90d13f8f694ad8250c6d2e869714422c5d7f3c2d6541bec7d1706f783", url="https://pypi.org/packages/a2/bb/275f32982bd4f7a5c52639a1cb9571f0716d1b50647e607beb88769d9ff3/pytest_fail_slow-0.3.0-py3-none-any.whl")
    version("0.2.0", sha256="f23a2d39e5e3122c553c93d30824cd5ac0565845deb4ba76101fd080ca088986", url="https://pypi.org/packages/74/bd/72b60ec93447adb8803fd8e78d8aa79610a12bc0e0fae94c0b3240d0099f/pytest_fail_slow-0.2.0-py3-none-any.whl")

    with default_args(type="run"):
        depends_on("py-pluggy@1.1:", when="@0.5:")
        depends_on("py-pytest@7.0.0:", when="@0.5:")
        depends_on("py-pytest@6.0.0:", when="@:0.4")

