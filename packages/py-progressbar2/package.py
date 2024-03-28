# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyProgressbar2(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
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
    version("3.55.0", sha256="e98fee031da31ab9138fd8dd838ac80eafba82764eb75a43d25e3ca622f47d14", url="https://pypi.org/packages/ed/19/afcfa7b88021a172f4f5308ca3cd95709c6ac39787caa720576e4b6cf6ba/progressbar2-3.55.0-py2.py3-none-any.whl")
    version("3.50.1", sha256="7849b84c01a39e4eddd2b369a129fed5e24dfb78d484ae63f9e08e58277a2928", url="https://pypi.org/packages/3d/b6/c76b09749f889bd53ca9aa1a4ec1dc990ff6d004cf079b43f5022ee37855/progressbar2-3.50.1-py2.py3-none-any.whl")
    version("3.43.1", sha256="39a987c263401d94e687869562c0943e6f9bfaa3215aebda180dfa935be72e38", url="https://pypi.org/packages/a3/72/1e88c46edd372d46f989db9b0168951b080a83666b6820bb8159a3d62280/progressbar2-3.43.1-py2.py3-none-any.whl")
    version("3.39.3", sha256="1ea89e2aaa1da85450aabbd2af62cefa04f1ee1c567f3a11ee0d8ded14fd1fea", url="https://pypi.org/packages/fb/89/d90f9ff03285d8eb56994e8cec1b73a4d0dc9bb529c1f8e8e10b1b663843/progressbar2-3.39.3-py2.py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-python-utils@3.8.1:", when="@4.3.0:")
        depends_on("py-python-utils@3:", when="@4:4.2")
    # END DEPENDENCIES

