##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyHttpie(PythonPackage):
    version("3.2.1", sha256="34dd03abdab7651eef2bca967b6aa5c73e8c24f32bd8784d19ac1b0f212bfd79", url="https://pypi.org/packages/54/da/ccd73ba27c3e0378a5342ebefd59054f4941afe261d111659433f8b641fe/httpie-3.2.1-py3-none-any.whl")
    version("2.6.0", sha256="58fe1b845b4015a04b0dfc172b6f85c0960cebedc44cee09c9146291692083d7", url="https://pypi.org/packages/d6/a9/3d8d10d6f803454afebd1c7db5f59d1e0ed43a7a52a7433f09e400ecab9c/httpie-2.6.0-py3-none-any.whl")
    version("2.5.0", sha256="cc54d5e1fd1dea68c932938adabeed0958d5bd8b22957062e316bf385b4b9fbb", url="https://pypi.org/packages/b5/c2/3f172692041ac10457a348314a90ee0219995282a911e37fdafc7e253219/httpie-2.5.0-py3-none-any.whl")

    with default_args(type="run"):
        depends_on("py-charset-normalizer@2:", when="@2.6:")
        depends_on("py-colorama@0.2.4:", when="@1.0.3: platform=windows")
        depends_on("py-defusedxml@0.6.0:", when="@2.5:")
        depends_on("py-multidict@4.7:", when="@3:")
        depends_on("py-pip", when="@3.2:")
        depends_on("py-pygments@2.5.2:", when="@2:")
        depends_on("py-requests@2.22:+socks", when="@2.3:")
        depends_on("py-requests-toolbelt@0.9.1:", when="@2.3:")
        depends_on("py-rich@9.10:", when="@3.2:")
        depends_on("py-setuptools", when="@2.5:")

