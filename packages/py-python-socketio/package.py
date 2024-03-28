# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPythonSocketio(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("5.11.2", sha256="b9f22a8ff762d7a6e123d16a43ddb1a27d50f07c3c88ea999334f2f89b0ad52b", url="https://pypi.org/packages/af/bf/be12875b17709b591d8505811e513a88b31316e4ce0e801da351b4765ea5/python_socketio-5.11.2-py3-none-any.whl")
    version("5.11.1", sha256="f1a0228b8b1fbdbd93fbbedd821ebce0ef54b2b5bf6e98fcf710deaa7c574259", url="https://pypi.org/packages/06/50/1dc8262920f10e2f94376295fe4c6c7237d5dfadbf34365f403e24727345/python_socketio-5.11.1-py3-none-any.whl")
    version("5.11.0", sha256="cfcb0163d77c8d23b98285754e79016786740dd901268654a52823da0bc73382", url="https://pypi.org/packages/5c/6d/dd2447d27979c4ca84738bb4d5a9245aa8e1f736b4054d894f7fd2030c84/python_socketio-5.11.0-py3-none-any.whl")
    version("5.10.0", sha256="fb18d9b84cfb05289dc207b790c3de59cd242310d9b980b1c31e9faf4f79101a", url="https://pypi.org/packages/f8/bf/4790ed063ca2daa58fb20285fc3707218cf01e174209355d081d83094f6d/python_socketio-5.10.0-py3-none-any.whl")
    version("5.9.0", sha256="c20f12e4ed0cba57581af26bbeea9998bc2eeebb3b952fa92493a1e051cfe9dc", url="https://pypi.org/packages/2b/31/fd41960cf365177f323d8c10d774a0b017336556c6f0ba0a38403240914d/python_socketio-5.9.0-py3-none-any.whl")
    version("5.8.0", sha256="7adb8867aac1c2929b9c1429f1c02e12ca4c36b67c807967393e367dfbb01441", url="https://pypi.org/packages/5d/e9/f296186e2a91f1472b9da74346163411196dc1b17f425acf088f293b32cc/python_socketio-5.8.0-py3-none-any.whl")
    version("5.7.2", sha256="d9a9f047e6fdd306c852fbac36516f4b495c2096f8ad9ceb8803b8e5ff5622e3", url="https://pypi.org/packages/5c/27/3a215e5fc16e371fa8e9bca75d37e120d05c8dd5030905b6657ae8c96d13/python_socketio-5.7.2-py3-none-any.whl")
    version("5.7.1", sha256="86ee93591c1e781d339d9a61940e62fd6cbc838390653b52a7bcc4f7ce89fe47", url="https://pypi.org/packages/d3/b0/862b095d2c6e7892c7be2056efe02d4faea62ee35b3ed10b905fdfa3d74a/python_socketio-5.7.1-py3-none-any.whl")
    version("5.7.0", sha256="874eeba29129618b30189ecb277e2d5e646c39e50b1a997289c0473ee6c1f5c8", url="https://pypi.org/packages/af/48/0bb17751d2481ea1734114b84db81f489be4c0ad632e9d77a5a419056461/python_socketio-5.7.0-py3-none-any.whl")
    version("5.6.0", sha256="41d6d93831aac6e0e4917dee2a1d0a0fadaa3fb362d34fc14e98c379e6f20503", url="https://pypi.org/packages/5a/57/02593427a762774d6c9e9dec82fde33763723e6b17cce3feaed275d8bf7c/python_socketio-5.6.0-py3-none-any.whl")
    version("1.8.4", sha256="b09f5ab6253f54f745a4a36ff29d2e15c2cd6cc07587c7e8e73d5410f30f50c8", url="https://pypi.org/packages/c7/30/9bb9747a78a8680deffeaf82d36e89db20452b72c0fddaf65574227832b9/python_socketio-1.8.4-py2.py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    variant("eventlet", default=False)
    # END VARIANTS

    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-bidict@0.21:", when="@5:")
        depends_on("py-python-engineio@4.8:", when="@5.10:")
        depends_on("py-python-engineio@4.7:", when="@5.9")
        depends_on("py-python-engineio@4.3:", when="@5.5:5.8")
    # END DEPENDENCIES

