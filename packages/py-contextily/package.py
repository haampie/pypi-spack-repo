# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyContextily(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("1.6.0", sha256="8a0900ac5cfcec0f4ae46b5d83fe176625355dfeff2376a66b6e61694c2fe9cb", url="https://pypi.org/packages/d2/84/dbcd682289fe8fa3f7c16318e06a7626608f767a9a163954df58f245adef/contextily-1.6.0-py3-none-any.whl")
    version("1.5.2", sha256="d7dbf4228ecd42e58e2fa8559c550bdd7a9585ba6ba4f78a263ac60509a003d6", url="https://pypi.org/packages/00/89/c09ddb0345f944f194f0e0ce0591cdfdda72e58165e09526c1bfefad6b8e/contextily-1.5.2-py3-none-any.whl")
    version("1.5.1", sha256="d09ace7421048a124979a6cf3cdfa7d21269841e614f78e042a5b5025cb82b8a", url="https://pypi.org/packages/06/9f/00c346214569e7ded8ffae6b025c32acf43b10313a7c0c68f4b8eebf3d0b/contextily-1.5.1-py3-none-any.whl")
    version("1.5.0", sha256="53bbd4c1ec125a41b0b483ec4a9dd0fd97842917bd6284f7fa459b2650473441", url="https://pypi.org/packages/17/19/1051cd673ea58286b5148bf5c6eb42bdadb0b0b335c601cd5cea549aa17b/contextily-1.5.0-py3-none-any.whl")
    version("1.4.0", sha256="bb3bf6d595c1850d9c31587b548d734b1f6eb9ffe4f3a4d778504f50a0aa7cd3", url="https://pypi.org/packages/83/35/562e72099bf50228fa2a8e161db35a94090f3939cb73aa54e385096ca3ff/contextily-1.4.0-py3-none-any.whl")
    version("1.3.0", sha256="c7f0ddf62c87fd20e46a435aaa0551707a552b776f16eb545df5a61d32d80d75", url="https://pypi.org/packages/5d/05/1f9a5bcde8b46e250393883c3dc47f0bfbc7f25337bd768579f4c4fd84b3/contextily-1.3.0-py3-none-any.whl")
    version("1.2.0", sha256="f3c63082b6b2c4c7cfb58bbd0db8c57140d88eb829654bf3e04e5c53b4c5b17d", url="https://pypi.org/packages/97/c9/c6dcadf139384322a814503b30ff56ec58153f82ba5763d932d908df5085/contextily-1.2.0-py3-none-any.whl")
    version("1.1.0", sha256="152d6e23273faf9ce862376465e2bd5ca72de9667a5a2bd34ce10e06de313deb", url="https://pypi.org/packages/d3/8a/f7916ad000c30b86793a0c7a63946baa413f40f33edb5b10f78a1b150d24/contextily-1.1.0-py3-none-any.whl")
    version("1.0.1", sha256="945b31a3fab38a31f06379cefa6d625d02ac56610c3a4dedd5b5b7dc82a8cb7a", url="https://pypi.org/packages/93/2a/22b34b6129303c594c21cb80ded800ebd6d13037f00d162d9b3a3785d5ea/contextily-1.0.1-py3-none-any.whl")
    version("1.0.0", sha256="5380f9845a75075c11b8f09ebc3d9471f4ba39105a33b2875ebdd2938ea43684", url="https://pypi.org/packages/c1/95/6a228a25a5e93ae236efe42a36659b61b1b4e7ceee75dd5bc4bab8944c44/contextily-1.0.0-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("python@3.9:", when="@1.6:")
        depends_on("py-geopy", when="@1:")
        depends_on("py-joblib", when="@1.0-rc2:")
        depends_on("py-matplotlib", when="@1.0-rc2:")
        depends_on("py-mercantile", when="@1:")
        depends_on("py-pillow", when="@1:")
        depends_on("py-rasterio", when="@1:")
        depends_on("py-requests", when="@1:")
        depends_on("py-xyzservices", when="@1.2:")
    # END DEPENDENCIES

