# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyScons(PythonPackage):
    # BEGIN VERSIONS
    version("4.5.2", sha256="2f66a1c5c485068a496c12356583eefb2d79e17177278c7334b12b460f0503ce", url="https://pypi.org/packages/a1/a9/a160614f5630192e51bc6e35127d5b39ea6c457f07bc5e34063776370d0e/SCons-4.5.2-py3-none-any.whl")
    version("4.5.1", sha256="d7b0f1c92869c7679eec357b497737803620228d44de123d89fe4ae92e890cb0", url="https://pypi.org/packages/41/87/72d174c9bf6c0a21b9e54067eff65c052fcd5b960f7cf64123f502c88503/SCons-4.5.1-py3-none-any.whl")
    version("4.4.0", sha256="cbbd73b83cf85f1aaaf986370359de1bbfd3af97a765cb3554734f6dcec734e1", url="https://pypi.org/packages/1a/e1/7fad50e1baa7068e3e2382b11c4d00190238798d62bfa6bbfa8619c19f39/SCons-4.4.0-py3-none-any.whl")
    version("4.3.0", sha256="8c13911a2aa40552553488f7d625af4c0768fc8cdedab4a858d8ce42c8c3664d", url="https://pypi.org/packages/6d/41/8d65a5a7f2642a4444dda4538496228a08f0da37230fd79b3f1897d319e0/SCons-4.3.0-py3-none-any.whl")
    version("4.2.0", sha256="663f819e744ddadcdf4f46b03289a7210313b86041efe1b9c8dde81dba437b72", url="https://pypi.org/packages/d8/29/401703b6ce7ad8b4009ab16a435a7c08827357e1c7217ad39e750e75a358/SCons-4.2.0-py3-none-any.whl")
    version("4.1.0.post1", sha256="52272288986f3e401d28590562c573405dff0decfbf701926e751c0954b64da6", url="https://pypi.org/packages/de/8c/4da2c7dd43466383b7ade4189d995c2102248f507af7ba6f456df0854920/SCons-4.1.0.post1-py3-none-any.whl")
    version("4.0.1", sha256="9b4696a806fb73f402fbf5e37ab0e8b6cd0dcef990a91210d7ed4aacbcc5231d", url="https://pypi.org/packages/46/0d/2fd3d3c6bc1c60836d165c643d419c33ebcb8fa6dbc6855f36db1f9721d8/SCons-4.0.1-py3-none-any.whl")
    version("4.0.0", sha256="cfeacab4686e1f764ac8aeb8373b5bd11bdd1c3e6961fc0dde7936bba1acdd58", url="https://pypi.org/packages/03/88/d1e6b14bb83ad0b849568cb20a78e3717bf64ebb2ff5126ccb56b8bee265/SCons-4.0.0-py3-none-any.whl")
    version("3.1.2", sha256="0f860678cd96fc943ff2294389b0f33cbe51080801591497bc652e72237f0176", url="https://pypi.org/packages/90/ff/01a273c627f48079285a8be6bf4aadb95d6d6c1793c114c6876fc28aab5c/scons-3.1.2-py2.py3-none-any.whl")
    version("3.1.1", sha256="822b99f82295dfa1270f613d63a9cd43cd007c7e98b48cee28067d9c3c9fd593", url="https://pypi.org/packages/ab/82/b27f1795375f3112552709f472990560e174fca1a80b9ea66e9cd21a3ffd/scons-3.1.1-py2.py3-none-any.whl")
    version("3.1.0", sha256="84ff89dc0509420ed76c16a8f18076a572dc1f88d51fe5ada01fce5df5cbbbf9", url="https://pypi.org/packages/27/f8/9f5b901eb29ba8529568a5af44c36c269f683e8f6f641040fbec7eb8755f/scons-3.1.0-py2.py3-none-any.whl")
    version("3.0.5", sha256="8c2353ae3ce559e9361baa254c0c85d3eb099d5f96e44b5bc586801b7c756a06", url="https://pypi.org/packages/65/41/ac58638421414acc64e26fc120c81c12bc2b1ebcea9e7e0939149878f0a3/scons-3.0.5-py2.py3-none-any.whl")
    version("3.0.4", sha256="ed5939fcd9c6aa196e054026501627a28e9fe08e3afc57237713fcfd69d2b857", url="https://pypi.org/packages/13/31/43b96f5b79731468a6731e4dbc71601f67fdeddad053bd4f1d1e2f0dbeec/scons-3.0.4-py2.py3-none-any.whl")
    version("3.0.1", sha256="24475e38d39c19683bc88054524df018fe6949d70fbd4c69e298d39a0269f173", url="https://pypi.org/packages/c1/0a/520a3c86ce5cff36e81af5e91d4dcd741ebc189c2f0f42d54cc12a8a7519/scons-3.0.1.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-pywin32", when="@4:4.0 platform=windows")
        depends_on("py-setuptools", when="@4:4.6")
    # END DEPENDENCIES

