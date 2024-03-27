##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyLibclang(PythonPackage):
    version("16.0.0", sha256="a043138caaf2cb076ebb060c6281ec95612926645d425c691991fc9df00e8a24", url="https://pypi.org/packages/a1/82/1fd88a2df784dbcfdfba7dbb335653f4178c7c73fa7fe95bae888e60d34b/libclang-16.0.0-py2.py3-none-manylinux2010_x86_64.whl")
    version("15.0.6.1", sha256="0bf192c48a8d2992fc5034393ddc99e772ac30e105df84927d62fc88ef8a659f", url="https://pypi.org/packages/3f/46/286604ecc39eabc34455311055407e5742f64c415229bb74040bad1f36c0/libclang-15.0.6.1-py2.py3-none-macosx_11_0_arm64.whl")
    version("14.0.6", sha256="7b06fc76bd1e67c8b04b5719bf2ac5d6a323b289b245dfa9e468561d99538188", url="https://pypi.org/packages/95/18/09e5b7f474c84254e7d581a95f0125c4ea9d6c8b7fa12c3dae0cd975fcd4/libclang-14.0.6-py2.py3-none-macosx_11_0_arm64.whl")
    version("14.0.1", sha256="7c344b16d32e80c06cd7d42bfad0ef3ffeadc96fd77b6674dd66d97bf23889ea", url="https://pypi.org/packages/05/d7/458c5cdfbfa19f758402226e2ea8fbb7d60f044cb66620a16834ab706e7c/libclang-14.0.1-py2.py3-none-win_arm64.whl")
    version("13.0.0", sha256="b0acfcfbd1f6d411f654cf6ec4f09cecf0f80b3480e4c9f834d1dcb1f8bd6907", url="https://pypi.org/packages/06/d2/359e2330fc845ea77480d85d6e0640dd372aa76858d01119837cff5e5504/libclang-13.0.0-py2.py3-none-win_arm64.whl")
    version("11.1.0", sha256="39d07c8965a3c963fb2686496339b6dbacf42acbd32e4bc7361373a45e98cebe", url="https://pypi.org/packages/3c/9e/b3e5cc2b4bca9146b4e6641b0459f599bc86b4bb11bb664111f347df060d/libclang-11.1.0-py2.py3-none-manylinux2014_aarch64.whl")
    version("11.0.1", sha256="d8c48f66a3b0752eb96db954bcc25e09a49c7f00c85798ff150d1a887917822b", url="https://pypi.org/packages/f2/79/f9ea60674bfff992895daab13e487ea3ba56b3134f1a3d1c2bc00658cad5/libclang-11.0.1-1-py2.py3-none-manylinux1_x86_64.whl")
    version("11.0.0", sha256="c0f51898bb50ea5633bb349a3c5731eb35b634d215f16aa09557d150c1e1f461", url="https://pypi.org/packages/7e/72/78b998b43348e4cc5df96737b315e1f79cb6d418c6dd3fcc0e9cd5c05e5f/libclang-11.0.0-2-py2.py3-none-macosx_10_9_x86_64.whl")
    version("10.0.1", sha256="64a031b5df280cde03cdcb8af03253ade3edd5a5e8d08306c9a363de2b8261d7", url="https://pypi.org/packages/6a/58/5719b10d71af4c83b9a8c3d82d3e787908b62d3d0e5613702e4f3e1a8015/libclang-10.0.1-py2.py3-none-win_amd64.whl")


