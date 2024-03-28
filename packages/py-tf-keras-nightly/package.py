# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyTfKerasNightly(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("2.17.0.dev2024031909", sha256="47edc96d3499bfea9784194e988143c54dd82bd4e28f6cd696e90bfa920fccda", url="https://pypi.org/packages/70/4c/fa4fd060ba625659ba0e37a474fdd3497e76a0b5c3ffce74395f1a2da262/tf_keras_nightly-2.17.0.dev2024031909-py3-none-any.whl")
    version("2.17.0.dev2024031809", sha256="7e61d237f9e53151ad80d8bcefe977cd72b6a366b1df8f4983527abf8a177e98", url="https://pypi.org/packages/c0/00/0ae7b5c5bb711e1367bd7cd6550d78c4d4b3e7824828d74f191c2e7ba43b/tf_keras_nightly-2.17.0.dev2024031809-py3-none-any.whl")
    version("2.17.0.dev2024031709", sha256="8a3e716c6df411d4f7f344fc909fa8cb7ca1574c688ec800e8e7933a71ba9221", url="https://pypi.org/packages/6c/49/8080ba54e0e3aef9a574cc508c6a02d2a882f6e349c4049180a9e0d228a4/tf_keras_nightly-2.17.0.dev2024031709-py3-none-any.whl")
    version("2.17.0.dev2024031609", sha256="7a8bcde5592187271b24bc04b03464d4fff7ec93683645a699d6afa7adfabb75", url="https://pypi.org/packages/ea/22/62dd14f5d9aeae9ba9c90372d00d5ca74e0c3e4e83fdccbdf0befd747d82/tf_keras_nightly-2.17.0.dev2024031609-py3-none-any.whl")
    version("2.17.0.dev2024031509", sha256="de70b5a0931a7a1ef57d3d3860d28b1f96575a3a3c46aa319458b074081e6b01", url="https://pypi.org/packages/3f/7a/c369dfe23c603abd00703f0e1586ff01e7304ac837b6f94050c850bed2cc/tf_keras_nightly-2.17.0.dev2024031509-py3-none-any.whl")
    version("2.17.0.dev2024031409", sha256="bdd4da890c232b891ebb341b582ce584149adea06f5f10dc7cdc1c18ad4269f9", url="https://pypi.org/packages/2d/87/2295b6dab2d57a00f17d4b5f94b89d209270c0eedc281b00debb801a1b9a/tf_keras_nightly-2.17.0.dev2024031409-py3-none-any.whl")
    version("2.17.0.dev2024031309", sha256="c76b90a2d8c15bf4d8e7f76850fb5bef759e4a9a808bb63b91d11c25c58e3a7f", url="https://pypi.org/packages/e8/08/9b1d6c2800849aeac91c049b727483cca98514395a088e756096b093dd0f/tf_keras_nightly-2.17.0.dev2024031309-py3-none-any.whl")
    version("2.17.0.dev2024031210", sha256="fa7038ed9e485ebfdf5d1011566bdb282f646cc9ecc00ea11f4c5727f8667573", url="https://pypi.org/packages/12/3e/9f90a76b2466deb81e9e5193003fdc2e5c71524d5981c4db8c7a6c884631/tf_keras_nightly-2.17.0.dev2024031210-py3-none-any.whl")
    version("2.17.0.dev2024031109", sha256="d7fe18137d90b0d56a75ffce06b1dbfa2c8da0202d6b038c4690645a3535b614", url="https://pypi.org/packages/76/29/116fd418c5aebba76e0d8ae614445513f72475357fb47752de18c8900902/tf_keras_nightly-2.17.0.dev2024031109-py3-none-any.whl")
    version("0.0.0", sha256="bf24dcff1170cca1e39a95787549e8564f166fa64f59dd139a641d9d14e3751e", url="https://pypi.org/packages/1d/4a/7a18e0809f4ddc2ece9c02e55ed924fd06d01e7d2353c4bdda09e1ea8e9f/tf_keras_nightly-0.0.0-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("python@3.9:", when="@2.16:")
        depends_on("py-tf-nightly@2.17:", when="@2.17:")
    # END DEPENDENCIES

