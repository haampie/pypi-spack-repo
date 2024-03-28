# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyWerkzeug(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("3.0.1", sha256="90a285dc0e42ad56b34e696398b8122ee4c681833fb35b8334a095d82c56da10", url="https://pypi.org/packages/c3/fc/254c3e9b5feb89ff5b9076a23218dafbc99c96ac5941e900b71206e6313b/werkzeug-3.0.1-py3-none-any.whl")
    version("3.0.0", sha256="cbb2600f7eabe51dbc0502f58be0b3e1b96b893b05695ea2b35b43d4de2d9962", url="https://pypi.org/packages/b6/a5/54b01f663d60d5334f6c9c87c26274e94617a4fd463d812463626423b10d/werkzeug-3.0.0-py3-none-any.whl")
    version("2.3.8", sha256="bba1f19f8ec89d4d607a3bd62f1904bd2e609472d93cd85e9d4e178f472c3748", url="https://pypi.org/packages/fd/21/0a674dfe66e9df9072c46269c882e9f901d36d987d8ea50ead033a9c1e01/werkzeug-2.3.8-py3-none-any.whl")
    version("2.3.7", sha256="effc12dba7f3bd72e605ce49807bbe692bd729c3bb122a3b91747a6ae77df528", url="https://pypi.org/packages/9b/59/a7c32e3d8d0e546a206e0552a2c04444544f15c1da4a01df8938d20c6ffc/werkzeug-2.3.7-py3-none-any.whl")
    version("2.3.6", sha256="935539fa1413afbb9195b24880778422ed620c0fc09670945185cce4d91a8890", url="https://pypi.org/packages/ba/d6/8040faecaba2feb84e1647af174b3243c9b90c163c7ea407820839931efe/Werkzeug-2.3.6-py3-none-any.whl")
    version("2.3.5", sha256="26c6a6a63a8a8d10a8d4e13e7f10821772ff5f138909262e89e946717c72b857", url="https://pypi.org/packages/46/f9/c25e781ee706fd9f487048b6b639836b0a3e22547c9591de1b77343e4031/Werkzeug-2.3.5-py3-none-any.whl")
    version("2.3.4", sha256="48e5e61472fee0ddee27ebad085614ebedb7af41e88f687aaf881afb723a162f", url="https://pypi.org/packages/c2/2f/f0dc628295bd23571c962d5a349307d9c8796a05bfca6571659eaded38e2/Werkzeug-2.3.4-py3-none-any.whl")
    version("2.3.3", sha256="4866679a0722de00796a74086238bb3b98d90f423f05de039abb09315487254a", url="https://pypi.org/packages/d1/3d/2f818de3e6f693f215f1de41604ab8fad5c215b1b18eec70a2cc5900ff6c/Werkzeug-2.3.3-py3-none-any.whl")
    version("2.3.2", sha256="b7b8bc1609f35ae8e45d48a9b58d7a4eb1e41eec148d37e977e5df6ebf3398b2", url="https://pypi.org/packages/80/b2/7b7467a8c766121d061bae61f378fc62726c49511c5c8ae435a76d146361/Werkzeug-2.3.2-py3-none-any.whl")
    version("2.3.1", sha256="69a4b8fcbb30a4c3fa81a5cebd961541273e4d222a4c08593b0b18312e14f64a", url="https://pypi.org/packages/9b/5a/6259e936ce9b9043293dd8473943f5e6bba244c2cb6e3e5354406dfb0700/Werkzeug-2.3.1-py3-none-any.whl")
    version("2.2.2", sha256="f979ab81f58d7318e064e99c4506445d60135ac5cd2e177a2de0089bfd4c9bd5", url="https://pypi.org/packages/c8/27/be6ddbcf60115305205de79c29004a0c6bc53cec814f733467b1bb89386d/Werkzeug-2.2.2-py3-none-any.whl")
    version("2.0.2", sha256="63d3dc1cf60e7b7e35e97fa9861f7397283b75d765afcaefd993d6046899de8f", url="https://pypi.org/packages/1e/73/51137805d1b8d97367a8a77cae4a792af14bb7ce58fbd071af294c740cf0/Werkzeug-2.0.2-py3-none-any.whl")
    version("0.16.1", sha256="1e0dedc2acb1f46827daa2e399c1485c8fa17c0d8e70b6b875b4e7f54bf408d2", url="https://pypi.org/packages/c2/e4/a859d2fe516f466642fa5c6054fd9646271f9da26b0cac0d2f37fc858c8f/Werkzeug-0.16.1-py2.py3-none-any.whl")
    version("0.16.0", sha256="e5f4a1f98b52b18a93da705a7458e55afb26f32bff83ff5d19189f92462d65c4", url="https://pypi.org/packages/ce/42/3aeda98f96e85fd26180534d36570e4d18108d62ae36f87694b476b83d6f/Werkzeug-0.16.0-py2.py3-none-any.whl")
    version("0.15.6", sha256="00d32beac38fcd48d329566f80d39f10ec2ed994efbecfb8dd4b320062d05902", url="https://pypi.org/packages/b7/61/c0a1adf9ad80db012ed7191af98fa05faa95fa09eceb71bb6fa8b66e6a43/Werkzeug-0.15.6-py2.py3-none-any.whl")
    version("0.15.5", sha256="87ae4e5b5366da2347eb3116c0e6c681a0e939a33b2805e2c0cbd282664932c4", url="https://pypi.org/packages/d1/ab/d3bed6b92042622d24decc7aadc8877badf18aeca1571045840ad4956d3f/Werkzeug-0.15.5-py2.py3-none-any.whl")
    version("0.15.4", sha256="865856ebb55c4dcd0630cdd8f3331a1847a819dda7e8c750d3db6f2aa6c0209c", url="https://pypi.org/packages/9f/57/92a497e38161ce40606c27a86759c6b92dd34fcdb33f64171ec559257c02/Werkzeug-0.15.4-py2.py3-none-any.whl")
    version("0.15.3", sha256="97660b282aa7e29f94f3fe378e5c7162d7ab9d601a8dbb1cbb2ffc8f0e54607d", url="https://pypi.org/packages/3d/bf/79101bd1d6a2b3fe0888e8d6e039800b173f26b7388308fc4bcc45de8d0a/Werkzeug-0.15.3-py2.py3-none-any.whl")
    version("0.15.2", sha256="7fad9770a8778f9576693f0cc29c7dcc36964df916b83734f4431c0e612a7fbc", url="https://pypi.org/packages/18/79/84f02539cc181cdbf5ff5a41b9f52cae870b6f632767e43ba6ac70132e92/Werkzeug-0.15.2-py2.py3-none-any.whl")
    version("0.15.1", sha256="96da23fa8ccecbc3ae832a83df5c722c11547d021637faacb0bec4dd2f4666c8", url="https://pypi.org/packages/24/4d/2fc4e872fbaaf44cc3fd5a9cd42fda7e57c031f08e28c9f35689e8b43198/Werkzeug-0.15.1-py2.py3-none-any.whl")
    version("0.15.0", sha256="ee11b0f0640c56fb491b43b38356c4b588b3202b415a1e03eacf1c5561c961cf", url="https://pypi.org/packages/29/5e/d54398f8ee78166d2cf07e46d19096e55aba506e44de998a1ad85b83ec8d/Werkzeug-0.15.0-py2.py3-none-any.whl")
    version("0.14.1", sha256="d5da73735293558eb1651ee2fddc4d0dedcfa06538b8813a2e20011583c9e49b", url="https://pypi.org/packages/20/c4/12e3e56473e52375aa29c4764e70d1b8f3efa6682bef8d0aae04fe335243/Werkzeug-0.14.1-py2.py3-none-any.whl")
    version("0.12.2", sha256="e8549c143af3ce6559699a01e26fa4174f4c591dbee0a499f3cd4c3781cdec3d", url="https://pypi.org/packages/97/02/306e0d57fdbf467ec1c763bc1757ec6ba20b1332e0ea7e49111533d71d1c/Werkzeug-0.12.2-py2.py3-none-any.whl")
    version("0.11.15", sha256="c6f6f89124df0514d886782c658c3e12f2caaa94da34cee3fd82eebf4ebf052b", url="https://pypi.org/packages/ef/c6/3c431fea5f93c8bc869ec9c7bdad9ffef4ff9c81bfe1d294217447206c46/Werkzeug-0.11.15-py2.py3-none-any.whl")
    version("0.11.11", sha256="eb3108af06aed08fb2f4fc883f2adf04c8f4997f6368517591b2becf15ae0da2", url="https://pypi.org/packages/a9/5e/41f791a3f380ec50f2c4c3ef1399d9ffce6b4fe9a7f305222f014cf4fe83/Werkzeug-0.11.11-py2.py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-markupsafe@2.1.1:", when="@2.2:")
    # END DEPENDENCIES

