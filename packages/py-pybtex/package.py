##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPybtex(PythonPackage):
    version("0.24.0", sha256="e1e0c8c69998452fea90e9179aa2a98ab103f3eed894405b7264e517cc2fcc0f", url="https://pypi.org/packages/ad/5f/40d8e90f985a05133a8895fc454c6127ecec3de8b095dd35bba91382f803/pybtex-0.24.0-py2.py3-none-any.whl")
    version("0.23.0", sha256="4d0dd7a45641976b318a413368e4ae07dc942dd8e3ab81e389b1df4f598944f7", url="https://pypi.org/packages/15/ef/9f93c1084aef4dcd190c86a9e405e97b065a96514c74ce34b2fd5c02fe73/pybtex-0.23.0-py2.py3-none-any.whl")
    version("0.22.2", sha256="9ce2ce13d8d4f5a8d3848463f58167dbbbe75a53511f1088eaa6197637cdf8cf", url="https://pypi.org/packages/94/2a/11039970561f1bbc74fbaca89b59c26b398a0a70bba8caad553ac779b4f7/pybtex-0.22.2-py2.py3-none-any.whl")
    version("0.22.1", sha256="edbf334b5a4c8da4988f833b09e9b96efba37a6bfb938a65ae85110266f1f152", url="https://pypi.org/packages/7f/0c/0003c237c4c6c4fd7263394d48dc2b68e3ab6fdf15c5db9fbe69a1452563/pybtex-0.22.1-py2.py3-none-any.whl")
    version("0.22.0", sha256="e2adcf103c229f9a0e6b81292f17c4eb461ba8e9db99f9688fede1b2ab275b69", url="https://pypi.org/packages/f9/3e/ae3dd1039209307ba93b838ce3d36c0a2c1185c9ef04d65cf5727df15486/pybtex-0.22.0-py2.py3-none-any.whl")
    version("0.21", sha256="af8a6c7c74954ad305553b118d2757f68bc77c5dd5d5de2cc1fd16db90046000", url="https://pypi.org/packages/82/59/d46b4a84faacd7c419cfc9a442b7940d6d625d127b83d83666e2a8b203d8/pybtex-0.21.tar.gz")
    version("0.20.1", sha256="0be4149eb12670bd71a9dcb33614e61fbea46190fdb9ff82eccf6b17ac373e9c", url="https://pypi.org/packages/f3/38/369b006acf408e6a8e609e731fac1f426a07413f3e5f69f4fb34813ce1cb/pybtex-0.20.1.zip")
    version("0.20", sha256="c624bb858e63965d0486c1d133ef98c722f097777cd73231c00653123f0c2a19", url="https://pypi.org/packages/88/1e/583892b59ee7a31c0b5cb652b68c9bd60587c1aa769dbc7a81ebbdbead54/pybtex-0.20.tar.bz2")
    version("0.19", sha256="7f9b18149e4686643605338486d8a9fd523a0398d70296755d62d131648f5648", url="https://pypi.org/packages/b7/41/761702c0f1be329e8ec4fd1bb90a0e8e5cdaf9080ad5116bde8ecf8d3caf/pybtex-0.19.tar.bz2")
    version("0.18", sha256="fa152603ed30393bae43c9ef2eb410f98d0866d0f655b5c2fcdfbe6e9ca99e93", url="https://pypi.org/packages/d8/7d/b96bede652938c7ec8185357e0c2bdf241f8c5606bd72182b78718926346/pybtex-0.18.tar.bz2")

    with default_args(type="run"):
        depends_on("py-latexcodec@1.0.4:", when="@0.22:")
        depends_on("py-pyyaml", when="@0.22:")
        depends_on("py-six", when="@0.22:")

