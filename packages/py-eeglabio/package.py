# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyEeglabio(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("0.0.2.post4", sha256="76ce4da4a33fc6ec53830756dab04cdda9f7b4e01ee91b0d7d4055d3382d17ae", url="https://pypi.org/packages/71/1e/4d4df763057a0e003255603dc2634ce9e0ef352fbaa16b101b2492763212/eeglabio-0.0.2.post4-py3-none-any.whl")
    version("0.0.2.post3", sha256="0416106a390bcb1a2f74f25f4a2d3591c7fe3812475c6114345356abf648eb14", url="https://pypi.org/packages/b8/ac/153041bc35301359b31ab894486004c2b657b3c7e92e0f472b4f82253fbb/eeglabio-0.0.2.post3-py3-none-any.whl")
    version("0.0.2.post2", sha256="9ea2081aea2b756ae0c1478bee6e6ad6773927d0a9ef3f82a9e43c6f03aa072a", url="https://pypi.org/packages/d1/9e/5e3cc66d957767478146cd8a402c23aaa37a418e24b59f9127f981b6bf65/eeglabio-0.0.2.post2-py3-none-any.whl")
    version("0.0.2.post1", sha256="ab6a9738f89fec84313c56553e793a1ccc772ea36fd6e066bc0f9644d0d21c42", url="https://pypi.org/packages/3d/d0/46d244bc1d506807e5f957433e4ec08cfc8ed7b73d52ea419baaeeae972d/eeglabio-0.0.2.post1-py3-none-any.whl")
    version("0.0.2", sha256="b459ef955ecb9306711e15a29941f38ee42cbf46eb67b6382cb8fb05d3f0e523", url="https://pypi.org/packages/b2/f6/a086af930c75c87d319995b0d2036556cd783a0d94a2a24c000b41a42fdf/eeglabio-0.0.2-py3-none-any.whl")
    version("0.0.1.post7", sha256="d9729e3fa21165e2e8fbac6efb6a9bf804350b83bf4946689238da7797e29299", url="https://pypi.org/packages/f6/f5/eabadd0e4c559b49a72aedcb04723058c013bf4bafa9efd455c22a82bf31/eeglabio-0.0.1.post7-py3-none-any.whl")
    version("0.0.1.post6", sha256="d1e78c982faffd1811e4e23989a875e71796c6f9d486005d23a6a7ba3e703138", url="https://pypi.org/packages/03/71/7066cc70840dd50ac4d3d0925559d4979dbe8e792c4be243e0a4bf63f701/eeglabio-0.0.1.post6-py3-none-any.whl")
    version("0.0.1", sha256="16a83a483d273f4061703e36f12bc7213379646b84054c5e634f4420e10d9944", url="https://pypi.org/packages/13/b8/3dbae7b94ffd0cdff139e91feccbce56eadc49a171f3cdbceeab787e073a/eeglabio-0.0.1-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-numpy")
        depends_on("py-scipy")
    # END DEPENDENCIES

