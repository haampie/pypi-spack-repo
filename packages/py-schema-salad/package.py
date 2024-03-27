##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PySchemaSalad(PythonPackage):
    version("8.5.20240311110950", sha256="76bd1d0792622c12c5882cc8448bb9ce9a6083ca7d0c02e7884f746dd011fedc", url="https://pypi.org/packages/4b/c6/6f1d5cc35f0fb69efcf2729eb6da6a1198bfea4456aaf4a4cab2e4537dae/schema-salad-8.5.20240311110950.tar.gz")
    version("8.5.20240102191335", sha256="7d32704f50e3fc6c096dc162084bf00bebce70aa762cb4a897239a64ae00a20c", url="https://pypi.org/packages/8d/09/655a633dc905ac97f654845f5b8f900f06bf38113ca972b4fb0f85162373/schema-salad-8.5.20240102191335.tar.gz")
    version("8.5.20231201181309", sha256="ab8763701b7ef0f1147a458d2a58af2a70d7ac904050a199d76e76ca6fc4e1b2", url="https://pypi.org/packages/70/65/fa4b7f6b09dfecdea54f6802da7fa8065bcd6a2d1c0caa0e00ad8764193e/schema-salad-8.5.20231201181309.tar.gz")
    version("8.4.20231117150958", sha256="b3e2c2fe00dfb943f8fa15893809bb241875abe0cdefa831cf5df2351dafc245", url="https://pypi.org/packages/75/a3/df1b69a7b64423de60b68a05bd6781904ec22121078c076dd7f693b35d90/schema-salad-8.4.20231117150958.tar.gz")
    version("8.4.20231113094720", sha256="e6f1f5c216bc7aa446a300ea5f71c0ab19734df64ee55980c89b4ce4f5a9416a", url="https://pypi.org/packages/28/19/b1c231e4b59f77765fc774f4979f7929d7a10e473d1c25d67ed6d554cd4d/schema-salad-8.4.20231113094720.tar.gz")
    version("8.4.20231024070348", sha256="a7cdd70f75a67f08ca5068cc4c4b6b266358953435d8519d6ae22458a0c53984", url="https://pypi.org/packages/68/20/fbb299fa0052784a2239b1ab4221f2518ab78d4f7030a48e951c9f188169/schema-salad-8.4.20231024070348.tar.gz")
    version("8.4.20230927144413", sha256="2018cca36ed29c304010fd89daf2f8e42ba7257efb4447af17bfb6cc59a81534", url="https://pypi.org/packages/58/82/350aab56ffd3ad7e2d285be889ca5c68f9ce5dd58eb7dd5be39dcbd93bbd/schema-salad-8.4.20230927144413.tar.gz")
    version("8.4.20230808163024", sha256="6a2e2fbfa1055f8c9347cb2046ca621be33c6bca1af372c89493c65fbabe29dd", url="https://pypi.org/packages/87/0f/b86777565c9a5c5ead3af83a88f7833f63a5e3c312ebeae83fadb963fe43/schema-salad-8.4.20230808163024.tar.gz")
    version("8.4.20230606143604", sha256="f19a3d6614b4afecec93b9c7121d31ee01d8c1aa169b272d41844ca61d3d9af6", url="https://pypi.org/packages/34/a0/245b852857d738cb771d7f7baf9abbd91942317fd9776f82d8b7ea1487c0/schema-salad-8.4.20230606143604.tar.gz")
    version("8.4.20230601112322", sha256="8d2c8ac3caf2eb404bdd94a4c2a0e31345c5cc0884801d1c5dc5ca86d18040b4", url="https://pypi.org/packages/c8/eb/1c9310b0fc0677951f75a475ccd4d11599f8181738c246189b4727273bc7/schema-salad-8.4.20230601112322.tar.gz")
    version("8.3.20221209165047", sha256="d97cc9a4d7c4255eb8000bcebaa8ac0d1d31801c921fd4113ab3051c1e326c7c", url="https://pypi.org/packages/22/10/b4519f55e08badba227829586f110e77798f7ab19bb60b349e67423ad8c5/schema-salad-8.3.20221209165047.tar.gz")

    with default_args(type="run"):
        depends_on("python@:3.12", when="@8.4.20230808163024:")
        depends_on("python@:3.11", when="@8.3.20221115203138:8.4.20230606143604")
        depends_on("python@:3.11.0", when="@8.3.20220825114525:8.3.20221028160159")
        depends_on("py-black", when="@8.2.20211014142459")
        depends_on("py-cachecontrol@0.11.7:+filecache", when="@8.5.20240311110950:")
        depends_on("py-cachecontrol@0.11.7:0.13+filecache", when="@8.4.20230927144413:8.5.20240102191335")
        depends_on("py-importlib-resources@1.4:", when="@8.5: ^python@:3.8")
        depends_on("py-importlib-resources@1.4:", when="@8.4.20230927144413:8.4")
        depends_on("py-mistune@3.0.0:", when="@8.5.20240311110950:")
        depends_on("py-mistune@2.0.3:2", when="@8.4.20230927144413:8.5.20240102191335")
        depends_on("py-mypy-extensions", when="@8.4.20230927144413:")
        depends_on("py-rdflib@4.2.2:", when="@8.4.20230927144413:")
        depends_on("py-requests@1:", when="@2.6.20170806163416,2.6.20171031091636:2.6.20171102064032,2.6.20180214144209:7.1.20210309094900,7.1.20210611090601:8.0.20210624094941,8.2.20211014142459,8.2.20211222191353,8.3:8.3.20220717021618,8.4.20230927144413:")
        depends_on("py-ruamel-yaml@0.17.6:", when="@8.4.20231024070348:")
        depends_on("py-ruamel-yaml@0.17.6:0.17", when="@8.4.20230927144413")

