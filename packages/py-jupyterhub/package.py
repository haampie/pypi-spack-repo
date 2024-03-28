# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyJupyterhub(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("4.0.2", sha256="2f389e7d3067e1b11bb4091719048eedecee161039fd2e5b025d031f7ab23c62", url="https://pypi.org/packages/70/4c/1f9cb10007990023f24bebf049e3ac1fcdf846992e8470422da11bf53ee0/jupyterhub-4.0.2-py3-none-any.whl")
    version("4.0.1", sha256="b96e3f83a5d7c543b414266e43407eb380fb590212bcc70097f6c837d5611387", url="https://pypi.org/packages/70/97/850439996c487f1ebab15fe1295f78ce6b6e89cbb27bcf6bbef241c32301/jupyterhub-4.0.1-py3-none-any.whl")
    version("4.0.0", sha256="1f2c2ff069e1bc66bcaa032b15f8ab602356ee3ed19ff5d483c68e73ad13317c", url="https://pypi.org/packages/ff/60/f871001204b71a930cda9ced36064d6023cc7d02184881f263c1b80956f9/jupyterhub-4.0.0-py3-none-any.whl")
    version("3.1.1", sha256="a56cf362859ce36a57c78369901c5968b5e2421b5be999f50ac4f0cb86c4b563", url="https://pypi.org/packages/ec/4b/40ba8344b4b477df8c6cfbef5392e40d8c7dda11e6c72ac95790b5fd47e5/jupyterhub-3.1.1-py3-none-any.whl")
    version("3.1.0", sha256="da510020ae3240f7902f9539aea047b1eb5ecc7235e39c5b7251b25c5a5fc2b7", url="https://pypi.org/packages/cb/93/7c7cf1bedb5ba58e13c4a7d9279c850ec7ba065f23fdc43c9b4b27a8141f/jupyterhub-3.1.0-py3-none-any.whl")
    version("3.0.0", sha256="1d0b437033d8fd75d7ab4715ee3853da3069d6f14b4a0b9092f705efd0faa3b4", url="https://pypi.org/packages/88/71/164957bb282876b4dd21ebdb49bfaf386820e16708a84c94f96677946459/jupyterhub-3.0.0-py3-none-any.whl")
    version("2.3.1", sha256="0fd5a5671187d501f81daa57e40178cf2804bfd2f325741ccad31a2ce5ff0c5f", url="https://pypi.org/packages/21/68/7b63ede015432c936561e7ede2e920bd399c1c03a2fa41ec23d23b9eda71/jupyterhub-2.3.1-py3-none-any.whl")
    version("2.3.0", sha256="bfaa961485adbea682241c17a0be1def8f29198f61f66ee5fd7c8915b2fdf69b", url="https://pypi.org/packages/5d/ca/236c16b3f927b74513df865d5aa219887e9267a0d4d790745bfee4cd29a9/jupyterhub-2.3.0-py3-none-any.whl")
    version("2.2.2", sha256="f7dd09087428853eef07a741f299e0ebc4b1b5c1deb7f66fe9c23dc005d9d134", url="https://pypi.org/packages/93/cf/4564e6c4057948c63ced0050641b4bad71a37be5b13093003cda5a85063b/jupyterhub-2.2.2-py3-none-any.whl")
    version("2.2.1", sha256="62e338ef2d138857f142a2ddd07935333eee478be8084912ab10e7b619fc2562", url="https://pypi.org/packages/4a/7e/0e47172f0ae7b190525ee818e49ddef75e1d5487878aeabd7880a13281f7/jupyterhub-2.2.1-py3-none-any.whl")
    version("1.4.1", sha256="20372a507b103a5351bd1dd7782c7524c14b013f43c71d95e37a0efaa9ec6ae9", url="https://pypi.org/packages/ac/95/3bb31d8d42aa52f71e713a9027fe3318897f21f76146e7f8843608bb5dbb/jupyterhub-1.4.1-py3-none-any.whl")
    version("1.0.0", sha256="e5ba12ba158ffcb1d42ac351f850d0065be14fce012af765cdf30dfe97a7346a", url="https://pypi.org/packages/0d/67/c1e7d691bcb635fcde61c544d8fbca1edebb7bb4f68f34f5de291eba02d0/jupyterhub-1.0.0-py3-none-any.whl")
    version("0.9.4", sha256="6fd5b19ae152cc637bed2f528ca1bd510042782dc770a32e7ab1ed34e6867873", url="https://pypi.org/packages/23/7d/8f272ff69f05d51143e85753939884ca1e578639e273a8bfc1bda69f15bf/jupyterhub-0.9.4-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-alembic@1.4:", when="@1.4:")
        depends_on("py-alembic", when="@0.7:1.3")
        depends_on("py-async-generator@1.9:", when="@1.3:")
        depends_on("py-async-generator@1.8:", when="@0.9:1.2")
        depends_on("py-certipy@0.1.2:", when="@1:")
        depends_on("py-entrypoints", when="@1:2")
        depends_on("py-importlib-metadata@3.6:", when="@3: ^python@:3.9")
        depends_on("py-jinja2@2.11:", when="@1.3:")
        depends_on("py-jinja2", when="@0.4:0.4.0,0.6:1.2")
        depends_on("py-jupyter-telemetry@0.1:", when="@1.2:")
        depends_on("py-oauthlib@3:", when="@1.0.0-beta2:")
        depends_on("py-packaging", when="@2:")
        depends_on("py-pamela", when="@1.2.2: platform=linux")
        depends_on("py-pamela", when="@1.2.2: platform=freebsd")
        depends_on("py-pamela", when="@1.2.2: platform=darwin")
        depends_on("py-pamela", when="@1.2.2: platform=cray")
        depends_on("py-pamela", when="@0.4:0.4.0,0.6:1.2.1")
        depends_on("py-prometheus-client@0.4:", when="@1.3:")
        depends_on("py-prometheus-client@0.0.21:", when="@0.9:1.2")
        depends_on("py-psutil@5.6.5:", when="@1.1.0: platform=windows")
        depends_on("py-python-dateutil", when="@0.9:")
        depends_on("py-python-oauth2@1:", when="@0.8:0")
        depends_on("py-requests", when="@0.4:0.4.0,0.6:")
        depends_on("py-sqlalchemy@1.4.0:", when="@4:")
        depends_on("py-sqlalchemy@1.1.0:", when="@0.8.0-beta5:3")
        depends_on("py-tornado@5.1:", when="@1.3:")
        depends_on("py-tornado@5.0:", when="@0.9:1.2")
        depends_on("py-traitlets@4.3.2:", when="@0.8:")
    # END DEPENDENCIES

