# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyOmegaconf(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("2.4.0.dev3", sha256="acffa42eab0d9cb09ccead6e80d1dfd20a625e21602353f267f3bc2cd131f7b2", url="https://pypi.org/packages/dc/08/29b30970ce5e22440e2bc1fd929a79de08feb3c6c054bc7e832228fc1a94/omegaconf-2.4.0.dev3-py3-none-any.whl")
    version("2.4.0.dev2", sha256="23b3837e5943ab46ea27b8ef7c54741bc320cb7895028fccc95580b260320492", url="https://pypi.org/packages/a8/3f/0c50b5e353837c14f99923b07a281b6da7687044b39e7efdebe8e6bd01f7/omegaconf-2.4.0.dev2-py3-none-any.whl")
    version("2.4.0.dev1", sha256="6c202560ac43d3a5aa5aa52d0d5911ea86dc35e56ab02d9e1675f11c7984e729", url="https://pypi.org/packages/67/d4/f0117bc2d36185e0b90c39755259dcdfb86e0f362a9c9db46193501f7c9e/omegaconf-2.4.0.dev1-py3-none-any.whl")
    version("2.4.0.dev0", sha256="60f1c3cf5b1814bd292ced4474c59ae27592bf062b445e24ff424c3dd87dde0e", url="https://pypi.org/packages/c7/a2/e87a9ede29f8b150de5733850797a058b463d2831a8d587319e3d60cd21a/omegaconf-2.4.0.dev0-py3-none-any.whl")
    version("2.3.0", sha256="7b4df175cdb08ba400f45cae3bdcae7ba8365db4d165fc65fd04b050ab63b46b", url="https://pypi.org/packages/e3/94/1843518e420fa3ed6919835845df698c7e27e183cb997394e4a670973a65/omegaconf-2.3.0-py3-none-any.whl")
    version("2.3.0.dev2", sha256="9358d82b2c568f916ea9cca1505c323b1982df9a4017f5e23d45446413fed97d", url="https://pypi.org/packages/a6/d4/ede8fea281d9525f1422bdd0762bfb1d6489917020aab171c92b06bd88c4/omegaconf-2.3.0.dev2-py3-none-any.whl")
    version("2.3.0.dev1", sha256="1d1a083e99151a671f43d0c200e9fd8d7b19dbe145b92c5ea96a129a6343afbd", url="https://pypi.org/packages/51/96/255e7a0648b5fa8c4fa15583d3e4f70f115270640f6ef04c0441b8231e6b/omegaconf-2.3.0.dev1-py3-none-any.whl")
    version("2.3.0.dev0", sha256="18797ee9b1e4861b8d6908db2721b027bc54ebb4aa8cfa52aadb30c9a0785bdd", url="https://pypi.org/packages/31/d6/bb58c36a59217d0468b5a546350f6e02fe77594810b9beb6e11442b47527/omegaconf-2.3.0.dev0-py3-none-any.whl")
    version("2.2.3", sha256="d6f2cbf79a992899eb76c6cb1aedfcf0fe7456a8654382edd5ee0c1b199c0657", url="https://pypi.org/packages/98/c3/f00dcd6935c11555db6ad55bdada58706120974cacf9a861a7b948ea0619/omegaconf-2.2.3-py3-none-any.whl")
    version("2.2.2", sha256="556917181487fb66fe832d3c7b324f51b2f4c8adc373dd5091be921501b7d420", url="https://pypi.org/packages/ce/56/ffc5a96c317f94aad1cdfa1e00307a9c18b4c79841663d8d6decb15afcf1/omegaconf-2.2.2-py3-none-any.whl")
    version("2.2.1", sha256="5ce512b0a8996b5acddc7b30f6bffa337a4b0ada1d96b4270588365e2a69e6d5", url="https://pypi.org/packages/d0/a2/b6e1792865fbc202c92fb9216e8dc1284d00a7d860b830953d4a0aac3ff2/omegaconf-2.2.1-py3-none-any.whl")
    version("2.2.0", sha256="61ade5dbc667cb51d290e8f5e7d54850ebf145f14dddf81222123bab5f0f7bc1", url="https://pypi.org/packages/b5/f6/b463d1ddb249ae59a9b1c7c2ef423b60262973da70db781e06aee19d5f8b/omegaconf-2.2.0-py3-none-any.whl")
    version("2.1.2", sha256="2ae9cbbc1105991da5301b7a0ac8b960958c311239bb2dfd4e3f5e60d2a51029", url="https://pypi.org/packages/2f/ae/5fd6ba3e3ef122bc5acf51e58a0dce03c9aa90e69069993133aa190be768/omegaconf-2.1.2-py3-none-any.whl")
    version("2.1.1", sha256="be93d73eaa2564fbe52d88ee13e3b79f4c6e04876b2f326551a21391f7dc6367", url="https://pypi.org/packages/66/c8/7ef11e12f3844b210add2e003abf8a0c7981ce7b5553dc630b635e7b905e/omegaconf-2.1.1-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-antlr4-python3-runtime@4.9", when="@2.2.0.dev3:2.4.0.dev0")
        depends_on("py-antlr4-python3-runtime@4.8", when="@2.1:2.2.0.dev2")
        depends_on("py-pyyaml@5.1:", when="@2.1:")
        depends_on("py-typing-extensions", when="@2.4.0.dev1: ^python@:3.9.0")
        depends_on("py-typing-extensions", when="@2.0.0-rc3:2.0")
    # END DEPENDENCIES

