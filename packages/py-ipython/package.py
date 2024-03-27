##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyIpython(PythonPackage):
    version("8.22.2", sha256="3c86f284c8f3d8f2b6c662f885c4889a91df7cd52056fd02b7d8d6195d7f56e9", url="https://pypi.org/packages/2f/4c/a960e920f0566d46084b7dd03888c1fec2a86e9f09dddae3bedfaab1d459/ipython-8.22.2-py3-none-any.whl")
    version("8.22.1", sha256="869335e8cded62ffb6fac8928e5287a05433d6462e3ebaac25f4216474dd6bc4", url="https://pypi.org/packages/11/3e/956d40991c152010d71b38b1a9763edc8fe5944d360e1c256fae60cb9165/ipython-8.22.1-py3-none-any.whl")
    version("8.22.0", sha256="a3e962e1d42927f5825dab048f4de617f5856cf3272fff1cb9245bea0c785a46", url="https://pypi.org/packages/06/96/8e836e2144d294fe2db06b0529c30f723d8b3c0d75a4834309a03a00d9dd/ipython-8.22.0-py3-none-any.whl")
    version("8.21.0", sha256="1050a3ab8473488d7eee163796b02e511d0735cf43a04ba2a8348bd0f2eaf8a5", url="https://pypi.org/packages/fb/e7/07dc8b6541affd4de15f0e8fc855f238cb93d04c4f8490757226d12cdb5a/ipython-8.21.0-py3-none-any.whl")
    version("8.20.0", sha256="bc9716aad6f29f36c449e30821c9dd0c1c1a7b59ddcc26931685b87b4c569619", url="https://pypi.org/packages/db/04/1bf767de3ee9e462a09efb1eab3074d715ef5ab582b8a0cb6d5d5615212d/ipython-8.20.0-py3-none-any.whl")
    version("8.19.0", sha256="2f55d59370f59d0d2b2212109fe0e6035cfea436b1c0e6150ad2244746272ec5", url="https://pypi.org/packages/1d/c6/c29c0509ce3235fa392779db476396e7e5d0a9c854967fdf411f168187a5/ipython-8.19.0-py3-none-any.whl")
    version("8.18.1", sha256="e8267419d72d81955ec1177f8a29aaa90ac80ad647499201119e2f05e99aa397", url="https://pypi.org/packages/47/6b/d9fdcdef2eb6a23f391251fde8781c38d42acd82abe84d054cb74f7863b0/ipython-8.18.1-py3-none-any.whl")
    version("8.18.0", sha256="d538a7a98ad9b7e018926447a5f35856113a85d08fd68a165d7871ab5175f6e0", url="https://pypi.org/packages/7a/57/ef12725f8af19920db1d8f2eaee44ebbaee6d9fdcf853be5db76bfdb9ce6/ipython-8.18.0-py3-none-any.whl")
    version("8.17.2", sha256="1e4d1d666a023e3c93585ba0d8e962867f7a111af322efff6b9c58062b3e5444", url="https://pypi.org/packages/20/45/18f0dc2cbc3ee6680a004f620fb1400c6511ded0a76a2dd241813786ce73/ipython-8.17.2-py3-none-any.whl")
    version("8.17.1", sha256="b4510d0a163c89c78cf81be68acc841dde4a8290b6ee3f3c9578ccdd2574553c", url="https://pypi.org/packages/bc/0b/186c64787e5957a8fd55a4fbc40f9edd678afd5f14c940e62d324ee39561/ipython-8.17.1-py3-none-any.whl")
    version("8.14.0", sha256="248aca623f5c99a6635bc3857677b7320b9b8039f99f070ee0d20a5ca5a8e6bf", url="https://pypi.org/packages/52/d1/f70cdafba20030cbc1412d7a7d6a89c5035071835cc50e47fc5ed8da553c/ipython-8.14.0-py3-none-any.whl")
    version("8.12.3", sha256="b0340d46a933d27c657b211a329d0be23793c36595acf9e6ef4164bc01a1804c", url="https://pypi.org/packages/8d/97/8fe103906cd81bc42d3b0175b5534a9f67dccae47d6451131cf8d0d70bb2/ipython-8.12.3-py3-none-any.whl")
    version("8.11.0", sha256="5b54478e459155a326bf5f42ee4f29df76258c0279c36f21d71ddb560f88b156", url="https://pypi.org/packages/ac/91/23e08c442657cf493598b0222008437c9e0aef0709a8fd65a5d5d68ffa21/ipython-8.11.0-py3-none-any.whl")
    version("8.5.0", sha256="6f090e29ab8ef8643e521763a4f1f39dc3914db643122b1e9d3328ff2e43ada2", url="https://pypi.org/packages/13/0d/ad3266203acb01189588aac9c1fc4dc982b58b0512ddb3cd4bea3cc26e22/ipython-8.5.0-py3-none-any.whl")
    version("8.0.1", sha256="c503a0dd6ccac9c8c260b211f2dd4479c042b49636b097cc9a0d55fe62dff64c", url="https://pypi.org/packages/ef/88/3e505ba3accd31f464f92dcd8c229f2d0d7af14ead91c1899c52648336be/ipython-8.0.1-py3-none-any.whl")
    version("7.34.0", sha256="c175d2440a1caff76116eb719d40538fbb316e214eda85c5515c303aacbfb23e", url="https://pypi.org/packages/7c/6a/1f1365f4bf9fcb349fcaa5b61edfcefa721aa13ff37c5631296b12fab8e5/ipython-7.34.0-py3-none-any.whl")
    version("7.33.0", sha256="916a3126896e4fd78dd4d9cf3e21586e7fd93bae3f1cd751588b75524b64bf94", url="https://pypi.org/packages/e0/fe/9ebd7029678bd9730bcabba366e98b53db955c5a7dc78d4e51f7514f08c2/ipython-7.33.0-py3-none-any.whl")
    version("7.32.0", sha256="86df2cf291c6c70b5be6a7b608650420e89180c8ec74f376a34e2dc15c3400e7", url="https://pypi.org/packages/38/7a/4cb724163ceb72183dc41a267e28be3e8412fdb036e6d7ce806136a6112f/ipython-7.32.0-py3-none-any.whl")
    version("7.31.1", sha256="55df3e0bd0f94e715abd968bedd89d4e8a7bce4bf498fb123fed4f5398fea874", url="https://pypi.org/packages/b8/b4/4d6c2753effd9c4e0d93fad9a3827760eaecec8331fe550f5d49e22cce89/ipython-7.31.1-py3-none-any.whl")
    version("7.31.0", sha256="4c4234cdcc6b8f87c5b5c7af9899aa696ac5cfcf0e9f6d0688018bbee5c73bce", url="https://pypi.org/packages/8f/b4/1913fff4fd4ec3c77dfbe4611d1a076be23c42fa725057fcd1651a553ac4/ipython-7.31.0-py3-none-any.whl")
    version("7.30.1", sha256="fc60ef843e0863dd4e24ab2bb5698f071031332801ecf8d1aeb4fb622056545c", url="https://pypi.org/packages/83/32/323a72ee073041ec631c928aad8048bb6e6c3db2cd06a496fe6ff031f8af/ipython-7.30.1-py3-none-any.whl")
    version("7.30.0", sha256="c8f3e07aefb9cf9e067f39686f035ce09b27a1ee602116a3030b91b6fc138ee4", url="https://pypi.org/packages/56/32/bf656aed2b2e708ee4aca8730e9be78a5e732c767a67c6068a777af5987d/ipython-7.30.0-py3-none-any.whl")
    version("7.29.0", sha256="a658beaf856ce46bc453366d5dc6b2ddc6c481efd3540cb28aa3943819caac9f", url="https://pypi.org/packages/d5/9b/ef198141dab782de95e09590603a1878ceb647143119bbb610e169d46bdd/ipython-7.29.0-py3-none-any.whl")
    version("7.28.0", sha256="f16148f9163e1e526f1008d7c8d966d9c15600ca20d1a754287cf96d00ba6f1d", url="https://pypi.org/packages/76/d1/e6166fc278a0aab9c2997ae241346837368fc9aa0c6eea9b0dbe2d727004/ipython-7.28.0-py3-none-any.whl")
    version("7.27.0", sha256="75b5e060a3417cf64f138e0bb78e58512742c57dc29db5a5058a2b1f0c10df02", url="https://pypi.org/packages/50/b1/618daafee1bbc6e7e9dceb105eca919ca8eceeeda8b80282e25d416df39b/ipython-7.27.0-py3-none-any.whl")
    version("7.26.0", sha256="892743b65c21ed72b806a3a602cca408520b3200b89d1924f4b3d2cdb3692362", url="https://pypi.org/packages/25/a0/e0b850415984ac29f14775b075efc54d73b38f0d50c6ebdea7820ffb1c12/ipython-7.26.0-py3-none-any.whl")
    version("7.21.0", sha256="34207ffb2f653bced2bc8e3756c1db86e7d93e44ed049daae9814fed66d408ec", url="https://pypi.org/packages/3b/43/6dbd0610550708fc418ad027fda97b5f415da9053749641654fdacfec93f/ipython-7.21.0-py3-none-any.whl")
    version("7.18.1", sha256="2e22c1f74477b5106a6fb301c342ab8c64bb75d702e350f05a649e8cb40a0fb8", url="https://pypi.org/packages/72/36/89e1bb437f4f2275c33acc6eb333ab2d1c64e732ad23d6f34825b512e1a3/ipython-7.18.1-py3-none-any.whl")
    version("7.5.0", sha256="54c5a8aa1eadd269ac210b96923688ccf01ebb2d0f21c18c3c717909583579a8", url="https://pypi.org/packages/a9/2e/41dce4ed129057e05a555a7f9629aa2d5f81fdcd4d16568bc24b75a1d2c9/ipython-7.5.0-py3-none-any.whl")
    version("7.3.0", sha256="5d3e020a6b5f29df037555e5c45ab1088d6a7cf3bd84f47e0ba501eeb0c3ec82", url="https://pypi.org/packages/14/3b/3fcf422a99a04ee493e6a4fc3014e3c8ff484a7feed238fef68bdc285085/ipython-7.3.0-py3-none-any.whl")
    version("5.8.0", sha256="4bac649857611baaaf76bc82c173aa542f7486446c335fe1a6c05d0d491c8906", url="https://pypi.org/packages/41/a6/2d25314b1f9375639d8f8e0f8052e8cec5df511d3449f22c4f1c2d8cb3c6/ipython-5.8.0.tar.gz")
    version("5.1.0", sha256="2db893efa27c237f314a4f28294279f5dabafff1d0a7bbb45f95e44edb17810c", url="https://pypi.org/packages/d4/0b/70c913ed4c99eb84c589e5e25b28985ba93ca2a57e08959bb14372f7f5f8/ipython-5.1.0.zip")

    with default_args(type="run"):
        depends_on("python@3.10:", when="@8.19:")
        depends_on("python@3.9:", when="@8.13.1:8.18")
        depends_on("py-appnope", when="@4.0.3:8.17 platform=darwin")
        depends_on("py-backcall", when="@6.3:8.16")
        depends_on("py-black", when="@8:8.0")
        depends_on("py-colorama", when="@5: platform=windows")
        depends_on("py-decorator", when="@4.0.3:")
        depends_on("py-exceptiongroup", when="@8.15: ^python@:3.10")
        depends_on("py-jedi@0.16:", when="@7.18:7.18.0,7.20:")
        depends_on("py-jedi@0.10:", when="@6:7.16.1,7.17,7.18.1:7.19")
        depends_on("py-matplotlib-inline", when="@7.23:")
        depends_on("py-pexpect@4.3.1:", when="@7.18: platform=linux")
        depends_on("py-pexpect@4.3.1:", when="@7.18: platform=freebsd")
        depends_on("py-pexpect@4.3.1:", when="@7.18: platform=darwin")
        depends_on("py-pexpect@4.3.1:", when="@7.18: platform=cray")
        depends_on("py-pexpect", when="@4.0.3:7.17 platform=linux")
        depends_on("py-pexpect", when="@4.0.3:7.17 platform=freebsd")
        depends_on("py-pexpect", when="@4.0.3:7.17 platform=darwin")
        depends_on("py-pexpect", when="@4.0.3:7.17 platform=cray")
        depends_on("py-pickleshare", when="@4.0.3:8.16")
        depends_on("py-prompt-toolkit@3.0.41:", when="@8.18.1:")
        depends_on("py-prompt-toolkit@3.0.30:3.0.36,3.0.38:", when="@8.11:8.18.0")
        depends_on("py-prompt-toolkit@3.0.2:", when="@8.5:8.6")
        depends_on("py-prompt-toolkit@2,3.0.2:", when="@7.10.1:8.4")
        depends_on("py-prompt-toolkit@2", when="@7:7.9")
        depends_on("py-prompt-toolkit@1.0.4:1", when="@5.2:6.2")
        depends_on("py-prompt-toolkit@1.0.3:1", when="@5.0.0-rc1:5.1")
        depends_on("py-pygments@2.4:", when="@8.1:")
        depends_on("py-pygments", when="@5:5.9,6:8.0")
        depends_on("py-setuptools@18.5:", when="@4.1:8.4")
        depends_on("py-simplegeneric@0.8.1:", when="@4.0.3:7.0")
        depends_on("py-stack-data", when="@8:")
        depends_on("py-traitlets@5.13:", when="@8.22.1:")
        depends_on("py-traitlets@5.0.0:", when="@8:8.22.0")
        depends_on("py-traitlets@4.2:", when="@5:7")
        depends_on("py-typing-extensions", when="@8.12: ^python@:3.9")
        depends_on("py-win-unicode-console@0.5:", when="@5.0.0-rc1:5.1 platform=windows")

