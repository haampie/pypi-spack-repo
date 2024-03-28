# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyInvoke(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
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
    version("1.6.0", sha256="769e90caeb1bd07d484821732f931f1ad8916a38e3f3e618644687fc09cb6317", url="https://pypi.org/packages/de/8b/6fea06c4e75a9c2390103c9960ab3533b64e9816207744665072e094336c/invoke-1.6.0-py3-none-any.whl")
    version("1.5.1", sha256="4cbabe49ef2e1ac8dfc881e6a23b3703cbb2f07485153736642786379468da55", url="https://pypi.org/packages/5e/f0/5e08f403ecd2a276ffc22c476cab2709dd2cec80ba48dc9d0a1901939f2f/invoke-1.5.1-py2-none-any.whl")
    version("1.5.0", sha256="da7c2d0be71be83ffd6337e078ef9643f41240024d6b2659e7b46e0b251e339f", url="https://pypi.org/packages/fb/a1/42cfa5ad6101e478798c7f77614e060cb66843b8f755e563a311d742e937/invoke-1.5.0-py2-none-any.whl")
    version("1.4.1", sha256="87b3ef9d72a1667e104f89b159eaf8a514dbf2f3576885b2bbdefe74c3fb2132", url="https://pypi.org/packages/2c/16/f00efa99ae9f255142a230ce6819c37ae9dd29a7144477c1161cc72d01ed/invoke-1.4.1-py3-none-any.whl")
    version("1.4.0", sha256="e04faba8ea7cdf6f5c912be42dcafd5c1074b7f2f306998992c4bfb40a9a690b", url="https://pypi.org/packages/ae/8d/82734f4ab785c0c7c82d4a35a99976d5423ed71a28f2c7c2939f651b58d7/invoke-1.4.0-py3-none-any.whl")
    version("1.3.1", sha256="5a8558521dc5621b2483a1d90944567e2e104e09dda7be6ae4079eb3247f4a3b", url="https://pypi.org/packages/43/c8/af255b3907f0446f75766327edb25cda3ef18b1ba03fd66f2e8e4b62f763/invoke-1.3.1-py3-none-any.whl")
    version("1.2.0", sha256="4f4de934b15c2276caa4fbc5a3b8a61c0eb0b234f2be1780d2b793321995c2d6", url="https://pypi.org/packages/be/9f/8508712c9cad73ac0c8eeb2c3e51c9ef65136653dda2b512bde64109f023/invoke-1.2.0-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    # END DEPENDENCIES

