##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyOss2(PythonPackage):
    version("2.18.4", sha256="be1e7a871a8cc267726367333017d78333ee8fae88c727ad61396f59c1c0e4d0", url="https://pypi.org/packages/d5/63/b6c355af7f04a8a1d5759fa6fc47539e25ef8e6f2745372a242fdadcac65/oss2-2.18.4.tar.gz")
    version("2.18.3", sha256="4e61f546a17cc5c4a2efc0baee83e4b12a64fba87f13ff51166d269ab4629bea", url="https://pypi.org/packages/b2/9c/a16e0d92ccef9ee31f5c1ae2a96d5502bbed94eae554c31c77e07c018920/oss2-2.18.3.tar.gz")
    version("2.18.2", sha256="55193cf5c6fd79ba3c1ad3ae6747b90a662d8fae268ea5b6498526527d7f2c3d", url="https://pypi.org/packages/32/7a/6a1353991ce78d0693bad8bc320fd26a9c94d698eb7ac4a69dca30c6fdd0/oss2-2.18.2.tar.gz")
    version("2.18.1", sha256="5a901f6c0f3ac42f792e16a1e1c04e60f34e6cc9eb2bc4c0c3ce6e7bda2da4cc", url="https://pypi.org/packages/4a/e7/08b90651a435acde68c537eebff970011422f61c465f6d1c88c4b3af6774/oss2-2.18.1.tar.gz")
    version("2.18.0", sha256="335c52bec7d8f7ee05f3e816d18a125a86a0a6d014c9e9045ca3b91a2484bbd4", url="https://pypi.org/packages/ae/42/ca0a686a56def81bf3c7bb651c8fb552458258099203849f6ead54f3fc87/oss2-2.18.0.tar.gz")
    version("2.17.0", sha256="da4489b89c76ec72c9dd4888bd2787c9e106cdd412cf6e14be00898e7dbcc859", url="https://pypi.org/packages/86/e7/017f8a5948d70e130815eebd14c25dfad916bd574590f2d7e046f19eee3f/oss2-2.17.0.tar.gz")
    version("2.16.0", sha256="a08ca287dbadb19767a204297540c185f5ccccad7ef6f9ca3a180f77b6dc8376", url="https://pypi.org/packages/7a/d2/33b2607395c625f685c9e225d94fa2f56a4debabfe53b9b00c9eaed22f6d/oss2-2.16.0.tar.gz")
    version("2.15.0", sha256="d8b5a10ba2291ff4c78246576f243dcec262f1f646344e61f3192dc262e87430", url="https://pypi.org/packages/16/d0/cfe6e199900a97d6e3db55e48ab525c630052e49475722fd20f0f7c7b793/oss2-2.15.0.tar.gz")
    version("2.14.0", sha256="7fed58200da934ad4b8c1fb2754a1ac6bfd40a073f35e65b94880268b9f7fb48", url="https://pypi.org/packages/4e/0a/c2c1bc04f2b0c43e5b54ade829f4e8c35aa13db42171252b1dd62780ffa5/oss2-2.14.0.tar.gz")
    version("2.13.1", sha256="8548ea7d43326f6fd679bc8b79b3a2dfbfe9c6a60ed57e2410818fec57023dda", url="https://pypi.org/packages/ee/95/64d63ba18d07e5903663259334d84e1d6a3d58e25136dced1e0ae879c8f8/oss2-2.13.1.tar.gz")

    with default_args(type="run"):
        depends_on("py-aliyun-python-sdk-core@2.13.12:", when="@2.18.2")
        depends_on("py-aliyun-python-sdk-kms@2.4.1:", when="@2.7,2.18.2")
        depends_on("py-crcmod@1.7:", when="@2.7,2.18.2")
        depends_on("py-pycryptodome@3.4.7:", when="@2.7,2.18.2")
        depends_on("py-requests@:2.8,2.9.1:", when="@2.7,2.18.2")
        depends_on("py-six", when="@2.18.2")

