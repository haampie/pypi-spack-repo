##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyInvoke(PythonPackage):
    version("2.2.0", sha256="6ea924cc53d4f78e3d98bc436b08069a03077e6f85ad1ddaa8a116d7dad15820", url="https://pypi.org/packages/0a/66/7f8c48009c72d73bc6bbe6eb87ac838d6a526146f7dab14af671121eb379/invoke-2.2.0-py3-none-any.whl")
    version("2.1.3", sha256="51e86a08d964160e01c44eccd22f50b25842bd96a9c63c11177032594cb86740", url="https://pypi.org/packages/62/52/1844f196ac220d11f9d205351ce496dc31f819dadbad938d87482ffa90b2/invoke-2.1.3-py3-none-any.whl")
    version("2.1.2", sha256="bfc904df1c9e9fe1a881933de661fe054b8db616ff2c4cf78e00407fe473ba5d", url="https://pypi.org/packages/37/f9/c641be98cfb9daa1e428776ed14d305256993a6f3de79f972fd713bc3542/invoke-2.1.2-py3-none-any.whl")
    version("2.1.1", sha256="e86a53046eca453d3e609e7017f65db5f66b947d4d337b60658859eb8c8a80e3", url="https://pypi.org/packages/5d/b0/067446c192c98814ddaf59f432c5f66b3c7afad2748d9a349d9474f5e590/invoke-2.1.1-py3-none-any.whl")
    version("2.1.0", sha256="409c9cff8325d697f44308fda3026a97691972adc4ab81575d655a2100b50abc", url="https://pypi.org/packages/69/1c/1fdb9628818d89d10df9b90fe1ab35b27618ce043864153aec8610481ff5/invoke-2.1.0-py3-none-any.whl")
    version("2.0.1", sha256="037393e21de251078b2a59f539dc63b7cc7bb778787aa56f6dc4d86d3b29abec", url="https://pypi.org/packages/0e/e5/302428dd2b42ac17bf07933526e424274117bea995685ad3deb4728d642f/invoke-2.0.1-py3-none-any.whl")
    version("2.0.0", sha256="a860582bcf7a4b336fe18ef53937f0f28cec1c0053ffa767c2fcf7ba0b850f59", url="https://pypi.org/packages/d9/75/3bf3074efac102f49302f1c7d5194001321886046ac68d46e8c0d6cc0812/invoke-2.0.0-py3-none-any.whl")
    version("1.7.3", sha256="d9694a865764dd3fd91f25f7e9a97fb41666e822bbb00e670091e3f43933574d", url="https://pypi.org/packages/f5/ba/82b528626d0dba120796893e40853623f01445d3d78e77598e5d8c66793b/invoke-1.7.3-py3-none-any.whl")
    version("1.7.2", sha256="21fa37a84dfe398784f386ed176974d0e8ddd4f1a270ab1e0ef347e9f1174cd8", url="https://pypi.org/packages/f2/93/9b53282de5cc1c866d799ae9b703bb608288c6011202d1f84c0f021e48ab/invoke-1.7.2-py3-none-any.whl")
    version("1.7.1", sha256="2dc975b4f92be0c0a174ad2d063010c8a1fdb5e9389d69871001118b4fcac4fb", url="https://pypi.org/packages/10/f1/e46f24b6a81172324882fda07c77210f65619790ef166c059901d325d427/invoke-1.7.1-py3-none-any.whl")
    version("1.7.0", sha256="a5159fc63dba6ca2a87a1e33d282b99cea69711b03c64a35bb4e1c53c6c4afa0", url="https://pypi.org/packages/27/04/a2fbeaee825d320e6df439d37b3331e668336318b54bd3e1f2713e158b06/invoke-1.7.0-py3-none-any.whl")
    version("1.6.0", sha256="374d1e2ecf78981da94bfaf95366216aaec27c2d6a7b7d5818d92da55aa258d3", url="https://pypi.org/packages/37/b3/0b88358ee07789688d17ec7074a656da68ced50a122183187be12928b535/invoke-1.6.0.tar.gz")
    version("1.5.1", sha256="31adc245fb5803f5d30b6791db513b44c305630162a82b8e5a19ebeb5385577b", url="https://pypi.org/packages/a9/1d/27275ca4a13974cc704b0ea565e638cb41c306a263823484ec7f7e3c49f3/invoke-1.5.1.tar.gz")
    version("1.5.0", sha256="f0c560075b5fb29ba14dad44a7185514e94970d1b9d57dcd3723bec5fed92650", url="https://pypi.org/packages/f0/bf/12827f26d127549b0c17aeb075b8bec2b0a48873418c51fca4bfcd0bd985/invoke-1.5.0.tar.gz")
    version("1.4.1", sha256="de3f23bfe669e3db1085789fd859eb8ca8e0c5d9c20811e2407fa042e8a5e15d", url="https://pypi.org/packages/b6/08/b345475cfaaa542ae78a172d5b23979ad0577f15a32b16e5e54b2a7e80c6/invoke-1.4.1.tar.gz")
    version("1.4.0", sha256="ae7b4513638bde9afcda0825e9535599637a3f65bd819a27098356027bb17c8a", url="https://pypi.org/packages/d7/2a/7a0a89a1b8e3e74a198e2614bc8afdb58347bdf1d036eaa96fe73b02b667/invoke-1.4.0.tar.gz")
    version("1.3.1", sha256="dae041ff458e1ef05448aae3b76e8c2a176c4b7c6a9d5e8ce880f16251803661", url="https://pypi.org/packages/43/4d/76c285ee991b0d20c115e62894a77dde243fa3289eebe3bafc363e416af6/invoke-1.3.1.tar.gz")
    version("1.2.0", sha256="dc492f8f17a0746e92081aec3f86ae0b4750bf41607ea2ad87e5a7b5705121b7", url="https://pypi.org/packages/ef/80/cef14194e2dd62582cc0a4f5f2db78fb00de3ba5d1bc0e50897b398ea984/invoke-1.2.0.tar.gz")


