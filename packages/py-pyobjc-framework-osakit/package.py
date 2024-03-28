# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPyobjcFrameworkOsakit(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("10.2", sha256="fbad23e47e31d795a005c18a20d84bff68d90d6dd0f87b6a343e46f87c00034a", url="https://pypi.org/packages/df/01/a26e5651a11bff4b0a99a63de71ade332e4adf70625752932db1b9dd4889/pyobjc_framework_OSAKit-10.2-py2.py3-none-any.whl")
    version("10.1", sha256="af34b4dccc17a772d80c283c9356bdb5a5a300bd54c2557c26671aca4f2f86cb", url="https://pypi.org/packages/a9/fe/7cb4fa27e2d90ea84f7e60838a02322e8ffff401a98cc184faf1d4e644b0/pyobjc_framework_OSAKit-10.1-py2.py3-none-any.whl")
    version("10.0", sha256="b87bb4ac330da116c33ffefa2da0b7946ac8a840150da848cafd7fff19f7e674", url="https://pypi.org/packages/9a/55/abe0ca036fcac674483d840ac65d06c15bf755ea8b79eeda9c8bbcb0e2f3/pyobjc_framework_OSAKit-10.0-py2.py3-none-any.whl")
    version("9.2", sha256="4ddbf9ba2bffb80d9080ce9854baff40c58087c31eabb9ad49c6847ff19256c8", url="https://pypi.org/packages/43/a1/164008304189f963301916a17c349751dd56777283988b5d99a8d9958931/pyobjc_framework_OSAKit-9.2-py2.py3-none-any.whl")
    version("9.1.1", sha256="bef666303f96ff0da0319caaa123e4f71f4361754e766a4b4e347c15e1fa7c70", url="https://pypi.org/packages/d4/8b/38ef340ac3a4ef41995730c9d5f517bfbbdbb2ee6078fc794109ec7f83f3/pyobjc_framework_OSAKit-9.1.1-py2.py3-none-any.whl")
    version("9.1", sha256="eb8c8f95cc5626c0b53f97d0fb40c5f75118ca2de1465378d6e46a4b5186f919", url="https://pypi.org/packages/5d/3a/9c7b2e47b8f1f8d03998fa4228fe8dfa455cbc4d033e9fee55dd4a8defe6/pyobjc_framework_OSAKit-9.1-py2.py3-none-any.whl")
    version("9.0.1", sha256="061831f13ac75ad3ac9a22df550f651bfcaa983ec3d6a390867fed9df86e716c", url="https://pypi.org/packages/91/fb/56dfbe790ea9a562f3d04c946c3bd8b8719aff08fb0731b9cd57dd854c75/pyobjc_framework_OSAKit-9.0.1-py2.py3-none-any.whl")
    version("9.0", sha256="3d306e2140292c51a1d245a6721dfae4a0d921ab248e1e835a7c6a2539673376", url="https://pypi.org/packages/28/46/ba73eae7472774baae63c80d48426258bbdf9d395e82c24d5c4a66629100/pyobjc_framework_OSAKit-9.0-py2.py3-none-any.whl")
    version("8.5.1", sha256="e8a8e1d59ce570ed20d7f44dbc3f34c12fd747410b753d12a0d305858f783cbe", url="https://pypi.org/packages/a2/45/7e878eb5abc14c8b55e4165594d7122a988817815f2037f9500b6858e274/pyobjc_framework_OSAKit-8.5.1-py2.py3-none-any.whl")
    version("8.5", sha256="161f665b37acac32938d2f698ea3df652e9a721b36b08a507cf39f80f5b03af8", url="https://pypi.org/packages/59/d6/af0f3f43b7703baeeb8239d2dcabd7b49a5b41c18953f657457350e69c16/pyobjc_framework_OSAKit-8.5-py2.py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-pyobjc-core@10.2:", when="@10.2:")
        depends_on("py-pyobjc-core@10.1:", when="@10.1")
        depends_on("py-pyobjc-core@10:", when="@10:10.0")
        depends_on("py-pyobjc-core@9.2:", when="@9.2:9")
        depends_on("py-pyobjc-core@9.1.1:", when="@9.1.1:9.1")
        depends_on("py-pyobjc-core@9.1:", when="@9.1:9.1.0")
        depends_on("py-pyobjc-core@9.0.1:", when="@9.0.1:9.0")
        depends_on("py-pyobjc-core@9:", when="@9:9.0.0")
        depends_on("py-pyobjc-core@8.5.1:", when="@8.5.1:8")
        depends_on("py-pyobjc-core@8.5:", when="@8.5:8.5.0")
        depends_on("py-pyobjc-framework-cocoa@10.2:", when="@10.2:")
        depends_on("py-pyobjc-framework-cocoa@10.1:", when="@10.1")
        depends_on("py-pyobjc-framework-cocoa@10:", when="@10:10.0")
        depends_on("py-pyobjc-framework-cocoa@9.2:", when="@9.2:9")
        depends_on("py-pyobjc-framework-cocoa@9.1.1:", when="@9.1.1:9.1")
        depends_on("py-pyobjc-framework-cocoa@9.1:", when="@9.1:9.1.0")
        depends_on("py-pyobjc-framework-cocoa@9.0.1:", when="@9.0.1:9.0")
        depends_on("py-pyobjc-framework-cocoa@9:", when="@9:9.0.0")
        depends_on("py-pyobjc-framework-cocoa@8.5.1:", when="@8.5.1:8")
        depends_on("py-pyobjc-framework-cocoa@8.5:", when="@8.5:8.5.0")
    # END DEPENDENCIES

