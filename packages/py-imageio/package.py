# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyImageio(PythonPackage):
    # BEGIN VERSIONS
    version("2.30.0", sha256="e045e9593ed94af41759901d6a51d5313b1e78fc118b6befbbfbf4e9cbe7398a", url="https://pypi.org/packages/26/ae/862bd5b3751d9b7bf8db5fb1595bd06d2875997ca79d85bd5847eb7916af/imageio-2.30.0-py3-none-any.whl")
    version("2.22.0", sha256="aff0e9b5faf4936728f982a1ab63797b1339847a4533c3e4c8343635149dfbfc", url="https://pypi.org/packages/78/7a/3e4e595faea7112785de0a78efd8349a860b2ce6cd4d8fc15afe42c27f5f/imageio-2.22.0-py3-none-any.whl")
    version("2.16.0", sha256="1ee35330318bcb0ce25de778fc1f61555558a159433a568887d7e3d0317ce63c", url="https://pypi.org/packages/58/fc/1547b93534279bbf2de88f7c4a88975a65cecafd32c2bd3c518b2054ef76/imageio-2.16.0-py3-none-any.whl")
    version("2.10.3", sha256="93ee376a8dc96182ead8d773c3ac2becf79c6f2b93d38f31d7ac036c62a6c72e", url="https://pypi.org/packages/17/be/4a836c9262b40454c2834c5ab1a20a35e2f23216b0744f666395fab8a046/imageio-2.10.3-py3-none-any.whl")
    version("2.9.0", sha256="3604d751f03002e8e0e7650aa71d8d9148144a87daf17cb1f3228e80747f2e6b", url="https://pypi.org/packages/6e/57/5d899fae74c1752f52869b613a8210a2480e1a69688e65df6cb26117d45d/imageio-2.9.0-py3-none-any.whl")
    version("2.5.0", sha256="1a2bbbb7cd38161340fa3b14d806dfbf914abf3ee6fd4592af2afb87d049f209", url="https://pypi.org/packages/af/0a/943c965d372dae0b1f1482677d29030ab834351a61a9a632fd62f27f1523/imageio-2.5.0-py3-none-any.whl")
    version("2.4.1", sha256="16b8077bc8a5fa7a58b3e744f7ecbb156d8c088132df31e0f4f546c98de3514a", url="https://pypi.org/packages/28/b4/cbb592964dfd71a9de6a5b08f882fd334fb99ae09ddc82081dbb2f718c81/imageio-2.4.1.tar.gz")
    version("2.3.0", sha256="0f8281453c74433fcf4c7a1cf36801e6da9a4ba3117799fffd5a4db7d745e1b7", url="https://pypi.org/packages/a7/1d/33c8686072148b3b0fcc12a2e0857dd8316b8ae20a0fa66c8d6a6d01c05c/imageio-2.3.0-py2.py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("python@3.7:", when="@2.16.1:2.31.2")
        depends_on("py-numpy@1.20.0:", when="@2.16")
        depends_on("py-numpy", when="@2.10:2.15,2.17:")
        depends_on("py-pillow@8.3.2:", when="@2.10:2.31.5,2.33:")
    # END DEPENDENCIES

