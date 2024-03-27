##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPygments(PythonPackage):
    version("2.17.2", sha256="b27c2826c47d0f3219f29554824c30c5e8945175d888647acd804ddd04af846c", url="https://pypi.org/packages/97/9c/372fef8377a6e340b1704768d20daaded98bf13282b5327beb2e2fe2c7ef/pygments-2.17.2-py3-none-any.whl")
    version("2.17.1", sha256="1b37f1b1e1bff2af52ecaf28cc601e2ef7077000b227a0675da25aef85784bc4", url="https://pypi.org/packages/4f/34/6a8073bd275d7034476b4af94a5f3ca206b86e4c206a61eeb4e3d73b4a06/pygments-2.17.1-py3-none-any.whl")
    version("2.17.0", sha256="cd0c46944b2551af02ecc15961050182ea120d3895000e2676160820f3421527", url="https://pypi.org/packages/5b/66/a48025f51da4dec44c7a3de9b643fdc34ffb92ad1f2b3e90ebc6305d2c0f/pygments-2.17.0-py3-none-any.whl")
    version("2.16.1", sha256="13fc09fa63bc8d8671a6d247e1eb303c4b343eaee81d861f3404db2935653692", url="https://pypi.org/packages/43/88/29adf0b44ba6ac85045e63734ae0997d3c58d8b1a91c914d240828d0d73d/Pygments-2.16.1-py3-none-any.whl")
    version("2.16.0", sha256="90e046f72a58b65edd7e6bd99926ffa1b9d19e23db166905046bea0069c0894d", url="https://pypi.org/packages/ec/9a/40aa8248006cbe35b8bffc83cfca0ffdf68306d4354bca334a25b4b275a0/Pygments-2.16.0-py3-none-any.whl")
    version("2.15.1", sha256="db2db3deb4b4179f399a09054b023b6a586b76499d36965813c71aa8ed7b5fd1", url="https://pypi.org/packages/34/a7/37c8d68532ba71549db4212cb036dbd6161b40e463aba336770e80c72f84/Pygments-2.15.1-py3-none-any.whl")
    version("2.15.0", sha256="77a3299119af881904cd5ecd1ac6a66214b6e9bed1f2db16993b54adede64094", url="https://pypi.org/packages/08/4c/c587fc05d6f15f4deff971cb1a5b624429d6187c19f7274a50670edf3ec8/Pygments-2.15.0-py3-none-any.whl")
    version("2.14.0", sha256="fa7bd7bd2771287c0de303af8bfdfc731f51bd2c6a47ab69d117138893b82717", url="https://pypi.org/packages/0b/42/d9d95cc461f098f204cd20c85642ae40fbff81f74c300341b8d0e0df14e0/Pygments-2.14.0-py3-none-any.whl")
    version("2.13.0", sha256="f643f331ab57ba3c9d89212ee4a2dabc6e94f117cf4eefde99a0574720d14c42", url="https://pypi.org/packages/4f/82/672cd382e5b39ab1cd422a672382f08a1fb3d08d9e0c0f3707f33a52063b/Pygments-2.13.0-py3-none-any.whl")
    version("2.12.0", sha256="dc9c10fb40944260f6ed4c688ece0cd2048414940f1cea51b8b226318411c519", url="https://pypi.org/packages/5c/8e/1d9017950034297fffa336c72e693a5b51bbf85141b24a763882cf1977b5/Pygments-2.12.0-py3-none-any.whl")
    version("2.10.0", sha256="b8e67fe6af78f492b3c4b3e2970c0624cbf08beb1e493b2c99b9fa1b67a20380", url="https://pypi.org/packages/78/c8/8d9be2f72d8f465461f22b5f199c04f7ada933add4dae6e2468133c17471/Pygments-2.10.0-py3-none-any.whl")
    version("2.6.1", sha256="ff7a40b4860b727ab48fad6360eb351cc1b33cbf9b15a0f689ca5353e9463324", url="https://pypi.org/packages/2d/68/106af3ae51daf807e9cdcba6a90e518954eb8b70341cee52995540a53ead/Pygments-2.6.1-py3-none-any.whl")
    version("2.4.2", sha256="71e430bc85c88a430f000ac1d9b331d2407f681d6f6aec95e8bcfbc3df5b0127", url="https://pypi.org/packages/5c/73/1dfa428150e3ccb0fa3e68db406e5be48698f2a979ccbcec795f28f44048/Pygments-2.4.2-py2.py3-none-any.whl")
    version("2.3.1", sha256="e8218dd399a61674745138520d0d4cf2621d7e032439341bc3f647bff125818d", url="https://pypi.org/packages/13/e5/6d710c9cf96c31ac82657bcfb441df328b22df8564d58d0c4cd62612674c/Pygments-2.3.1-py2.py3-none-any.whl")
    version("2.2.0", sha256="78f3f434bcc5d6ee09020f92ba487f95ba50f1e3ef83ae96b9d5ffa1bab25c5d", url="https://pypi.org/packages/02/ee/b6e02dc6529e82b75bb06823ff7d005b141037cb1416b10c6f00fc419dca/Pygments-2.2.0-py2.py3-none-any.whl")
    version("2.1.3", sha256="88e4c8a91b2af5962bfa5ea2447ec6dd357018e86e94c7d14bd8cacbc5b55d81", url="https://pypi.org/packages/b8/67/ab177979be1c81bc99c8d0592ef22d547e70bb4c6815c383286ed5dec504/Pygments-2.1.3.tar.gz")
    version("2.0.2", sha256="7320919084e6dac8f4540638a46447a3bd730fca172afc17d2c03eed22cf4f51", url="https://pypi.org/packages/f4/c6/bdbc5a8a112256b2b6136af304dbae93d8b1ef8738ff2d12a51018800e46/Pygments-2.0.2.tar.gz")
    version("2.0.1", sha256="5e039e1d40d232981ed58914b6d1ac2e453a7e83ddea22ef9f3eeadd01de45cb", url="https://pypi.org/packages/91/ee/7b36fa4ef73009d896af9d505305871427ee753b19efce40b797ae8942dc/Pygments-2.0.1.tar.gz")


