##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyJsonpathNg(PythonPackage):
    version("1.6.1", sha256="8f22cd8273d7772eea9aaa84d922e0841aa36fdb8a2c6b7f6c3791a16a9bc0be", url="https://pypi.org/packages/16/0a/3b1ee3721b4bd684b0e29c724ab82ed3b2c0e42285beb8bf9e18de8c903f/jsonpath_ng-1.6.1-py3-none-any.whl")
    version("1.6.0", sha256="6fd04833412c4b3d9299edf369542f5e67095ca84efa17cbb7f06a34958adc9f", url="https://pypi.org/packages/92/8d/f6592a8267fcf85d4066605d671b509b456866b962554112c562d2b8be4b/jsonpath_ng-1.6.0-py3-none-any.whl")
    version("1.5.3", sha256="a273b182a82c1256daab86a313b937059261b5c5f8c4fa3fc38b882b344dd567", url="https://pypi.org/packages/cd/c2/5cd85d8a7de7818892fd8f751d30b6d050a8471c6647d2fda47cc542f9b4/jsonpath-ng-1.5.3.tar.gz")
    version("1.5.2", sha256="93d1f248be68e485eb6635c3a01b2d681f296dc349d71e37c8755837b8944d36", url="https://pypi.org/packages/ae/03/a8a12e49e88ba7983d704ef518e25041206aa2e934686270516f1bc439ff/jsonpath_ng-1.5.2-py3-none-any.whl")
    version("1.5.1", sha256="77b1f93f4444a50c924cb11cdc273546ff79f41830d485916fc6ddf4e0c1ce55", url="https://pypi.org/packages/85/24/981fa76e1e415bcceb3a9741d5be04b32c10edd42d88f6783faa750b1239/jsonpath-ng-1.5.1.tar.gz")

    with default_args(type="run"):
        depends_on("py-decorator", when="@1.5:1.5.2")
        depends_on("py-ply", when="@1.5:1.5.2,1.6:")
        depends_on("py-six", when="@1.5:1.5.2")

