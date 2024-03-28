# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyGoogleCloudCore(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("2.4.1", sha256="a9e6a4422b9ac5c29f79a0ede9485473338e2ce78d91f2370c01e730eab22e61", url="https://pypi.org/packages/5e/0f/2e2061e3fbcb9d535d5da3f58cc8de4947df1786fe6a1355960feb05a681/google_cloud_core-2.4.1-py2.py3-none-any.whl")
    version("2.4.0", sha256="f8af1b71002b685345ffcac2c96e0207b3782c358c3d4f9bafe601f470481a34", url="https://pypi.org/packages/06/97/7cba235a8e762f28c85af41a42893c1a63dfe797a8abe35d89040661b1b5/google_cloud_core-2.4.0-py2.py3-none-any.whl")
    version("2.4.0-rc1", sha256="23a5bcad078376448961e35dcd093932eea1d717160ce332f06fcaebfece0682", url="https://pypi.org/packages/8f/5f/7cd1cf1b838f220fb3567301d3802208f3c4a64ecb1ca2fbb61f10352492/google_cloud_core-2.4.0rc1-py2.py3-none-any.whl")
    version("2.3.3", sha256="fbd11cad3e98a7e5b0343dc07cb1039a5ffd7a5bb96e1f1e27cee4bda4a90863", url="https://pypi.org/packages/a2/40/02045f776fdb6e44194f34b6375a26ce8a61bd9bd03cd8930ed91cf51a62/google_cloud_core-2.3.3-py2.py3-none-any.whl")
    version("2.3.2", sha256="8417acf6466be2fa85123441696c4badda48db314c607cf1e5d543fa8bdc22fe", url="https://pypi.org/packages/ac/4d/bae84e736080ed465a6b02e9f447c89c60c00fcdade2eb6911fecf3f46aa/google_cloud_core-2.3.2-py2.py3-none-any.whl")
    version("2.3.1", sha256="113ba4f492467d5bd442c8d724c1a25ad7384045c3178369038840ecdd19346c", url="https://pypi.org/packages/ac/4f/f011ffb5f00d78630e032c27ad0650a3103982d53b17618b2c9a6950686b/google_cloud_core-2.3.1-py2.py3-none-any.whl")
    version("2.3.0", sha256="35900f614045a33d5208e1d50f0d7945df98ce088388ce7237e7a2db12d5656e", url="https://pypi.org/packages/a8/46/aa46ebd6fc4db7938ef7f7179a0959f1e33f914617c51fcea0bbd5ddfb8f/google_cloud_core-2.3.0-py2.py3-none-any.whl")
    version("2.2.3", sha256="a423852f4c36622376c8f0be509b67533690e061062368b763b92694c4ee06a7", url="https://pypi.org/packages/72/f6/aa1f420491d417055b55909ec6547e7c0fc8dc5671ec6d8d9310fac11646/google_cloud_core-2.2.3-py2.py3-none-any.whl")
    version("2.2.2", sha256="d9cffaf86df6a876438d4e8471183bbe404c9a15de9afe60433bc7dce8cb4252", url="https://pypi.org/packages/46/f3/f9c5c8f21c0e8650df13378d52399f8eb239c50caa4593505767248202cc/google_cloud_core-2.2.2-py2.py3-none-any.whl")
    version("2.2.1", sha256="ab6cee07791afe4e210807ceeab749da6a076ab16d496ac734bf7e6ffea27486", url="https://pypi.org/packages/9d/ea/b051b33ee2cdd1b367ffd5a983653f8887552cafb0df5fa82fc3fdc8b73d/google_cloud_core-2.2.1-py2.py3-none-any.whl")
    version("2.2.0", sha256="469afa08e790f55b7616fa6548fdd99377ae09a4c3fdb05839b7629b124c7090", url="https://pypi.org/packages/06/b4/714188755831c855ae266c054bb171b63633dd385d73010b23bc1791f02f/google_cloud_core-2.2.0-py2.py3-none-any.whl")
    version("1.7.3", sha256="d5af737c60a73b9588a0511332ac0cdc6294ad8e477c7b82be03a1afc7c3f7b6", url="https://pypi.org/packages/18/52/f1e01017a8e799e303b53f458bc5a09f864b7ac47a5afafbb6effed05b6d/google_cloud_core-1.7.3-py2.py3-none-any.whl")
    version("1.7.2", sha256="5b77935f3d9573e27007749a3b522f08d764c5b5930ff1527b2ab2743e9f0c15", url="https://pypi.org/packages/f0/55/e8253cfd0b811cd0dc934a980c3842bfb8064944e363c1e6245f0c8a46c6/google_cloud_core-1.7.2-py2.py3-none-any.whl")
    version("1.7.1", sha256="31e8c8596d3fbe2ecbe8708572b48741f8b247a78740aebfaf4da445487a1af5", url="https://pypi.org/packages/88/a7/b74266a6fd888d91a6f517c574c17425731181fe44e2df1e414d4b77fbe8/google_cloud_core-1.7.1-py2.py3-none-any.whl")
    version("1.7.0", sha256="9bd528810423aeaa428a9a178e7320883bbb690a8b0bb38297b794dc319c415a", url="https://pypi.org/packages/f7/10/e1afff08fc67491717d430aeca479ef4f0255843c9c8b472e5efd62782dc/google_cloud_core-1.7.0-py2.py3-none-any.whl")
    version("1.6.0", sha256="40d9c2da2d03549b5ac3dcccf289d4f15e6d1210044c6381ce45c92913e62904", url="https://pypi.org/packages/ad/fc/6e8c449185cb8862af353c1164100ff75e32d55ba1de3baf9eaa01b7d2a9/google_cloud_core-1.6.0-py2.py3-none-any.whl")
    version("1.5.0", sha256="99a8a15f406f53f2b11bda1f45f952a9cdfbdbba8abf40c75651019d800879f5", url="https://pypi.org/packages/36/82/d54bdbdbae02c66ec26c97eb684cfb27af82b3e286497625b815c4741792/google_cloud_core-1.5.0-py2.py3-none-any.whl")
    version("1.4.4", sha256="1445266e70e3ea068915259bfa9db2736076d01ac4c60b919c11ef75ba831adf", url="https://pypi.org/packages/b9/be/66b4b7c7e94879257f404a716385c62c0629e011351009c646dd04813175/google_cloud_core-1.4.4-py2.py3-none-any.whl")
    version("1.4.3", sha256="75abff9056977809937127418323faa3917f32df68490704d39a4f0d492ebc2b", url="https://pypi.org/packages/8c/00/24a1d64e7340485302d6ca5bc7328ac8a8ec785d2ae1dae12e0750b202cb/google_cloud_core-1.4.3-py2.py3-none-any.whl")
    version("1.4.2", sha256="64c35fc379e51cadac7fc9cdef0777369ca1370c2eb2d51823fd0cd4c2d16082", url="https://pypi.org/packages/f3/bc/e1778d923df12b9f10a587f09f98acdc6e603ceb27c16fd0f73e97c4f905/google_cloud_core-1.4.2-py2.py3-none-any.whl")
    version("1.4.1", sha256="4c9e457fcfc026fdde2e492228f04417d4c717fb0f29f070122fb0ab89e34ebd", url="https://pypi.org/packages/a8/c8/9be9810356f62daea7e417164db6eb4b5f5edf087a9516fa4602de8b1924/google_cloud_core-1.4.1-py2.py3-none-any.whl")
    version("1.0.3", sha256="0ee17abc74ff02176bee221d4896a00a3c202f3fb07125a7d814ccabd20d7eb5", url="https://pypi.org/packages/ee/f0/084f598629db8e6ec3627688723875cdb03637acb6d86999bb105a71df64/google_cloud_core-1.0.3-py2.py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-google-api-core@1.31.6:1,2.3.1:", when="@2.3.2:")
        depends_on("py-google-api-core@1.31.5:1,2.3.1:", when="@2.2.3:2.3.1")
        depends_on("py-google-api-core@1.21:", when="@1.7.3:2.2.2")
        depends_on("py-google-api-core@1.21:1", when="@1.4.4:1.7.2")
        depends_on("py-google-api-core@1.19:1", when="@1.4.1:1.4.3")
        depends_on("py-google-api-core@1.14:1", when="@1.0.3:1.1")
        depends_on("py-google-auth@1.25:", when="@2.2.3:")
        depends_on("py-google-auth@1.24:", when="@2:2.2.2")
        depends_on("py-google-auth@1.24:1", when="@1.6:1")
        depends_on("py-six@1.12:", when="@1.4.4:1")
    # END DEPENDENCIES

