# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PySelenium(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("4.19.0", sha256="5b4f49240d61e687a73f7968ae2517d403882aae3550eae2a229c745e619f1d9", url="https://pypi.org/packages/b4/f9/e9ac5e4c5d84b07c7d117d67b2c84be221bcb9e62ff31fd0a1bbc06099c0/selenium-4.19.0-py3-none-any.whl")
    version("4.18.1", sha256="b24a3cdd2d47c29832e81345bfcde0c12bb608738013e53c781b211b418df241", url="https://pypi.org/packages/3f/fd/c2e7bb547b5b96c7bd536b4a80c4564b7ce5cd38d10095fbba8648996ab9/selenium-4.18.1-py3-none-any.whl")
    version("4.18.0", sha256="d0ac1ab0aa50dffad8050e7f0170395ea23bcecccf7d59b69bc430e47eeb9dac", url="https://pypi.org/packages/5d/f5/9962920f79636d14c8ea62753d62b70a8342341824114c6d29a0f117c9dd/selenium-4.18.0-py3-none-any.whl")
    version("4.17.2", sha256="5aee79026c07985dc1b0c909f34084aa996dfe5b307602de9016d7a621a473f2", url="https://pypi.org/packages/97/e3/fd7272d6d2c49fd49a79a603cb28c8b5a71f8911861b4a0409b3c006a241/selenium-4.17.2-py3-none-any.whl")
    version("4.17.1", sha256="8375a25188ffd478ad54f653a125efe23477dfbce93af94d46667f3945270bcf", url="https://pypi.org/packages/cd/a7/496e7ff189f1394b011a9b8bbcf1aea8e2ee8c4ae496c2d41a141aceaaac/selenium-4.17.1-py3-none-any.whl")
    version("4.17.0", sha256="577a4796e1b6a3d8e5da7fc5c34a8701a4a8c159fe9b80cb609edb5e0ab0ba32", url="https://pypi.org/packages/d7/12/194a5ff4b922b8a08126bd8ce0cb4e8d8a9bad424a6dfb2504980569ee42/selenium-4.17.0-py3-none-any.whl")
    version("4.16.0", sha256="aec71f4e6ed6cb3ec25c9c1b5ed56ae31b6da0a7f17474c7566d303f84e6219f", url="https://pypi.org/packages/dc/72/96b5afa16908f9abc7c24b70adfd3a46c9740eb728ddfeab28379e38eaf9/selenium-4.16.0-py3-none-any.whl")
    version("4.15.2", sha256="9e82cd1ac647fb73cf0d4a6e280284102aaa3c9d94f0fa6e6cc4b5db6a30afbf", url="https://pypi.org/packages/0e/59/aae37fa93e2d4292c3148efcc3066c8ecfe5cfaa72bf8c0b1a5614622cf7/selenium-4.15.2-py3-none-any.whl")
    version("4.15.1", sha256="e3a4ebdcc3eed27eec69f8000d798923dbf4897c97cc6441eb88a1386809170d", url="https://pypi.org/packages/cc/8c/f5d381dbb171e2108f9a384e9f551af39dc5097c96c1fc635ab732437826/selenium-4.15.1-py3-none-any.whl")
    version("4.15.0", sha256="c566dd3b20765dad64e65edca19a52f421f601ed1739f87dd4c5c07aae5dae6f", url="https://pypi.org/packages/60/80/18b9a8a3e3097d660f85b01906f31c90733416c9a026cb6b67ba6d794eca/selenium-4.15.0-py3-none-any.whl")
    version("3.141.0", sha256="2d7131d7bc5a5b99a2d9b04aaf2612c411b03b8ca1b1ee8d3de5845a9be2cb3c", url="https://pypi.org/packages/80/d6/4294f0b4bce4de0abf13e17190289f9d0613b0a44e5dd6a7f5ca98459853/selenium-3.141.0-py2.py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-certifi@2021.10:", when="@4.4.3:")
        depends_on("py-trio@0.17:", when="@4.0.0-beta3:")
        depends_on("py-trio-websocket@0.9:", when="@4.0.0-beta3:")
        depends_on("py-typing-extensions@4.9.0:", when="@4.17.2:")
        depends_on("py-urllib3@1.26:+socks", when="@4.9.1:")
    # END DEPENDENCIES

