##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPytestArraydiff(PythonPackage):
    version("0.6.1", sha256="64be1cc8e79874203eca80b1959134b8bb7a47b41cf7631310ba7fe6e5840694", url="https://pypi.org/packages/cf/2a/2f8efb1ef8048aec7b44f37bc3fecb8c2c22e3238781d3e93c58d9c89268/pytest_arraydiff-0.6.1-py3-none-any.whl")
    version("0.6.0", sha256="ea06c6f6937ef2a283f2404a217059bfec6fc70bff224fbe7408eb24035e8c74", url="https://pypi.org/packages/44/b1/e6feda4d84a79d3fcfeb89286294b08de49f8e03a229f657ea610da1db06/pytest_arraydiff-0.6.0-py3-none-any.whl")
    version("0.5.0", sha256="3a638f8b30ed0174e680b7ae57b66884451ffcdd08000530e4f03da23539b6da", url="https://pypi.org/packages/10/dc/6a8a855f80b79491295174f986df6dc34a0bb0459a6b7aeb19ae9385638c/pytest_arraydiff-0.5.0-py3-none-any.whl")
    version("0.4.0", sha256="25635705a0a38b3ef336786afa39fa7a3525dac85c9699ba666055b0af6973e8", url="https://pypi.org/packages/23/df/c0808e83754dfbc7f6a6b0b614a686dd75980cf03efe465e5cd51570b88c/pytest_arraydiff-0.4.0-py3-none-any.whl")
    version("0.3", sha256="7d981cf9c09178f40d00c7b791a226438a2c1b46f210ddaaaa1c6aa63cae6456", url="https://pypi.org/packages/b2/dd/0096e95a7da9d6cd566c35bd85b97659303007c2e8a3573c5d51fbf5da3d/pytest_arraydiff-0.3-py2.py3-none-any.whl")
    version("0.2", sha256="0bc7ae769bfe02e7f797c1251481d0490fedfa5092c1ededa039cd3a316df850", url="https://pypi.org/packages/c5/13/fbaf81f14374c2a27782ed43a5e035d80af15982e27cc04888a1d3c8c244/pytest_arraydiff-0.2-py2.py3-none-any.whl")
    version("0.1", sha256="4ca5aaa9a8dc55f0cf621ce6cca3060e320e32b1a500e2f87298ade0a5ece7e1", url="https://pypi.org/packages/04/65/5d1c98e6f9f8ff97f771d9bc7a349948418f9a7e86c9285f63853861af51/pytest-arraydiff-0.1.tar.gz")

    with default_args(type="run"):
        depends_on("py-astropy", when="@0.4")
        depends_on("py-numpy", when="@0.2:")
        depends_on("py-pytest@4.6:", when="@0.4:")
        depends_on("py-pytest", when="@0.2:0.3")
        depends_on("py-six", when="@0.2:0.3")

