##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyS3fs(PythonPackage):
    version("2024.3.1", sha256="f4566a5446c473740d272ec08e0b4aae8db1aa05f662c42ff0aa2c89bb5060ea", url="https://pypi.org/packages/a2/dc/b373f0cfdc67a6b23bc80d0e743b8adf125f4066b39172acb4bb2b90e6be/s3fs-2024.3.1-py3-none-any.whl")
    version("2024.3.0", sha256="def23c00eb89e3a49bbe7211eb617204c99959cadf9a796faa512bafa861c115", url="https://pypi.org/packages/72/45/02935f47f1a180982555a1c53e63444aa1c7d48db60a9880867bb64c1e2e/s3fs-2024.3.0-py3-none-any.whl")
    version("2024.2.0", sha256="c140de37175c157cb662aa6ad7423365df732ac5f10ef5bf7b76078c6333a942", url="https://pypi.org/packages/7c/76/efa5f84237620d5aa38e58285945b47449d8a94bf7037cae06f680b34c41/s3fs-2024.2.0-py3-none-any.whl")
    version("2023.12.2", sha256="0d5a99039665f30b2dbee5495de3b299a022d51b3195a9440f5df47c2621b777", url="https://pypi.org/packages/5b/d6/b8a748b7d3fc7b0fd2ede1cf26a80281d65cc24d5d56b66c3a4c87e256e2/s3fs-2023.12.2-py3-none-any.whl")
    version("2023.12.1", sha256="ed0b7df8cc20a2b5cefe607b1cf4e860d37c5ca4ac2d68f55464805d75d18710", url="https://pypi.org/packages/78/f9/dc65842d80fa01d6cd9dcae7efb17c7789a0be6436aabbea4ae8b07c4682/s3fs-2023.12.1-py3-none-any.whl")
    version("2023.12.0", sha256="d895ea3286f2d68431a269609ef081de8b8519512645257e564bddbc9e427664", url="https://pypi.org/packages/8a/cd/ababa0a8ced0b37f821ffe9af155581bd3dc6f91803b95a6858edae84d65/s3fs-2023.12.0-py3-none-any.whl")
    version("2023.10.0", sha256="3df68ff4f5f70c3338219a66df92e91fd15c6b78d0f559e57f617dfdd49feb41", url="https://pypi.org/packages/55/d1/7d6279cf80ed186a35a884fa2c22b5423611609bcca9296e47bfed0da27b/s3fs-2023.10.0-py3-none-any.whl")
    version("2023.9.2", sha256="d0e0ad0267820f4e9ff16556e004e6759010e92378aebe2ac5d71419a6ff5387", url="https://pypi.org/packages/36/93/8aed66523d90361211a02dc0435855cc1ef357978decc2b05c8291fc515f/s3fs-2023.9.2-py3-none-any.whl")
    version("2023.9.1", sha256="3bd1f9f33e4ad090d150301c3b386061cb7085fc8bda3a9ec9198dccca765d6c", url="https://pypi.org/packages/51/dc/ef0a84b2d7d03e042bdced0a5bab9cfee1e11a0080f010e43b37222784ce/s3fs-2023.9.1-py3-none-any.whl")
    version("2023.9.0", sha256="98ad2b221514490f0fe49b730ccf4f0362031ee8ede6d5392cdd3977ca313b1a", url="https://pypi.org/packages/98/19/fb5e526056deefe616530678462b02bb457089eb5bf50d47e84e105d0c6f/s3fs-2023.9.0-py3-none-any.whl")
    version("2022.11.0", sha256="42d57a3ceedb478b18ee53e34bbe3305a3f07f6381ca1ab76135efe076c6a07d", url="https://pypi.org/packages/04/5c/6a5696e6e0fc30cfab334ed47e7e04707a6efd0ac1fe24158f5969fb4ef8/s3fs-2022.11.0-py3-none-any.whl")
    version("2022.1.0", sha256="3d20584130a6bf4679e4d9fa9a859597bab6553b8f4bd439168629c825d8ef01", url="https://pypi.org/packages/f1/ff/76ed699715acec23c487f3bb59b6b8be01289d1fe9ff2a447d8c400b6ee8/s3fs-2022.1.0-py3-none-any.whl")
    version("0.5.2", sha256="0e7a3fdab0ff66af7c8afd9cdc69723643e10ba6ce37776332fdad9f41bec3dd", url="https://pypi.org/packages/d0/47/8f96b4a3af8bd54dda28df960307978679b3cc64bc8ec5460697c30bc783/s3fs-0.5.2-py3-none-any.whl")

    with default_args(type="run"):
        depends_on("py-aiobotocore@2.5.4:", when="@2023.12:")
        depends_on("py-aiobotocore@2.7", when="@2023.10")
        depends_on("py-aiobotocore@2.5.4:2.5", when="@2023.9")
        depends_on("py-aiobotocore@2.4", when="@2022.8:2022")
        depends_on("py-aiobotocore@2.1", when="@2022:2022.2")
        depends_on("py-aiobotocore@1.0.1:", when="@0.5:2021.7")
        depends_on("py-aiohttp@:3", when="@2022.8:")
        depends_on("py-aiohttp", when="@2021.11.1:2022.5")
        depends_on("py-fsspec@2024.3.1:", when="@2024.3.1:")
        depends_on("py-fsspec@2024.3:2024.3.0", when="@2024.3:2024.3.0")
        depends_on("py-fsspec@2024:2024.2", when="@2024:2024.2")
        depends_on("py-fsspec@2023.12.2:2023", when="@2023.12.2:2023")
        depends_on("py-fsspec@2023.12.1", when="@2023.12.1")
        depends_on("py-fsspec@2023.12:2023.12.0", when="@2023.12:2023.12.0")
        depends_on("py-fsspec@2023.10", when="@2023.10")
        depends_on("py-fsspec@2023.9.2:2023.9", when="@2023.9.2:2023.9")
        depends_on("py-fsspec@2023.9.1", when="@2023.9.1")
        depends_on("py-fsspec@2023.9:2023.9.0", when="@2023.9:2023.9.0")
        depends_on("py-fsspec@2022.11:2022", when="@2022.11:2022")
        depends_on("py-fsspec@2022:2022.1", when="@2022:2022.1")
        depends_on("py-fsspec@0.8:", when="@0.5:0")

