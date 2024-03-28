# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyTempora(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("5.5.1", sha256="33c1ef063c41d9ea14e7c2f809783241c982863e813d6a9cd138d1a48d796ce8", url="https://pypi.org/packages/a5/94/f5d4d08524113849fadb1d8d1669d82dad885b0f9a41b1b633b7525166b0/tempora-5.5.1-py3-none-any.whl")
    version("5.5.0", sha256="defd976c9144fc9f20432ed0d75926c1c48dd0c7c701b3493e02d5316598e8fe", url="https://pypi.org/packages/3f/8c/db20cbcd6c8bcd06fe6a893fbb437e68e9962542f77ea273cb47109347e8/tempora-5.5.0-py3-none-any.whl")
    version("5.4.0", sha256="319accf5adb2e6c780e5e642a8ca97ba856f8c936652c23fe42d2b71aa043042", url="https://pypi.org/packages/bb/2e/2f7afa803506f21b9c228a6b87ca587c22a7a311c532465e412195777a37/tempora-5.4.0-py3-none-any.whl")
    version("5.3.0", sha256="66b2fd527b52d96fb48f90df843195d1a6846f41e6a255c6a0738ac2d34f852d", url="https://pypi.org/packages/7f/1f/493c6edae91aca7fb267b197b5cc0938d8160c109f0ebd2cd2bebc659d95/tempora-5.3.0-py3-none-any.whl")
    version("5.2.2", sha256="003873654acaa49ecca810cee44665d827301134422505386e76f7b080461edb", url="https://pypi.org/packages/86/fa/3f956372b84f977f8f4e9181d42fa2ba8459f8d8f056dcd2f91358571559/tempora-5.2.2-py3-none-any.whl")
    version("5.2.1", sha256="6a04665b35a2e0c3bef2aa71ce15d3d381b912e4fc3340b0b8a73719c2aeeb75", url="https://pypi.org/packages/e4/dc/484ee953d1deef7d2c762c7d97529cbcb49396484ac3fd221b0879bc39bd/tempora-5.2.1-py3-none-any.whl")
    version("5.2.0", sha256="2e57fedfdd11da1aee4b30b6e7af81bce3de2d5da65e996241b66de554eedeee", url="https://pypi.org/packages/63/63/88634fd717538bb9dc5181e6cbf7b2e60836d07572fdba9f4c1b017d51e8/tempora-5.2.0-py3-none-any.whl")
    version("5.1.1", sha256="662989c284d2f8cd5f409fa710ab469d6dfa749cdc3c7e54c9999b60ba15b59b", url="https://pypi.org/packages/49/ec/af472ab591838436459f57df39c362888b22d080ec481b27519af8296476/tempora-5.1.1-py3-none-any.whl")
    version("5.1.0", sha256="c2807480b7d97d2eb059e75540c214bff7ce78e5a638c90ca892c197557ad3ba", url="https://pypi.org/packages/7f/62/81ace1fd57017ca3eb34bbd7506d0feaf0681e254eec98c1e85eda332343/tempora-5.1.0-py3-none-any.whl")
    version("5.0.2", sha256="e65d32ae68ad772ee738d802689f689b3f883e165e8dadd39aa89ef317b12b99", url="https://pypi.org/packages/4f/7e/872038fa04eeb69b7832a10ecc04f52d9950c41333cfaf2966fd5b06e65c/tempora-5.0.2-py3-none-any.whl")
    version("1.14.1", sha256="d28a03d2f64ee81aec6e6bff374127ef306fe00c1b7e27c7ff1618344221a699", url="https://pypi.org/packages/5c/12/4c97c44e5c9d111649e363353a4ca3ece9c6cc04b11cc48540f26e42d7b9/tempora-1.14.1-py2.py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-jaraco-functools@1.20:", when="@1.13:5.1,5.2.1:")
        depends_on("py-pytz", when="@1.6:")
        depends_on("py-six", when="@1.6:1")
    # END DEPENDENCIES

