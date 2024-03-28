# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPythonBox(PythonPackage):
    # BEGIN VERSIONS
    version("7.1.1", sha256="2a3df244a5a79ac8f8447b5d11b5be0f2747d7b141cb2866060081ae9b53cc50", url="https://pypi.org/packages/69/0d/b463241f95bc0dc47dee176508fb0c1cf2d5ca100832ccf10b75401bfed4/python-box-7.1.1.tar.gz")
    version("7.1.0", sha256="695eab5c10198d76011f2020ba4dec4a41f640a389fd9991169a060eb1ed132f", url="https://pypi.org/packages/d4/eb/e2fef51eeb6104216c54e0ebf40b8bb9ca5dfd365f99f7ef0c2172176cab/python-box-7.1.0.tar.gz")
    version("7.0.1", sha256="dc6724f88255ccbc07092abd506281439cc2b75c6569c754ffc2b22580e7ae06", url="https://pypi.org/packages/11/b4/3db81c812236f252f833dcfd470a559a26d0a86a0371be70b84f4f283440/python-box-7.0.1.tar.gz")
    version("7.0.0", sha256="727af276177b3c2c0e7e2acea2152269ec85d9fc012a4ffe8df962e2a2d57613", url="https://pypi.org/packages/1f/93/4670446f88543f4b0a8316a6f9b93637c419c50c11dcfba6c9d53654f389/python_box-7.0.0.tar.gz")
    version("6.1.0", sha256="6e7c243b356cb36e2c0f0e5ed7850969fede6aa812a7f501de7768996c7744d7", url="https://pypi.org/packages/9a/85/b02b80d74bdb95bfe491d49ad1627e9833c73d331edbe6eed0bdfe170361/python-box-6.1.0.tar.gz")
    version("6.0.2", sha256="c15f09fa2a8730702115396b490ddc17dde3d4276a4f24eb754e35f102c41347", url="https://pypi.org/packages/39/c5/4091b5e7829144e91b5f4ecd4d5a457a63fb6b9be94de714d3fdae0a14ea/python-box-6.0.2.tar.gz")
    version("6.0.1", sha256="3f394c69e1c484eb18a1a1d6e969428ec9cc70b5f47b921da798c2e41b15d1f7", url="https://pypi.org/packages/26/fb/5ab3045def9e454dc0b5e9bf696980ff7eb363f8de1cbf46014cfb33423a/python-box-6.0.1.tar.gz")
    version("6.0.0", sha256="417a82e67eef760e2ae6278ee5124ff85183b20a8d0138343adadd002c32f253", url="https://pypi.org/packages/7f/d7/fe03663ecae5bbe6f0d43b7eec9d74608869cac937caa2a8654be3d8ac82/python-box-6.0.0.tar.gz")
    version("5.4.1", sha256="60ae9156de34cf92b899bd099580950df70a5b0813e67a3310a1cdd1976457fa", url="https://pypi.org/packages/db/e8/cf1e8543ee7c9cc9b858bf033870c669a91f0fb0e4901a474eff01de6d1e/python_box-5.4.1-py3-none-any.whl")
    version("5.4.0", sha256="992b550d4b51f7fdab80b5d770fd25b03ac47f54042d5bd4c32c6da004d63a0d", url="https://pypi.org/packages/92/67/f4f34c196550cb2694dd69c8224c3ec9f7a28e52b7bfcbfa6f649f6a8bdc/python_box-5.4.0-py3-none-any.whl")
    version("5.3.0", sha256="f2a531f9f5bbef078c175fad6abb31e9b59d40d121ea79993197e6bb221c6be6", url="https://pypi.org/packages/ae/55/b81be1c1456d93db93905b364d19cac5dde22fb8f442b42d41087c2fe28f/python_box-5.3.0-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    variant("extras", default=False)
    # END VARIANTS

    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-ruamel-yaml@0.17:", when="@7.0.0-rc2:7.0.0-rc3")
        depends_on("py-ruamel-yaml", when="@4")
        depends_on("py-toml", when="@4")
        depends_on("py-tomli@1.2.3:", when="@7.0.0-rc2:7.0.0-rc3 ^python@:3.10")
    # END DEPENDENCIES

