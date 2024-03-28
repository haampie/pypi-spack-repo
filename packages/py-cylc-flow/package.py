# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyCylcFlow(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("8.2.4", sha256="26938f7fe24cd8b0de62a89cb3a341eb701f39e1a024d6de57d68e37fac33c4e", url="https://pypi.org/packages/b1/ef/07a30c229d4987f057a2843ffe020c6a22526e98c0b025e2110d5e1de4a8/cylc_flow-8.2.4-py3-none-any.whl")
    version("8.2.3", sha256="ad09fd8072f7bc47b0adf3c29deeb9e52d81e151f651beb689f10b7d083d5af6", url="https://pypi.org/packages/cf/1f/8b9f6faff518138d7220cefd1aa01721ad1326b21ed2c94b8c3bbc6ff8cc/cylc_flow-8.2.3-py3-none-any.whl")
    version("8.2.2", sha256="b92a4b59dedaeae035c2dab7cd79547b33ff7e9f70f741b5081ce29b11839fe4", url="https://pypi.org/packages/d1/25/f817a0aa8d88461d813e3fa6c42080a9a39c07e8829061070d0969240453/cylc_flow-8.2.2-py3-none-any.whl")
    version("8.2.1", sha256="8b03152a03538f8a69e5ae87782854eb3bca02a2ff3409479bdad6f78b0cdc09", url="https://pypi.org/packages/7f/9d/31ae5eb3fdaa523b39533fe760ca49dd7fa148532dfe60467a395aab1a19/cylc_flow-8.2.1-py3-none-any.whl")
    version("8.2.0", sha256="62bb7201f6aae8258749bd0065bd71c538116f72bb1e711028b9f4812fd59e01", url="https://pypi.org/packages/7f/39/8958c62393ce821730058b0bf4686480302a9982f5716fa94c0539a30403/cylc_flow-8.2.0-py3-none-any.whl")
    version("8.1.4", sha256="da404e7f6b3e5204fe1fb613602bb1e3be6aea6895999630a62d21833be3c359", url="https://pypi.org/packages/de/2c/bdaba24b3fa802153f23bfea21149502e5a57210fcb20033d16e0b8d1900/cylc_flow-8.1.4-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-aiofiles@0.7", when="@8.0-beta2:8.1")
        depends_on("py-ansimarkup@1:", when="@8.0-alpha1:")
        depends_on("py-async-timeout@3:", when="@8.0-rc1:")
        depends_on("py-colorama@0.4:", when="@8.0-beta0:")
        depends_on("py-graphene@2.1:2", when="@8.0-alpha1:")
        depends_on("py-jinja2@3:3.0", when="@8.0.0:")
        depends_on("py-metomi-isodatetime@1.3:", when="@8.2.3:")
        depends_on("py-metomi-isodatetime@1.3:1.3.0", when="@8.0-rc3:8.2.2")
        depends_on("py-promise", when="@8.0-rc3:")
        depends_on("py-protobuf@4.21.2:4.21", when="@8.1:")
        depends_on("py-psutil@5.6:", when="@8.0-alpha2:")
        depends_on("py-pyzmq@22:", when="@8.2:")
        depends_on("py-pyzmq@22", when="@8.0-rc1:8.1")
        depends_on("py-rx", when="@8.0-rc3:")
        depends_on("py-setuptools@49:66,68:", when="@8.2:")
        depends_on("py-setuptools@49:66", when="@8.1")
        depends_on("py-tomli@2:", when="@8.1: ^python@:3.10")
        depends_on("py-urwid@2:", when="@8.0-alpha2:")
    # END DEPENDENCIES

