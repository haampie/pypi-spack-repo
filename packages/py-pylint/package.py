##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPylint(PythonPackage):
    version("3.1.0", sha256="507a5b60953874766d8a366e8e8c7af63e058b26345cfcb5f91f89d987fd6b74", url="https://pypi.org/packages/4d/2b/dfcf298607c73c3af47d5a699c3bd84ba580f1b8642a53ba2a53eead7c49/pylint-3.1.0-py3-none-any.whl")
    version("3.0.4", sha256="59ab3532506f32affefeb50d5057a221bb351f5a1383fa36c424c2c6c05e7005", url="https://pypi.org/packages/86/97/d4b9cf8ea5d8660f38ec6812c3a0c22562b6a5add9676f3841471859a971/pylint-3.0.4-py3-none-any.whl")
    version("3.0.3", sha256="7a1585285aefc5165db81083c3e06363a27448f6b467b3b0f30dbd0ac1f73810", url="https://pypi.org/packages/0b/59/289c76e3ebdaa2ce9910b366aea437dbc1e0e602a0a513abca757fc4997a/pylint-3.0.3-py3-none-any.whl")
    version("3.0.2", sha256="60ed5f3a9ff8b61839ff0348b3624ceeb9e6c2a92c514d81c9cc273da3b6bcda", url="https://pypi.org/packages/30/2e/228a17bc770bbb5b327e7a5ed50deb698e2d94f13dadca34cd36933ec4e6/pylint-3.0.2-py3-none-any.whl")
    version("3.0.1", sha256="9c90b89e2af7809a1697f6f5f93f1d0e518ac566e2ac4d2af881a69c13ad01ea", url="https://pypi.org/packages/73/79/e9649dd36ea3ada2b7a14e279b3dc6a9502541e1fd2ba5ed73cbd9e27840/pylint-3.0.1-py3-none-any.whl")
    version("3.0.0", sha256="21da8ed1294f88d66c82eb3e624a0993291613548bb17fbccaa220c31c41293b", url="https://pypi.org/packages/61/f4/9def99e8ba9f2a8376a2315102695193711bca79dd00bcc5e110207d490f/pylint-3.0.0-py3-none-any.whl")
    version("2.17.7", sha256="27a8d4c7ddc8c2f8c18aa0050148f89ffc09838142193fdbe98f172781a3ff87", url="https://pypi.org/packages/b4/49/cea450a83079445a84f16050e571a7c383d3f474b13c5caedfebd4e35def/pylint-2.17.7-py3-none-any.whl")
    version("2.17.6", sha256="18a1412e873caf8ffb56b760ce1b5643675af23e6173a247b502406b24c716af", url="https://pypi.org/packages/5c/2d/bb7e0a20b8bfd395ae6c95ebd49a2a5d652b8f06cffc7baf739399c5dfd0/pylint-2.17.6-py3-none-any.whl")
    version("2.17.5", sha256="73995fb8216d3bed149c8d51bba25b2c52a8251a2c8ac846ec668ce38fab5413", url="https://pypi.org/packages/63/cc/00cbe3f09bd6d98d79ee66cf76451d253fb1a8a59029535ea2b6ba8a824d/pylint-2.17.5-py3-none-any.whl")
    version("2.17.4", sha256="7a1145fb08c251bdb5cca11739722ce64a63db479283d10ce718b2460e54123c", url="https://pypi.org/packages/04/4c/3f7d42a1378c40813772bc5f25184144da09f00ffbe3f60ae985ffa7e10f/pylint-2.17.4-py3-none-any.whl")
    version("2.16.2", sha256="ff22dde9c2128cd257c145cfd51adeff0be7df4d80d669055f24a962b351bbe4", url="https://pypi.org/packages/e1/1b/b34a9c3485151db12402ab701f9cb836359cb95668870d071d5b2e327f67/pylint-2.16.2-py3-none-any.whl")
    version("2.15.0", sha256="4b124affc198b7f7c9b5f9ab690d85db48282a025ef9333f51d2d7281b92a6c3", url="https://pypi.org/packages/5e/1b/920b36e0db0fe3d4b583a934e1889153699bcccbca0a41b18202d2d2e1e9/pylint-2.15.0-py3-none-any.whl")
    version("2.14.4", sha256="89b61867db16eefb7b3c5b84afc94081edaf11544189e2b238154677529ad69f", url="https://pypi.org/packages/30/7a/db35d167413665b8cb82caa043d2931a45c4a05622367b1f19ceea65e415/pylint-2.14.4-py3-none-any.whl")
    version("2.13.5", sha256="c149694cfdeaee1aa2465e6eaab84c87a881a7d55e6e93e09466be7164764d1e", url="https://pypi.org/packages/9f/53/e1d8da0d381e4a303cc812238e733073abdd9099525c42cb100b20faf8b9/pylint-2.13.5-py3-none-any.whl")
    version("2.11.1", sha256="0f358e221c45cbd4dad2a1e4b883e75d28acdcccd29d40c76eb72b307269b126", url="https://pypi.org/packages/37/42/948d1486727806df2e0016f1cfc2d3beafe289f96d53dfc85d967f79afc5/pylint-2.11.1-py3-none-any.whl")
    version("2.8.2", sha256="f7e2072654a6b6afdf5e2fb38147d3e2d2d43c89f648637baab63e026481279b", url="https://pypi.org/packages/10/f0/9705d6ec002876bc20b6923cbdeeca82569a895fc214211562580e946079/pylint-2.8.2-py3-none-any.whl")

    with default_args(type="run"):
        depends_on("py-astroid@3.1:", when="@3.1:")
        depends_on("py-astroid@3.0.1:3.0", when="@3.0.2:3.0")
        depends_on("py-astroid@3.0.0:3.0", when="@3.0.0-beta0:3.0.1")
        depends_on("py-astroid@2.15.8:2", when="@2.17.7:2")
        depends_on("py-astroid@2.15.7:2", when="@2.17.6")
        depends_on("py-astroid@2.15.6:2", when="@2.17.5")
        depends_on("py-astroid@2.15.4:2", when="@2.17.3:2.17.4")
        depends_on("py-astroid@2.14.2:2", when="@2.16.2:2.16")
        depends_on("py-astroid@2.12.4:2.13", when="@2.15:2.15.0")
        depends_on("py-astroid@2.11.6:2.11", when="@2.14.2:2.14")
        depends_on("py-astroid@2.11.2:2.11", when="@2.13.2:2.13.5")
        depends_on("py-astroid@2.8", when="@2.11")
        depends_on("py-astroid@2.5.6:2.6", when="@2.8.1:2.8.1.0,2.8.2")
        depends_on("py-colorama@0.4.5:", when="@2.14.3:2,3.0.0-alpha6: platform=windows")
        depends_on("py-colorama", when="@1.7.5:2.14.2,3:3.0.0-alpha5 platform=windows")
        depends_on("py-dill@0.3.7:", when="@3.0.0-alpha7: ^python@3.12:")
        depends_on("py-dill@0.3.6:", when="@2.15.9:2.16.0.0,2.16.1:2,3.0.0-alpha6: ^python@3.11:")
        depends_on("py-dill@0.2:", when="@2.15.9:2.16.0.0,2.16.1:2,3.0.0-alpha6: ^python@:3.10")
        depends_on("py-dill@0.2:", when="@2.13:2.15.8,2.16.0.dev:2.16.0,3.0.0-alpha5")
        depends_on("py-isort@4.2.5:5.12,5.13.1:5", when="@3.0.3:")
        depends_on("py-isort@4.2.5:5", when="@2:3.0.2")
        depends_on("py-mccabe@0.6:", when="@2.13:2,3.0.0-alpha5:")
        depends_on("py-mccabe@0.6", when="@2:2.12,3:3.0.0-alpha4")
        depends_on("py-platformdirs@2.2:", when="@2.10.2:2,3.0.0-alpha5:")
        depends_on("py-toml@0.7.1:", when="@2:2.11,3:3.0.0-alpha4")
        depends_on("py-tomli@1.1:", when="@2.13:2,3.0.0-alpha5: ^python@:3.10")
        depends_on("py-tomlkit@0.10.1:", when="@2.14:2,3.0.0-alpha5:")
        depends_on("py-typing-extensions@3.10:", when="@2.11:2,3.0.0-alpha5: ^python@:3.9")

