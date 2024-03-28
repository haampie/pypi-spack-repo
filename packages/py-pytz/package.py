# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPytz(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("2024.1", sha256="328171f4e3623139da4983451950b28e95ac706e13f3f2630a879749e7a8b319", url="https://pypi.org/packages/9c/3d/a121f284241f08268b21359bd425f7d4825cffc5ac5cd0e1b3d82ffd2b10/pytz-2024.1-py2.py3-none-any.whl")
    version("2023.4", sha256="f90ef520d95e7c46951105338d918664ebfd6f1d995bd7d153127ce90efafa6a", url="https://pypi.org/packages/3b/dd/9b84302ba85ac6d3d3042d3e8698374838bde1c386b4adb1223d7a0efd4e/pytz-2023.4-py2.py3-none-any.whl")
    version("2023.3.post1", sha256="ce42d816b81b68506614c11e8937d3aa9e41007ceb50bfdcb0749b921bf646c7", url="https://pypi.org/packages/32/4d/aaf7eff5deb402fd9a24a1449a8119f00d74ae9c2efa79f8ef9994261fc2/pytz-2023.3.post1-py2.py3-none-any.whl")
    version("2023.3", sha256="a151b3abb88eda1d4e34a9814df37de2a80e301e68ba0fd856fb9b46bfbbbffb", url="https://pypi.org/packages/7f/99/ad6bd37e748257dd70d6f85d916cafe79c0b0f5e2e95b11f7fbc82bf3110/pytz-2023.3-py2.py3-none-any.whl")
    version("2023.2", sha256="8a8baaf1e237175b02f5c751eea67168043a749c843989e2b3015aa1ad9db68b", url="https://pypi.org/packages/a3/21/0ffac8dacd94d20f4d1ceaaa91cf28ad94ec22e8f3ec9056976f1066ff24/pytz-2023.2-py2.py3-none-any.whl")
    version("2022.7.1", sha256="78f4f37d8198e0627c5f1143240bb0206b8691d8d7ac6d78fee88b78733f8c4a", url="https://pypi.org/packages/2e/09/fbd3c46dce130958ee8e0090f910f1fe39e502cc5ba0aadca1e8a2b932e5/pytz-2022.7.1-py2.py3-none-any.whl")
    version("2022.7", sha256="93007def75ae22f7cd991c84e02d434876818661f8df9ad5df9e950ff4e52cfd", url="https://pypi.org/packages/3d/19/4de17f0d5cf5a0d87aa67532d4c2fa75e6e7d8df13c27635ff40fa6f4b76/pytz-2022.7-py2.py3-none-any.whl")
    version("2022.6", sha256="222439474e9c98fced559f1709d89e6c9cbf8d79c794ff3eb9f8800064291427", url="https://pypi.org/packages/85/ac/92f998fc52a70afd7f6b788142632afb27cd60c8c782d1452b7466603332/pytz-2022.6-py2.py3-none-any.whl")
    version("2022.5", sha256="335ab46900b1465e714b4fda4963d87363264eb662aab5e65da039c25f1f5b22", url="https://pypi.org/packages/b5/d7/91fd8911d22e7fac794803095dd192bf1ebd70c7603272085230d915e738/pytz-2022.5-py2.py3-none-any.whl")
    version("2022.4", sha256="2c0784747071402c6e99f0bafdb7da0fa22645f06554c7ae06bf6358897e9c91", url="https://pypi.org/packages/d8/66/309545413162bc8271c73e622499a41cdc37217b499febe26155ff9f93ed/pytz-2022.4-py2.py3-none-any.whl")
    version("2022.2.1", sha256="220f481bdafa09c3955dfbdddb7b57780e9a94f5127e35456a48589b9e0c0197", url="https://pypi.org/packages/d5/50/54451e88e3da4616286029a3a17fc377de817f66a0f50e1faaee90161724/pytz-2022.2.1-py2.py3-none-any.whl")
    version("2022.2", sha256="d9b245e63af49c4e51afdec5402f56b99c0cb483a84a12bb8b7db980386baade", url="https://pypi.org/packages/67/31/3a5547f8b077b6b2b5c2b953d126e1cfcf40c2655d51242839014583a987/pytz-2022.2-py2.py3-none-any.whl")
    version("2022.1", sha256="e68985985296d9a66a881eb3193b0906246245294a881e7c8afe623866ac6a5c", url="https://pypi.org/packages/60/2e/dec1cc18c51b8df33c7c4d0a321b084cf38e1733b98f9d15018880fb4970/pytz-2022.1-py2.py3-none-any.whl")
    version("2021.3", sha256="3672058bc3453457b622aab7a1c3bfd5ab0bdae451512f6cf25f64ed37f5b87c", url="https://pypi.org/packages/d3/e3/d9f046b5d1c94a3aeab15f1f867aa414f8ee9d196fae6865f1d6a0ee1a0b/pytz-2021.3-py2.py3-none-any.whl")
    version("2021.1", sha256="eb10ce3e7736052ed3623d49975ce333bcd712c7bb19a58b9e2089d4057d0798", url="https://pypi.org/packages/70/94/784178ca5dd892a98f113cdd923372024dc04b8d40abe77ca76b5fb90ca6/pytz-2021.1-py2.py3-none-any.whl")
    version("2020.1", sha256="a494d53b6d39c3c6e44c3bec237336e14305e4f29bbf800b599253057fbb79ed", url="https://pypi.org/packages/4f/a4/879454d49688e2fad93e59d7d4efda580b783c745fd2ec2a3adf87b0808d/pytz-2020.1-py2.py3-none-any.whl")
    version("2019.3", sha256="1c557d7d0e871de1f5ccd5833f60fb2550652da6be2693c1e02300743d21500d", url="https://pypi.org/packages/e7/f9/f0b53f88060247251bf481fa6ea62cd0d25bf1b11a87888e53ce5b7c8ad2/pytz-2019.3-py2.py3-none-any.whl")
    version("2019.2", sha256="c894d57500a4cd2d5c71114aaab77dbab5eabd9022308ce5ac9bb93a60a6f0c7", url="https://pypi.org/packages/87/76/46d697698a143e05f77bec5a526bf4e56a0be61d63425b68f4ba553b51f2/pytz-2019.2-py2.py3-none-any.whl")
    version("2019.1", sha256="303879e36b721603cc54604edcac9d20401bdbe31e1e4fdee5b9f98d5d31dfda", url="https://pypi.org/packages/3d/73/fe30c2daaaa0713420d0382b16fbb761409f532c56bdcc514bf7b6262bb6/pytz-2019.1-py2.py3-none-any.whl")
    version("2018.9", sha256="32b0891edff07e28efe91284ed9c31e123d84bea3fd98e1f72be2508f43ef8d9", url="https://pypi.org/packages/61/28/1d3920e4d1d50b19bc5d24398a7cd85cc7b9a75a490570d5a30c57622d34/pytz-2018.9-py2.py3-none-any.whl")
    version("2018.7", sha256="8e0f8568c118d3077b46be7d654cc8167fa916092e28320cde048e54bfc9f1e6", url="https://pypi.org/packages/f8/0e/2365ddc010afb3d79147f1dd544e5ee24bf4ece58ab99b16fbb465ce6dc0/pytz-2018.7-py2.py3-none-any.whl")
    version("2018.6", sha256="91e3ccf2c344ffaa6defba1ce7f38f97026943f675b7703f44789768e4cb0ece", url="https://pypi.org/packages/52/8b/876c5745f617630be90cfb8fafe363c6d7204b176dc707d1805d1e9a0a35/pytz-2018.6-py2.py3-none-any.whl")
    version("2018.5", sha256="a061aa0a9e06881eb8b3b2b43f05b9439d6583c206d0a6c340ff72a7b6669053", url="https://pypi.org/packages/30/4e/27c34b62430286c6d59177a0842ed90dc789ce5d1ed740887653b898779a/pytz-2018.5-py2.py3-none-any.whl")
    version("2018.4", sha256="65ae0c8101309c45772196b21b74c46b2e5d11b6275c45d251b150d5da334555", url="https://pypi.org/packages/dc/83/15f7833b70d3e067ca91467ca245bae0f6fe56ddc7451aa0dc5606b120f2/pytz-2018.4-py2.py3-none-any.whl")
    version("2018.3", sha256="07edfc3d4d2705a20a6e99d97f0c4b61c800b8232dc1c04d87e8554f130148dd", url="https://pypi.org/packages/3c/80/32e98784a8647880dedf1f6bf8e2c91b195fe18fdecc6767dcf5104598d6/pytz-2018.3-py2.py3-none-any.whl")
    version("2017.3", sha256="c41c62827ce9cafacd6f2f7018e4f83a6f1986e87bfd000b8cfbd4ab5da95f1a", url="https://pypi.org/packages/a3/7f/e7d1acbd433b929168a4fb4182a2ff3c33653717195a26c1de099ad1ef29/pytz-2017.3-py2.py3-none-any.whl")
    version("2016.10", sha256="a1ea35e87a63c7825846d5b5c81d23d668e8a102d3b1b465ce95afe1b3a2e065", url="https://pypi.org/packages/f5/fa/4a9aefc206aa49a4b5e0a72f013df1f471b4714cdbe6d78f0134feeeecdb/pytz-2016.10-py2.py3-none-any.whl")
    version("2016.6.1", sha256="7833bf559800232d3965b70e69642ebdadc76f7988f8d0a1440e072193ecd949", url="https://pypi.org/packages/ba/c7/3d54cad4fb6cf7bf375d39771e67680ec779a541c68459210fcfdc3ba952/pytz-2016.6.1-py2.py3-none-any.whl")
    version("2016.3", sha256="2e4859a1c1b5c77bdc247013332ae1edbd5b3a7fb3737e33c5f26efcf5e150fb", url="https://pypi.org/packages/e2/87/e774b15dd6468889e5268ebbc00040c9f9da546c462099c4d43e14697e04/pytz-2016.3-py2.py3-none-any.whl")
    version("2015.4", sha256="4d64ed1b9e0e73095f5cfa87f0e97ddb4c840049e8efeb7e63b46118ba1d623a", url="https://pypi.org/packages/2d/cb/c9b0c9e4cf54bc3517b2d52904c9f328be2e88cf07392fea51ee0c3c4b28/pytz-2015.4-py2.py3-none-any.whl")
    version("2014.10", sha256="5438d749e923c914741fe2a410b528abe27053000fbf878bc437428d08ae0ab1", url="https://pypi.org/packages/c5/bc/995a7472f9ca49980ce07ca7a68b0b7c01bc87fc7f9f09707cbfde282a8f/pytz-2014.10-py2.py3-none-any.whl")
    version("2014.9", sha256="431c78bcf827c92a19d7829cd9ae7902d52d6dfcb23d98904fc807ddea1ec076", url="https://pypi.org/packages/2a/de/7c55dffb7464509aee814047f50490886925226846bcb8c622677619f15e/pytz-2014.9-py2.py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    # END DEPENDENCIES

