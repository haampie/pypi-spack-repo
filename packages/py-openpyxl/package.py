# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyOpenpyxl(PythonPackage):
    # BEGIN VERSIONS
    version("3.1.2", sha256="f91456ead12ab3c6c2e9491cf33ba6d08357d802192379bb482f1033ade496f5", url="https://pypi.org/packages/6a/94/a59521de836ef0da54aaf50da6c4da8fb4072fb3053fa71f052fd9399e7a/openpyxl-3.1.2-py2.py3-none-any.whl")
    version("3.0.7", sha256="46af4eaf201a89b610fcca177eed957635f88770a5462fb6aae4a2a52b0ff516", url="https://pypi.org/packages/39/08/595298c9b7ced75e7d23be3e7596459980d63bc35112ca765ceccafbe9a4/openpyxl-3.0.7-py2.py3-none-any.whl")
    version("3.0.3", sha256="547a9fc6aafcf44abe358b89ed4438d077e9d92e4f182c87e2dc294186dc4b64", url="https://pypi.org/packages/95/8c/83563c60489954e5b80f9e2596b93a68e1ac4e4a730deb1aae632066d704/openpyxl-3.0.3.tar.gz")
    version("2.4.5", sha256="78c331e819fb0a63a1339d452ba0b575d1a31f09fdcce793a31bec7e9ef4ef21", url="https://pypi.org/packages/85/19/0794013228f8e68dbdfdde3fb5f75cd14e729ff55dee77c3500db3db59d8/openpyxl-2.4.5.tar.gz")
    version("2.2.0", sha256="c34e3f7e3106dbe6d792f35d9a2f01c08fdd21a6fe582a2f540e39a70e7443c4", url="https://pypi.org/packages/de/6c/46a2c08780ae44d6e4b7f2cb36fcf2b6d9a0ff30c188870d5b5805194fad/openpyxl-2.2.0.tar.gz")
    version("1.8.6", sha256="87fdfe6ada6a296e696777bdd9b1eba019d38332d5e1efdbeb6ea7e1f02161ac", url="https://pypi.org/packages/eb/38/e52d897f0529c470a335b347c6b4e7feb5992d231e3601f2ea0b33745075/openpyxl-1.8.6-py2.py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-et-xmlfile", when="@2.6.0-beta1,3.0.4:")
    # END DEPENDENCIES

