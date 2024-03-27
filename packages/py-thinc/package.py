##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyThinc(PythonPackage):
    version("8.2.3", sha256="f5afc5222912a80bda8bdcec958362a2ba538d7027dc8db6154845d2859dca76", url="https://pypi.org/packages/a4/97/064317586536d825c36037a9e99046f76b174d966f281291803f6991799b/thinc-8.2.3.tar.gz")
    version("8.2.2", sha256="6e85b944672c0f95241a71f67f9882e1ab319c449a47740b0d159f4cf86d1587", url="https://pypi.org/packages/61/19/f38625fadcfb0e5c97d1abb7f9d14e9890f946ff0e72c8d7b8a8ba2b2d8c/thinc-8.2.2.tar.gz")
    version("8.2.1", sha256="cd7fdb3d883a15e6906254e7fb0162f69878e9ccdd1f8519db6ffbfe46bf6f49", url="https://pypi.org/packages/b2/c8/9641507cde8ef43ece2b0267f9c9d558c4d463e2d0a56aa4d11438687c3e/thinc-8.2.1.tar.gz")
    version("8.2.0", sha256="82ca1e7831e354d74c6776ed87dbd73f4aad59ed258c8746cbe868688186fc49", url="https://pypi.org/packages/f2/68/73009f29388fce841b8f5a113532fb7a52d3770d820eee17942dc3e084fc/thinc-8.2.0.tar.gz")
    version("8.1.12", sha256="9dd12c5c79b176f077ce9416b49c9752782bd76ff0ea649d66527882e83ea353", url="https://pypi.org/packages/e5/bf/ef29e2525abfbd4a7515defeb44ec7390841a6497d6477410cc96c5c1b1a/thinc-8.1.12.tar.gz")
    version("8.1.11", sha256="98545474a17d927bebf5cacac9e58cf3717da91476cb2f2b4ea588b004f833e5", url="https://pypi.org/packages/74/43/8b403b961543706524bd565c59c734665619254ed4ee9de4cf2d4a81ded9/thinc-8.1.11.tar.gz")
    version("8.1.10", sha256="6c4a48d7da07e044e84a68cbb9b22f32f8490995a2bab0bfc60e412d14afb991", url="https://pypi.org/packages/fb/aa/daaff7c5c5878cad416b906bb8b573b5a4023e11a138ad082f1fb089eab8/thinc-8.1.10.tar.gz")
    version("8.1.9", sha256="8a1e65529c6d0796271d2a7e5ca6ea013fcb7dad69ec609d5093a25808107f51", url="https://pypi.org/packages/31/4d/7c07727e1d4f08e307c367c6574baf5f44fd5c4e1dfb06ea8606d047c02a/thinc-8.1.9.tar.gz")
    version("8.1.8", sha256="35c657cbedb04fc5bc247865d665921cec3d55ef35fbfce3ee1a20486b720683", url="https://pypi.org/packages/8b/0a/74fd5732268cb33a145cade6d0daaddd7ca518f23e6f931a41aebd1bc617/thinc-8.1.8.tar.gz")
    version("7.4.1", sha256="0139fa84dc9b8d88af15e648fc4ae13d899b8b5e49cb26a8f4a0604ee9ad8a9e", url="https://pypi.org/packages/17/5d/4343b3a79565af88ba2d53818d97995c3c239288f2565b826865f376d271/thinc-7.4.1.tar.gz")
    version("7.4.0", sha256="523e9be1bfaa3ed1d03d406ce451b6b4793a9719d5b83d2ea6b3398b96bc58b8", url="https://pypi.org/packages/f3/0b/10bbd6c847ea4cf2c54f6857ac3d4d0dda269ecb75ec37630ac860280571/thinc-7.4.0.tar.gz")

    with default_args(type="run"):
        depends_on("py-blis@0.7.8:0.7", when="@8.2.1:8,9.0.0.dev4:")
        depends_on("py-blis@0.4:0.4.0.0,0.4.1:0.4", when="@7.1:7.1.0.0,7.2:7.2.0.0,7.3:7.3.0.0,7.3.1:7.4.1,8.0.0.dev:8.0.0.dev0")
        depends_on("py-catalogue@2.0.4:2.0", when="@8.2.1:8,9.0.0.dev4:")
        depends_on("py-catalogue@0.0.7:1", when="@7.4:7.4.1,8.0.0.dev:8.0.0.dev0")
        depends_on("py-confection@0.0.1:", when="@8.2.1:8,9.0.0.dev4:")
        depends_on("py-cymem@2:", when="@7.0.8:7.1.0.0,7.2:7.2.0.0,7.3:7.3.0.0,7.3.1:7.4.1,8:8.0.0-alpha18,8.0.0-alpha20,8.0.0.dev:8.0.0,8.2.1:8,9.0.0.dev4:")
        depends_on("py-murmurhash@1.0.2:1.0.2.0,1.0.3:1.0", when="@8.2.1:8,9.0.0.dev4:")
        depends_on("py-murmurhash@0.28:1.0", when="@7.0.8:7.1.0.0,7.2:7.2.0.0,7.3:7.3.0.0,7.3.1:7.4.1,8:8.0.0-alpha18,8.0.0-alpha20,8.0.0.dev:8.0.0")
        depends_on("py-numpy@1.15.0:", when="@8.2.1:8,9.0.0.dev4: ^python@:3.8")
        depends_on("py-numpy@1.19.0:", when="@8.2.1:8,9.0.0.dev4: ^python@3.9:")
        depends_on("py-numpy@1.7:", when="@5.0.8:5,7.0.8:7.1.0.0,7.2:7.2.0.0,7.3:7.3.0.0,7.3.1:7.4.1,8:8.0.0-alpha18,8.0.0-alpha20,8.0.0.dev:8.0.0")
        depends_on("py-packaging@20:", when="@8.2.1:8,9.0.0.dev4:")
        depends_on("py-plac@0.9.6:1.1", when="@7.3.1:7.4.1")
        depends_on("py-preshed@3.0.2:3", when="@8:8.0.0-alpha18,8.0.0-alpha20,8.0.0.dev:8.0.0,8.2.1:8,9.0.0.dev4:")
        depends_on("py-preshed@1.0.1:3", when="@7.2:7.2.0.0,7.3:7.3.0.0,7.3.1:7.4.1")
        depends_on("py-pydantic@1.7.4:1.7,1.8.2:", when="@8.2.1:8,9.0.0.dev4:")
        depends_on("py-setuptools", when="@8:8.0.0-alpha18,8.0.0-alpha20,8.0.0.dev:8.0.0,8.2.1:8,9.0.0.dev4:")
        depends_on("py-srsly@2.4:2.4.0.0,2.4.1:", when="@8.2.1:8,9.0.0.dev4:")
        depends_on("py-srsly@0.0.6:1", when="@7.0.8:7.1.0.0,7.2:7.2.0.0,7.3:7.3.0.0,7.3.1:7.4.1")
        depends_on("py-tqdm@4.10:", when="@7.0.8:7.1.0.0,7.2:7.2.0.0,7.3:7.3.0.0,7.3.1:7.4.1")
        depends_on("py-wasabi@0.8.1:", when="@8.2.1:8,9.0.0.dev4:")
        depends_on("py-wasabi@0.0.9:0", when="@7.0.8:7.1.0.0,7.2:7.2.0.0,7.3:7.3.0.0,7.3.1:7.4.1")

