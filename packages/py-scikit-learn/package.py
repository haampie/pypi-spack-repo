# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyScikitLearn(PythonPackage):
    # BEGIN VERSIONS
    version("1.4.0", sha256="d4373c984eba20e393216edd51a3e3eede56cbe93d4247516d205643c3b93121", url="https://pypi.org/packages/a0/25/f95b39549240d07c7fefa2ab0f81ac418f0ea192c53334f655bbed5015f9/scikit-learn-1.4.0.tar.gz")
    version("1.3.2", sha256="a2f54c76accc15a34bfb9066e6c7a56c1e7235dda5762b990792330b52ccfb05", url="https://pypi.org/packages/88/00/835e3d280fdd7784e76bdef91dd9487582d7951a7254f59fc8004fc8b213/scikit-learn-1.3.2.tar.gz")
    version("1.3.1", sha256="1a231cced3ee3fa04756b4a7ab532dc9417acd581a330adff5f2c01ac2831fcf", url="https://pypi.org/packages/4b/49/4b3e90399f49e875a1a6a0e72bb99d7e8fe808fcfe0a6a12b43a77e7d64d/scikit-learn-1.3.1.tar.gz")
    version("1.3.0", sha256="8be549886f5eda46436b6e555b0e4873b4f10aa21c07df45c4bc1735afbccd7a", url="https://pypi.org/packages/72/cd/4761675df1b3dd93072c89697278f3ed3dc004a60c034cd2603c43ff64b5/scikit-learn-1.3.0.tar.gz")
    version("1.2.2", sha256="8429aea30ec24e7a8c7ed8a3fa6213adf3814a6efbea09e16e0a0c71e1a1a3d7", url="https://pypi.org/packages/c9/fa/8e158d81e3602da1e7bafbd4987938bc003fe4b0f44d65681e7f8face95a/scikit-learn-1.2.2.tar.gz")
    version("1.2.1", sha256="fbf8a5c893c9b4b99bcc7ed8fb3e8500957a113f4101860386d06635520f7cfb", url="https://pypi.org/packages/86/cc/f2685fc3fc37122fe8be22e6c0dfdaeab49026625b8c2cf41bc87b1cdd4d/scikit-learn-1.2.1.tar.gz")
    version("1.2.0", sha256="680b65b3caee469541385d2ca5b03ff70408f6c618c583948312f0d2125df680", url="https://pypi.org/packages/27/a0/95eae31ceabeb7710a694367816edfcc0ccb001c794c14b3b234c148ae50/scikit-learn-1.2.0.tar.gz")
    version("1.1.3", sha256="bef51978a51ec19977700fe7b86aecea49c825884f3811756b74a3b152bb4e35", url="https://pypi.org/packages/38/bc/319f789ce0988d9bf1379d6e40498dc119b30bec133bf76cd82ca549b69a/scikit-learn-1.1.3.tar.gz")
    version("1.1.2", sha256="7c22d1305b16f08d57751a4ea36071e2215efb4c09cb79183faa4e8e82a3dbf8", url="https://pypi.org/packages/10/ae/123b6d1fdb2fdb1aea6793abe33ed1bf19efd0a936d2f39040a5e99f402b/scikit-learn-1.1.2.tar.gz")
    version("1.1.1", sha256="3e77b71e8e644f86c8b5be7f1c285ef597de4c384961389ee3e9ca36c445b256", url="https://pypi.org/packages/41/11/e931951f048908ceaf2423db48ca6ad10e0b818c2960a3bc2dacb4fa4c1d/scikit-learn-1.1.1.tar.gz")
    version("1.1.0", sha256="80f9904f5b1356adfc32406725dd94c8cc9c8d265047d98390033a6c238cbb29", url="https://pypi.org/packages/8b/99/b1ec652f2d60a13871a3053f312f9d78977be57e420f2a49d52ba503f1f4/scikit-learn-1.1.0.tar.gz")
    version("1.0.2", sha256="b5870959a5484b614f26d31ca4c17524b1b0317522199dc985c3b4256e030767", url="https://pypi.org/packages/75/44/074b780d8ac0b0899937e9b8ba6d5d8873a71b99aa915219251ef85a8890/scikit-learn-1.0.2.tar.gz")
    version("1.0.1", sha256="ac2ca9dbb754d61cfe1c83ba8483498ef951d29b93ec09d6f002847f210a99da", url="https://pypi.org/packages/62/7c/596ff7b32f655f379d3abdfa82607e5cb3b70f46baad4604706511cfeb85/scikit-learn-1.0.1.tar.gz")
    version("1.0", sha256="776800194e757cd212b47cd05907e0eb67a554ad333fe76776060dbb729e3427", url="https://pypi.org/packages/e1/4d/15c3542a17eebf61e48bd71dc55b5f3b5031f1cd0dc4aad1ff9ac9651e49/scikit-learn-1.0.tar.gz")
    version("0.24.2", sha256="d14701a12417930392cd3898e9646cf5670c190b933625ebe7511b1f7d7b8736", url="https://pypi.org/packages/05/04/507280f20fafc8bc94b41e0592938c6f4a910d0e066be7c8ff1299628f5d/scikit-learn-0.24.2.tar.gz")
    version("0.24.1", sha256="a0334a1802e64d656022c3bfab56a73fbd6bf4b1298343f3688af2151810bbdf", url="https://pypi.org/packages/f4/7b/d415b0c89babf23dcd8ee631015f043e2d76795edd9c7359d6e63257464b/scikit-learn-0.24.1.tar.gz")
    version("0.24.0", sha256="076369634ee72b5a5941440661e2f306ff4ac30903802dc52031c7e9199ac640", url="https://pypi.org/packages/db/e2/9c0bde5f81394b627f623557690536b12017b84988a4a1f98ec826edab9e/scikit-learn-0.24.0.tar.gz")
    version("0.23.2", sha256="20766f515e6cd6f954554387dfae705d93c7b544ec0e6c6a5d8e006f6f7ef480", url="https://pypi.org/packages/aa/f6/75297be19f48b7a8c2577753a3a700f98fc4db49d0e5ed3820dd8dee43d4/scikit-learn-0.23.2.tar.gz")
    version("0.23.1", sha256="e3fec1c8831f8f93ad85581ca29ca1bb88e2da377fb097cf8322aa89c21bc9b8", url="https://pypi.org/packages/23/b0/ff0f4ffa3da1ddb242a295d5d19dd1775f567ad73a6ea7474eaa55e04836/scikit-learn-0.23.1.tar.gz")
    version("0.23.0", sha256="639a53df6273acc6a7510fb0c658b94e0c70bb13dafff9d14932c981ff9baff4", url="https://pypi.org/packages/72/e4/75247cf75e9e3ba1bf296c9d26ba1cfc71d781821d32bcdb4d9b4b1b4153/scikit-learn-0.23.0.tar.gz")
    version("0.22.2.post1", sha256="57538d138ba54407d21e27c306735cbd42a6aae0df6a5a30c7a6edde46b0017d", url="https://pypi.org/packages/e4/40/8bc77d8f536be0a892b37fff19fd81f15935e24724303480f85238ec7f22/scikit-learn-0.22.2.post1.tar.gz")
    version("0.22.1", sha256="51ee25330fc244107588545c70e2f3570cfc4017cff09eed69d6e1d82a212b7d", url="https://pypi.org/packages/18/28/5a48b00599b476875415b97bdfdb3849bafb31183c1d785501dbc8a77aa2/scikit-learn-0.22.1.tar.gz")
    version("0.22", sha256="314abf60c073c48a1e95feaae9f3ca47a2139bd77cebb5b877c23a45c9e03012", url="https://pypi.org/packages/4f/2c/04e10167991ed6209fb251a212ca7c3148006f335f4aadf1808db2cbeda8/scikit-learn-0.22.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    variant("openmp", default=False, description="openmp")
    # END VARIANTS

    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("python@3.9:", when="@1.4:")
        depends_on("python@3.8:", when="@1.1:1.3")
        depends_on("python@3.7:", when="@1:1.0")
        depends_on("py-joblib@0.11:", when="@0.21-rc2:0.23.1")
        depends_on("py-numpy@1.13.3:", when="@0.23:0.23.1")
        depends_on("py-numpy@1.11.0:", when="@0.21-rc2:0.22")
        depends_on("py-scipy@0.19.1:", when="@0.23:0.23.1")
        depends_on("py-scipy@0.17:", when="@0.21-rc2:0.22")
        depends_on("py-threadpoolctl@2:", when="@0.23:0.23.1")
    # END DEPENDENCIES

