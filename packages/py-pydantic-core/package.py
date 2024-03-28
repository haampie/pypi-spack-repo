# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPydanticCore(PythonPackage):
    # BEGIN VERSIONS
    version("2.16.3", sha256="1cac689f80a3abab2d3c0048b29eea5751114054f032a941a32de4c852c59cad", url="https://pypi.org/packages/77/3f/65dbe5231946fe02b4e6ea92bc303d2462f45d299890fd5e8bfe4d1c3d66/pydantic_core-2.16.3.tar.gz")
    version("2.16.2", sha256="0ba503850d8b8dcc18391f10de896ae51d37fe5fe43dbfb6a35c5c5cad271a06", url="https://pypi.org/packages/0d/72/64550ef171432f97d046118a9869ad774925c2f442589d5f6164b8288e85/pydantic_core-2.16.2.tar.gz")
    version("2.16.1", sha256="daff04257b49ab7f4b3f73f98283d3dbb1a65bf3500d55c7beac3c66c310fe34", url="https://pypi.org/packages/a0/a7/61d013c73773bb03d02de9de8e4e5b2ed2c100dc98ae7046d54485ecf5d4/pydantic_core-2.16.1.tar.gz")
    version("2.14.6", sha256="1fd0c1d395372843fba13a51c28e3bb9d59bd7aebfeb17358ffaaa1e4dbbe948", url="https://pypi.org/packages/b2/7d/8304d8471cfe4288f95a3065ebda56f9790d087edc356ad5bd83c89e2d79/pydantic_core-2.14.6.tar.gz")
    version("2.14.5", sha256="6d30226dfc816dd0fdf120cae611dd2215117e4f9b124af8c60ab9093b6e8e71", url="https://pypi.org/packages/64/26/cffb93fe9c6b5a91c497f37fae14a4b073ecbc47fc36a9979c7aa888b245/pydantic_core-2.14.5.tar.gz")
    version("2.14.3", sha256="3ad083df8fe342d4d8d00cc1d3c1a23f0dc84fce416eb301e69f1ddbbe124d3f", url="https://pypi.org/packages/4c/ee/b3479b31f47226bae5d9033761971bec215774a6078ce08e8618d6381470/pydantic_core-2.14.3.tar.gz")
    version("2.4.0", sha256="ec3473c9789cc00c7260d840c3db2c16dbfc816ca70ec87a00cddfa3e1a1cdd5", url="https://pypi.org/packages/8a/6a/2609fb28f3c289eacb2a2ddaceb7ad0d327b4b4678146573295d98f012b8/pydantic_core-2.4.0.tar.gz")
    version("2.3.0", sha256="5cfb5ac4e82c47d5dc25b209dd4c3989e284b80109f9e08b33c895080c424b4f", url="https://pypi.org/packages/57/ea/edff47ad42857534f3abcc87472802b3181041f4e4fbeac988a5ecfcffae/pydantic_core-2.3.0.tar.gz")
    version("2.1.2", sha256="d2c790f0d928b672484eac4f5696dd0b78f3d6d148a641ea196eb49c0875e30a", url="https://pypi.org/packages/66/68/9703e44f0bcc29eeaacb1c063675687524646a1bbe3c4527d45475cf120e/pydantic_core-2.1.2.tar.gz")
    version("2.0.2", sha256="996ffb7ae3c8cb7506a58dae52bbf13a7bbbfce6c3110a2b44c20d2587e57b9b", url="https://pypi.org/packages/bb/c9/a03a85dcfdfac6907b7203f375368460e473f2d48417ad83c88b564995a0/pydantic_core-2.0.2.tar.gz")
    version("2.0.1", sha256="f9fffcb5507bff84a1312d1616406cad157806f105d78bd184d1e6b3b00e6417", url="https://pypi.org/packages/22/c3/0219aff361b6975724349a1894f0a6ef808d65b268e52a9c8b1efdf8758c/pydantic_core-2.0.1.tar.gz")
    version("0.25.0", sha256="6ed58ce669d13c076095adaea3331f48ab914485eb1ce6f462c08c982edf935e", url="https://pypi.org/packages/3c/05/64fd21f0151ad7387b3ef19e9ebbf313eb6ebb4d94c377419fbb252148fb/pydantic_core-0.25.0.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("python@3.9:", when="@:0.0")
        depends_on("py-typing-extensions@4.6:4.7.0-rc1,4.7.1:", when="@2.0.2:")
        depends_on("py-typing-extensions@4.6:", when="@2:2.0.1")
        depends_on("py-typing-extensions", when="@0.1:0 ^python@:3.10")
    # END DEPENDENCIES

