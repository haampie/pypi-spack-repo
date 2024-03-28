# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyJoblib(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("1.3.2", sha256="ef4331c65f239985f3f2220ecc87db222f08fd22097a3dd5698f693875f8cbb9", url="https://pypi.org/packages/10/40/d551139c85db202f1f384ba8bcf96aca2f329440a844f924c8a0040b6d02/joblib-1.3.2-py3-none-any.whl")
    version("1.3.1", sha256="89cf0529520e01b3de7ac7b74a8102c90d16d54c64b5dd98cafcd14307fdf915", url="https://pypi.org/packages/28/08/9dcdaa5aac4634e4c23af26d92121f7ce445c630efa0d3037881ae2407fb/joblib-1.3.1-py3-none-any.whl")
    version("1.3.0", sha256="172d56d4c43dd6bcd953bea213018c4084cf754963bbf54b8dae40faea716b98", url="https://pypi.org/packages/1e/f2/6ec7eb9e48c88c750da04050a5ba8250ca9949dfcf6e624ccee12d2fc653/joblib-1.3.0-py3-none-any.whl")
    version("1.2.0", sha256="091138ed78f800342968c523bdde947e7a305b8594b910a0fea2ab83c3c6d385", url="https://pypi.org/packages/91/d4/3b4c8e5a30604df4c7518c562d4bf0502f2fa29221459226e140cf846512/joblib-1.2.0-py3-none-any.whl")
    version("1.1.1", sha256="f9d6c3cdf2a7778e9058e10e9dba028e47771a1a355e5768f46704bf05342eba", url="https://pypi.org/packages/7c/91/d3ba0401e62d7e42816bc7d97b82d19c95c164b3e149a87c0a1c026a735e/joblib-1.1.1-py2.py3-none-any.whl")
    version("1.1.0", sha256="f21f109b3c7ff9d95f8387f752d0d9c34a02aa2f7060c2135f465da0e5160ff6", url="https://pypi.org/packages/3e/d5/0163eb0cfa0b673aa4fe1cd3ea9d8a81ea0f32e50807b0c295871e4aab2e/joblib-1.1.0-py2.py3-none-any.whl")
    version("1.1.0-alpha0", sha256="441b7bec8c9a445b34efd86fbdac7ee3a3c44ff013877cf66776bbef21212aa3", url="https://pypi.org/packages/be/32/f33d3d25476b50916f6e266d4d8ba4fe51078653023c48d520c3b9ee4b1c/joblib-1.1.0a0-py2.py3-none-any.whl")
    version("1.0.1", sha256="feeb1ec69c4d45129954f1b7034954241eedfd6ba39b5e9e4b6883be3332d5e5", url="https://pypi.org/packages/55/85/70c6602b078bd9e6f3da4f467047e906525c355a4dacd4f71b97a35d9897/joblib-1.0.1-py3-none-any.whl")
    version("1.0.0", sha256="75ead23f13484a2a414874779d69ade40d4fa1abe62b222a23cd50d4bc822f6f", url="https://pypi.org/packages/34/5b/bd0f0fb5564183884d8e35b81d06d7ec06a20d1a0c8b4c407f1554691dce/joblib-1.0.0-py3-none-any.whl")
    version("0.17.0", sha256="698c311779f347cf6b7e6b8a39bb682277b8ee4aba8cf9507bc0cf4cd4737b72", url="https://pypi.org/packages/fc/c9/f58220ac44a1592f79a343caba12f6837f9e0c04c196176a3d66338e1ea8/joblib-0.17.0-py3-none-any.whl")
    version("0.16.0", sha256="d348c5d4ae31496b2aa060d6d9b787864dd204f9480baaa52d18850cb43e9f49", url="https://pypi.org/packages/51/dd/0e015051b4a27ec5a58b02ab774059f3289a94b0906f880a3f9507e74f38/joblib-0.16.0-py3-none-any.whl")
    version("0.15.1", sha256="6825784ffda353cc8a1be573118085789e5b5d29401856b35b756645ab5aecb5", url="https://pypi.org/packages/b8/a6/d1a816b89aa1e9e96bcb298eb1ee1854f21662ebc6d55ffa3d7b3b50122b/joblib-0.15.1-py3-none-any.whl")
    version("0.15.0", sha256="a55f5268c5e402e4a892202089ebda1730db81e82f704d2bee8a6bc499ebc264", url="https://pypi.org/packages/ec/6f/40d92f607be42dd0d2edf5e47c1ed31160addda005e977867f5c1ea8f835/joblib-0.15.0-py3-none-any.whl")
    version("0.14.1", sha256="bdb4fd9b72915ffb49fde2229ce482dd7ae79d842ed8c2b4c932441495af1403", url="https://pypi.org/packages/28/5c/cf6a2b65a321c4a209efcdf64c2689efae2cb62661f8f6f4bb28547cf1bf/joblib-0.14.1-py2.py3-none-any.whl")
    version("0.14.0", sha256="006108c7576b3eb6c5b27761ddbf188eb6e6347696325ab2027ea1ee9a4b922d", url="https://pypi.org/packages/8f/42/155696f85f344c066e17af287359c9786b436b1bf86029bb3411283274f3/joblib-0.14.0-py2.py3-none-any.whl")
    version("0.13.2", sha256="21e0c34a69ad7fde4f2b1f3402290e9ec46f545f15f1541c582edfe05d87b63a", url="https://pypi.org/packages/cd/c1/50a758e8247561e58cb87305b1e90b171b8c767b15b12a1734001f41d356/joblib-0.13.2-py2.py3-none-any.whl")
    version("0.11", sha256="cf3420e27048c66916754472bc3a2d4717271103a4806f31f11707a3d82a991f", url="https://pypi.org/packages/4f/51/870b2ec270fc29c5d89f85353da420606a9cb39fba4747127e7c7d7eb25d/joblib-0.11-py2.py3-none-any.whl")
    version("0.10.3", sha256="90cda39dcef85cb6f64bff51cb812ce6eed9df7217d8e78b8c693ab1c370653e", url="https://pypi.org/packages/23/ad/17c2e3f1e1f58f1a3efb5d6eb4478ea61b5a782c0361bb4e0e65b93cf013/joblib-0.10.3-py2.py3-none-any.whl")
    version("0.10.2", sha256="9e3b22d672c960dff76c152fb68f153ea4e61527c36e552a01eadaeb73384fe1", url="https://pypi.org/packages/f1/56/321f33c8cf1b6ec4e3d3002d71454a266d6a45b05eca6d728bf030a9b155/joblib-0.10.2-py2.py3-none-any.whl")
    version("0.10.0", sha256="e626f35a344a457e4a32d0e66ecb6b7d3a81bf662882e88db0e796d65ef85e4a", url="https://pypi.org/packages/fd/b1/8481d7cea05c6ca8d417497f2106def4c26b80d5d32e19fb45bc18b11195/joblib-0.10.0-py2.py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    # END DEPENDENCIES

