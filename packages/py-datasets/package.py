# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyDatasets(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("2.18.0", sha256="f1bbf0e2896917a914de01cbd37075b14deea3837af87ad0d9f697388ccaeb50", url="https://pypi.org/packages/95/fc/661a7f06e8b7d48fcbd3f55423b7ff1ac3ce59526f146fda87a1e1788ee4/datasets-2.18.0-py3-none-any.whl")
    version("2.17.1", sha256="346974daf2fe9c14ddb35646896b2308b95e7dc27709d1a6e25273573b140cf8", url="https://pypi.org/packages/73/75/ead8e4489217835fd8004c9c89dad8217deacd7e2591340dbe249b58c29f/datasets-2.17.1-py3-none-any.whl")
    version("2.17.0", sha256="1479667383d002c2b4a4fc6ac0fb99a7f8e7e440f348991ae7343837f9fc84db", url="https://pypi.org/packages/74/4d/63b033169534f0742b7fe13957118cae08c83b04bfde46511f397872e2e7/datasets-2.17.0-py3-none-any.whl")
    version("2.16.1", sha256="fafa300c78ff92d521473a3d47d60c2d3e0d6046212cc03ceb6caf6550737257", url="https://pypi.org/packages/ec/93/454ada0d1b289a0f4a86ac88dbdeab54921becabac45da3da787d136628f/datasets-2.16.1-py3-none-any.whl")
    version("2.16.0", sha256="301cc39b3d81cd751100b79c85f8ae8626c17b0b113819ba2831c204d90b43f2", url="https://pypi.org/packages/a0/93/da8a22a292e51ab76f969eb87bda8fd70cc3963b4dd71f67bb92a70a7992/datasets-2.16.0-py3-none-any.whl")
    version("2.15.0", sha256="6d658d23811393dfc982d026082e1650bdaaae28f6a86e651966cb072229a228", url="https://pypi.org/packages/e2/cf/db41e572d7ed958e8679018f8190438ef700aeb501b62da9e1eed9e4d69a/datasets-2.15.0-py3-none-any.whl")
    version("2.14.7", sha256="1a64041a7da4f4130f736fc371c1f528b8ddd208cebe156400f65719bdbba79d", url="https://pypi.org/packages/00/23/80a2147a547cb2fd59eb92a13787c849b3efaefcea02a5c963dfc93f7c56/datasets-2.14.7-py3-none-any.whl")
    version("2.14.6", sha256="4de857ffce21cfc847236745c69f102e33cd1f0fa8398e7be9964525fd4cd5db", url="https://pypi.org/packages/7c/55/b3432f43d6d7fee999bb23a547820d74c48ec540f5f7842e41aa5d8d5f3a/datasets-2.14.6-py3-none-any.whl")
    version("2.14.5", sha256="dd4155091034cba04d5a28711f2ed3944275ed15c5d0c5a2d0b6b9ea34a2bdfe", url="https://pypi.org/packages/09/7e/fd4d6441a541dba61d0acb3c1fd5df53214c2e9033854e837a99dd9e0793/datasets-2.14.5-py3-none-any.whl")
    version("2.14.4", sha256="29336bd316a7d827ccd4da2236596279b20ca2ac78f64c04c9483da7cbc2459b", url="https://pypi.org/packages/66/f8/38298237d18d4b6a8ee5dfe390e97bed5adb8e01ec6f9680c0ddf3066728/datasets-2.14.4-py3-none-any.whl")
    version("2.8.0", sha256="f36cb362bb5587659bab18e594b6d25d9d28486d735a571319c82efeb5a4e5df", url="https://pypi.org/packages/24/57/6b07e4dc51479ae3e9bbc774af348b0307e2b66957ceae94d25e3f9d7dcf/datasets-2.8.0-py3-none-any.whl")
    version("1.8.0", sha256="9d449ff7dbb67e2af52f9658c19902890e9f3672053bdb56500717fd8888b3fd", url="https://pypi.org/packages/08/a2/d4e1024c891506e1cee8f9d719d20831bac31cb5b7416983c4d2f65a6287/datasets-1.8.0-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-aiohttp", when="@1.12:")
        depends_on("py-dill@0.3:", when="@2.17:")
        depends_on("py-dill@0.3:0.3.7", when="@2.14:2.16")
        depends_on("py-dill@:0.3.6", when="@2.7:2.9")
        depends_on("py-dill", when="@1:2.2.1")
        depends_on("py-filelock", when="@1:1.1.2,2.16:")
        depends_on("py-fsspec@2023:2024.2+http", when="@2.18:")
        depends_on("py-fsspec@2023:2023.10+http", when="@2.14.6:2.17")
        depends_on("py-fsspec@2023:2023.6+http", when="@2.14.5")
        depends_on("py-fsspec@2021.11.1:+http", when="@2.4:2.14.4")
        depends_on("py-fsspec", when="@1.3:1.8")
        depends_on("py-huggingface-hub@0.19.4:", when="@2.16:")
        depends_on("py-huggingface-hub@0.18.0:", when="@2.15")
        depends_on("py-huggingface-hub@0.14.0:0.14.0.0,0.14.1:", when="@2.14")
        depends_on("py-huggingface-hub@0.2:", when="@2.5.2:2.10")
        depends_on("py-huggingface-hub@:0.0", when="@1.5:1.11")
        depends_on("py-multiprocess", when="@1.1:")
        depends_on("py-numpy@1.17.0:", when="@1:")
        depends_on("py-packaging", when="@1.6:")
        depends_on("py-pandas", when="@1:")
        depends_on("py-pyarrow@12:", when="@2.17:")
        depends_on("py-pyarrow@8:", when="@2.11:2.16")
        depends_on("py-pyarrow@6:", when="@2.2:2.10")
        depends_on("py-pyarrow@1:3", when="@1.7:1.8")
        depends_on("py-pyarrow-hotfix", when="@2.14.7:")
        depends_on("py-pyyaml@5.1:", when="@2.6:")
        depends_on("py-requests@2.19:", when="@1:")
        depends_on("py-responses@:0.18", when="@1.18.4:2.12")
        depends_on("py-tqdm@4.62.1:", when="@1.12:")
        depends_on("py-tqdm@4.27:4.49", when="@1.1.2:1.8")
        depends_on("py-xxhash", when="@1:")

        # marker: (sys_platform != "darwin" or platform_machine != "arm64") and extra == "dev"
        # depends_on("py-tensorflow@2.2.0:2.6.0-rc2,2.6.2:", when="@2.14.1:")
        # depends_on("py-tensorflow@2.3.0:2.6.0-rc2,2.6.2:", when="@2.7:")

        # marker: (sys_platform != "darwin" or platform_machine != "arm64") and extra == "docs"
        # depends_on("py-tensorflow@2.2.0:2.6.0-rc2,2.6.2:", when="@2.14.1:")

        # marker: (sys_platform != "darwin" or platform_machine != "arm64") and extra == "tensorflow"
        # depends_on("py-tensorflow@2.2.0:2.6.0-rc2,2.6.2:", when="@2.7:")

        # marker: (sys_platform != "darwin" or platform_machine != "arm64") and extra == "tests"
        # depends_on("py-tensorflow@2.3.0:2.6.0-rc2,2.6.2:", when="@2.7:")

        # marker: (sys_platform == "darwin" and platform_machine == "arm64") and extra == "dev"
        # depends_on("py-tensorflow-macos", when="@2.7:")

        # marker: (sys_platform == "darwin" and platform_machine == "arm64") and extra == "docs"
        # depends_on("py-tensorflow-macos", when="@2.14.1:")

        # marker: (sys_platform == "darwin" and platform_machine == "arm64") and extra == "tensorflow"
        # depends_on("py-tensorflow-macos", when="@2.7:")

        # marker: (sys_platform == "darwin" and platform_machine == "arm64") and extra == "tests"
        # depends_on("py-tensorflow-macos", when="@2.7:")
    # END DEPENDENCIES

