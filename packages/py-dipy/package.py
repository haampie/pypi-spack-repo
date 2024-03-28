# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyDipy(PythonPackage):
    # BEGIN VERSIONS
    version("1.9.0", sha256="eb0f7a211202d48f30961743528c86ec9804fcba8ca440a7484e0a113fa2cc4f", url="https://pypi.org/packages/0f/a3/488a52b7fe5afb4f8978c7d5e537f6bfb9c5620c910ca8f41fafc64f2472/dipy-1.9.0.tar.gz")
    version("1.8.0", sha256="cc3845585b6ccd5d7bf43094d52a00eb73111072eee36c2149fabdb1b071f008", url="https://pypi.org/packages/45/ce/75b5114eb8124406b3ec69ea76f841326b737b58fc02e4bde32f57cfb793/dipy-1.8.0.tar.gz")
    version("1.7.0", sha256="59bb647128aae7793215c813bb8ea35dae260ac9f0d938c724064f0af5a05cc3", url="https://pypi.org/packages/1a/62/6f1751dbf39790bfc170449c311fa36f97353d993fd057d1e39d47fc5153/dipy-1.7.0.tar.gz")
    version("1.6.0", sha256="41a8487689ddff32f6c45bd046548f9c89a66306779c57c64d7f31400cc4fd6d", url="https://pypi.org/packages/fa/b6/0439408d4692e396a223397d1a48d1d7a81c070bd0e0d84a0f0c55582420/dipy-1.6.0.tar.gz")
    version("1.5.0", sha256="a19cf40166be09c5b7c31ab00b12fed136ae9531483a9cd7019cc3f3b95f6271", url="https://pypi.org/packages/10/8b/2793e13c5b9cae66b4d7deb4476d41357d0b57864f422778933552211e10/dipy-1.5.0.tar.gz")
    version("1.4.1", sha256="b4bf830feae751f3f985d54cb71031fc35cea612838320f1f74246692b8a3cc0", url="https://pypi.org/packages/ad/c1/2af22bd7d96c3b3b17636417aa48e379bd9e028c323a1a442333d9b05175/dipy-1.4.1.tar.gz")
    version("1.4.0", sha256="56d3e028bdbe554cf734b4f53255ee68ed5d069cb1fddb0201b53a8ad16d57cd", url="https://pypi.org/packages/00/28/44a0d69370bd0533a6c694ff8e0636951eb4bb0aa4a479dd3b9b8ca7df04/dipy-1.4.0.tar.gz")
    version("1.3.0", sha256="c5be00719a01f63be0e22eed389eaa0ec2423a863e16a83dea3e9eeaa9cf6034", url="https://pypi.org/packages/7d/e3/b100e6cdfc0f40078a124f36b117e8a86e0e4773b19ef45257073a171818/dipy-1.3.0.tar.gz")
    version("1.2.0", sha256="7bd87ec59a92a59de436178404ae90580dd97394d11b2bf9e0e84147bf7716f4", url="https://pypi.org/packages/b9/f9/25a5fd0667ac86d4fee7267ceb444420a9bbd9178e48a92b0c6696fc6f3a/dipy-1.2.0.tar.gz")
    version("1.1.0", sha256="06db0bc1b44b8d38097945597edcfabca4316c64adee5c29d28ffad12d96135b", url="https://pypi.org/packages/be/69/30b11d120d1ecf34eb7a6c2e8c44b76195ce7dfa6088df26cc705429e586/dipy-1.1.0.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("python@3.9:", when="@1.9:")
        depends_on("py-cython@0.29.24:0.29.28,0.29.30:", when="@1.8")
        depends_on("py-h5py@3.1:", when="@1.8:")
        depends_on("py-h5py@2.4.0:", when="@0.16:1.1")
        depends_on("py-nibabel@3.0.0:", when="@1.1,1.8:")
        depends_on("py-numpy@1.22.4:", when="@1.8:")
        depends_on("py-packaging@21:", when="@1.8:")
        depends_on("py-scipy@1.8.0:", when="@1.8:")
        depends_on("py-tqdm@4.30:", when="@1.8:")
        depends_on("py-trx-python@0.2.9:", when="@1.8:")
    # END DEPENDENCIES

