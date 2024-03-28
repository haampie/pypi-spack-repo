# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PySphinxTabs(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("3.4.5", sha256="92cc9473e2ecf1828ca3f6617d0efc0aa8acb06b08c56ba29d1413f2f0f6cf09", url="https://pypi.org/packages/20/9f/4ac7dbb9f23a2ff5a10903a4f9e9f43e0ff051f63a313e989c962526e305/sphinx_tabs-3.4.5-py3-none-any.whl")
    version("3.4.4", sha256="85939b689a0b0a24bf0da418b9acf14b0b0fca7a7a5cd35461ee452a2d4e716b", url="https://pypi.org/packages/ff/a0/82125f3a296bece2ac4673f4b4dc676049c2dc87344b14aa65341f6c950b/sphinx_tabs-3.4.4-py3-none-any.whl")
    version("3.4.1", sha256="7cea8942aeccc5d01a995789c01804b787334b55927f29b36ba16ed1e7cb27c6", url="https://pypi.org/packages/4f/2d/80293fbb2aa82d457f9df0de85800b11e3bfd5008b118bddb303a797e5c5/sphinx_tabs-3.4.1-py3-none-any.whl")
    version("3.4.0", sha256="31dbe7594b5ef4cfa76a7960448d4607dca167ff21467000213920572c302072", url="https://pypi.org/packages/f1/53/ea26867c61b517f23349c68ea861db06c1b7da30f97524a07aba6166c42e/sphinx_tabs-3.4.0-py3-none-any.whl")
    version("3.3.1", sha256="73209aa769246501f6de9e33051cfd2d54f5900e0cc28a63367d8e4af4c0db5d", url="https://pypi.org/packages/a5/d7/beda6ab57bb591416f95dfb2486960a7f4f4db43105993a5b02c4782803b/sphinx_tabs-3.3.1-py3-none-any.whl")
    version("3.3.0", sha256="7a7d20f1035c72c1862f641e81118cd5eedb726453142e7a726dda861b118f34", url="https://pypi.org/packages/fc/5f/d42c76e1816a81d344ea4fa95c9f9c2351538de3c639171178cc4a73eb5d/sphinx_tabs-3.3.0-py3-none-any.whl")
    version("3.2.0", sha256="1e1b1846c80137bd81a78e4a69b02664b98b1e1da361beb30600b939dfc75065", url="https://pypi.org/packages/15/be/4fa8ecfb7a9ba5e8d5aa6e27351faaf5f20c9066652064e473a853431916/sphinx_tabs-3.2.0-py3-none-any.whl")
    version("3.1.0", sha256="63df94e84bc05eb8598419a313ffc24455a14d1a580d174bb748404063958a67", url="https://pypi.org/packages/36/56/506dd97607b2f684612f5d927721141a4fdb644e353a300859b9fb81c39c/sphinx_tabs-3.1.0-py3-none-any.whl")
    version("3.0.0", sha256="2abbcaaa3b8a857de06f3db31762a7bdd17aba1b8979d000f193debe6f917c2c", url="https://pypi.org/packages/dd/fb/38ca6ad4ca4dcb63873000358965f09674029f3eba012d6397f2c893a188/sphinx_tabs-3.0.0-py3-none-any.whl")
    version("2.1.0", sha256="9d8db61afe9499aa84b33bc1c0d891f8a0df88ae513739f5babde15430c1fdaf", url="https://pypi.org/packages/65/7b/9d662dfd94d5b2f9f8ec2f25e4186a4a8924f191b931132788b35cf62b80/sphinx_tabs-2.1.0-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-docutils", when="@3.4.5:")
        depends_on("py-docutils@0.18", when="@3.4.1:3.4.4")
        depends_on("py-docutils@0.17", when="@3.3:3.4.0")
        depends_on("py-docutils@0.16", when="@3:3.2")
        depends_on("py-jinja2@:3.0", when="@3.4:3.4.0")
        depends_on("py-pygments", when="@1.2:")
        depends_on("py-sphinx", when="@3.4.1:")
        depends_on("py-sphinx@2.0.0:5", when="@3.4:3.4.0")
        depends_on("py-sphinx@2.0.0:4", when="@3:3.3")
        depends_on("py-sphinx@2.0.0:3", when="@1.2:2")
    # END DEPENDENCIES

