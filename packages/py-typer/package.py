# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyTyper(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("0.11.0", sha256="049cc47bef39f46b043eddd9165492209fdd9bc7d79afa7ba9cc5cd017caa817", url="https://pypi.org/packages/ed/55/c47933592c0bb9f4355e1b31c5f15088c0b3c8a93ebdf3f0e0347decea77/typer-0.11.0-py3-none-any.whl")
    version("0.10.0", sha256="b8a587aa06d3c5422c09c2e9935eb80b4c9de8605fd5ab702b2f92d72246ca48", url="https://pypi.org/packages/d9/07/8100c125307a26f03c305764f22cd995ae1878071ddf1df3588add73b53c/typer-0.10.0-py3-none-any.whl")
    version("0.9.4", sha256="aa6c4a4e2329d868b80ecbaf16f807f2b54e192209d7ac9dd42691d63f7a54eb", url="https://pypi.org/packages/62/39/82c9d3e10979851847361d922a373bdfef4091020da7f893acfaf07c0225/typer-0.9.4-py3-none-any.whl")
    version("0.9.3", sha256="683d3055ac04e63d062de74db0ce2051e91bd784605200865e2aa42b5808f4f8", url="https://pypi.org/packages/82/e9/eeae6b93f120d7a74147456f6eac95cce43cce121fb28af05e5014f4ca78/typer-0.9.3-py3-none-any.whl")
    version("0.9.2", sha256="d67f1dc319032c402afa63a47807efc4040837b9555bf73ed35f73127cd6be6b", url="https://pypi.org/packages/26/58/3178f8086929015ad3fdc9e39989bcc87efec90b33daed1bd10230a4dfaa/typer-0.9.2-py3-none-any.whl")
    version("0.9.1", sha256="aa06ca6c9b34631afb6ec402009b2cc67f40e8221171fd7f0b319dd62e3bb741", url="https://pypi.org/packages/7a/27/208876e4a9e9e3c2a6c8af883d13edb6a1a738825c736d6f56157abb6151/typer-0.9.1-py3-none-any.whl")
    version("0.9.0", sha256="5d96d986a21493606a358cae4461bd8cdf83cbf33a5aa950ae629ca3b51467ee", url="https://pypi.org/packages/bf/0e/c68adf10adda05f28a6ed7b9f4cd7b8e07f641b44af88ba72d9c89e4de7a/typer-0.9.0-py3-none-any.whl")
    version("0.8.0", sha256="07dd96b7961d11da53be3f9b9cd0eb76f413d5ef06df7942cb2f85bd03dd2633", url="https://pypi.org/packages/f6/72/70eeb30ab87d294b40f51dfd087fee64534c9c6cac73fa823fc3289684c9/typer-0.8.0-py3-none-any.whl")
    version("0.7.0", sha256="b5e704f4e48ec263de1c0b3a2387cd405a13767d2f907f44c1a08cbad96f606d", url="https://pypi.org/packages/0d/44/56c3f48d2bb83d76f5c970aef8e2c3ebd6a832f09e3621c5395371fe6999/typer-0.7.0-py3-none-any.whl")
    version("0.6.1", sha256="54b19e5df18654070a82f8c2aa1da456a4ac16a2a83e6dcd9f170e291c56338e", url="https://pypi.org/packages/e8/9b/7470461c68588ed09c2e53cbb16b802815232796d95f7b4744cc8842f19d/typer-0.6.1-py3-none-any.whl")
    version("0.6.0", sha256="211be18a88cf2b4a3edbefa48e2eac2d6f590833252b51075464e72ac35192c2", url="https://pypi.org/packages/43/ca/da2ef672f4930d9f0bdc05310cf3e270db1b27d63c6aa666c99b3fc99e02/typer-0.6.0-py3-none-any.whl")
    version("0.5.0", sha256="a34409c0029ba7e48cb9e4f54c6400bf4158a6145b5dea32788e7a36ebbcb312", url="https://pypi.org/packages/81/3b/5f09648e180279eefe964c6792c40525840e0e21ad57f8fef1a2c3ddddf7/typer-0.5.0-py3-none-any.whl")
    version("0.4.2", sha256="023bae00d1baf358a6cc7cea45851639360bb716de687b42b0a4641cd99173f1", url="https://pypi.org/packages/9d/ea/b565bc44a1af5278ef2ff9d571cdb4f4bc31fd450b0630441c93401c243c/typer-0.4.2-py3-none-any.whl")
    version("0.4.1", sha256="e8467f0ebac0c81366c2168d6ad9f888efdfb6d4e1d3d5b4a004f46fa444b5c3", url="https://pypi.org/packages/52/bb/2bf41b92ea42ed36874669afad18ffe1c5b95d96d2f26dacfa33edb22b79/typer-0.4.1-py3-none-any.whl")
    version("0.4.0", sha256="d81169725140423d072df464cad1ff25ee154ef381aaf5b8225352ea187ca338", url="https://pypi.org/packages/4f/bd/77f6cb38c291717c5109cc2638086033fd7de4f8aeb0ed95e9ed484efa82/typer-0.4.0-py3-none-any.whl")
    version("0.3.2", sha256="ba58b920ce851b12a2d790143009fa00ac1d05b3ff3257061ff69dbdfc3d161b", url="https://pypi.org/packages/90/34/d138832f6945432c638f32137e6c79a3b682f06a63c488dcfaca6b166c64/typer-0.3.2-py3-none-any.whl")
    version("0.3.1", sha256="778a9695e68eb26a0a0321ca9d3f1a8809783f6f083549b84c67bc2385bf014e", url="https://pypi.org/packages/73/5d/94781aa6849c98bf71e9389efc7112ecc171fe544b55ceab8583228d039d/typer-0.3.1-py3-none-any.whl")
    version("0.3.0", sha256="a2a7b4b6388debc2b7160c8b7a54368df85b56c3f1447846bad630e99d629ffc", url="https://pypi.org/packages/20/82/d8e6c9100f31b7cffb7274603d41e77af1c70ea2d9f03671313ec7868454/typer-0.3.0-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-click@8.0.0:", when="@0.11:")
        depends_on("py-click@7.1.1:", when="@0.4:0.10")
        depends_on("py-click@7.1.1:7", when="@0.0.10:0.3")
        depends_on("py-typing-extensions@3.7.4.3:", when="@0.9:")
    # END DEPENDENCIES

