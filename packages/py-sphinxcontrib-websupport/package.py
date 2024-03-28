# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PySphinxcontribWebsupport(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("1.2.7", sha256="2dc179d7f821ebd54f31f93c894ca52435ebc5364e4e4dfb0da834ac119d51fd", url="https://pypi.org/packages/be/36/bd45372471d95ef2d08dd17528b5ffb5fab04acefeb3b9dd1029821757e1/sphinxcontrib_websupport-1.2.7-py3-none-any.whl")
    version("1.2.6", sha256="c43c2031b93799ad688c2af233e330740768adc57c02746d5ec197e815b9469e", url="https://pypi.org/packages/40/d2/fd1c52203f1385bc95775d36e9f334358cc457ea3e44046fc6d78a868d10/sphinxcontrib_websupport-1.2.6-py3-none-any.whl")
    version("1.2.5", sha256="e438d4bb72b4536c135768bfd88495fa43ad4e71b107df362d97cb8a6a30de00", url="https://pypi.org/packages/1d/5b/b6f6d68a2478654bf9120bc04430551cf5011a9288c88d38c6541c36086e/sphinxcontrib_websupport-1.2.5-py3-none-any.whl")
    version("1.2.4", sha256="6fc9287dfc823fe9aa432463edd6cea47fa9ebbf488d7f289b322ffcfca075c7", url="https://pypi.org/packages/e9/e5/2a547830845e6e6e5d97b3246fc1e3ec74cba879c9adc5a8e27f1291bca3/sphinxcontrib_websupport-1.2.4-py2.py3-none-any.whl")
    version("1.2.3", sha256="a2100b79096bbaea5a41e03261cee279d19c803218b9401a1d84ef6aeae17338", url="https://pypi.org/packages/f4/b0/8aca97e77c31478ec5d998b8203711865588d23003a31e39aca166d92125/sphinxcontrib_websupport-1.2.3-py2.py3-none-any.whl")
    version("1.2.2", sha256="c155cfa18e8b7c832b3cac0a2d41810ebacd26b26ba9624cd2f42c3496dad04b", url="https://pypi.org/packages/4e/69/df9ce924e183967ac37d040e3b7008cfa6af141df08cb11230367e7f1718/sphinxcontrib_websupport-1.2.2-py2.py3-none-any.whl")
    version("1.2.1", sha256="69364896eae5d1145d82b6ee09f66d597099ef8069615e2888921ec48005470f", url="https://pypi.org/packages/f4/5e/61a42a9be8933c51fcae5450e436f6b8ebf802f3dec79dd29909cfdcaa2b/sphinxcontrib_websupport-1.2.1-py2.py3-none-any.whl")
    version("1.2.0", sha256="50fb98fcb8ff2a8869af2afa6b8ee51b3baeb0b17dacd72505105bf15d506ead", url="https://pypi.org/packages/e8/f3/660c7df68d36fb314303155863136c4541bad3ec360d93406c20535f3f1d/sphinxcontrib_websupport-1.2.0-py2.py3-none-any.whl")
    version("1.1.2", sha256="e02f717baf02d0b6c3dd62cf81232ffca4c9d5c331e03766982e3ff9f1d2bc3f", url="https://pypi.org/packages/2a/59/d64bda9b7480a84a3569be4dde267c0f6675b255ba63b4c8e84469940457/sphinxcontrib_websupport-1.1.2-py2.py3-none-any.whl")
    version("1.1.0", sha256="68ca7ff70785cbe1e7bccc71a48b5b6d965d79ca50629606c7861a21b206d9dd", url="https://pypi.org/packages/52/69/3c2fbdc3702358c5b34ee25e387b24838597ef099761fc9a42c166796e8f/sphinxcontrib_websupport-1.1.0-py2.py3-none-any.whl")
    version("1.0.1", sha256="f4932e95869599b89bf4f80fc3989132d83c9faa5bf633e7b5e0c25dffb75da2", url="https://pypi.org/packages/56/0f/3ee19ca5e5a1d9751cf4bbeb372d40a46421c4321fe55a4703ba66d0bafb/sphinxcontrib_websupport-1.0.1-py2.py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("python@3.9:", when="@1.2.5:")
        depends_on("py-jinja2", when="@1.2.5:")
        depends_on("py-sphinx@5.0.0:", when="@1.2.5:")
        depends_on("py-sphinxcontrib-serializinghtml", when="@1.2.4:")
    # END DEPENDENCIES

