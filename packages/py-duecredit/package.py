# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyDuecredit(PythonPackage):
    # BEGIN VERSIONS
    version("0.9.2", sha256="fb64bdbadfbbc598b0acc5066154a5c46e2772f975738365573c1746ffcaf31b", url="https://pypi.org/packages/14/89/3143635ce114edf19f03a1e16f3c71a76f5a43402257b43a36a9ce155638/duecredit-0.9.2-py3-none-any.whl")
    version("0.9.1", sha256="202944e97f195503d964f838a4f7994c8d9efbdbb71027f0e3ed5fc42e83e6da", url="https://pypi.org/packages/37/8a/9c69652395715d88ea72a4f9733e687f17d5f7937b7b0745d02e792e9b5a/duecredit-0.9.1-py3-none-any.whl")
    version("0.6.5", sha256="da3746c24f048e1b2e9bd15c001f0f453a29780ebb9d26367f478a63d15dee9b", url="https://pypi.org/packages/a6/6c/cf8dcf6522f342c624ecd39f86dc1358041863028e8b9bbab7e194e033f2/duecredit-0.6.5.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-citeproc-py@0.4:", when="@0.9.1:")
        depends_on("py-requests", when="@0.9.1:")
        depends_on("py-six", when="@0.9.1:0.9.2")
    # END DEPENDENCIES

