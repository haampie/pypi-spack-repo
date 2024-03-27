##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyDocutils(PythonPackage):
    version("0.20.1", sha256="96f387a2c5562db4476f09f13bbab2192e764cac08ebbf3a34a95d9b1e4a59d6", url="https://pypi.org/packages/26/87/f238c0670b94533ac0353a4e2a1a771a0cc73277b88bff23d3ae35a256c1/docutils-0.20.1-py3-none-any.whl")
    version("0.20", sha256="a428f10de4de4774389734c986a01b4af2d802d26717108b0f1b9356862937c5", url="https://pypi.org/packages/41/3b/11740ed0f36e408ff3d5bd259af0c3330d899c17562f9964b7fbc90756f9/docutils-0.20-py3-none-any.whl")
    version("0.20-rc1", sha256="f9cd313159e9611199127c59b63c4890e808cb8cb6c2fe5f9a271cfd6df32676", url="https://pypi.org/packages/73/f1/455c0f5f29e853956947745299e65c494fe7ed49bce41fd05a738d931da3/docutils-0.20rc1-py3-none-any.whl")
    version("0.19", sha256="5e1de4d849fee02c63b040a4a3fd567f4ab104defd8a5511fbbc24a8a017efbc", url="https://pypi.org/packages/93/69/e391bd51bc08ed9141ecd899a0ddb61ab6465309f1eb470905c0c8868081/docutils-0.19-py3-none-any.whl")
    version("0.19-beta1", sha256="bf87502630148119873347981a8efc2438e6f254f995b7699501f0e4aa538915", url="https://pypi.org/packages/ac/f7/aec2c4e0acabe771b207ff2b480f2bc1adaef02771ff12f9561e66df33cf/docutils-0.19b1-py2.py3-none-any.whl")
    version("0.18.1", sha256="23010f129180089fbcd3bc08cfefccb3b890b0050e1ca00c867036e9d161b98c", url="https://pypi.org/packages/8d/14/69b4bad34e3f250afe29a854da03acb6747711f3df06c359fa053fae4e76/docutils-0.18.1-py2.py3-none-any.whl")
    version("0.18.1-beta0", sha256="6c9a32514c7aea91b507093d695e4fefcd68112237155ac8ab039962c6bc88bb", url="https://pypi.org/packages/6f/32/7d9d1acf3f725d2e00bfa1464db90723d8c1505b1c7cc547b4fdf0b87deb/docutils-0.18.1b0-py2.py3-none-any.whl")
    version("0.18", sha256="a31688b2ea858517fa54293e5d5df06fbb875fb1f7e4c64529271b77781ca8fc", url="https://pypi.org/packages/4c/42/5aefc2ffc563ef8456276430da8f045f55176c45746b0c3434c0c474c746/docutils-0.18-py2.py3-none-any.whl")
    version("0.18-beta1", sha256="3288f0fb1e18c681813b974db198f400afb0f5f35a2a5df1ee5c47ae6d47bf1e", url="https://pypi.org/packages/58/40/03275c077b2771e401d04702b16f7644717f484b9cf8425005f6eda1314a/docutils-0.18b1-py2.py3-none-any.whl")
    version("0.17.1", sha256="cf316c8370a737a022b72b56874f6602acf974a37a9fba42ec2876387549fc61", url="https://pypi.org/packages/4c/5e/6003a0d1f37725ec2ebd4046b657abb9372202655f96e76795dca8c0063c/docutils-0.17.1-py2.py3-none-any.whl")
    version("0.17.1-beta1", sha256="cc7828ebbce3ed8972076bf1607dac0d70717cba075b0816d46ae7e0dc64188b", url="https://pypi.org/packages/17/22/9e435091ff332c356b38b10235682e1d694901afeaff47a0bdf7d1d63562/docutils-0.17.1b1.dev0-py2.py3-none-any.whl")
    version("0.17", sha256="a71042bb7207c03d5647f280427f14bfbd1a65c9eb84f4b341d85fafb6bb4bdf", url="https://pypi.org/packages/9a/65/76aea825b59727b556cca74e28d68e4d73244d2e1e8a8945c29d6d3d5e11/docutils-0.17-py2.py3-none-any.whl")
    version("0.17-beta1", sha256="656d947c1a26d3fd75e731978c78331a93c326df270a8e1de5d19a560cb835f6", url="https://pypi.org/packages/d5/66/f2415daa484787060e88d6750f031ceb0dc9ffcab8e02d21b794f70a932d/docutils-0.17b1-py2.py3-none-any.whl")
    version("0.16", sha256="0c5b78adfbf7762415433f5515cd5c9e762339e23369dbe8000d84a4bf4ab3af", url="https://pypi.org/packages/81/44/8a15e45ffa96e6cf82956dd8d7af9e666357e16b0d93b253903475ee947f/docutils-0.16-py2.py3-none-any.whl")
    version("0.16-rc1", sha256="6dd0078bcfecbef00123531c6b0ca38460b291334ef8dd05c00e060e90ead6ce", url="https://pypi.org/packages/4d/a7/84b1d4a627bafcb2d9f5a5d896d03234122cc44b630ffbe9ec60cb346480/docutils-0.16rc1-py2.py3-none-any.whl")
    version("0.16-beta0", sha256="f1bad547016f945f7b35b28d8bead307821822ca3f8d4f87a1bd2ad1a8faab51", url="https://pypi.org/packages/74/40/0c46153ca7f9af1c0ccd001f9d774a831ef5f5ca687ce8fc1a83bc7e98d6/docutils-0.16b0.dev0-py2.py3-none-any.whl")
    version("0.15.2", sha256="a2aeea129088da402665e92e0b25b04b073c04b2dce4ab65caaa38b7ce2e1a99", url="https://pypi.org/packages/93/22/953e071b589b0b1fee420ab06a0d15e5aa0c7470eb9966d60393ce58ad61/docutils-0.15.2.tar.gz")
    version("0.15.1", sha256="f33ddb723332c6d6b6d99731ee1fc0c35eb4044a2df5cca1c64c8aa78eaf22cb", url="https://pypi.org/packages/d4/12/6c3fd74a590c7327c98cae008c11d536029fa9cd7924de477e8cb8804186/docutils-0.15.1-post1.tar.gz")
    version("0.15", sha256="54a349c622ff31c91cbec43b0b512f113b5b24daf00e2ea530bb1bd9aac14849", url="https://pypi.org/packages/72/0b/d728058694261c99fd5980419d77e1c4d63a390b26a6a0ea7f0993cd5c57/docutils-0.15.tar.gz")
    version("0.14", sha256="51e64ef2ebfb29cae1faa133b3710143496eca21c530f3f71424d77687764274", url="https://pypi.org/packages/84/f4/5771e41fdf52aabebbadecc9381d11dea0fa34e4759b4071244fa094804c/docutils-0.14.tar.gz")
    version("0.14-rc2", sha256="3caee0bcb2a49fdf24fcfa70849a60abb7a181aa68b030f7cb7494096181830c", url="https://pypi.org/packages/6b/57/6e68a5457ea9579f970d7854c090a6c991c8ab481df12e6be25ff505a4b0/docutils-0.14rc2.tar.gz")
    version("0.13.1", sha256="718c0f5fb677be0f34b781e04241c4067cbd9327b66bdd8e763201130f5175be", url="https://pypi.org/packages/05/25/7b5484aca5d46915493f1fd4ecb63c38c333bd32aa9ad6e19da8d08895ae/docutils-0.13.1.tar.gz")
    version("0.12", sha256="c7db717810ab6965f66c8cf0398a98c9d8df982da39b4cd7f162911eb89596fa", url="https://pypi.org/packages/37/38/ceda70135b9144d84884ae2fc5886c6baac4edea39550f28bcd144c1234d/docutils-0.12.tar.gz")
    version("0.11", sha256="9af4166adf364447289c5c697bb83c52f1d6f57e77849abcccd6a4a18a5e7ec9", url="https://pypi.org/packages/7f/49/3ff69dcb212900199462a291886e2f30f57ab3a69dc88e31eda6404a17c0/docutils-0.11.tar.gz")
    version("0.10", sha256="370624e61b6773da2f2fb17cc2a4eaea4bb596c3585d13f75ff193c1c738603e", url="https://pypi.org/packages/66/40/2b11ec2ec96d527ef933332a5847cc90860fd8bbee46da2cc468794ea25b/docutils-0.10.tar.gz")
    version("0.9.1", sha256="e89f187dbbc6674f839239c89fec44af9f18809b66a8a55a41b57b9ee2356994", url="https://pypi.org/packages/d1/fd/e569a6139d5bfda5574b3a4bd840dd1b23d03fc7fcbb193bd1f450f98cc4/docutils-0.9.1.tar.gz")


