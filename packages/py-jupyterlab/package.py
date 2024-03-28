# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyJupyterlab(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("4.1.5", sha256="3bc843382a25e1ab7bc31d9e39295a9f0463626692b7995597709c0ab236ab2c", url="https://pypi.org/packages/b4/bb/1f9f7ddf04cfe26b21aab739ec905bbafa401642614ac9c9d26cf13cb7a3/jupyterlab-4.1.5-py3-none-any.whl")
    version("4.1.4", sha256="f92c3f2b12b88efcf767205f49be9b2f86b85544f9c4f342bb5e9904a16cf931", url="https://pypi.org/packages/0a/16/8477e15aeca6bd93ff0ae15570bf829605952c71fdd252b9975229d0913d/jupyterlab-4.1.4-py3-none-any.whl")
    version("4.1.3", sha256="67dbec7057c6ad46f08a3667a80bdb890df9453822c93b5ddfd5e8313a718ef9", url="https://pypi.org/packages/2e/23/66990c58d0f205841fa1b76c2f80cb564fc4d0347ada63980bcd4a9b3471/jupyterlab-4.1.3-py3-none-any.whl")
    version("4.1.2", sha256="aa88193f03cf4d3555f6712f04d74112b5eb85edd7d222c588c7603a26d33c5b", url="https://pypi.org/packages/73/85/00afa8fcb102f8480790861277d58d624f46968baad4f43fb4e15e696772/jupyterlab-4.1.2-py3-none-any.whl")
    version("4.1.1", sha256="fa3e8c18b804eac04e51ceebd9dd3dd396e08106816f0d09cc426799d7087632", url="https://pypi.org/packages/61/9b/8b974903425893806b15413fc899fefa78b0ed53e1699bcb8838c01a0ab2/jupyterlab-4.1.1-py3-none-any.whl")
    version("4.1.0", sha256="5380e85fb4f11a227ed2db13103e513cfea274d1011f6210e62d611e92e0369d", url="https://pypi.org/packages/d0/c9/ac2353a6fd4aeeaa9a76de7568f8d229d3eada77d67325338ccd0bb0b6ee/jupyterlab-4.1.0-py3-none-any.whl")
    version("4.0.13", sha256="3aa81c364d50cc715f6c2935674c7cca8936bd74b5898d6ad6598aef08c43808", url="https://pypi.org/packages/7b/af/4e8fffc503dc70d3c73328b0421181e3d238f76831769578c4f245130ae9/jupyterlab-4.0.13-py3-none-any.whl")
    version("4.0.12", sha256="53f132480e5f6564f4e20d1b5ed4e8b7945952a2decd5bdfa43760b1b536c99d", url="https://pypi.org/packages/14/08/0608b1d192ad4a4f800fe68341bdcb23141edd2610a82833d4ffa3bd0bc2/jupyterlab-4.0.12-py3-none-any.whl")
    version("4.0.11", sha256="536bf0e78723153a5016ca7efb88ed0ecd7070d3f1555d5b0e2770658f900a3c", url="https://pypi.org/packages/3c/e1/824088b7eed57a38bf20c5ef0363a0e4554d2d824571d60f8bc2460b0c94/jupyterlab-4.0.11-py3-none-any.whl")
    version("4.0.10", sha256="fe010ad9e37017488b468632ef2ead255fc7c671c5b64d9ca13e1f7b7e665c37", url="https://pypi.org/packages/cb/26/f4de12ccf86b7a714cbd972036676319729cf50451b9b380f6d14893521e/jupyterlab-4.0.10-py3-none-any.whl")
    version("4.0.9", sha256="9f6f8e36d543fdbcc3df961a1d6a3f524b4a4001be0327a398f68fa4e534107c", url="https://pypi.org/packages/a7/f2/b3ed35a9d75c22c7a90dc51963e57373d000007ba3ccbfc6277ba6448aa8/jupyterlab-4.0.9-py3-none-any.whl")
    version("4.0.8", sha256="2ff5aa2a51eb21df241d6011c236e88bd1ff9a5dbb75bebc54472f9c18bfffa4", url="https://pypi.org/packages/8b/80/1f6653ad59fdbd4824b1d5a157eed83a23a3ce571d1de56ed5ad5225ed12/jupyterlab-4.0.8-py3-none-any.whl")
    version("4.0.7", sha256="08683045117cc495531fdb39c22ababb9aaac6977a45e67cfad20046564c9c7c", url="https://pypi.org/packages/08/fa/b3c7d72df1f323483ae5107ad6036b9d06f677deff2aa51ac7e2b676720a/jupyterlab-4.0.7-py3-none-any.whl")
    version("4.0.6", sha256="7d9dacad1e3f30fe4d6d4efc97fda25fbb5012012b8f27cc03a2283abcdee708", url="https://pypi.org/packages/3b/43/2368d8ffee6e33f282f548d42fa222bd385cc9f66545b260e7d08e90046b/jupyterlab-4.0.6-py3-none-any.whl")
    version("4.0.5", sha256="13b3a326e7b95d72746fe20dbe80ee1e71165d6905e01ceaf1320eb809cb1b47", url="https://pypi.org/packages/71/a3/38b9d6492a393dcfdae9e82021655432a9fd6e8f4c03c30a7b55036c0d70/jupyterlab-4.0.5-py3-none-any.whl")
    version("4.0.4", sha256="23eef35d22be8f2ad9b873ec41ceb2e8c3b0dc8ae740c0f973e2de09e587530f", url="https://pypi.org/packages/db/1d/a4645d6385cd03aa7703a8695317b431e92460a5a9168b9fac59d2aafd60/jupyterlab-4.0.4-py3-none-any.whl")
    version("4.0.1", sha256="f3ebd90e41d3ba1b8152c8eda2bd1a18e0de490192b4be1a6ec132517cfe43ef", url="https://pypi.org/packages/77/94/0d4f2a8dc006eb4f510cb714a3fbe3b8931c45943fd95c6159509bb8edc7/jupyterlab-4.0.1-py3-none-any.whl")
    version("3.4.8", sha256="4626a0434c76a3a22f11c4efaa1d031d2586367f72cfdbdbff6b08b6ef0060f7", url="https://pypi.org/packages/9b/67/be3e254f846d5a143edc385bdfd61ee366be70a3223808f30f0b6b3d8f62/jupyterlab-3.4.8-py3-none-any.whl")
    version("3.4.2", sha256="f749fff221e12fe384dd91e6f8c004e6a59cd3bf4271208002ab02cb4218618c", url="https://pypi.org/packages/90/53/3eb1697790df866f847600b9aaa5e82e72dbeae8160b2fda7bda70bb4454/jupyterlab-3.4.2-py3-none-any.whl")
    version("3.2.9", sha256="729d1f06e97733070badc04152aecf9fb2cd036783eebbd9123ff58aab83a8f5", url="https://pypi.org/packages/4b/0d/03deff4501e9ffafe755e561e375ffa9f5822fec93a09ce1c7c5147bdcb3/jupyterlab-3.2.9-py3-none-any.whl")
    version("3.2.1", sha256="6fe0240f1880cde1325072b9ff1ef2f442784de4aed5df1ab802a027c9791f62", url="https://pypi.org/packages/b7/ed/f47b38a48d67726862e9c1237c079150154a00bbcc60c25731f8211ad850/jupyterlab-3.2.1-py3-none-any.whl")
    version("3.1.19", sha256="5fea3ceed4ad364a175b5ec85220c9b6362575965b4b291f8ad1c66eb32b5795", url="https://pypi.org/packages/ae/0a/7175659da388876dd675c6c816f2a14fd3d1091ce4923d9b17efb02d3a10/jupyterlab-3.1.19-py3-none-any.whl")
    version("3.1.18", sha256="3bedbc732ae86b616bd5c7855a6d071fe76ad47186378d36df77f4fc58ae322a", url="https://pypi.org/packages/32/e2/577343b7048c5ec6cf6d271dcbd36cb9d12eb0e7111c40e88c90ecd46379/jupyterlab-3.1.18-py3-none-any.whl")
    version("3.1.14", sha256="1241ff4ab8604a281eda5d8215fe59e418737edcdfe71df09a0bd5fdd4ccfd2c", url="https://pypi.org/packages/a5/83/d4232dc1399a93d5b6f665c92156cf564b25b4d51a641bcdf904796704ee/jupyterlab-3.1.14-py3-none-any.whl")
    version("3.0.18", sha256="4a8d2e96711cd35ce0e0c0c826c8991834daf51a2e7f7908413cdeace4fc13f3", url="https://pypi.org/packages/5f/ef/59d2f9358e232376806f50ae96cd97fc4eb33f04850a38d846c2727c4d49/jupyterlab-3.0.18-py3-none-any.whl")
    version("3.0.16", sha256="88f6e7580c15cf731d96495fda362e786753e18d1e3e7e735915862efb602a92", url="https://pypi.org/packages/f7/5a/e9a52aea224ae01a3c34732c886389745fbbc14f0374a96d555add1f5034/jupyterlab-3.0.16-py3-none-any.whl")
    version("2.2.7", sha256="a0a1882456098d2fab4c241a0b16a1df96c36de1c45bddbf5fc40867e3d9340e", url="https://pypi.org/packages/82/bc/8ca618d6a18d49675ad39f544bcd6ad8a9f31a5784d059d7053c8ec3197b/jupyterlab-2.2.7-py3-none-any.whl")
    version("2.1.0", sha256="6663eed77b10d567499ab998eb71dabb510572f7337ec8efc48ed56cd37f9c5f", url="https://pypi.org/packages/2f/4a/b25d71392bb6982b7afa05eba1be22556f7e2d852bd5af9a1682da93916f/jupyterlab-2.1.0-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-async-lru@1:", when="@4.0.0-alpha29:")
        depends_on("py-httpx@0.25:", when="@4.1.0-alpha3:")
        depends_on("py-importlib-metadata@4.8.3:", when="@4.0.0-alpha31: ^python@:3.9")
        depends_on("py-importlib-resources@1.4:", when="@4.0.0-alpha24: ^python@:3.8")
        depends_on("py-ipykernel", when="@4.0.0-alpha20:")
        depends_on("py-ipython", when="@3.0.0-alpha5:4.0.0-alpha19")
        depends_on("py-jinja2@3.0.3:", when="@4.0.0-alpha22:")
        depends_on("py-jinja2@2.1:", when="@3.0.15:3.0,3.1.0-alpha5:4.0.0-alpha21")
        depends_on("py-jinja2@2.10:", when="@1.0.7:1.0,1.1.0-rc0:3.0.14,3.1:3.1.0-alpha4")
        depends_on("py-jupyter-core", when="@3.0.0-rc7:")
        depends_on("py-jupyter-lsp@2:", when="@4.0.0-alpha37:")
        depends_on("py-jupyter-server@2.4:", when="@4.0.0-beta1:")
        depends_on("py-jupyter-server@1.16:1", when="@3.4")
        depends_on("py-jupyter-server@1.4:1", when="@3.0.9:3.0,3.1.0-alpha4:3.3,4:4.0.0-alpha21")
        depends_on("py-jupyterlab-server@2.19:", when="@4.0.0-alpha33:")
        depends_on("py-jupyterlab-server@2.10:", when="@3.3.0-alpha2:3.6.0-rc0,4.0.0-alpha19:4.0.0-alpha22")
        depends_on("py-jupyterlab-server@2.3:", when="@3.0.9:3.0,3.1.0-alpha4:3.3.0-alpha1,4:4.0.0-alpha18")
        depends_on("py-jupyterlab-server@1.1.5:1", when="@2.2:3.0.0-alpha4")
        depends_on("py-jupyterlab-server@1.1:", when="@2.1:2.1.1")
        depends_on("py-nbclassic", when="@3.4.4:3")
        depends_on("py-nbclassic@0.2.0:0", when="@3.0.0-rc14:3.4.3,4:4.0.0-alpha19")
        depends_on("py-notebook@:6", when="@3.4.4:3")
        depends_on("py-notebook@4.3.1:", when="@0.23:3.0.0-alpha4")
        depends_on("py-notebook-shim@0.2:", when="@4.0.0-alpha31:")
        depends_on("py-packaging", when="@3.0.0-beta6:")
        depends_on("py-tomli", when="@3.6.0-alpha3:3,4.0.0-alpha31: ^python@:3.10")
        depends_on("py-tomli", when="@3.4.7:3.6.0-alpha2,4.0.0-alpha27:4.0.0-alpha30")
        depends_on("py-tornado@6.2:", when="@4.0.0-alpha33:")
        depends_on("py-tornado@6.1:", when="@3.0.0-rc14:4.0.0-alpha32")
        depends_on("py-tornado@:6.0-beta1,6.0.3:", when="@1.0.0-rc1:3.0.0-rc13")
        depends_on("py-traitlets", when="@4.0.0-alpha29:")
    # END DEPENDENCIES

