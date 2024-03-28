# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyFsspec(PythonPackage):
    # BEGIN VERSIONS
    version("2024.2.0", sha256="817f969556fa5916bc682e02ca2045f96ff7f586d45110fcb76022063ad2c7d8", url="https://pypi.org/packages/ad/30/2281c062222dc39328843bd1ddd30ff3005ef8e30b2fd09c4d2792766061/fsspec-2024.2.0-py3-none-any.whl")
    version("2023.10.0", sha256="346a8f024efeb749d2a5fca7ba8854474b1ff9af7c3faaf636a4548781136529", url="https://pypi.org/packages/e8/f6/3eccfb530aac90ad1301c582da228e4763f19e719ac8200752a4841b0b2d/fsspec-2023.10.0-py3-none-any.whl")
    version("2023.1.0", sha256="b833e2e541e9e8cde0ab549414187871243177feb3d344f9d27b25a93f5d8139", url="https://pypi.org/packages/bd/64/f0d369ede0ca54fdd520bdee5086dbaf0af81dac53a2ce847bd1ec6e0bf1/fsspec-2023.1.0-py3-none-any.whl")
    version("2022.11.0", sha256="d6e462003e3dcdcb8c7aa84c73a228f8227e72453cd22570e2363e8844edfe7b", url="https://pypi.org/packages/37/57/eb7c3c10b187d3b8565946772ce0229c79e3c623010eda0aeb5032ff56f4/fsspec-2022.11.0-py3-none-any.whl")
    version("2021.7.0", sha256="86822ccf367da99957f49db64f7d5fd3d8d21444fac4dfdc8ebc38ee93d478c6", url="https://pypi.org/packages/40/e1/7111d8afc76ee3171f4f99592cd29bac9d233ae1aa34623011506f955434/fsspec-2021.7.0-py3-none-any.whl")
    version("2021.4.0", sha256="70dae1d8d51072c4a1196acb9ba1bf8f5b9cdd83c4bb67e8a31dac604a49594b", url="https://pypi.org/packages/e9/91/2ef649137816850fa4f4c97c6f2eabb1a79bf0aa2c8ed198e387e373455e/fsspec-2021.4.0-py3-none-any.whl")
    version("0.9.0", sha256="7e98ea66f3f0156601e126fb2799e5d0ed87c3108b519f64c834b4284509fc82", url="https://pypi.org/packages/62/11/f7689b996f85e45f718745c899f6747ee5edb4878cadac0a41ab146828fa/fsspec-0.9.0-py3-none-any.whl")
    version("0.8.0", sha256="ce109f41ffe62853d5de84888f3e455c39f2a0796c05b558474c77156e19b570", url="https://pypi.org/packages/d3/66/974e01194980d9780cc09724315111f9cccba26b4351552fdb4d97eb842e/fsspec-0.8.0-py3-none-any.whl")
    version("0.7.3", sha256="9f0e3f4915b463b94c5788afa37b89d2c29c696f0d4da7d05f9cb5b17c8c84f7", url="https://pypi.org/packages/e9/fa/51b4b5630d6c8ce08aac7370989949d534052fb0e80a749fe8980b1d86d9/fsspec-0.7.3-py3-none-any.whl")
    version("0.4.4", sha256="97697a46e8bf8be34461c2520d6fc4bfca0ed749b22bb2b7c21939fd450a7d63", url="https://pypi.org/packages/44/99/39445aabe009d2327a369e74dea98178a5d757023e214ee478fdbec5844d/fsspec-0.4.4.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    variant("http", default=False)
    # END VARIANTS

    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-aiohttp@:3", when="@2022.8:+http")
        depends_on("py-aiohttp", when="@0.8.1:2022.7+http")
        depends_on("py-requests", when="@0.8.1:2023+http")
    # END DEPENDENCIES

