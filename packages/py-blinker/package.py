# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyBlinker(PythonPackage):
    # BEGIN VERSIONS
    version("1.7.0", sha256="c3f865d4d54db7abc53758a01601cf343fe55b84c1de4e3fa910e420b438d5b9", url="https://pypi.org/packages/fa/2a/7f3714cbc6356a0efec525ce7a0613d581072ed6eb53eb7b9754f33db807/blinker-1.7.0-py3-none-any.whl")
    version("1.6.3", sha256="296320d6c28b006eb5e32d4712202dbcdcbf5dc482da298c2f44881c43884aaa", url="https://pypi.org/packages/bf/2b/11bcedb7dee4923253a4a21bae3be854bcc4f06295bd827756352016d97c/blinker-1.6.3-py3-none-any.whl")
    version("1.6.2", sha256="c3d739772abb7bc2860abf5f2ec284223d9ad5c76da018234f6f50d6f31ab1f0", url="https://pypi.org/packages/0d/f1/5f39e771cd730d347539bb74c6d496737b9d5f0a53bc9fdbf3e170f1ee48/blinker-1.6.2-py3-none-any.whl")
    version("1.6.1", sha256="8fa2dc7c28c15c8ddfd8b3a21834790984c7e4a89b336dc3f45eeb70e0c5a407", url="https://pypi.org/packages/a8/42/29714f0b9d6296a099d881b300ef76a04040b68ac70d73ddc18d74218ce5/blinker-1.6.1-py3-none-any.whl")
    version("1.6", sha256="eeebd5dfc782e1817fe4261ce79936c8c8cefb90d685caf50cec458029f773c1", url="https://pypi.org/packages/17/50/cd9207254dd9ab92d300717721600e367d99b0fcb83b6338af8dc34a8fa1/blinker-1.6-py3-none-any.whl")
    version("1.5", sha256="1eb563df6fdbc39eeddc177d953203f99f097e9bf0e2b8f9f3cf18b6ca425e36", url="https://pypi.org/packages/30/41/caa5da2dbe6d26029dfe11d31dfa8132b4d6d30b6d6b61a24824075a5f06/blinker-1.5-py2.py3-none-any.whl")
    version("1.4", sha256="471aee25f3992bd325afa3772f1063dbdbbca947a041b8b89466dc00d606f8b6", url="https://pypi.org/packages/1b/51/e2a9f3b757eb802f61dc1f2b09c8c99f6eb01cf06416c0671253536517b6/blinker-1.4.tar.gz")
    version("1.3", sha256="6811010809262261e41ab7b92f3f6d23f35cf816fbec2bc05077992eebec6e2f", url="https://pypi.org/packages/c9/66/c15dbe2e2cac59bf1d4670d52aa88b8746fd5a47f8353aa4ffac0dde00c4/blinker-1.3.tar.gz")
    version("1.2", sha256="7062c05e9f724e2208835e335df5ffdc169004fe372ca91fb6408cd0f8e3aa85", url="https://pypi.org/packages/bf/92/b8c23de91e995d0f0245c5ebbae0e8a803bc1811be15921258a15efa1df5/blinker-1.2.tar.gz")
    version("1.1", sha256="429a2b7433715b0c9bceb65aa0a93181d57f3548f89b9794697bedeb6b513a8f", url="https://pypi.org/packages/0e/1b/4696208d895d71539aaecece524d8a0d38de86ae4a3299150b8622353a68/blinker-1.1.zip")
    version("1.0", sha256="be3495250e7a5bdf8b5cd0fcd4f3a3e235b74f7209581283ece9ca14d77a71a6", url="https://pypi.org/packages/5d/a7/cd7c985c1ce71c64f443fa2d46d93c6986505606982093d7d0cb9d79ff3e/blinker-1.0.tar.gz")
    version("0.9", sha256="564feb8981c69c8cb9eae7b08be864ebed60ab8c57e98429bf72765d68dcda26", url="https://pypi.org/packages/f7/6a/d6fe7d2ee708e019ff36cfee72567bab2b4255a38e825056d91f801b1e76/blinker-0.9.tar.gz")
    version("0.8", sha256="262256946fc67237de1f974261aab30cd1ece8b4fce251909b2bdd18318b1ed4", url="https://pypi.org/packages/66/6e/59a9fcfdaea1b6f16654b7242687e292b34aa145ece7520bc3b0649a1443/blinker-0.8.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-typing-extensions@4.2:", when="@1.6.1")
        depends_on("py-typing-extensions", when="@1.6:1.6.0")
    # END DEPENDENCIES

