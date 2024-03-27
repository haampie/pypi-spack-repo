##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyMmtfPython(PythonPackage):
    version("1.1.3", sha256="502031c509a8a6d73e042781abbd88b84c1afffe65097eb0c1b70f329ffd1e6e", url="https://pypi.org/packages/3c/f1/efea3da858043ed9c078f507ab744b6d00933c7bc8a75a24821937600178/mmtf_python-1.1.3-py2.py3-none-any.whl")
    version("1.1.2", sha256="a00136e9798e84f58f509a8bc341834e497169c1079bd757c12bc1a4ce736b57", url="https://pypi.org/packages/af/d2/aabefd607ff89e35704574205b382a351f531885cc98bfd91baaf192a9fe/mmtf_python-1.1.2-py2.py3-none-any.whl")
    version("1.1.1", sha256="9b9bfeb360815ba0228a64c6375434c5960ce351feee1c3f47d64f287e0de917", url="https://pypi.org/packages/13/f0/7d61237cebccbd8c0fd06f952ebd3b899989648dce4cdfb45a9f0395c0fd/mmtf_python-1.1.1-py2.py3-none-any.whl")
    version("1.1.0", sha256="4f546018781892a342904ee53a1b73c416eceb7c77ccb6bf5eed98191b8152d3", url="https://pypi.org/packages/bf/dd/7b32297dbe01e3d3ab0d78e6da1bf4abc37666a18d652efb2900bda874c7/mmtf_python-1.1.0-py2.py3-none-any.whl")
    version("1.0.12", sha256="d9c7f602787de65e8a5590fce0560271d43dc52c032c5594e8e5ffa9eec46a68", url="https://pypi.org/packages/c5/ea/640543206702d225f63c418ec0f5ab3485cad0e1076a754883e423dbdf4f/mmtf_python-1.0.12-py2.py3-none-any.whl")
    version("1.0.11", sha256="a7f1f24355425270b5ca6fe0253efde8c0f850920e2d5f20c8b7ec376da1b729", url="https://pypi.org/packages/60/22/849dfd18af78745dab098bae85d3e499c58ad54ed13e719c619a67637a6f/mmtf_python-1.0.11-py2.py3-none-any.whl")
    version("1.0.10", sha256="7c9ca14081f3aab666ab7a869b68b2f9f72c9e1f29295808c9a9c5f4b0f555aa", url="https://pypi.org/packages/61/91/3c6eefb2a4456d391ec780660e7bf35754229810e04de5f69aad6088aa82/mmtf_python-1.0.10-py2.py3-none-any.whl")
    version("1.0.9", sha256="cad7ff97af14a65218fc260ec3c05dc80402e91f74d5f36b4d3fcd599fd9fb11", url="https://pypi.org/packages/44/8e/dd99344f1f69dc4630824f22dc0f6fe4e1522b36c788ab0bbc9b7de3ab4e/mmtf_python-1.0.9-py2.py3-none-any.whl")
    version("1.0.7", sha256="e91c9ec2aef02c9a1136f0e481b934c18667f04584ad29e28855fc3316c6f055", url="https://pypi.org/packages/ec/8d/937affce884fb217ebf840ce189306e29bcc95a1ab9005b2940489bb70bb/mmtf-python-1.0.7.tar.gz")
    version("1.0.6", sha256="4b92567baf09a1c50244f30f3aba2d006e967e82fe679418ae4c5a7d48e9258f", url="https://pypi.org/packages/7f/08/ee39222787d9eebd907f6ffa3fab61c5c5be00838b41e54901e88992f017/mmtf-python-1.0.6.tar.gz")

    with default_args(type="run"):
        depends_on("py-msgpack@1.0.0:", when="@1.1.3:")
        depends_on("py-msgpack@0.5.6:", when="@1.1.2")
        depends_on("py-msgpack-python", when="@1.0.9:1.1.1")

