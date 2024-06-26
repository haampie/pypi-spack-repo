# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyLibensemble(PythonPackage):
    # BEGIN VERSIONS
    version("1.2.2", sha256="936e34ed4e8129a9980187b21d586472b6362403889a739595d6b631335a8678", url="https://pypi.org/packages/95/21/137deb1c213f62ad310819e9f523052070f8747ef9721286c63d14b7ade2/libensemble-1.2.2.tar.gz")
    version("1.2.1", sha256="b80e77548a1e2a71483352b3b00e22b47191e45ca5741324c2b0f20b05579a3d", url="https://pypi.org/packages/60/42/8d0caf3d3ae01befff3388db28798aada8913122b00907f573e546585e90/libensemble-1.2.1.tar.gz")
    version("1.2.0", sha256="e1076e8eea7844d3799f92d136586eca4da34ec753bf41a8d1be04d7a45ec4c1", url="https://pypi.org/packages/68/4a/fc682ef3503950248f4b57efc9b2dbf5f84d31be603e997220273474180d/libensemble-1.2.0.tar.gz")
    version("1.1.0", sha256="3e3ddc4233272d3651e9d62c7bf420018930a4b9b135ef9ede01d5356235c1c6", url="https://pypi.org/packages/ad/34/e2558349e9191df3c5a6fee4152c962d6e244ac1a9a9026265e7cbc3c74f/libensemble-1.1.0.tar.gz")
    version("1.0.0", sha256="b164e044f16f15b68fd565684ad8ce876c93aaeb84e5078f4ea2a29684b110ca", url="https://pypi.org/packages/44/bb/d2bb3dfd6069f5cf39d32e4767842ca63d8a923a762aa606ebd9eba5a054/libensemble-1.0.0.tar.gz")
    version("0.10.2", sha256="ef8dfe5d233dcae2636a3d6aa38f3c2ad0f42c65bd38f664e99b3e63b9f86622", url="https://pypi.org/packages/cc/85/a7bdf3a89f3a54a3439be0cf95e5d29c3ede9e0276001f056f55b5d0fd9e/libensemble-0.10.2.tar.gz")
    version("0.10.1", sha256="56ae42ec9a28d3df8f46bdf7d016db9526200e9df2a28d849902e3c44fe5c1ba", url="https://pypi.org/packages/88/a2/5fa38df321949ec68cdd1d17fc83d676433914341f4bffe99fd325083338/libensemble-0.10.1.tar.gz")
    version("0.10.0", sha256="f800f38d02def526f1d2a325710d01fdd3637cd1e33a9a083a3cf4a7f419a726", url="https://pypi.org/packages/31/be/e0687c9f90431f18ae28c5577257df98cb307b684c044b72b644f88d0232/libensemble-0.10.0.tar.gz")
    version("0.9.3", sha256="00e5a65d6891feee6a686c048d8de72097b8bff164431f163be96ec130a9c390", url="https://pypi.org/packages/55/fe/9cef349389c8756a02aaa213400de71160af282dddabc562b4583cb1155c/libensemble-0.9.3.tar.gz")
    version("0.9.2", sha256="e46598e5696f770cbff4cb90507b52867faad5654f1b80de35405a95228c909f", url="https://pypi.org/packages/4b/2f/e2be1f732a5ceff2e56c7738f437dd0b4d0bbd9f6d026e40756b6f96e4a6/libensemble-0.9.2.tar.gz")
    version("0.9.1", sha256="684e52b0ea64f5ec610e7868b7e4c9fa5fd2316a370a726870aa5fd5fb1b0ede", url="https://pypi.org/packages/6e/43/464a3430bb18ebcd3b5fb20c8778519a1de4dc4eb9f88e57fedc7577653a/libensemble-0.9.1.tar.gz")
    version("0.9.0", sha256="34976e775f0d2ba5955744560104eab214fd22cb47173440eb5136e852a8ec38", url="https://pypi.org/packages/f1/1b/9bdf0a4bb9a9e5bd2cb96e88b112be6320051de34668fc0cbcb5dedcbd25/libensemble-0.9.0.tar.gz")
    version("0.8.0", sha256="1102e56c6381c9692de6888add23780ec69f18ad33f12119dc0391776a9a7300", url="https://pypi.org/packages/b2/26/f15ada935fb984ec49bb7eecdad088b7f62a33878f34f1355c917823e87a/libensemble-0.8.0.tar.gz")
    version("0.7.2", sha256="69b64304d1ecce4d57687ea6062f89bd813ae93b2a290bb1f595c5626ab6f197", url="https://pypi.org/packages/ed/10/37002791e4bf21e5d42ac6f356da23411f222edee612d763dbca8d22f575/libensemble-0.7.2.tar.gz")
    version("0.7.1", sha256="5cb294269624c1284ea25be9ed3bc668a2333e21e97a97b57ad339eb85435e46", url="https://pypi.org/packages/c1/b0/6884dea47900b5191d8c86b49d3d5cb1f87ac998c284c20b6cb0ee1f3fb2/libensemble-0.7.1.tar.gz")
    version("0.7.0", sha256="4c3c16ef3d4750b7a54198fae5d7ae402c5f5411ae85189da41afd20e20027dc", url="https://pypi.org/packages/17/88/3eaf19ded75a211fc6e49ea1d3d053ab6273cd51f2fde3892036697963d3/libensemble-0.7.0.tar.gz")
    version("0.6.0", sha256="3f6a926d3868da53835ed93fc2e2a047b368dacb648c7608ee3a66debcee4d38", url="https://pypi.org/packages/ee/61/aa81ede3c2a45f6828b9fcda68f84c152a9106f31cbd8ad3ef1f0f48ccf5/libensemble-0.6.0.tar.gz")
    version("0.5.2", sha256="3e36c29a4a2adc0984ecfcc998cb5bb8a2cdfbe7a1ae92f7b35b06e41d21b889", url="https://pypi.org/packages/b7/80/4abc923148ec71b5dfa5761c13b1ef92c7943f58debee3fdddeb481eceed/libensemble-0.5.2.tar.gz")
    version("0.5.1", sha256="522e0cc086a3ed75a101b704c0fe01eae07f2684bd8d6da7bdfe9371d3187362", url="https://pypi.org/packages/b9/b7/8429174292bac619333a69445914057432eaabd8d5c563efdfa8428ce25e/libensemble-0.5.1.tar.gz")
    version("0.5.0", sha256="c4623171dee049bfaa38a9c433609299a56b1afb774db8b71321247bc7556b8f", url="https://pypi.org/packages/f0/3e/900cb9888cab130b99a661945563b5eb75ccfbc683b8898ecbabea8f599e/libensemble-0.5.0.tar.gz")
    version("0.4.1", sha256="282c32ffb79d84cc80b5cc7043c202d5f0b8ebff10f63924752f092e3938db5e", url="https://pypi.org/packages/52/15/0fe09221a520da598113b7461d727206782c71bac38a08aa08d2dff1ab7e/libensemble-0.4.1.tar.gz")
    version("0.4.0", sha256="9384aa3a58cbc20bbd1c6fddfadb5e6a943d593a3a81c8665f030dbc6d76e76e", url="https://pypi.org/packages/34/db/fa2748caefae7d4efaaf0ec537cc0e79d65c65dd750ff94a4616673468cb/libensemble-0.4.0.tar.gz")
    version("0.3.0", sha256="c8efdf45d0da0ef6299ee778cea1c285c95972af70d3a729ee6dc855e66f9294", url="https://pypi.org/packages/c4/48/1830dbe7fcc8f5fef31283984df50fc55c93f18ac46f0d655e01d0890276/libensemble-0.3.0.tar.gz")
    version("0.2.0", sha256="ecac7275d4d0f4a5e497e5c9ef2cd998da82b2c020a0fb87546eeea262f495ff", url="https://pypi.org/packages/b1/73/bd3329cb1c558f1ba2c4bacf1aef6ec8851b71b7c581ba6091f502638b40/libensemble-0.2.0.tar.gz")
    version("0.1.0", sha256="0b27c59ae80f7af8b1bee92fcf2eb6c9a8fd3494bf2eb6b3ea17a7c03d3726bb", url="https://pypi.org/packages/38/25/541b860084b034a323615e8c6226e37225f8f255daea63f7a7d8d59440fc/libensemble-0.1.0.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    variant("deap", default=False, description="deap")
    variant("mpi", default=False, description="mpi")
    variant("mpmath", default=False, description="mpmath")
    variant("nlopt", default=False, description="nlopt")
    variant("petsc4py", default=False, description="petsc4py")
    variant("scipy", default=False, description="scipy")
    variant("tasmanian", default=False, description="tasmanian")
    # END VARIANTS

    # BEGIN DEPENDENCIES
    # END DEPENDENCIES

