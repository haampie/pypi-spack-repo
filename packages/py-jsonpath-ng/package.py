# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyJsonpathNg(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("1.6.1", sha256="8f22cd8273d7772eea9aaa84d922e0841aa36fdb8a2c6b7f6c3791a16a9bc0be", url="https://pypi.org/packages/16/0a/3b1ee3721b4bd684b0e29c724ab82ed3b2c0e42285beb8bf9e18de8c903f/jsonpath_ng-1.6.1-py3-none-any.whl")
    version("1.6.0", sha256="6fd04833412c4b3d9299edf369542f5e67095ca84efa17cbb7f06a34958adc9f", url="https://pypi.org/packages/92/8d/f6592a8267fcf85d4066605d671b509b456866b962554112c562d2b8be4b/jsonpath_ng-1.6.0-py3-none-any.whl")
    version("1.5.3", sha256="292a93569d74029ba75ac2dc3d3630fc0e17b2df26119a165fa1d498ca47bf65", url="https://pypi.org/packages/4c/b7/3627068d9aa6b2d49af117eb3897770a5dbc6bb3f4c09ed56a9eb749438e/jsonpath_ng-1.5.3-py3-none-any.whl")
    version("1.5.2", sha256="93d1f248be68e485eb6635c3a01b2d681f296dc349d71e37c8755837b8944d36", url="https://pypi.org/packages/ae/03/a8a12e49e88ba7983d704ef518e25041206aa2e934686270516f1bc439ff/jsonpath_ng-1.5.2-py3-none-any.whl")
    version("1.5.1", sha256="a4f014c28b5a1279c3a189fb1d2f37a98848f359f19fd296b54e38ec6fc841a9", url="https://pypi.org/packages/e9/6d/cab299e17c3fdcb65d473bae36997b3924fc82b0a7466e3e258fb590a993/jsonpath_ng-1.5.1-py2-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-decorator", when="@1.5")
        depends_on("py-ply", when="@1.5:")
        depends_on("py-six", when="@1.5")
    # END DEPENDENCIES

