##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyArrow(PythonPackage):
    version("1.3.0", sha256="c728b120ebc00eb84e01882a6f5e7927a53960aa990ce7dd2b10f39005a67f80", url="https://pypi.org/packages/f8/ed/e97229a566617f2ae958a6b13e7cc0f585470eac730a73e9e82c32a3cdd2/arrow-1.3.0-py3-none-any.whl")
    version("1.2.3", sha256="5a49ab92e3b7b71d96cd6bfcc4df14efefc9dfa96ea19045815914a6ab6b1fe2", url="https://pypi.org/packages/67/67/4bca5a595e2f89bff271724ddb1098e6c9e16f7f3d018d120255e3c30313/arrow-1.2.3-py3-none-any.whl")
    version("1.2.2", sha256="d622c46ca681b5b3e3574fcb60a04e5cc81b9625112d5fb2b44220c36c892177", url="https://pypi.org/packages/36/e7/3043959c8e3e3d6e346b69417e85daa591f9c018b99c383cc3f316bbf269/arrow-1.2.2-py3-none-any.whl")
    version("1.2.1", sha256="6b2914ef3997d1fd7b37a71ce9dd61a6e329d09e1c7b44f4d3099ca4a5c0933e", url="https://pypi.org/packages/f4/97/a6b394b0ee6c9a7f645308f3a205c6cfe4fc804aac1bf29e4aebb5cd5a16/arrow-1.2.1-py3-none-any.whl")
    version("1.2.0", sha256="8fb7d9d3d4bf90e49e734c22fa077bdd0964135c4b8120de2510575a8d1f620c", url="https://pypi.org/packages/d8/bd/9f0a4308b6b898c78dcbee4268b630c9a45922439043d45e608db6919e69/arrow-1.2.0-py3-none-any.whl")
    version("1.1.1", sha256="77a60a4db5766d900a2085ce9074c5c7b8e2c99afeaa98ad627637ff6f292510", url="https://pypi.org/packages/e8/59/4c21f8c501b43e2aabc82ad62e20f3730c273057c56f8731319980dec5ff/arrow-1.1.1-py3-none-any.whl")
    version("1.1.0", sha256="8cbe6a629b1c54ae11b52d6d9e70890089241958f63bc59467e277e34b7a5378", url="https://pypi.org/packages/e3/3a/dcb889af8de025f1fca9afd47f52726e24f4bc10aab3bc88a609cdd30250/arrow-1.1.0-py3-none-any.whl")
    version("1.0.3", sha256="3515630f11a15c61dcb4cdd245883270dd334c83f3e639824e65a4b79cc48543", url="https://pypi.org/packages/ea/22/482a480cbee1aa7795a58b411159a4df249d6d4ceacdd9987ab946f78210/arrow-1.0.3-py3-none-any.whl")
    version("1.0.2", sha256="cb1b7bc3a07eb1c1e98ccc740627460c9891636642bcf03c4097b71d8bc5ca1d", url="https://pypi.org/packages/60/14/eb71fc7e91384f2890405aca8b4b23e1adb725cb68beb456ae5898a99ac8/arrow-1.0.2-py3-none-any.whl")
    version("1.0.1", sha256="b1e106a0ab754e540f4aeb08747900830b688adef02d81240e65afc0e781a870", url="https://pypi.org/packages/84/e5/30f4ba280b2ae9931fa34f6aa9b5c4a9fed3f191764c0a05658b25a8ef78/arrow-1.0.1-py3-none-any.whl")
    version("0.16.0", sha256="98184d8dd3e5d30b96c2df4596526f7de679ccb467f358b82b0f686436f3a6b8", url="https://pypi.org/packages/ed/d2/aa994f2d8dd442113c753041761dc0732a35def05538de48f61adb28642a/arrow-0.16.0-py2.py3-none-any.whl")
    version("0.14.7", sha256="4bfacea734ead51495dc47df00421ecfd4ca1f2c0fbe58b9a26eaeddedc31caf", url="https://pypi.org/packages/b9/26/aff20e20eb4fc8f9cbe60434494b53b8cc327062585517461bfdff76125f/arrow-0.14.7-py2.py3-none-any.whl")
    version("0.14.6", sha256="8c53fad4e723a56c02d8df75fd7a879800148d6e51df4713f91502e70a65e1be", url="https://pypi.org/packages/05/f0/b1361311c875d7fad394b9f45044206338bead0efecf0aaa6db19cf47830/arrow-0.14.6-py2.py3-none-any.whl")
    version("0.14.5", sha256="a12de0124d812d15061ed36c7eb4a421fa1b95026a502a0b2062e9ea00fc4446", url="https://pypi.org/packages/4f/c6/32df2c68e02e2d6b4457223fa499634edabb2d4ff74f00087ffff49b4be4/arrow-0.14.5-py2.py3-none-any.whl")
    version("0.14.4", sha256="157dee94b557ffe9a2e13e05669bf48820064cb37d416f547f59baa0d25301d4", url="https://pypi.org/packages/b1/53/f39e3df45e4c5dc1b53e08b5445ff1da869ab5b50d7e58db8bb5341478ef/arrow-0.14.4-py2.py3-none-any.whl")
    version("0.14.3", sha256="33eb1599b93466daa5aba34a70b2507dbe2ce37a5b4cf23608ff2b7d52846132", url="https://pypi.org/packages/79/5b/025ac969a21ef46f40244859a83cf6e25b7d0ffa40bcd47194c9c7856688/arrow-0.14.3-py2.py3-none-any.whl")
    version("0.14.2", sha256="41be7ea4c53c2cf57bf30f2d614f60c411160133f7a0a8c49111c30fb7e725b5", url="https://pypi.org/packages/0e/29/a080c566b078dd72ac486991c94ec2f3dd508ac9ec8c254c9dbe30dcfbb2/arrow-0.14.2.tar.gz")
    version("0.14.1", sha256="2d30837085011ef0b90ff75aa0a28f5c7d063e96b7e76b6cbc7e690310256685", url="https://pypi.org/packages/90/7f/7fd8accc23aa507d215b5f07b509661c31583010d8276ba844896ee1f44b/arrow-0.14.1.tar.gz")
    version("0.14.0", sha256="f1837ac68cc954fd910b24c9f998172d1b430b0b255e875e9d190a16463e85e1", url="https://pypi.org/packages/a0/3b/0b5c7771a619ee4eae1f894669dd5f7c0aae9c92d87891c4c746937f9cc4/arrow-0.14.0.tar.gz")
    version("0.13.2", sha256="82dd5e13b733787d4eb0fef42d1ee1a99136dc1d65178f70373b3678b3181bfc", url="https://pypi.org/packages/3e/f3/2610612fb6653d85043f1c32ee4bd99350909a9c005204f2cc448f1c88fb/arrow-0.13.2.tar.gz")
    version("0.13.1", sha256="6f54d9f016c0b7811fac9fb8c2c7fa7421d80c54dbdd75ffb12913c55db60b8a", url="https://pypi.org/packages/56/7b/1131861f7f6c56551eb943df4252357e5aad4ff1310f0ddd950a0b99f4ff/arrow-0.13.1.tar.gz")

    with default_args(type="run"):
        depends_on("py-python-dateutil@2.7:", when="@0.16:")
        depends_on("py-python-dateutil", when="@0.14.3:0.15")
        depends_on("py-types-python-dateutil@2.8.10:", when="@1.3:")

