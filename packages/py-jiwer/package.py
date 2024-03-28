# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyJiwer(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("3.0.3", sha256="190d8238cb0262346781267d94f74c4fc8fc5094cf215a3d5d8317fb0954b842", url="https://pypi.org/packages/0d/4f/ee537ab20144811dd99321735ff92ef2b3a3230b77ed7454bed4c44d21fc/jiwer-3.0.3-py3-none-any.whl")
    version("3.0.2", sha256="cbf5872e0431942847765e444b338cd74ed9a96682532da87e46575010b76fd2", url="https://pypi.org/packages/23/a3/92c29a5e422acd87e3b4f2e6dc0ce877070cc9b2f81d30fe84122032338a/jiwer-3.0.2-py3-none-any.whl")
    version("3.0.1", sha256="425448ae5eacc3a49d6fe243ecb5bca5d6101fca07406d93166265c3105744e5", url="https://pypi.org/packages/04/1f/725023ef53fe04a20628a6dd3702ff79b897cd9efc48710b4676328f3d50/jiwer-3.0.1-py3-none-any.whl")
    version("3.0.0", sha256="d6f51a9c90270503545c6fdd38815b41e2ef240a450541994b089c50242b33c2", url="https://pypi.org/packages/22/2e/055d91e0d4182d15dd9bc7cdd97ed00839208082c23dcdd91465fae1815f/jiwer-3.0.0-py3-none-any.whl")
    version("2.6.0", sha256="1592a6898d44b8992a2e5a542c0ef2dba77d0a4a5f7efa5ce16bb4dd041a33e4", url="https://pypi.org/packages/7f/99/f397284437c85cd2afbc73b7bf92dd52b75c1fa9cfb053d9049c2d5d8dad/jiwer-2.6.0-py3-none-any.whl")
    version("2.5.2", sha256="3adf80a1ea6b86cc8f306890d4891244a092c58ebaaed5a86a3d2d40b5de6932", url="https://pypi.org/packages/9f/69/11d26b3bdaa30e58424f3bd980dcef61e5e921ee862ea1451563c1b7ffde/jiwer-2.5.2-py3-none-any.whl")
    version("2.5.1", sha256="968382fa72fa3e79015d77a4bd3bcd530809027fa4f159fb4e0e42991a554207", url="https://pypi.org/packages/d9/a3/560c31987df6893cf6f265837074ec6f241f262f6f3b23c936b5161b9873/jiwer-2.5.1-py3-none-any.whl")
    version("2.5.0", sha256="edbfd22f689d876d1faa783afa8ae0a05202d41d557f5cb2903e9f5403e4acb0", url="https://pypi.org/packages/38/eb/112a4a51aa6d5805e6d4e9301db41d52fcf72a12f25a09d34baebd64eb82/jiwer-2.5.0-py3-none-any.whl")
    version("2.4.0", sha256="b64784ba053614681c0a540c79856d25dcb54afa41f8fc3f6b2169b9cd00d96d", url="https://pypi.org/packages/89/df/0a83435e25f9755e6113323b4aeabe194949d3ffda8a8707822e391a9854/jiwer-2.4.0-py3-none-any.whl")
    version("2.3.0", sha256="ef972f8e4feb1b28402d0c0a4350a051e7b41c90119eb1e99d46b4a2002d512f", url="https://pypi.org/packages/69/f5/fdde62fec7d521238c22711f7e235a1b49e9d9aabd341b56fd98a73923d8/jiwer-2.3.0-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-click@8.1.3:", when="@2.6:")
        depends_on("py-levenshtein@0.20.2", when="@2.4:2.5.1")
        depends_on("py-python-levenshtein@0.12.2:0.12", when="@2.2.1:2.3")
        depends_on("py-rapidfuzz@3:", when="@3.0.3:")
        depends_on("py-rapidfuzz@2.13.7:2.13", when="@2.5.2:3.0.2")
    # END DEPENDENCIES

