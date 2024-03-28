# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPluggy(PythonPackage):
    # BEGIN VERSIONS
    version("1.4.0", sha256="7db9f7b503d67d1c5b95f59773ebb58a8c1c288129a88665838012cfb07b8981", url="https://pypi.org/packages/a5/5b/0cc789b59e8cc1bf288b38111d002d8c5917123194d45b29dcdac64723cc/pluggy-1.4.0-py3-none-any.whl")
    version("1.3.0", sha256="d89c696a773f8bd377d18e5ecda92b7a3793cbe66c87060a6fb58c7b6e1061f7", url="https://pypi.org/packages/05/b8/42ed91898d4784546c5f06c60506400548db3f7a4b3fb441cba4e5c17952/pluggy-1.3.0-py3-none-any.whl")
    version("1.2.0", sha256="c2fd55a7d7a3863cba1a013e4e2414658b1d07b6bc57b3919e0c63c9abb99849", url="https://pypi.org/packages/51/32/4a79112b8b87b21450b066e102d6608907f4c885ed7b04c3fdb085d4d6ae/pluggy-1.2.0-py3-none-any.whl")
    version("1.1.0", sha256="d81d19a3a88d82ed06998353ce5d5c02587ef07ee2d808ae63904ab0ccef0087", url="https://pypi.org/packages/5d/8e/293ae6e231bd3e2d56cf452b5784732d0cb3da1422f39b7f1fbb5a346873/pluggy-1.1.0-py3-none-any.whl")
    version("1.0.0", sha256="74134bbf457f031a36d68416e1509f34bd5ccc019f0bcc952c7b909d06b37bd3", url="https://pypi.org/packages/9e/01/f38e2ff29715251cf25532b9082a1589ab7e4f571ced434f98d0139336dc/pluggy-1.0.0-py2.py3-none-any.whl")
    version("1.0.0.dev0", sha256="467f0219e89bb5061a8429c6fc5cf055fa3983a0e68e84a1d205046306b37d9e", url="https://pypi.org/packages/65/3e/e685d8a32b0f959bcfce51df06b2bdd0c8b14399ee0da22fe35a3e987842/pluggy-1.0.0.dev0-py2.py3-none-any.whl")
    version("0.13.1", sha256="966c145cd83c96502c3c3868f50408687b38434af77734af1e9ca461a4081d2d", url="https://pypi.org/packages/a0/28/85c7aa31b80d150b772fbe4a229487bc6644da9ccb7e427dd8cc60cb8a62/pluggy-0.13.1-py2.py3-none-any.whl")
    version("0.13.0", sha256="0db4b7601aae1d35b4a033282da476845aa19185c1e6964b25cf324b5e4ec3e6", url="https://pypi.org/packages/92/c7/48439f7d5fd6bddb4c04b850bb862b42e3e2b98570040dfaf68aedd8114b/pluggy-0.13.0-py2.py3-none-any.whl")
    version("0.12.0", sha256="b9817417e95936bf75d85d3f8767f7df6cdde751fc40aed3bb3074cbcb77757c", url="https://pypi.org/packages/06/ee/de89e0582276e3551df3110088bf20844de2b0e7df2748406876cc78e021/pluggy-0.12.0-py2.py3-none-any.whl")
    version("0.11.0", sha256="964cedd2b27c492fbf0b7f58b3284a09cf7f99b0f715941fb24a439b3af1bd1a", url="https://pypi.org/packages/cc/e4/2003a5e4e445424602c8f06a436eeed9e78bcae4947128f64741c66c7216/pluggy-0.11.0-py2.py3-none-any.whl")
    version("0.10.0", sha256="1c0b297d4d41bc9bdfbdc17991b35f9e1d2cfe8eaa4d7c118e86d705870d34c8", url="https://pypi.org/packages/57/ba/54c93ac55084bde8f9195ed5cd04223b3c0d30d300801bf556565cb7675a/pluggy-0.10.0-py2.py3-none-any.whl")
    version("0.9.0", sha256="84d306a647cc805219916e62aab89caa97a33a1dd8c342e87a37f91073cd4746", url="https://pypi.org/packages/84/e8/4ddac125b5a0e84ea6ffc93cfccf1e7ee1924e88f53c64e98227f0af2a5f/pluggy-0.9.0-py2.py3-none-any.whl")
    version("0.8.1", sha256="980710797ff6a041e9a73a5787804f848996ecaa6f8a1b1e08224a5894f2074a", url="https://pypi.org/packages/2d/60/f58d9e8197f911f9405bf7e02227b43a2acc2c2f1a8cbb1be5ecf6bfd0b8/pluggy-0.8.1-py2.py3-none-any.whl")
    version("0.7.1", sha256="6e3836e39f4d36ae72840833db137f7b7d35105079aee6ec4a62d9f80d594dd1", url="https://pypi.org/packages/f5/f1/5a93c118663896d83f7bcbfb7f657ce1d0c0d617e6b4a443a53abcc658ca/pluggy-0.7.1-py2.py3-none-any.whl")
    version("0.6.0", sha256="d345c8fe681115900d6da8d048ba67c25df42973bda370783cd58826442dcd7c", url="https://pypi.org/packages/82/05/43e3947125a2137cba4746135c75934ceed1863f27e050fc560052104a71/pluggy-0.6.0-py2-none-any.whl")
    version("0.5.2", sha256="cab5800ece3d679358782c4d674be9912f52918bc919888b228fdf5705fcd067", url="https://pypi.org/packages/4d/d1/e478b8a33230f85f38e35b386376fbd115219de2a2c4c8783610851ad1c3/pluggy-0.5.2-py2.py3-none-any.whl")
    version("0.5.1", sha256="359f6d0fbcbb27950eb89909910ce909c90b834bfec8c4b1ca0840f6ba398bfb", url="https://pypi.org/packages/aa/2b/11b53318ae1c96f163d0317ddf10f2b1892b9b38ef56ab6aad554c68a4f2/pluggy-0.5.1-py2.py3-none-any.whl")
    version("0.5.0", sha256="99e205b82bc98cf3c37f6ded92eaf062f24ee539d71161473e194a54c367b86c", url="https://pypi.org/packages/0c/78/9ee1dd3a1df2f19d49ca1a8d03086db3aa96cce1f0c98ed7bb823f0adcdc/pluggy-0.5.0.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-importlib-metadata@0.12:", when="@0.12")
        depends_on("py-importlib-metadata@0.9:", when="@0.10")
    # END DEPENDENCIES

