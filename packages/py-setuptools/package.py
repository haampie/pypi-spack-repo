# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PySetuptools(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("69.2.0", sha256="c21c49fb1042386df081cb5d86759792ab89efca84cf114889191cd09aacc80c", url="https://pypi.org/packages/92/e1/1c8bb3420105e70bdf357d57dd5567202b4ef8d27f810e98bb962d950834/setuptools-69.2.0-py3-none-any.whl")
    version("69.1.1", sha256="02fa291a0471b3a18b2b2481ed902af520c69e8ae0919c13da936542754b4c56", url="https://pypi.org/packages/c0/7a/3da654f49c95d0cc6e9549a855b5818e66a917e852ec608e77550c8dc08b/setuptools-69.1.1-py3-none-any.whl")
    version("69.0.3", sha256="385eb4edd9c9d5c17540511303e39a147ce2fc04bc55289c322b9e5904fe2c05", url="https://pypi.org/packages/55/3a/5121b58b578a598b269537e09a316ad2a94fdd561a2c6eb75cd68578cc6b/setuptools-69.0.3-py3-none-any.whl")
    version("68.2.2", sha256="b454a35605876da60632df1a60f736524eb73cc47bbc9f3f1ef1b644de74fd2a", url="https://pypi.org/packages/bb/26/7945080113158354380a12ce26873dd6c1ebd88d47f5bc24e2c5bb38c16a/setuptools-68.2.2-py3-none-any.whl")
    version("68.0.0", sha256="11e52c67415a381d10d6b462ced9cfb97066179f0e871399e006c4ab101fc85f", url="https://pypi.org/packages/c7/42/be1c7bbdd83e1bfb160c94b9cafd8e25efc7400346cf7ccdbdb452c467fa/setuptools-68.0.0-py3-none-any.whl")
    version("67.6.0", sha256="b78aaa36f6b90a074c1fa651168723acbf45d14cb1196b6f02c0fd07f17623b2", url="https://pypi.org/packages/c3/9e/8a7ba2c9984a060daa6c6f9fff4d576b7ace3936239d6b771541eab972ed/setuptools-67.6.0-py3-none-any.whl")
    version("65.5.0", sha256="f62ea9da9ed6289bfe868cd6845968a2c854d1427f8548d52cae02a42b4f0356", url="https://pypi.org/packages/41/82/7f54bbfe5c247a8c9f78d8d1d7c051847bcb78843c397b866dba335c1e88/setuptools-65.5.0-py3-none-any.whl")
    version("65.0.0", sha256="fe9a97f68b064a6ddd4bacfb0b4b93a4c65a556d97ce906255540439d0c35cef", url="https://pypi.org/packages/a2/dd/d8cdd14320106ff58d4eb6e6553bae7a822e174ad5b05db486332d50d4ec/setuptools-65.0.0-py3-none-any.whl")
    version("64.0.0", sha256="63f463b90ff5e0a1422010100268fd688e15c44ae0798659013c8412963e15e4", url="https://pypi.org/packages/3e/83/e206edff58159a927c76bbfeef1bf8b39cb12bbb32ae3c6227deb16d0121/setuptools-64.0.0-py3-none-any.whl")
    version("63.4.3", sha256="7f61f7e82647f77d4118eeaf43d64cbcd4d87e38af9611694d4866eb070cd10d", url="https://pypi.org/packages/2a/a3/49c29680d6118273b992b40ebe881e8e899b8e26a4e951f37f223da8f862/setuptools-63.4.3-py3-none-any.whl")
    version("63.0.0", sha256="045aec56a3eee5c82373a70e02db8b6da9a10f7faf61ff89a14ab66c738ed370", url="https://pypi.org/packages/df/80/4620a4849ed16c5b0498963e3180d2c3e649660191f8d7d9be5a4bc8a773/setuptools-63.0.0-py3-none-any.whl")
    version("62.6.0", sha256="c1848f654aea2e3526d17fc3ce6aeaa5e7e24e66e645b5be2171f3f6b4e5a178", url="https://pypi.org/packages/e9/86/b2ede1d87122a6d4da86d84cc35d0e48b4aa2476e4281d06101c772c1961/setuptools-62.6.0-py3-none-any.whl")
    version("62.4.0", sha256="5a844ad6e190dccc67d6d7411d119c5152ce01f7c76be4d8a1eaa314501bba77", url="https://pypi.org/packages/d0/12/412167a1f80290555c557a556fb1fc294a6e889924fcf2b2db3a789b11a4/setuptools-62.4.0-py3-none-any.whl")
    version("62.3.2", sha256="68e45d17c9281ba25dc0104eadd2647172b3472d9e01f911efa57965e8d51a36", url="https://pypi.org/packages/e9/1c/ec080fde54ab30a738c92f794eab7f5d2f354f2b619ee95b2efe353e0766/setuptools-62.3.2-py3-none-any.whl")
    version("59.4.0", sha256="feb5ff19b354cde9efd2344ef6d5e79880ce4be643037641b49508bbb850d060", url="https://pypi.org/packages/6f/ea/e12311dabc63a6a434be25e6011c1513cc95d0cf22e5f13036f75b3ec508/setuptools-59.4.0-py3-none-any.whl")
    version("58.2.0", sha256="2551203ae6955b9876741a26ab3e767bb3242dafe86a32a749ea0d78b6792f11", url="https://pypi.org/packages/41/f4/a7ca4859317232b1efb64a826b8d2d7299bb77fb60bdb08e2bd1d61cf80d/setuptools-58.2.0-py3-none-any.whl")
    version("57.4.0", sha256="a49230977aa6cfb9d933614d2f7b79036e9945c4cdd7583163f4e920b83418d6", url="https://pypi.org/packages/bd/25/5bdf7f1adeebd4e3fa76b2e2f045ae53ee208e40a4231ad0f0c3007e4353/setuptools-57.4.0-py3-none-any.whl")
    version("57.1.0", sha256="ddae4c1b9220daf1e32ba9d4e3714df6019c5b583755559be84ff8199f7e1fe3", url="https://pypi.org/packages/a2/e1/902fbc2f61ad6243cd3d57ffa195a9eb123021ec912ec5d811acf54a39f8/setuptools-57.1.0-py3-none-any.whl")
    version("51.0.0", sha256="8c177936215945c9a37ef809ada0fab365191952f7a123618432bbfac353c529", url="https://pypi.org/packages/3d/f2/1489d3b6c72d68bf79cd0fba6b6c7497df4ebf7d40970e2d7eceb8d0ea9c/setuptools-51.0.0-py3-none-any.whl")
    version("50.3.2", sha256="2c242a0856fbad7efbe560df4a7add9324f340cf48df43651e9604924466794a", url="https://pypi.org/packages/6d/38/c21ef5034684ffc0412deefbb07d66678332290c14bb5269c85145fbd55e/setuptools-50.3.2-py3-none-any.whl")
    version("50.1.0", sha256="4537c77e6e7dc170081f8547564551d4ff4e4999717434e1257600bbd3a23296", url="https://pypi.org/packages/35/f7/f86e670ebd628f447845798aa3b6a1b6da235941a1591d664d718aac171c/setuptools-50.1.0-py3-none-any.whl")
    version("49.6.0", sha256="4dd5bb0a0a0cff77b46ca5dd3a84857ee48c83e8223886b556613c724994073f", url="https://pypi.org/packages/c3/a9/5dc32465951cf4812e9e93b4ad2d314893c2fa6d5f66ce5c057af6e76d85/setuptools-49.6.0-py3-none-any.whl")
    version("49.2.0", sha256="272c7f48f5cddc5af5901f4265274c421c7eede5c8bc454ac2903d3f8fc365e9", url="https://pypi.org/packages/8e/11/9e10f1cad4518cb307b484c255cae61e97f05b82f6d536932b1714e01b47/setuptools-49.2.0-py3-none-any.whl")
    version("46.1.3", sha256="4fe404eec2738c20ab5841fa2d791902d2a645f32318a7850ef26f8d7215a8ee", url="https://pypi.org/packages/a0/df/635cdb901ee4a8a42ec68e480c49f85f4c59e8816effbf57d9e6ee8b3588/setuptools-46.1.3-py3-none-any.whl")
    version("44.1.1", sha256="27a714c09253134e60a6fa68130f78c7037e5562c4f21f8f318f2ae900d152d5", url="https://pypi.org/packages/e1/b7/182161210a13158cd3ccc41ee19aadef54496b74f2817cc147006ec932b4/setuptools-44.1.1-py2.py3-none-any.whl")
    version("44.1.0", sha256="992728077ca19db6598072414fb83e0a284aca1253aaf2e24bb1e55ee6db1a30", url="https://pypi.org/packages/ab/b5/3679d7c98be5b65fa5522671ef437b792d909cf3908ba54fe9eca5d2a766/setuptools-44.1.0-py2.py3-none-any.whl")
    version("43.0.0", sha256="a67faa51519ef28cd8261aff0e221b6e4c370f8fb8bada8aa3e7ad8945199963", url="https://pypi.org/packages/91/af/18d58ed8a8e7e6b91d71b0367034faf8ea41e1004018811388ed07a7f2d6/setuptools-43.0.0-py2.py3-none-any.whl")
    version("41.4.0", sha256="8d01f7ee4191d9fdcd9cc5796f75199deccb25b154eba82d44d6a042cf873670", url="https://pypi.org/packages/6a/9a/50fadfd53ec909e4399b67c74cc7f4e883488035cfcdb90b685758fa8b34/setuptools-41.4.0-py2.py3-none-any.whl")
    version("41.3.0", sha256="e9832acd9be6f3174f4c34b40e7d913a146727920cbef6465c1c1bd2d21a4ec4", url="https://pypi.org/packages/84/14/d7aefed8d7d3c9eae31c43b830421afe4640f127daee2a193f7b7e6e5c88/setuptools-41.3.0-py2.py3-none-any.whl")
    version("41.0.1", sha256="c7769ce668c7a333d84e17fe8b524b1c45e7ee9f7908ad0a73e1eda7e6a5aebf", url="https://pypi.org/packages/ec/51/f45cea425fd5cb0b0380f5b0f048ebc1da5b417e48d304838c02d6288a1e/setuptools-41.0.1-py2.py3-none-any.whl")
    version("41.0.0", sha256="e67486071cd5cdeba783bd0b64f5f30784ff855b35071c8670551fd7fc52d4a1", url="https://pypi.org/packages/c8/b0/cc6b7ba28d5fb790cf0d5946df849233e32b8872b6baca10c9e002ff5b41/setuptools-41.0.0-py2.py3-none-any.whl")
    version("40.8.0", sha256="e8496c0079f3ac30052ffe69b679bd876c5265686127a3159cfa415669b7f9ab", url="https://pypi.org/packages/d1/6a/4b2fcefd2ea0868810e92d519dacac1ddc64a2e53ba9e3422c3b62b378a6/setuptools-40.8.0-py2.py3-none-any.whl")
    version("40.4.3", sha256="ce4137d58b444bac11a31d4e0c1805c69d89e8ed4e91fde1999674ecc2f6f9ff", url="https://pypi.org/packages/96/06/c8ee69628191285ddddffb277bd5abdf769166e7a14b867c2a172f0175b1/setuptools-40.4.3-py2.py3-none-any.whl")
    version("40.2.0", sha256="ea3796a48a207b46ea36a9d26de4d0cc87c953a683a7b314ea65d666930ea8e6", url="https://pypi.org/packages/66/e8/570bb5ca88a8bcd2a1db9c6246bb66615750663ffaaeada95b04ffe74e12/setuptools-40.2.0-py2.py3-none-any.whl")
    version("39.2.0", sha256="8fca9275c89964f13da985c3656cb00ba029d7f3916b37990927ffdf264e7926", url="https://pypi.org/packages/7f/e1/820d941153923aac1d49d7fc37e17b6e73bfbd2904959fffbad77900cf92/setuptools-39.2.0-py2.py3-none-any.whl")
    version("39.0.1", sha256="8010754433e3211b9cdbbf784b50f30e80bf40fc6b05eb5f865fab83300599b8", url="https://pypi.org/packages/20/d7/04a0b689d3035143e2ff288f4b9ee4bf6ed80585cc121c90bfd85a1a8c2e/setuptools-39.0.1-py2.py3-none-any.whl")
    version("25.2.0", sha256="2845247c359bb91097ccf8f6be8a69edfa44847f3d2d5def39aa43c3d7f615ca", url="https://pypi.org/packages/9b/81/5258d4928d2ba039c98f8175e6c3d3995814b9449b57802be9d71e37c944/setuptools-25.2.0-py2.py3-none-any.whl")
    version("20.7.0", sha256="8917a52aa3a389893221b173a89dae0471022d32bff3ebc31a1072988aa8039d", url="https://pypi.org/packages/73/73/57576f40b4d87a4f8d0fba656469d05559910337d852bc513ff34f47bdc8/setuptools-20.7.0-py2.py3-none-any.whl")
    version("20.6.7", sha256="9982ee4d279a2541dc1a7efee994ff9c535cfc05315e121e09df7f93da48c442", url="https://pypi.org/packages/45/11/e67731adbe045d384dabb5de73b900db57f37a1399bfd9ef12dcae4b35b9/setuptools-20.6.7-py2.py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("python@3.8:", when="@68.1:")
        depends_on("python@3.7:", when="@59.7:68.0")
    # END DEPENDENCIES

