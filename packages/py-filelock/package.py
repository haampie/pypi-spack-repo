# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyFilelock(PythonPackage):
    # BEGIN VERSIONS
    version("3.13.1", sha256="57dbda9b35157b05fb3e58ee91448612eb674172fab98ee235ccb0b5bee19a1c", url="https://pypi.org/packages/81/54/84d42a0bee35edba99dee7b59a8d4970eccdd44b99fe728ed912106fc781/filelock-3.13.1-py3-none-any.whl")
    version("3.13.0", sha256="a552f4fde758f4eab33191e9548f671970f8b06d436d31388c9aa1e5861a710f", url="https://pypi.org/packages/ea/c8/407364710cb9631ce306a97abff2d61836d603b258b5e5399b5f12a7f787/filelock-3.13.0-py3-none-any.whl")
    version("3.12.4", sha256="08c21d87ded6e2b9da6728c3dff51baf1dcecf973b768ef35bcbc3447edb9ad4", url="https://pypi.org/packages/5e/5d/97afbafd9d584ff1b45fcb354a479a3609bd97f912f8f1f6c563cb1fae21/filelock-3.12.4-py3-none-any.whl")
    version("3.12.3", sha256="f067e40ccc40f2b48395a80fcbd4728262fab54e232e090a4063ab804179efeb", url="https://pypi.org/packages/52/90/45223db4e1df30ff14e8aebf9a1bf0222da2e7b49e53692c968f36817812/filelock-3.12.3-py3-none-any.whl")
    version("3.12.2", sha256="cbb791cdea2a72f23da6ac5b5269ab0a0d161e9ef0100e653b69049a7706d1ec", url="https://pypi.org/packages/00/45/ec3407adf6f6b5bf867a4462b2b0af27597a26bd3cd6e2534cb6ab029938/filelock-3.12.2-py3-none-any.whl")
    version("3.12.1", sha256="42f1e4ff2b497311213d61ad7aac5fed9050608e5309573f101eefa94143134a", url="https://pypi.org/packages/e2/88/52dfc8182232b85ac63aaae9d5f0947ecd5d4ff24131bc1b3800c2bf7914/filelock-3.12.1-py3-none-any.whl")
    version("3.12.0", sha256="ad98852315c2ab702aeb628412cbf7e95b7ce8c3bf9565670b4eaecf1db370a9", url="https://pypi.org/packages/ad/73/b094a662ae05cdc4ec95bc54e434e307986a5de5960166b8161b7c1373ee/filelock-3.12.0-py3-none-any.whl")
    version("3.11.0", sha256="f08a52314748335c6460fc8fe40cd5638b85001225db78c2aa01c8c0db83b318", url="https://pypi.org/packages/9e/6b/fdcd53aeee771a868c4187f0955116894a2b1e82d73fb5990c2ef63afc18/filelock-3.11.0-py3-none-any.whl")
    version("3.10.7", sha256="bde48477b15fde2c7e5a0713cbe72721cb5a5ad32ee0b8f419907960b9d75536", url="https://pypi.org/packages/25/89/3c51e2896bf666fdda7e776f3421f1bfec843c34311c0a3486c90452a04d/filelock-3.10.7-py3-none-any.whl")
    version("3.10.6", sha256="52f119747b2b9c4730dac715a7b1ab34b8ee70fd9259cba158ee53da566387ff", url="https://pypi.org/packages/ea/2f/0459b7d1d7239d32b0b573f8330d89300a8763451a3150af0e0c8f2ef3b0/filelock-3.10.6-py3-none-any.whl")
    version("3.8.0", sha256="617eb4e5eedc82fc5f47b6d61e4d11cb837c56cb4544e39081099fa17ad109d4", url="https://pypi.org/packages/94/b3/ff2845971788613e646e667043fdb5f128e2e540aefa09a3c55be8290d6d/filelock-3.8.0-py3-none-any.whl")
    version("3.5.0", sha256="a7141afb4feca60925cfc090b411fb9faaf542d06d58ece4f93d940265e6b995", url="https://pypi.org/packages/d4/0b/6cb548cc9bb8450f9823b39f48e397be9fb8d042f7a9c405ba0a53270ad4/filelock-3.5.0-py3-none-any.whl")
    version("3.4.0", sha256="2e139a228bcf56dd8b2274a65174d005c4a6b68540ee0bdbb92c76f43f29f7e8", url="https://pypi.org/packages/e8/3b/b59c7bcacc4cccafcd6e927a9e191268657e79a0a75530132cbf03b22c47/filelock-3.4.0-py3-none-any.whl")
    version("3.0.12", sha256="929b7d63ec5b7d6b71b0fa5ac14e030b3f70b75747cef1b10da9b879fef15836", url="https://pypi.org/packages/93/83/71a2ee6158bb9f39a90c0dea1637f81d5eef866e188e1971a1b1ab01a35a/filelock-3.0.12-py3-none-any.whl")
    version("3.0.4", sha256="011327d4ed939693a5b28c0fdf2fd9bda1f68614c1d6d0643a89382ce9843a71", url="https://pypi.org/packages/2d/ba/db7e0717368958827fa97af0b8acafd983ac3a6ecd679f60f3ccd6e5b16e/filelock-3.0.4.tar.gz")
    version("3.0.3", sha256="7d8a86350736aa0efea0730e6a7f774195cbb1c2d61134c15f6be576399e87ff", url="https://pypi.org/packages/02/43/eeac4a7e32fd3cd7c4bdda042a7b33638a2fcc2c2851ab6e98d15fedfc3e/filelock-3.0.3.tar.gz")
    version("3.0.0", sha256="b3ad481724adfb2280773edd95ce501e497e88fa4489c6e41e637ab3fd9a456c", url="https://pypi.org/packages/ca/00/872754997bbb09582a1d3bd8c3179a50e32ffcc9d8b1ebe6b4d9bd310d56/filelock-3.0.0.tar.gz")
    version("2.0.13", sha256="d05079e7d7cae7576e192749d3461999ca6b0843d35b0f79f1fa956b0f6fc7d8", url="https://pypi.org/packages/45/4c/810fb0481b80766fd731981f93ce298fe36e4955ab7524ae66836499d743/filelock-2.0.13.tar.gz")
    version("2.0.12", sha256="eb4314a9a032707a914b037433ce866d4ed363fce8605d45f0c9d2cd6ac52f98", url="https://pypi.org/packages/e9/db/b5a9d2046c5048bbcf1e43312a66358b54012766f3b80f1a1d33b110a5f5/filelock-2.0.12.tar.gz")
    version("2.0.11", sha256="e9e370efe86c30b19a2c8c36dd9fcce8e5ce294ef4ed6ac86664b666eaf852ca", url="https://pypi.org/packages/61/c0/841be22e6da76b470fcd6a97aff9a14bcf647f832d1f6a6ff03073f8e575/filelock-2.0.11.tar.gz")
    version("2.0.10", sha256="c73bf706d8a0c5722de0b745495fed9cda0e46c0eabb44eb18ee3f00520fa85f", url="https://pypi.org/packages/c0/66/044ca468c7dd541e9636a5340d77cb418082c4b0dffcf1dabd28efc7a7e0/filelock-2.0.10.tar.gz")
    version("2.0.9", sha256="0f91dce339c9f25d6f2e0733a17e4f9a47b139dffda52619a0e61e013e5c6782", url="https://pypi.org/packages/0d/d1/b2e386af472844abc1c2986e657294495b0e0f732e70afeefec1bf20e8ab/filelock-2.0.9.tar.gz")
    version("2.0.8", sha256="7e48e4906de3c9a5d64d8f235eb3ae1050dfefa63fd65eaf318cc915c935212b", url="https://pypi.org/packages/55/fb/ad353636e03b66bc60c57e0e5e3e196bfdc08a030e5e16885da7cddf1bc0/filelock-2.0.8.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-typing-extensions@4.7.1:", when="@3.12.3 ^python@:3.10")
    # END DEPENDENCIES

