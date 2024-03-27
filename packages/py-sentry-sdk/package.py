##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PySentrySdk(PythonPackage):
    version("1.43.0", sha256="8d768724839ca18d7b4c7463ef7528c40b7aa2bfbf7fe554d5f9a7c044acfd36", url="https://pypi.org/packages/26/89/9b786c95b202b2da0d3a481497e79447cff6c753b4f0af5a3aecf3271a67/sentry_sdk-1.43.0-py2.py3-none-any.whl")
    version("1.42.0", sha256="a654ee7e497a3f5f6368b36d4f04baeab1fe92b3105f7f6965d6ef0de35a9ba4", url="https://pypi.org/packages/0b/63/feb288ae4fd4579208bcfba77ceea48e83fd02c50cfcf1c8fc2b0b585a1d/sentry_sdk-1.42.0-py2.py3-none-any.whl")
    version("1.41.0", sha256="be4f8f4b29a80b6a3b71f0f31487beb9e296391da20af8504498a328befed53f", url="https://pypi.org/packages/f0/3a/7c5f053e05c926fcbbd054ac07f61ba552015d099ce94bd4c4e4efd682c5/sentry_sdk-1.41.0-py2.py3-none-any.whl")
    version("1.40.6", sha256="becda09660df63e55f307570e9817c664392655a7328bbc414b507e9cb874c67", url="https://pypi.org/packages/42/1c/6919b23b9d1b58363525e8e40c4cb10132588abd070b54507231e3082f38/sentry_sdk-1.40.6-py2.py3-none-any.whl")
    version("1.40.5", sha256="d188b407c9bacbe2a50a824e1f8fb99ee1aeb309133310488c570cb6d7056643", url="https://pypi.org/packages/f6/21/e41b8dd0da432a06b8bf10b7ba634d6e62e60b9a79aba15146a2581265cc/sentry_sdk-1.40.5-py2.py3-none-any.whl")
    version("1.40.4", sha256="ac5cf56bb897ec47135d239ddeedf7c1c12d406fb031a4c0caa07399ed014d7e", url="https://pypi.org/packages/59/5f/481237f48ea0bb09134a3e8967daf486476d04c9e8e86790759e5637f1f1/sentry_sdk-1.40.4-py2.py3-none-any.whl")
    version("1.40.3", sha256="73383f28311ae55602bb6cc3b013830811135ba5521e41333a6e68f269413502", url="https://pypi.org/packages/25/ac/1c579ae80748f4026a60776b42dd9666bc355be2edc4f088d35e85346acf/sentry_sdk-1.40.3-py2.py3-none-any.whl")
    version("1.40.2", sha256="696ef61a323a207e6a20b018ddc6591adb81c671434c88d1a4f2e95ffa75556c", url="https://pypi.org/packages/78/2d/cb8e3b04b5873cc8c8c6028a258f82584b12000d9a0fb1e7f386ef9a2c74/sentry_sdk-1.40.2-py2.py3-none-any.whl")
    version("1.40.1", sha256="69fc5e7512371547207821d801485f45e3c62db629f02f56f58431a10864ac34", url="https://pypi.org/packages/ab/5c/b004ae4791f5c5bedab49e2aab2d0b7284fc3ed0f813cb334984f41884cf/sentry_sdk-1.40.1-py2.py3-none-any.whl")
    version("1.40.0", sha256="78575620331186d32f34b7ece6edea97ce751f58df822547d3ab85517881a27a", url="https://pypi.org/packages/04/48/8e4d52475cab1c85900f83fb0ade1c59e619d36b4ae02b5c3580cdef3f68/sentry_sdk-1.40.0-py2.py3-none-any.whl")
    version("1.5.5", sha256="3817274fba2498c8ebf6b896ee98ac916c5598706340573268c07bf2bb30d831", url="https://pypi.org/packages/3f/6a/01fb4e5417f5d2ef6279883a9deedabb6b6f223aa706892ea9caa6d7c1e4/sentry_sdk-1.5.5-py2.py3-none-any.whl")
    version("0.17.6", sha256="45486deb031cea6bbb25a540d7adb4dd48cd8a1cc31e6a5ce9fb4f792a572e9a", url="https://pypi.org/packages/c8/6c/6dcf4f21bec0b0d0685b4992ee414506342b09267e4a2ab24472625f9d8d/sentry_sdk-0.17.6-py2.py3-none-any.whl")

    with default_args(type="run"):
        depends_on("py-certifi", when="@:0.1.0-rc1,0.1.0-rc3,0.1.0-rc5:0.1.0-rc6,0.1.0-rc11,0.1.0-rc14,0.1.0-rc16:0.1.0,0.1.2,0.4:0.4.0,0.5:0.5.1,0.5.4,0.6:0.6.1,0.6.6,0.6.8:0.7.0,0.7.3,0.7.12,0.7.14:0.7,0.8.1:0.8,0.12:0.12.2,0.13.1,0.15:0.20.0,0.20.2:")
        depends_on("py-urllib3@1.26.11:", when="@1.9.2:")
        depends_on("py-urllib3@1.10:", when="@0.13.1,0.15:0.20.0,0.20.2:1.9.0")

