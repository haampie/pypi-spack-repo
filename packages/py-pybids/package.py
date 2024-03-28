# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPybids(PythonPackage):
    # BEGIN VERSIONS
    version("0.16.3", sha256="b9f47cd964c046a03cac607e771e96a92c63d9a3f0ac2e193a9561cda39f5c68", url="https://pypi.org/packages/87/b0/bf389f857ed3397d1698ae8828808ddf06caa86310951e383aed21765ee2/pybids-0.16.3-py3-none-any.whl")
    version("0.16.1", sha256="d7522dd2c7caea38bd83335d5584841f5d8b3430afe3621320d2b1ceffdf9075", url="https://pypi.org/packages/72/9a/5131a9270e8347fe13cf3331ea8fd200fbdc33067b2c680c132f5aefed80/pybids-0.16.1-py3-none-any.whl")
    version("0.15.3", sha256="da9d14954267e1e5e5a7f6248ac39baadf050239ecee9984b6eea5bbc83d39ef", url="https://pypi.org/packages/90/e4/5193d253d03cb91ad2e9a5780a21a9b6d95c5fecb9bcb34bf949887c4513/pybids-0.15.3-py3-none-any.whl")
    version("0.15.1", sha256="241095ae856603296a9aac3e2ef51c010792657d5d2252820387e7b54bed5044", url="https://pypi.org/packages/e5/f9/45a6e5342286b8847844854ef66166097b927c701b01b2eca04cf72060db/pybids-0.15.1-py3-none-any.whl")
    version("0.14.0", sha256="65e80a6b2dacf6a3964ceef88a6a5ac4fb076ff661382bc68fd153ebce83e324", url="https://pypi.org/packages/eb/50/378279902c19b4f0f30adc76bc479e76582b06662d959eb5a8e431309ca7/pybids-0.14.0-py3-none-any.whl")
    version("0.13.2", sha256="2b34939e7c147ee557d66699bfac3a74a34db53d27b2b7e12cf8a3556f7282c3", url="https://pypi.org/packages/02/cf/8bb4c2a321d34703c8fd70bee97f8bbf79a703f670b473a4fcd20c7c4a20/pybids-0.13.2-py3-none-any.whl")
    version("0.13.1", sha256="4ca3de27013befd899f1004b32fab6257f820e94cceb61ec5dca65893b406d36", url="https://pypi.org/packages/ab/84/4e24488d0ad14a1f614500a613c5d62802f732d22ab62d98aa1295ba5f38/pybids-0.13.1-py3-none-any.whl")
    version("0.9.5", sha256="9f3c4470746adca6b07620c420d0db7d5c7666b5cf9c891590518f697924e2a5", url="https://pypi.org/packages/f0/53/1b022516c02a91b844a88f8174503c427e1ddbd8550141f201f5251d33e5/pybids-0.9.5-py2.py3-none-any.whl")
    version("0.8.0", sha256="fe60fa7d1e171e75a38a04220ed992f1b062531a7452fcb7ce5ba81bb6abfdbc", url="https://pypi.org/packages/b3/98/f64bc00977eb27680d1b973998b281f8976037a64ee6e07c0232f09f60fa/pybids-0.8.0.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-bids-validator@1.11:", when="@0.16:")
        depends_on("py-bids-validator", when="@0.9.4:0.15")
        depends_on("py-click@8.0.0:", when="@0.15.2:")
        depends_on("py-click", when="@0.12.1:0.15.1")
        depends_on("py-formulaic@0.2.4:0.5", when="@0.15.6:")
        depends_on("py-formulaic@0.2.4:0.3", when="@0.15.1:0.15.5")
        depends_on("py-formulaic@0.2.4:0.2", when="@0.14.0:0.15.0")
        depends_on("py-nibabel@3.0.0:", when="@0.16:")
        depends_on("py-nibabel@2.1:", when="@0.9.4:0.15")
        depends_on("py-num2words@0.5.5:", when="@0.16:")
        depends_on("py-num2words", when="@0.9.4:0.15")
        depends_on("py-numpy@1.19.0:", when="@0.16:")
        depends_on("py-numpy", when="@0.9.4:0.15")
        depends_on("py-pandas@0.25.2:", when="@0.16:")
        depends_on("py-pandas@0.23.0:", when="@0.9.4:0.15")
        depends_on("py-patsy", when="@0.9.4:0.13")
        depends_on("py-scipy@1.5.0:", when="@0.16:")
        depends_on("py-scipy", when="@0.9.4:0.15")
        depends_on("py-sqlalchemy@1.3.16:", when="@0.16:")
        depends_on("py-sqlalchemy@:1.3", when="@0.12.4:0.15")
        depends_on("py-sqlalchemy", when="@0.9.4:0.12.3")
    # END DEPENDENCIES

