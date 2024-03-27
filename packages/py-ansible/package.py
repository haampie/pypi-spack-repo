##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyAnsible(PythonPackage):
    version("2.9.2", sha256="2f83f8ccc50640aa41a24f6e7757ac06b0ee6189fdcaacab68851771d3b42f3a", url="https://pypi.org/packages/f3/0d/ee54843308769f2c78be849d9e9f65dc8d63781941dc880f68507aae33ba/ansible-2.9.2.tar.gz")
    version("2.9.1", sha256="d87cb25df02284d59226ff1d935d7075a175f31d0db83564c2f1ca28bbbd4cb4", url="https://pypi.org/packages/4b/c5/fb70a2d9817eb48c358a67952ed3a1869e5cda8a5e4f1911cffc75f42375/ansible-2.9.1.tar.gz")
    version("2.9.0", sha256="9f9a9ace1d63cd8a4692ab6ee6ed04823743f1bd339a6ef188860c02cf7f46f1", url="https://pypi.org/packages/59/3a/5b8aeca9b0b68e7a02fdfd7260f265be3b0605839d7367501aba4bcb2e14/ansible-2.9.0.tar.gz")
    version("2.8.7", sha256="828239ca2b4d92865a00ab415caa932700f7c93f3e4838ddd55614ddf104c947", url="https://pypi.org/packages/4f/17/cbce93059ab9406f99216d8d9bd518b64ef4f0a2d2e347899f1b20cfb198/ansible-2.8.7.tar.gz")
    version("2.8.6", sha256="31203b27c9d61123e8c86b6eb5116a21859ed4f26d55a1a71eaf27bd92bce355", url="https://pypi.org/packages/1b/5c/8a59aba5ca0d40df673aab53d51e9f5890a9c2135c299a909aed5fdee164/ansible-2.8.6.tar.gz")
    version("2.7.15", sha256="99bf683d069b3f73704182ece95b6618ae2090594a66e146f4d286c0cac858ce", url="https://pypi.org/packages/5e/7e/07eff93fea8282326172b172766000b387d454a6445ca8488510736a4e7f/ansible-2.7.15.tar.gz")
    version("2.7.14", sha256="6a52f43b5e4446aa04f3907a750010fbbf41eb050cb726065c6c877ed3a98d02", url="https://pypi.org/packages/e8/2c/ad20be4315cc9c80c1197e18822c81089ee6450c8a62b48dd4a1a0328c2d/ansible-2.7.14.tar.gz")
    version("2.6.20", sha256="16cfb99d7f321cec408afcd3ead538337ebc3247c7a77080e5cabb58054e2a0b", url="https://pypi.org/packages/b1/da/6c8f2daff9b776a85eff1ab1ac9bbf3bc67f9e55fa616b4d45dab76fef90/ansible-2.6.20.tar.gz")

    with default_args(type="run"):
        depends_on("python@3.10:", when="@9.0.1:")
        depends_on("python@3.9:", when="@7:8")

