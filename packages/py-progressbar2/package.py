##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyProgressbar2(PythonPackage):
    version("4.4.2", sha256="ec157391635b008b8a422326fb05c27045ffbb2dc8dab5e4d90d4d412c4ffd39", url="https://pypi.org/packages/e6/7c/7da9fefe4429f21e16fb9ab95c05f47cd11ffa4fd79932b639a1380a52a3/progressbar2-4.4.2-py3-none-any.whl")
    version("4.4.1", sha256="714995e7725fb13e10a720eccf8ce8ff775d9f26247798c71f71447a15cfbe10", url="https://pypi.org/packages/99/6c/e3864761c8b7aa39e7131394201f20b70bba10ee961fdddd36cc10d6d3e7/progressbar2-4.4.1-py3-none-any.whl")
    version("4.4.0", sha256="a22bc53c0af44245c2ae5ffc9972723040d60155c75e27e64c833f6f2de000c6", url="https://pypi.org/packages/4e/47/1d0cb10ca62a72ad23df7ea69b831226deb3b363c497add8263cf061cc13/progressbar2-4.4.0-py3-none-any.whl")
    version("4.3.2", sha256="036fa3bd35ae27c92e73fce4fb18aa4ba5090a1880d880cf954ecb75ccd6f3fb", url="https://pypi.org/packages/7d/66/86ac1b2ad859641bf5186fae72d90ca091a25aee3d6a1ba1772ea19895ba/progressbar2-4.3.2-py3-none-any.whl")
    version("4.3.1", sha256="540e316648dcb71860a99ed3dce1ef81305b4574193a5784db6d1df706fda779", url="https://pypi.org/packages/f3/3e/ffe17a895366f1f469305fe3773ab84811bca3dd452b63ec6d4c8d582f1f/progressbar2-4.3.1-py3-none-any.whl")
    version("4.3.0", sha256="022d03eeaf48102b4a2f2d9d82e59c4d9f6fcf186c124de7068dd7c5636acdb6", url="https://pypi.org/packages/ef/cf/331e8d4a9e55d8713deb482fb8c2bf15a368abfe30fdccdbf11203a1bd27/progressbar2-4.3.0-py3-none-any.whl")
    version("4.2.0", sha256="1a8e201211f99a85df55f720b3b6da7fb5c8cdef56792c4547205be2de5ea606", url="https://pypi.org/packages/8b/de/a23d9e1141a3503f52d8b22694a7ca19a4706c8e0c74d1f0cdb207e8699d/progressbar2-4.2.0-py2.py3-none-any.whl")
    version("4.1.1", sha256="265f234573dcce84ea841dc53dcd1edb147a7b3cc5acb6f3b275f9205f591c09", url="https://pypi.org/packages/a8/f9/8878b8e7e2f9c896ff14b834dfe49b4e098f9f10376a3c9132d977909296/progressbar2-4.1.1-py2.py3-none-any.whl")
    version("4.1.0", sha256="eeda551057eb7318b9c9bb13158b479d788fcd666b3f400fe8ad43e9aed13e1a", url="https://pypi.org/packages/e7/39/0570ce4cd7e4a8c0feb3b2161a6f8d4fe01f35699c31440b9fc7ec1bc7b5/progressbar2-4.1.0-py2.py3-none-any.whl")
    version("4.0.0", sha256="2562ba3e554433f08e81fb7b786208b19de135f3ca1c5da1787d9b05558e6247", url="https://pypi.org/packages/e8/e7/a823e2c141d50930814af22fb3350b696b190318c7722055971be8519467/progressbar2-4.0.0-py2.py3-none-any.whl")
    version("3.55.0", sha256="86835d1f1a9317ab41aeb1da5e4184975e2306586839d66daf63067c102f8f04", url="https://pypi.org/packages/ec/91/8ccedd384153a4f070be8b8d0fc0f9f6436bcc0d1ad4b4d1f891343d109c/progressbar2-3.55.0.tar.gz")
    version("3.50.1", sha256="2c21c14482016162852c8265da03886c2b4dea6f84e5a817ad9b39f6bd82a772", url="https://pypi.org/packages/0c/f4/30d9ac2df519e0e81154880cdfb27b74020c1a7075211238b48ac6d5b832/progressbar2-3.50.1.tar.gz")
    version("3.43.1", sha256="87a403d2f80f6e48b7b55559feae5c75b903941f55189b22207b574fe5e62276", url="https://pypi.org/packages/32/05/1b0bf20c28aa413c74fcc9f63664e654316d6a32ac8b0762e0179996563e/progressbar2-3.43.1.tar.gz")
    version("3.39.3", sha256="8e5b5419e04193bb7c3fea71579937bbbcd64c26472b929718c2fe7ec420fe39", url="https://pypi.org/packages/12/1b/aea82bf4bd420405c78fa9b1c5782702bb86fc99b673c0603af0f3393f46/progressbar2-3.39.3.tar.gz")

    with default_args(type="run"):
        depends_on("py-python-utils@3.8.1:", when="@4.3.0:")
        depends_on("py-python-utils@3:", when="@4:4.2")

