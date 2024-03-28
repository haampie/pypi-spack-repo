# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyIgor2(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("0.5.5", sha256="352a78017bad583fb549d40683d6569fc1daae1f5869fbc1aaf059f297bf83c5", url="https://pypi.org/packages/74/63/08d9bcdeffdcf785558f38112698ccfbf810e609b7431fbc09acd6c5ffe3/igor2-0.5.5-py3-none-any.whl")
    version("0.5.3", sha256="bb7b54a5926ec640e0e9176f46e0dd88ad956fec2d17ba3b0a7687eba82cefee", url="https://pypi.org/packages/5c/b8/5c73c5c54804323c8b5b1a52b68ff5d34a22d52bbd9bc0dd6d63745e4f1e/igor2-0.5.3-py3-none-any.whl")
    version("0.5.2", sha256="ffa9582b79da8130bbb031b913b7da86c8ee49853f1d03b1c06448bb2556387f", url="https://pypi.org/packages/4a/5b/e1dab83d6b419af2e0887aeafb3a133d0d85fbc6fb5eaec6e63e364e9aa5/igor2-0.5.2-py3-none-any.whl")
    version("0.5.1", sha256="831b7bac48c24722380a88ce916a63957781425ba4e96a558e90647eecf88d0a", url="https://pypi.org/packages/37/e9/4b47d923eca05ae6b60835edce464fb893b9ffa805c9730c8b041cd3a7b3/igor2-0.5.1-py3-none-any.whl")
    version("0.4.0", sha256="442c624a1dddaee232958268dd549f2dae26334b465fca262568bfee0d57ec79", url="https://pypi.org/packages/c7/18/4514deb253da8382aeeca7a262740092af3d8222ad792bc66e6f86086bc2/igor2-0.4.0-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-numpy@1.25.1:", when="@0.5.3:")
        depends_on("py-numpy", when="@:0.5.2")
    # END DEPENDENCIES

