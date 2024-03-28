# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyCelery(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("5.3.6", sha256="9da4ea0118d232ce97dff5ed4974587fb1c0ff5c10042eb15278487cdd27d1af", url="https://pypi.org/packages/37/c2/4c8a67a4d98a6fcd55dbdd79b641f945d7f59637c3e885c4abbda3c431f6/celery-5.3.6-py3-none-any.whl")
    version("5.3.5", sha256="30b75ac60fb081c2d9f8881382c148ed7c9052031a75a1e8743ff4b4b071f184", url="https://pypi.org/packages/a3/fb/0bcea0312649a374601d5a15092b2a3659801d578e70cec03aa72053ccaa/celery-5.3.5-py3-none-any.whl")
    version("5.3.4", sha256="1e6ed40af72695464ce98ca2c201ad0ef8fd192246f6c9eac8bba343b980ad34", url="https://pypi.org/packages/98/e9/023b8f75128d747d4aee79da84e4ac58eff63bb21f1c0aa7c452a353d207/celery-5.3.4-py3-none-any.whl")
    version("5.3.3", sha256="d65c0be70d0949fcda8893876a071a7cfd9f248f9ad92e1919845e5cbc268db7", url="https://pypi.org/packages/a8/bb/81b716e1ffc0423af06efdafa0d2aa3abe657f33bdf6eed4077bd56d84de/celery-5.3.3-py3-none-any.whl")
    version("5.3.2", sha256="ebac6158429b82f9b502d64f0038ab6be4606cbb3656422cb1b8cfb673651c18", url="https://pypi.org/packages/f7/12/9d195055414b53846fcd22e3f2c61c70a9f4168913036a7a290d69c0b6ed/celery-5.3.2-py3-none-any.whl")
    version("5.3.1", sha256="27f8f3f3b58de6e0ab4f174791383bbd7445aff0471a43e99cfd77727940753f", url="https://pypi.org/packages/18/b9/cb8d519ea0094b9b8fe7480225c14937517729f8ec927643dc7379904f64/celery-5.3.1-py3-none-any.whl")
    version("5.3.0", sha256="95d29f9a93f41c4b122fddf1fe3ef13f872029dca4ad1f9af4f1a414442ceecf", url="https://pypi.org/packages/b8/b1/fb24a605e7f2fe654bb0b63985bb0c95b1bb5d5ffbfaf46134c92eb93f61/celery-5.3.0-py3-none-any.whl")
    version("5.2.7", sha256="138420c020cd58d6707e6257b6beda91fd39af7afde5d36c6334d175302c0e14", url="https://pypi.org/packages/1d/99/21fe9d1829cab4fc77d18f89d0c4cbcfe754e95f8b8f4af64fe4997c442f/celery-5.2.7-py3-none-any.whl")
    version("5.2.6", sha256="da31f8eae7607b1582e5ee2d3f2d6f58450585afd23379491e3d9229d08102d0", url="https://pypi.org/packages/a0/ed/8a2e381aa9fa6fa5ac6891b0b472e927892f57a39842eff18cc917ceba57/celery-5.2.6-py3-none-any.whl")
    version("5.2.5", sha256="1f31c196e61dde344e322f9c0d33d1bb88c0dbaccbab5019fbb519a43d44706d", url="https://pypi.org/packages/19/72/1075b1fdb3e44d8ae78fdb51f209403ec3a41860be6ba488a369b101fd97/celery-5.2.5-py3-none-any.whl")
    version("5.2.3", sha256="8aacd02fc23a02760686d63dde1eb0daa9f594e735e73ea8fb15c2ff15cb608c", url="https://pypi.org/packages/1e/c2/52a01d3f53ddf57c80b011714dd63295c69426121d35d0ff41976b83506c/celery-5.2.3-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    variant("redis", default=False)
    variant("sqlalchemy", default=False)
    # END VARIANTS

    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-backports-zoneinfo@0.2.1:", when="@5.3.0-rc1: ^python@:3.8")
        depends_on("py-billiard@4.2:", when="@5.3.5:")
        depends_on("py-billiard@4.1:", when="@5.3.0-beta2:5.3.4")
        depends_on("py-billiard@3.6.4:3", when="@5:5.2")
        depends_on("py-click@8.1.2:", when="@5.3:")
        depends_on("py-click@8.0.3:", when="@5.2.3:5.2")
        depends_on("py-click-didyoumean@0.3:", when="@5.3:")
        depends_on("py-click-didyoumean@0.0.3:", when="@5:5.2")
        depends_on("py-click-plugins@1.1.1:", when="@5:")
        depends_on("py-click-repl@0.2:", when="@5:")
        depends_on("py-kombu@5.3.4:", when="@5.3.6:")
        depends_on("py-kombu@5.3.3:", when="@5.3.5")
        depends_on("py-kombu@5.3.2:", when="@5.3.2:5.3.4")
        depends_on("py-kombu@5.3.1:", when="@5.3.1")
        depends_on("py-kombu@5.3.0:", when="@5.3.0")
        depends_on("py-kombu@5.2.3:", when="@5.2.3:5.2")
        depends_on("py-python-dateutil@2.8.2:", when="@5.3.0-rc2:")
        depends_on("py-pytz@2021.3:", when="@5.2.3:5.3.0-beta2")
        depends_on("py-redis@4.5.2:4.5.4,4.6:4", when="@5.3.2:5.3.4+redis")
        depends_on("py-redis@4.5.2:4.5.4,4.6:", when="@5.3.1,5.3.5:+redis")
        depends_on("py-redis@4.5.2:", when="@5.3.0-rc2:5.3.0+redis")
        depends_on("py-redis@3.4.1:4.0.0-rc2,4.0.2:", when="@5.2.3:5.2+redis")
        depends_on("py-setuptools@59.1.1:59.6", when="@5.2.3:5.2.4")
        depends_on("py-sqlalchemy@1.4.48:", when="@5.3.0-rc2:+sqlalchemy")
        depends_on("py-sqlalchemy", when="@5:5.2+sqlalchemy")
        depends_on("py-tzdata@2022.7:", when="@5.3.0-rc1:")
        depends_on("py-vine@5.1:", when="@5.3.5:")
        depends_on("py-vine@5.0.0:", when="@5:5.3.4")
    # END DEPENDENCIES

