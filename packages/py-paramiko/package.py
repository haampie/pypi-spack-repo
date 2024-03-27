##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyParamiko(PythonPackage):
    version("3.4.0", sha256="43f0b51115a896f9c00f59618023484cb3a14b98bbceab43394a39c6739b7ee7", url="https://pypi.org/packages/ad/50/8792484502c8141c20c996b802fefa8435a9c018a2bb440a06b172782118/paramiko-3.4.0-py3-none-any.whl")
    version("3.3.1", sha256="b7bc5340a43de4287bbe22fe6de728aa2c22468b2a849615498dd944c2f275eb", url="https://pypi.org/packages/bb/8f/3cef65d3fe76e59f320405027d594a0332e44852fef722f0ee4e81e2e7e3/paramiko-3.3.1-py3-none-any.whl")
    version("3.3.0", sha256="81d879b40a2f30ebad4befb842cbbcd70ffed4c2413f53729861cdb86e8afd7f", url="https://pypi.org/packages/55/62/6cf369c3faaba30287871af7754977770aa77a402e9850de5d2bc2542ec6/paramiko-3.3.0-py3-none-any.whl")
    version("3.2.0", sha256="df0f9dd8903bc50f2e10580af687f3015bf592a377cd438d2ec9546467a14eb8", url="https://pypi.org/packages/97/dc/d326721840be423d3728c1329be0c61a34ab3eec514f830c01fec31cd9ad/paramiko-3.2.0-py3-none-any.whl")
    version("3.1.0", sha256="f0caa660e797d9cd10db6fc6ae81e2c9b2767af75c3180fcd0e46158cd368d7f", url="https://pypi.org/packages/56/7c/9dd558ec0869fcecb661765d0a2504978dbfe85de24cbcccc847aa9b58e4/paramiko-3.1.0-py3-none-any.whl")
    version("3.0.0", sha256="6bef55b882c9d130f8015b9a26f4bd93f710e90fe7478b9dcc810304e79b3cd8", url="https://pypi.org/packages/ae/fe/3ab1540ee3f956fed7c738ac60b17586b3e57629a6b8f8dcbb790fca00c2/paramiko-3.0.0-py3-none-any.whl")
    version("2.12.0", sha256="b2df1a6325f6996ef55a8789d0462f5b502ea83b3c990cbb5bbe57345c6812c4", url="https://pypi.org/packages/71/6d/95777fd66507106d2f8f81d005255c237187951644f85a5bd0baeec8a88f/paramiko-2.12.0-py2.py3-none-any.whl")
    version("2.11.1", sha256="d9951c09e159d12fb0d69d6f45821d5e831bb44f51c613db59c304fdab13a65c", url="https://pypi.org/packages/26/df/e34ace16dcb337a2a2d3dc71d8658b7f20dedc9623933d34aad29c388dcb/paramiko-2.11.1-py2.py3-none-any.whl")
    version("2.11.0", sha256="655f25dc8baf763277b933dfcea101d636581df8d6b9774d1fb653426b72c270", url="https://pypi.org/packages/04/e5/39ec73dd4a8769d6759b8d6c60a1b2c9337f585407c2ae8bfb8ccb734278/paramiko-2.11.0-py2.py3-none-any.whl")
    version("2.10.6", sha256="02f07596062e4a81eacef10f9608d9a05f6f2485e50a1c3865ccf7b3b04138ad", url="https://pypi.org/packages/d7/9c/f1096f986c974d7297d9d56060a6e72933ec8227a3d72d1b78c96e8364e3/paramiko-2.10.6-py2.py3-none-any.whl")
    version("2.10.5", sha256="501c7bf79dd1d685ae045e3b28d5438b3aec92dafba517960e26e7e8ba68b4f6", url="https://pypi.org/packages/4f/97/886eddddd1b2d6f962bc3a2626ece907a1304e9ed1af72bea9022ff972fd/paramiko-2.10.5-py2.py3-none-any.whl")
    version("2.10.4", sha256="3c9ed6084f4b671ab66dc3c729092d32d96c3258f1426071301cb33654b09027", url="https://pypi.org/packages/e4/9e/dfb78fd52501cf2d8adf747373f9ebbe9d4ace3dfefb40640c570b8569f1/paramiko-2.10.4-py2.py3-none-any.whl")
    version("2.10.3", sha256="ac6593479f2b47a9422eca076b22cff9f795495e6733a64723efc75dd8c92101", url="https://pypi.org/packages/be/6f/f0ec5f5fb00d270ebd80946be561795c67468473eb495222794cae285d40/paramiko-2.10.3-py2.py3-none-any.whl")
    version("2.10.2", sha256="abf71533ea9332079db7cbcc039066c3d7575eed2df10766fa03496c3bf78cf1", url="https://pypi.org/packages/ad/c3/da7cd6cd7307160bd330735455b3066deed68c3b64de85a4235ac15e6a5c/paramiko-2.10.2-py2.py3-none-any.whl")
    version("2.10.1", sha256="f6cbd3e1204abfdbcd40b3ecbc9d32f04027cd3080fe666245e21e7540ccfc1b", url="https://pypi.org/packages/f0/0b/cee4e43d1f98ccb6567ca636dff936521e5430a4a2763c4aecc591b01a73/paramiko-2.10.1-py2.py3-none-any.whl")
    version("2.10.0", sha256="8543e214ccc9fbfd3199048932116e73213283c4942dd6011ba2812eccf62327", url="https://pypi.org/packages/a0/83/1639ffd310ae210af62696a165a0c2c862a0072aff9039e16441c14f900b/paramiko-2.10.0-py2.py3-none-any.whl")
    version("2.9.2", sha256="04097dbd96871691cdb34c13db1883066b8a13a0df2afd4cb0a92221f51c2603", url="https://pypi.org/packages/60/3e/84c52fb09db84548c5d366bac8863125c6db099b87495e04c8af5527e6f1/paramiko-2.9.2-py2.py3-none-any.whl")
    version("2.7.1", sha256="9c980875fa4d2cb751604664e9a2d0f69096643f5be4db1b99599fe114a97b2f", url="https://pypi.org/packages/06/1e/1e08baaaf6c3d3df1459fd85f0e7d2d6aa916f33958f151ee1ecc9800971/paramiko-2.7.1-py2.py3-none-any.whl")
    version("2.1.2", sha256="bdf239647e18b9b9ddbc2894fd1de9786b7a9144b1d19e32a5be3bb4bb63ae5d", url="https://pypi.org/packages/14/1e/2988f842e3194daf4d6e14e6e38e8d7085b2b45c669c3b635708c4a7618c/paramiko-2.1.2-py2.py3-none-any.whl")

    with default_args(type="run"):
        depends_on("py-bcrypt@3.2:", when="@3:")
        depends_on("py-bcrypt@3.1.3:", when="@2.2.1:2")
        depends_on("py-cryptography@3.3:", when="@3:")
        depends_on("py-cryptography@2.5:", when="@2.5:2")
        depends_on("py-cryptography@1.1:", when="@2:2.2")
        depends_on("py-pyasn1@0.1.7:", when="@2:2.4")
        depends_on("py-pynacl@1.5:", when="@3:")
        depends_on("py-pynacl@1.0.1:", when="@2.2:2")
        depends_on("py-six", when="@2.9.3:2")

