##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PySpacyLoggers(PythonPackage):
    version("1.0.5", sha256="196284c9c446cc0cdb944005384270d775fdeaf4f494d8e269466cfa497ef645", url="https://pypi.org/packages/33/78/d1a1a026ef3af911159398c939b1509d5c36fe524c7b644f34a5146c4e16/spacy_loggers-1.0.5-py3-none-any.whl")
    version("1.0.4", sha256="e050bf2e63208b2f096b777e494971c962ad7c1dc997641c8f95c622550044ae", url="https://pypi.org/packages/62/8c/814e0bd139a8c94b50298be3a4e640d90cdce78efe0099e373a767b7d854/spacy_loggers-1.0.4-py3-none-any.whl")
    version("1.0.3", sha256="f74386b390a023f9615dcb499b7b4ad63338236a8187f0ec4dfe265a9f665ee8", url="https://pypi.org/packages/61/4c/3ca1dec23a20466be5789601e87a4ebb4f1d6f53d324f9126b7821346869/spacy_loggers-1.0.3-py3-none-any.whl")
    version("1.0.2", sha256="d48c9313a577ad1818da961cf6db71a73fd1e556ae47e6e68d7e28b541d11e18", url="https://pypi.org/packages/e9/b4/b0c53c5e2ffeeed07e101a7574228bd56d8b1f115b752c2fffd96b0c80a4/spacy_loggers-1.0.2-py3-none-any.whl")
    version("1.0.1", sha256="5e610c980efb831fa428c24fd659e5dd850ea6140c9ed987efe0e8d26df3ee7c", url="https://pypi.org/packages/9a/34/44741cf6abdf29b6baee3bc8a0b868213ecb9ed2b9f1c83a276053a32a92/spacy_loggers-1.0.1-py3-none-any.whl")
    version("1.0.0", sha256="670e5cf0e61b0cd4eb8c568487382ae3baf1909cfbfb7c4f34549e657a4f96ba", url="https://pypi.org/packages/6f/13/f229d0e16390965b9001e4d61b08a863e69f70effe22c5c9993274ca46f5/spacy_loggers-1.0.0-py3-none-any.whl")

    with default_args(type="run"):
        depends_on("py-wasabi@0.8.1:0", when="@:1.0.3")

