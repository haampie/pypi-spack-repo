# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyHorovod(PythonPackage):
    # BEGIN VERSIONS
    version("0.28.1", sha256="92a43f5a94c43907a56805bad15f19700c62ffc83b7ca483f9e104e229f67ef0", url="https://pypi.org/packages/e4/86/da559fcc1620ac7831a16ccb2ad3acb477a8da8a631f75a83b6410507210/horovod-0.28.1.tar.gz")
    version("0.28.0", sha256="32bba0bdc9fc1bf0b2ba63950fbefce8d8be095a3a87d3977a3dc3f1eb12ffab", url="https://pypi.org/packages/23/6e/88a7a300fb389d83091234b7c89cdac8df69d6a1ae3a031ab63210f23348/horovod-0.28.0.tar.gz")
    version("0.27.0", sha256="8a76a98266579de46a1b1cde53d5ec115fc163ffdaa65a8f771aee936e804b33", url="https://pypi.org/packages/ff/40/4cdb91cb3e44990ca83ce80feb53e9b15519c174fdf545fd8b052abb5111/horovod-0.27.0.tar.gz")
    version("0.26.1", sha256="0079e4efb4ffe3f042e9e00470fbb457973903e748f75909de71e492d2474e94", url="https://pypi.org/packages/b3/1b/fecb25c66a1956e5530a6561ebbf97a7cda71717443526cd71531d423fe5/horovod-0.26.1.tar.gz")
    version("0.26.0", sha256="c89dab945e38fec482e0a52a0b560e192e7abd137a9a6323f104f15ac9423f64", url="https://pypi.org/packages/4c/2c/04899b71809c2de804d7ac3aa9ea401a507a026e2bf15b58f47f04a8d03e/horovod-0.26.0.tar.gz")
    version("0.25.0", sha256="bc9fed57b67c1b55259671d2439cdbc93aa897ea6e5da459e11e7556972b2355", url="https://pypi.org/packages/a7/8b/fcf373aade011f88dafe48628f7d348471d2891974eb5762ceeff3f13920/horovod-0.25.0.tar.gz")
    version("0.24.3", sha256="af24e4b1ed9adaa0db98f6375c023d438f65f116aa80ad5e7a321780362b3e7f", url="https://pypi.org/packages/fb/e4/15bdfa48be484a56c97f4ba49c35afd719d62fb7f6552c45f30c4e8f5712/horovod-0.24.3.tar.gz")
    version("0.24.2", sha256="22d6c2f3967426810510113bc6fd93649aa23e6e47e040e0a5ced0f48c34fca5", url="https://pypi.org/packages/42/02/1bd5d10799d95f538df29bcd80b261b8e213d5d1f8d0e23324f779efbd04/horovod-0.24.2.tar.gz")
    version("0.24.1", sha256="260bd96b1c74c5e27f7fca8a53f5f01ee7bdbf3af536836a5da23ed773fd3390", url="https://pypi.org/packages/54/d2/4543a6ca118290d378ccb2b512d76bfef0cffa222858276a7d047142bb44/horovod-0.24.1.tar.gz")
    version("0.24.0", sha256="16f77c96c5f90b699729f635619d4edc8cbb84b6bc6f3e13d213c252bf99be89", url="https://pypi.org/packages/dd/78/f17d8ff33c75aa4ad643c5cf0be3439d37f1be25b110983454e1be44b240/horovod-0.24.0.tar.gz")
    version("0.23.0", sha256="72ab3e5f59df6a000473999937e52e6831ad1a5e4e7bd23885a04bcdd4d8691c", url="https://pypi.org/packages/75/f2/a4e5d68d19bc46f93bb8bf4d88d0bc5c06d7015b3a2de3fc83dc6bfa3849/horovod-0.23.0.tar.gz")
    version("0.22.1", sha256="c45bfcb9bd96852d79c62976eda12e9320b58b64f55bee3772877b3fc6243f2a", url="https://pypi.org/packages/8f/67/ac837162b18eeb839e93a12f5ab945ebe15d7e82a71684dc9197ffa02fe4/horovod-0.22.1.tar.gz")
    version("0.22.0", sha256="ed7526eeb5a9aca8a8a49a04a41a4648cb7b0a265857875fc5d6a04a739fdb37", url="https://pypi.org/packages/59/e9/c672fbd6aeb55a32ad97f7b1b79a7903f6afbdca85906f0c0cc07eb821ff/horovod-0.22.0.tar.gz")
    version("0.21.3", sha256="dee8b2387b1ec9f54fe1737a95b992a52ce20cb3f1a4388017215fae14978f95", url="https://pypi.org/packages/12/99/8e6c86ef89aadd8f2b49d0fcec96d215589faf7d259a6a7927e219aa3450/horovod-0.21.3.tar.gz")
    version("0.21.2", sha256="b9ea0b048327b14f1fe331a3c3b053127c0f2fe944c6ef434f1e4a7f95931fc2", url="https://pypi.org/packages/0e/27/af0dc65602f59beb2d7c648a97e76e7a0c6f2a37ca7f68a447653fc67067/horovod-0.21.2.tar.gz")
    version("0.21.1", sha256="874dd3ac469944464bb77e1a42296500d0028177183ad5ab5af8ec61a34a1ed7", url="https://pypi.org/packages/d3/93/503830d0de5c7390d65c94ffa60db3719826f3deeb0d055fcfa35b4d7927/horovod-0.21.1.tar.gz")
    version("0.21.0", sha256="89c28de73524216f2b9433ffd858f79151da6c6b9cf63c9698c4d0b009c13901", url="https://pypi.org/packages/65/b2/9da3f1ad59a6d15263228e8e01ad3a4ee6c7233756abfb08813203ebaa11/horovod-0.21.0.tar.gz")
    version("0.20.3", sha256="6ebc90d627af486d44335ed48489e1e8dc190607574758867c52e4e17d75a247", url="https://pypi.org/packages/6f/bd/b979db25c1337967472630714d0f98ec596ad9f199a3d1777dc36453d713/horovod-0.20.3.tar.gz")
    version("0.20.2", sha256="80aad735969b914bf03b950729dde652704a587118ed5d1fcb0bb79c64b42f6c", url="https://pypi.org/packages/bc/f1/81c2dfffce3b25e13010a60608bb51550ea46d58369a501f0c80ce464679/horovod-0.20.2.tar.gz")
    version("0.20.1", sha256="25566d939b771c49f558f5c28770d5976c9248f6a9a475773a8b6118d5dda758", url="https://pypi.org/packages/dd/34/8df9eeb311b6e36cf80a88338830d248096438dc98c94dbbac6cbda37737/horovod-0.20.1.tar.gz")
    version("0.20.0", sha256="88522b65d83cb9690193b200e2e8fd1e08864b27d72b7ff1bbc5e7b8ae4f32ed", url="https://pypi.org/packages/71/4a/35e6a929a29ce0dd593700835b0d8ef30f02eb90938c7f98d564a188915f/horovod-0.20.0.tar.gz")
    version("0.19.5", sha256="428d9ba5ff277467be77e4e707d40b915f7d9e6920a2645f647fcb2cea59c366", url="https://pypi.org/packages/25/3a/289d100467ae33bce717daa3b285c72e0c82c761c5de37cc61940982c83c/horovod-0.19.5.tar.gz")
    version("0.19.4", sha256="b4bb14ce3cab5abf09790bb28d4e7b66ad67fb6dc520d760a060d989d9020d46", url="https://pypi.org/packages/21/38/eb90f95f73fb352c662b642c54785b6abadaf2d736928406c9e649d7b558/horovod-0.19.4.tar.gz")
    version("0.19.3", sha256="5e6ef552d2565f8ef144343ce835864a4baf2c8d05b8ad4f70c9f07416b52815", url="https://pypi.org/packages/1a/a4/10f01433d02f2bfcd8c470d3f3da0e0fe9036013fad87df56f549c85ef20/horovod-0.19.3.tar.gz")
    version("0.19.2", sha256="981f302ee8c71c3b7d0cb8007aced707ecdb44068f207f10c61fa610c6b61d85", url="https://pypi.org/packages/af/7a/d1ecb3b8911ece7b3b7e7c23cb074c7bbfee73b3149a668cfeee59480fa9/horovod-0.19.2.tar.gz")
    version("0.19.1", sha256="2e7a609a985a54effead95512a568d5b94e2957cfc821c2bee5d49850fdd9ae3", url="https://pypi.org/packages/c0/31/dae1f224a284ccaf0fd700565a53658bfba9c3d5964719305953e72a11e0/horovod-0.19.1.tar.gz")
    version("0.19.0", sha256="478775ef5af7d33981d6114db4ad10c57ed69b8c3887b7a0d45b65fef924bf56", url="https://pypi.org/packages/e8/1b/51c36afc6dab9afad1caed2a11366d1e238e42f3c51177d06779356f8f1a/horovod-0.19.0.tar.gz")
    version("0.18.2", sha256="a8c9c48976a41ff04ed3d69eb92c59ff444cc414dd45ef047750eab25c03e803", url="https://pypi.org/packages/2b/ae/c86526c637e427c4bac1b6eff890ae39493ddde7ff48b7bb497d0ceaef1b/horovod-0.18.2.tar.gz")
    version("0.18.1", sha256="26a7751b090caabeba27808786b106cc672bc0aef3e7993361e99479c08beeb3", url="https://pypi.org/packages/8b/a0/27b00807e6ed78bcab146594acd680e6493d9e49b43ed1649ccf70e2a95d/horovod-0.18.1.tar.gz")
    version("0.18.0", sha256="5182ca12a11a6dfa5215e8f00e3d873bdba01214077d5f08626b62cc453e3aa6", url="https://pypi.org/packages/3e/f0/182fa04184ee38588d17c83f5998b3079af79345822df8d1f5228db16de1/horovod-0.18.0.tar.gz")
    version("0.16.4", sha256="871de9f0dfef7ddda637ee78ce7d95494340f7f8eb9fbd0c3cf13df7e68c5812", url="https://pypi.org/packages/42/f8/0a2fedf45122d8a1b2dbd573e737ccb32cd0776aa4c4b157d3f18b9ff0ca/horovod-0.16.4.tar.gz")
    version("0.16.3", sha256="816a429693894439eabfae7377b3bf2959691a87edc633e0773d1b393c5a02c9", url="https://pypi.org/packages/ca/91/cf326c8504be35f09ef128ac62311ea373e9facc56f53cf9e9bf84594ab1/horovod-0.16.3.tar.gz")
    version("0.16.2", sha256="9a035dff619e52b5e1b20c170a556dc8ea0eafe12f9a6bcb0832ee5ffc84a7fd", url="https://pypi.org/packages/4b/89/d1a64d0a9c15abfa8a72eb8b20ebe8cd4b144579301a69fadec18ccc6232/horovod-0.16.2.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    variant("controllers", default=False, description="controllers")
    variant("cuda", default=False, description="cuda")
    variant("cuda_arch", default=False, description="cuda_arch")
    variant("frameworks", default=False, description="frameworks")
    variant("rocm", default=False, description="rocm")
    variant("tensor_ops", default=False, description="tensor_ops")
    # END VARIANTS

    # BEGIN DEPENDENCIES
    # END DEPENDENCIES

