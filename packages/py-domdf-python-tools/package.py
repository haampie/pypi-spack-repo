# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyDomdfPythonTools(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("3.8.0.post2", sha256="ad2c763c8d00850a7fa92ad95e9891a1918281ea25322c4dbb1734fd32f905dd", url="https://pypi.org/packages/fc/f4/04a47fc3cbb88b8353e8656b58a75e9d6512d367fc2132adcd6a18b8d720/domdf_python_tools-3.8.0.post2-py3-none-any.whl")
    version("3.8.0", sha256="538473f77bb1c4165dec40eac6c4a08bca7a722bf1cb5a61e82d4324e0dcc704", url="https://pypi.org/packages/32/1c/c32f829c5687396b12d5e5fd44d51e250b04b0bc7e35637d32d2aa4d3059/domdf_python_tools-3.8.0-py3-none-any.whl")
    version("3.7.0", sha256="7b4d1c3bdb7402b872d43953824bf921ae2e52f893adbe5c0052a21a6efa2fe4", url="https://pypi.org/packages/3d/3e/7184534c0e48ee06d1a245878c4e01aad235fd0eebb5d80a7cb47272cba3/domdf_python_tools-3.7.0-py3-none-any.whl")
    version("3.6.1", sha256="e18158460850957f18e740eb94ede56f580ddb0cb162ab9d9834ed8bbb1b6431", url="https://pypi.org/packages/1d/02/3f4c36a3f2c4ee55bf28c31c36b0a795ccaed144cebb4ece9c94ac587952/domdf_python_tools-3.6.1-py3-none-any.whl")
    version("3.6.0", sha256="7a0a3b2c716854465b09b5c0c5f53d41f37562c5a0cd8746cd042ad7955430f1", url="https://pypi.org/packages/22/bb/607177e87ebfbc7d8d86a2e134fff4bda20def1ecd8bc8d1ca79939af974/domdf_python_tools-3.6.0-py3-none-any.whl")
    version("3.5.1", sha256="286aa13883ff648be3543199535519d2fb3e897c3cb1f413fad5502222574143", url="https://pypi.org/packages/6d/26/edd75ea74f54082541befba71f37fc39c61c88fe08b5c6b5662be75c7263/domdf_python_tools-3.5.1-py3-none-any.whl")
    version("3.5.0", sha256="51450c885ee8f02c7e53749a7105df8925dbf3ec0bd822899776a6f941ff8f01", url="https://pypi.org/packages/9e/7c/bbb303376c79c599351cfa18e67972955602b5c1aea6683542b15e8c0222/domdf_python_tools-3.5.0-py3-none-any.whl")
    version("3.4.0", sha256="fe2cd1785964f079067d5fa90ae57bb481f1fc385216b629683c096d8de3282c", url="https://pypi.org/packages/af/5b/4fa14103dccbb34916e6c6bb2f044500933db6059be5fef88bcc55db9bdc/domdf_python_tools-3.4.0-py3-none-any.whl")
    version("3.3.0", sha256="692a33cfc4bc4270a30f18b95beb8f65bf56935d122a4bdb0af7f7760452d41c", url="https://pypi.org/packages/40/d6/de8b9c9c42f0dff38b68f271e5e782ae9a89284b8b81d7e52cf544099feb/domdf_python_tools-3.3.0-py3-none-any.whl")
    version("3.2.2.post1", sha256="70a9771dea6f5aa37779d2a86d4abaf63f8fa305e3313a53f71f45b8c8c5fd08", url="https://pypi.org/packages/20/72/b7c3a3eae2d227a6e837599ff56ff96392b79bd8613594b81a44bc7a8bb5/domdf_python_tools-3.2.2.post1-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-importlib-metadata@3.6:", when="@3: ^python@:3.8")
        depends_on("py-natsort@7.0.1:", when="@3:")
        depends_on("py-typing-extensions@3.7.4.1:", when="@3:")
    # END DEPENDENCIES

