##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyLoguru(PythonPackage):
    version("0.7.2", sha256="003d71e3d3ed35f0f8984898359d65b79e5b21943f78af86aa5491210429b8eb", url="https://pypi.org/packages/03/0a/4f6fed21aa246c6b49b561ca55facacc2a44b87d65b8b92362a8e99ba202/loguru-0.7.2-py3-none-any.whl")
    version("0.7.1", sha256="046bf970cb3cad77a28d607cbf042ac25a407db987a1e801c7f7e692469982f9", url="https://pypi.org/packages/19/a9/4e91197b121a41c640367641a510fd9a05bb7a3259fc9678ee2976c8fd00/loguru-0.7.1-py3-none-any.whl")
    version("0.7.0", sha256="b93aa30099fa6860d4727f1b81f8718e965bb96253fa190fab2077aaad6d15d3", url="https://pypi.org/packages/71/bd/337f7a0cd2628c4c77512d78e26f93b13c327a2ddf2132001dd78c000bf4/loguru-0.7.0-py3-none-any.whl")
    version("0.6.0", sha256="4e2414d534a2ab57573365b3e6d0234dfb1d84b68b7f3b948e6fb743860a77c3", url="https://pypi.org/packages/fe/21/e1d1da2586865a159fc73b611f36bdd50b6c4043cb6132d3d5e972988028/loguru-0.6.0-py3-none-any.whl")
    version("0.5.3", sha256="f8087ac396b5ee5f67c963b495d615ebbceac2796379599820e324419d53667c", url="https://pypi.org/packages/6d/48/0a7d5847e3de329f1d0134baf707b689700b53bd3066a5a8cfd94b3c9fc8/loguru-0.5.3-py3-none-any.whl")
    version("0.5.2", sha256="a5e5e196b9958feaf534ac2050171d16576bae633074ce3e73af7dda7e9a58ae", url="https://pypi.org/packages/a0/f7/85704c74dd5b616a528aa724d359033f4dbec896b604cf12b65c4f9badb1/loguru-0.5.2-py3-none-any.whl")
    version("0.5.1", sha256="e5d362a43cd2fc2da63551d79a6830619c4d5b3a8b976515748026f92f351b61", url="https://pypi.org/packages/59/4f/baee593c195cd4b56cf008c9473347f3b0795b47d3b946e03706a8b43fca/loguru-0.5.1-py3-none-any.whl")
    version("0.5.0", sha256="4688d9e1f31d70e1ec7ccce5305967bc28f377eb1048d009108c11faebe05bcf", url="https://pypi.org/packages/80/b0/4413a201fcdcdc6789050c536d3b4ece601975ded9e0d676ef47f582348d/loguru-0.5.0-py3-none-any.whl")
    version("0.4.1", sha256="074b3caa6748452c1e4f2b302093c94b65d5a4c5a4d7743636b4121e06437b0e", url="https://pypi.org/packages/b2/f4/2c8b94025c6e30bdb331c7ee628dc152771845aedff35f0365c2a4dacd42/loguru-0.4.1-py3-none-any.whl")
    version("0.4.0", sha256="6e3e8d865201f5a301a4eb7563f4c9e979d80fbe6f6fa919b3e3a7e095106c7b", url="https://pypi.org/packages/57/dd/be19f64691d250bbd98906254307abd626dbbd674b019a313f57d6338bc7/loguru-0.4.0-py3-none-any.whl")
    version("0.3.0", sha256="85408b9552adb9a795af102221c7517f35c8b56ffe7b43d98d37e883283854de", url="https://pypi.org/packages/4a/59/9deeeba62ecfcb771c0e76d63fab565e2c229e1e418d0c410d9313fa7a4c/loguru-0.3.0-py3-none-any.whl")
    version("0.2.5", sha256="ebac59630946721fd6207264679b267a8bdc290b086226067d6aad86830e3123", url="https://pypi.org/packages/c4/2d/2861600f1abed3c85e157c78308d3b1de974ad64d67de852a79da9ae7205/loguru-0.2.5-py3-none-any.whl")

    with default_args(type="run"):
        depends_on("py-ansimarkup@1.4:", when="@:0.2")
        depends_on("py-better-exceptions-fork@0.2.1.post6:", when="@:0.2")
        depends_on("py-colorama@0.3.4:", when="@0.3: platform=windows")
        depends_on("py-colorama@0.3.4:", when="@0.2.3:0.2")
        depends_on("py-win32-setctime", when="@0.3: platform=windows")

