# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyStdlibList(PythonPackage):
    # BEGIN VERSIONS
    version("0.10.0", sha256="b3a911bc441d03e0332dd1a9e7d0870ba3bb0a542a74d7524f54fb431256e214", url="https://pypi.org/packages/13/d9/9085375f0d23a4896b307bf14dcc61b49ec8cc67cb33e06cf95bf3af3966/stdlib_list-0.10.0-py3-none-any.whl")
    version("0.9.0", sha256="f79957d59e41930d44afcd81e465f740b9a7a9828707a40e24ab1092b12bd423", url="https://pypi.org/packages/be/f4/08daf83c6414031b46e883cb5e06286077e52e8e2f1ae4b3662819a211aa/stdlib_list-0.9.0-py3-none-any.whl")
    version("0.8.0", sha256="2ae0712a55b68f3fbbc9e58d6fa1b646a062188f49745b495f94d3310a9fdd3e", url="https://pypi.org/packages/7a/b1/52f59dcf31ead2f0ceff8976288449608d912972b911f55dff712cef5719/stdlib_list-0.8.0-py3-none-any.whl")
    version("0.7.0", sha256="0ed79a0badf4f666aad046cde364ccac68ca1438a211ec74b0153e0eb5642a3e", url="https://pypi.org/packages/01/ff/14394967130e95720c30ba2bbe4b4e25695afd5304bd128134116e293c0e/stdlib_list-0.7.0-py3-none-any.whl")
    version("0.6.0", sha256="133cc99104f5a4e1604dc88ebb393529bd4c2b99ae7e10d46c0b596f3c67c3f0", url="https://pypi.org/packages/85/1b/48e7ab73af72f49226651a0bb389e5d7c1db8daf9c6fa93f792c371a1787/stdlib-list-0.6.0.tar.gz")
    version("0.5.0", sha256="fe30e9fc98304de4207f545311c75a6ad7701719bbeb1ac018a0fcf6aa70c0ce", url="https://pypi.org/packages/14/85/4bdbceb14c9a75507d3991066e5fed8415acc231957d4d9529cc8ec7e3fc/stdlib_list-0.5.0-py3-none-any.whl")
    version("0.4.0", sha256="3f6cafd9a2e86b22d475a52433d95143c1ee64c02b73d403c6ef6df38ce3f8fd", url="https://pypi.org/packages/41/38/56992f4afe91c26bf78d4d9d37e10f5c8291a4a206063a945bac77d505c1/stdlib_list-0.4.0-py2.py3-none-any.whl")
    version("0.3.4", sha256="f23a24827ff1220be5352fa8ecb27f72223cd6d8e2c59fa2e2d27541c2f1a6a8", url="https://pypi.org/packages/39/57/57968c714f6d993fe7360580af19b1e2a48715f41bde75c20f15e84e69d2/stdlib_list-0.3.4-py2.py3-none-any.whl")
    version("0.3.3", sha256="e0ea0ead3a63193a4efc4cf02b5f3ccd3bcad8455bfe9de0464d7787ee03d0d5", url="https://pypi.org/packages/52/76/a2e16778b3c9c9bc733e4995f9c4ec342410ef396c3e5d72cea969ae3575/stdlib_list-0.3.3-py2.py3-none-any.whl")
    version("0.3.2", sha256="fd173144671b5beebcaaf68341533fafc038b09fdbfee67ce2b222dd7a70c9b3", url="https://pypi.org/packages/68/c1/e3840a0c608bb98d418a9a2b909823e24b0c1e256ebb076c8672ed51b87a/stdlib_list-0.3.2-py2.py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-sphinx", when="@0.3.2")
    # END DEPENDENCIES

