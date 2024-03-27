##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyTimm(PythonPackage):
    version("0.9.16", sha256="bf5704014476ab011589d3c14172ee4c901fd18f9110a928019cac5be2945914", url="https://pypi.org/packages/68/99/2018622d268f6017ddfa5ee71f070bad5d07590374793166baa102849d17/timm-0.9.16-py3-none-any.whl")
    version("0.9.12", sha256="2a828afac5b710a80ec66d0f85807e171e342faf5c0703b33102d8aa206f19dc", url="https://pypi.org/packages/01/a5/eeb717242343d9ca34e7de554a6c08d96a0cfc7005ece4f847b1753581a6/timm-0.9.12-py3-none-any.whl")
    version("0.9.11", sha256="02bba56786633ff46b55ee0ce3b991fa85375556844e500ad18e6b12921dc3da", url="https://pypi.org/packages/76/aa/4b54f6047c442883243f68f6f9e3a0ab77aaae4b3e6e51a98b371e73dd77/timm-0.9.11-py3-none-any.whl")
    version("0.9.10", sha256="c5bdd76403ee68bf57a1aab44c117e44f378779d868976cdd820edf1d223b9f9", url="https://pypi.org/packages/f0/1e/05287cb8984229d101874433df472b1fa3dcd6f746ccb6e8a26c7deeb1c7/timm-0.9.10-py3-none-any.whl")
    version("0.9.9", sha256="656503f4322fa1dc175001d160d4f13ce23afbe375a359c95efcbf9e2ef6124e", url="https://pypi.org/packages/02/e9/7346e2b6ddbc8af12a31c56ec2e06319c6d182e7439e508931095e1858a6/timm-0.9.9-py3-none-any.whl")
    version("0.9.8", sha256="198632472f470d69397088a5996823eff7f8900413a7616dc96ca7d7b7460026", url="https://pypi.org/packages/df/e4/3a56b85846102b67af6937410f9f8dc314fc60529d6891fc003611fc3796/timm-0.9.8-py3-none-any.whl")
    version("0.9.7", sha256="1cf1082007aa1353550921804abe292292d51acc8631a140273f81f29b48059f", url="https://pypi.org/packages/7a/bd/2c56be7a3b5bc71cf85a405246b89d5359f942c9f7fb6db6306d9d056092/timm-0.9.7-py3-none-any.whl")
    version("0.9.6", sha256="7549a924b86a6151d4083a880c27ae86ce729e1b5c8c6099657217d0a0526a4e", url="https://pypi.org/packages/35/57/84a71b5b540152fb5f5ec7a34f4fcd7fafa4e21053098146c831874e29e5/timm-0.9.6-py3-none-any.whl")
    version("0.9.5", sha256="6e70af3a347bddb4167db46c3252a83c59165332ecf6b3df480d49c22866fa46", url="https://pypi.org/packages/14/38/05b37b7692e521bbada22593ac3b6d7ba3f378d56b5d1ccb322a541bbb6e/timm-0.9.5-py3-none-any.whl")
    version("0.9.2", sha256="8da40cc58ed32b0622bf87d8714f9b7023398ba4cfa8fa678578d2aefde4a909", url="https://pypi.org/packages/29/90/94f5deb8d76e24a89813aef95e8809ca8fd7414490428480eda19b133d4a/timm-0.9.2-py3-none-any.whl")
    version("0.9.1", sha256="af5fff9a3f33abf7224bdc1b33dd21ba129207c84ec1e035f20aec03b71832d8", url="https://pypi.org/packages/ca/68/92012b248227134be8f5babdca3f684129175c902ef4f9cbd5fb3dd3945f/timm-0.9.1-py3-none-any.whl")
    version("0.9.0", sha256="1aeb4e3bbb1bfaa775b3f49e80bfaebfe45efb0b4733d0c57653a121a15d48a8", url="https://pypi.org/packages/38/b5/068b486caa27fa2d883dfc499dadd38e0065a33695182eda552f4d3c53b2/timm-0.9.0-py3-none-any.whl")
    version("0.6.13", sha256="ea5aed42f94062a80da414e6f1791cb82012fdb54f7db72c607637914a521345", url="https://pypi.org/packages/f6/c6/806d9b2fa95f418ad700dd206a935d5e8d7355505589dd13a70eb3a45048/timm-0.6.13-py3-none-any.whl")
    version("0.6.12", sha256="3dfa19b82afa707acc0c2392a84c0e549dd9ea626c285fb2e8d9e4073b58dbd1", url="https://pypi.org/packages/89/4e/97622efc48a6e0c11781ed8a3472c679f2c8a5cf6ebd58a57b050e758bfe/timm-0.6.12-py3-none-any.whl")
    version("0.6.11", sha256="8a10e536ecc7caf32a7e42a612a1ae561a1e0d3f1aa836905855f8aff2efa644", url="https://pypi.org/packages/19/99/504af0c961e6b6a9494447b3d83d72b79969e9ac17b89394ae343583fb0c/timm-0.6.11-py3-none-any.whl")
    version("0.6.7", sha256="4bbd7a5c9ae462ec7fec3d99ffc62ac2012010d755248e3de778d50bce5f6186", url="https://pypi.org/packages/72/ed/358a8bc5685c31c0fe7765351b202cf6a8c087893b5d2d64f63c950f8beb/timm-0.6.7-py3-none-any.whl")
    version("0.6.5", sha256="719f999bba180f108b3eea76a432e3b3c2813a9583522f0e52c77e93e53c2e81", url="https://pypi.org/packages/68/f7/eea026fd781585ccd66dc6998d3e7d83ac86f140b89e9829c233c2d46fdf/timm-0.6.5-py3-none-any.whl")
    version("0.6.2.dev0", sha256="438f5891752c9ecb96b9c6d5f6963323c052f6d4b4ed8c9da4475bca2c340010", url="https://pypi.org/packages/d4/69/c5b24d2cd9e5171b4d93eda1bc42b4bf5c2bd52010d32b8c53fe78710775/timm-0.6.2.dev0-py3-none-any.whl")
    version("0.5.4", sha256="0592c8fd2d46d0769c0b7e954b3dacea93769eee40dabb4bd7f2acb85243b588", url="https://pypi.org/packages/49/65/a83208746dc9c0d70feff7874b49780ff110810feb528df4b0ecadcbee60/timm-0.5.4-py3-none-any.whl")
    version("0.4.12", sha256="dba6b1702b7d24bf9f0f1c2fc394b4ee28f93cde5404f1dc732d63ccd00533b6", url="https://pypi.org/packages/90/fc/606bc5cf46acac3aa9bd179b3954433c026aaf88ea98d6b19f5d14c336da/timm-0.4.12-py3-none-any.whl")

    with default_args(type="run"):
        depends_on("py-huggingface-hub", when="@0.6.11:")
        depends_on("py-pyyaml", when="@0.6.11:")
        depends_on("py-safetensors", when="@0.8.13:")
        depends_on("py-torch", when="@0.9.16:")
        depends_on("py-torch@1.7:", when="@0.6.11:0.9.12")
        depends_on("py-torch@1.4:", when="@0.2,0.3.4:0.6.7")
        depends_on("py-torchvision")

