# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyRospkg(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("1.5.0", sha256="420f2f23a4751ecbd6ab6ab02f1f7ce692f1f9f897b87210cdb59e2a3a00f0f7", url="https://pypi.org/packages/62/15/91e07b85c6aa7feec86257c3e9966de1d6bb61844d133d2b939294bc2ccf/rospkg-1.5.0-py3-none-any.whl")
    version("1.4.0", sha256="582388a583df05cbe6252a69d02d0fbc313f4ce65ee2dc96582baa96b0811f61", url="https://pypi.org/packages/9b/be/70454d42c1a8f670385d6b679ca672102a4e3b9ecfb4ed922ea9ba19b9ab/rospkg-1.4.0-py3-none-any.whl")
    version("1.3.0", sha256="dc8fab3ed3f163bc301f94ec65ed39a2c40ded6757615a0fb9f2cb2c82470fbe", url="https://pypi.org/packages/89/00/2e239dfe86120c9721f4570a0fc8233186331cdf89a517549b7be6ac4220/rospkg-1.3.0-py3-none-any.whl")
    version("1.2.10", sha256="307cbc1534fb931d336867bb47f20fffc6698c83a80633bfd4f13ae8671384e3", url="https://pypi.org/packages/67/73/5d5bb03c0d75dc0c4cea8c58ab42f7ca4e1fd50ec67156c48586a32be842/rospkg-1.2.10-py3-none-any.whl")
    version("1.2.9", sha256="7494c6c7c268c99c51e9d98b0a9eee82900cfd97408e485c6a4294898d834ad6", url="https://pypi.org/packages/66/78/5395e9e4d3767f27ae63d74777e3fd735a2aaf9d764de8fc9f042d899dfc/rospkg-1.2.9-py3-none-any.whl")
    version("1.2.8", sha256="61dc65c5575fe5fe8061fe1064f439fe64a17af6dcad42efefbe4ca0490661cc", url="https://pypi.org/packages/db/f5/055fd15c610452adb1915172365394564ebdf251a764320bcb40d4118df1/rospkg-1.2.8-py3-none-any.whl")
    version("1.2.7", sha256="ba47962001914a9fe9d62d9c52440a860de53b8bfb2f0437d60a9707e303e665", url="https://pypi.org/packages/d1/05/44c095057d86991025a30af02d16bcce182ab8323161e6297997162f52fd/rospkg-1.2.7-py3-none-any.whl")
    version("1.2.6", sha256="357632bd6a477fee4d5bf4f55eeef46d4dd5ddc714211d4298923994de356cc3", url="https://pypi.org/packages/f5/f0/342a15a23fd5dc6ad2c45c0dd87878501f1c6ddb2bd5a8a35850453d3f43/rospkg-1.2.6-py3-none-any.whl")
    version("1.2.5", sha256="8989f0c413f0a6d5c02751635bdb8de7de9be04a28238218842da1ff8383fe04", url="https://pypi.org/packages/c7/2f/a6ebe198c131541ce0b0a82e23bded0f64b3fbbfafa7f061bb46005fba2f/rospkg-1.2.5-py3-none-any.whl")
    version("1.2.4", sha256="03ce13e780ac475f8592e2eddd5d59bb3ca652b92ae1cac1787927a59f3c2d37", url="https://pypi.org/packages/0c/94/c7a7024e31cb51a5f00e1210f9983ece89d0e17ac8af5805a6cc18f79452/rospkg-1.2.4-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-catkin-pkg", when="@1.1.5:")
        depends_on("py-distro@1.4:", when="@1.4:")
        depends_on("py-distro", when="@1.2.1:1.2.4,1.2.6:1.3")
        depends_on("py-pyyaml", when="@1.1.5:")
    # END DEPENDENCIES

