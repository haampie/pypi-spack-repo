##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyClickRepl(PythonPackage):
    version("0.3.0", sha256="fb7e06deb8da8de86180a33a9da97ac316751c094c6899382da7feeeeb51b812", url="https://pypi.org/packages/52/40/9d857001228658f0d59e97ebd4c346fe73e138c6de1bce61dc568a57c7f8/click_repl-0.3.0-py3-none-any.whl")
    version("0.2.0", sha256="cd12f68d745bf6151210790540b4cb064c7b13e571bc64b6957d98d120dacfd8", url="https://pypi.org/packages/60/30/11d3f09eff5ae3627bca79563855035e8d241444520500a3c7914eae6a74/click-repl-0.2.0.tar.gz")
    version("0.1.6", sha256="b9f29d52abc4d6059f8e276132a111ab8d94980afe6a5432b9d996544afa95d5", url="https://pypi.org/packages/51/99/6a722e232f92fdc21c46fd042fea63e7c2fcda3086ff5db62edd595d3f49/click-repl-0.1.6.tar.gz")

    with default_args(type="run"):
        depends_on("py-click@7:", when="@0.3:")
        depends_on("py-prompt-toolkit@3.0.36:", when="@0.3:")

