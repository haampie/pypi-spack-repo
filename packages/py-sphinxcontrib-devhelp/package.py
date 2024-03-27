##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PySphinxcontribDevhelp(PythonPackage):
    version("1.0.6", sha256="6485d09629944511c893fa11355bda18b742b83a2b181f9a009f7e500595c90f", url="https://pypi.org/packages/a0/52/1049d918d1d1c72857d285c3f0c64c1cbe0be394ce1c93a3d2aa4f39fe3b/sphinxcontrib_devhelp-1.0.6-py3-none-any.whl")
    version("1.0.5", sha256="fe8009aed765188f08fcaadbb3ea0d90ce8ae2d76710b7e29ea7d047177dae2f", url="https://pypi.org/packages/c0/03/010ac733ec7b7f71c1dc88e7115743ee466560d6d85373b56fb9916e4586/sphinxcontrib_devhelp-1.0.5-py3-none-any.whl")
    version("1.0.4", sha256="d4e20a17f78865d4096733989b5efa0d5e7743900e98e1f6ecd6f489380febc8", url="https://pypi.org/packages/5d/b6/7f58acb86c93e54236ca8b5b79dd3873138397060a74a143b1c1e30ba6bf/sphinxcontrib_devhelp-1.0.4-py3-none-any.whl")
    version("1.0.3", sha256="09009e3b1dde7447c9c6973723c786253b9a9342ff0a856bc6957092ee106cd9", url="https://pypi.org/packages/30/68/7e7c2e823a50cc4d0835b962425924fe7006afa2bc7151a79c30b91fcf52/sphinxcontrib_devhelp-1.0.3-py3-none-any.whl")
    version("1.0.2", sha256="8165223f9a335cc1af7ffe1ed31d2871f325254c0423bc0c4c7cd1c1e4734a2e", url="https://pypi.org/packages/c5/09/5de5ed43a521387f18bdf5f5af31d099605c992fd25372b2b9b825ce48ee/sphinxcontrib_devhelp-1.0.2-py2.py3-none-any.whl")
    version("1.0.1", sha256="9512ecb00a2b0821a146736b39f7aeb90759834b07e81e8cc23a9c70bacb9981", url="https://pypi.org/packages/b0/a3/fea98741f0b2f2902fbf6c35c8e91b22cd0dd13387291e81d457f9a93066/sphinxcontrib_devhelp-1.0.1-py2.py3-none-any.whl")
    version("1.0.0", sha256="b89c68cb88a3c22e39f08f3a3ec96e8216547c31313e0c4b6464384a2563a56a", url="https://pypi.org/packages/d5/cb/cb000504c402505d96312ceeaeb8a39de2cb258fd1929a271b06439541e9/sphinxcontrib_devhelp-1.0.0-py2.py3-none-any.whl")

    with default_args(type="run"):
        depends_on("python@3.9:", when="@1.0.3:")
        depends_on("py-sphinx@5.0.0:", when="@1.0.3:1.0.5")

