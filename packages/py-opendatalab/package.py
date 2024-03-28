# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyOpendatalab(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("0.0.10", sha256="b6a317785b7db418739933d4af6d981a0e45f6cf20a3e113bef63ed9b4488251", url="https://pypi.org/packages/10/82/28fa3a91b7c4852fbad9ad32c7b49e4b1e212ab7ccf7296736da0935070d/opendatalab-0.0.10-py3-none-any.whl")
    version("0.0.9", sha256="4129a2e70820754538e24132e5b37acefa0abffda6ff687c75f42479e17d6e6f", url="https://pypi.org/packages/13/6e/5725353a3eb77c65b7400fc163f02e8b689d5f0c7e0504c55b1b1d33091f/opendatalab-0.0.9-py3-none-any.whl")
    version("0.0.8", sha256="bbee643adf9d68948d19a39aa58473283d09668687e9841ef8e5aa01563efc11", url="https://pypi.org/packages/5e/60/cf0c1b5aa3bca721073cd014c69a785122f9b8500312edf0fb5b079fc0d9/opendatalab-0.0.8-py3-none-any.whl")
    version("0.0.7", sha256="c8b8ee104a6f3fa9fcbffab68f70b0f4834c89b3a9785d9c347ee1d09927d7b2", url="https://pypi.org/packages/f3/59/5ca3a453c8fca10f540d172f015735006553a46379dbefd465c8261594b7/opendatalab-0.0.7-py3-none-any.whl")
    version("0.0.6", sha256="57e7040862a3ea6c7cee1a76f53d17b20b4ff9cfe24f82bfa298f8e5ac4f1abd", url="https://pypi.org/packages/ae/b5/fe268bd572401ed24abc662e993d4b43c68c47a7056008dd5862b599737e/opendatalab-0.0.6-py3-none-any.whl")
    version("0.0.4", sha256="8c49e7c1738467ffd4e6bf80b3d55c4272eda77583233b9db3c8d9bf62ab1d4c", url="https://pypi.org/packages/77/ad/73420a7c59bac3c9a089ec5119606c6afb46a0ba44bd3c4a66298e113568/opendatalab-0.0.4-py3-none-any.whl")
    version("0.0.3.1", sha256="e36883f435aa7715299907b5b9360842f3ac70387cf35dd8e9b5cc4a5bfc08bd", url="https://pypi.org/packages/ec/56/490004af0c8b911622bd9cf3743522d96b24b883452c9ba7043549fb472e/opendatalab-0.0.3.1-py3-none-any.whl")
    version("0.0.3", sha256="0080dae44dd4f290d49ab983efd2e96101eae4d46796cff005678e692f03faf0", url="https://pypi.org/packages/46/ba/5e1e4d4e39b3666a211bffcd9bf4f9372832ccaa57e0a2c2dc2fc9059003/opendatalab-0.0.3-py3-none-any.whl")
    version("0.0.2", sha256="4ab2c49c186808bf738c47f3d77c69dd6e62e97627b63101e811f822715b4dce", url="https://pypi.org/packages/c7/79/fb7ae213a0c4da677600a35b7507f97237a37ea32ba51610f09d99213835/opendatalab-0.0.2-py3-none-any.whl")
    version("0.0.1", sha256="c84441a940551c4ec0eaf4377108d0845a36bcfc6b129886e9b7af67a37bedd0", url="https://pypi.org/packages/80/76/b1a660758259b6c4ca36695bd3b3a09031e5880e9f666e10fc6c4da4af85/opendatalab-0.0.1-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-click@7:", when="@0.0.1-beta54:")
        depends_on("py-colorama", when="@0.0.1-beta71:")
        depends_on("py-openxlab", when="@0.0.10:")
        depends_on("py-oss2", when="@:0.0.4")
        depends_on("py-pycryptodome", when="@0.0.6:")
        depends_on("py-pywin32", when="@0.0.1-beta92: platform=windows")
        depends_on("py-requests@2.4.2:", when="@0.0.1-beta54:")
        depends_on("py-rich", when="@0.0.1-beta75:")
        depends_on("py-tqdm@4.14:", when="@0.0.1-beta54:0.0.4")
        depends_on("py-tqdm", when="@:0.0.1-beta53,0.0.6:")
    # END DEPENDENCIES

