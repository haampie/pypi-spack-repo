# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyStatsmodels(PythonPackage):
    # BEGIN VERSIONS
    version("0.14.1", sha256="2260efdc1ef89f39c670a0bd8151b1d0843567781bcafec6cda0534eb47a94f6", url="https://pypi.org/packages/4b/80/c4e279a6a13468ae2f1f01af2a07ddb44f397ac4d7636af13c5b3b83dde1/statsmodels-0.14.1.tar.gz")
    version("0.14.0", sha256="6875c7d689e966d948f15eb816ab5616f4928706b180cf470fd5907ab6f647a4", url="https://pypi.org/packages/13/a3/a8bf1c9e6d0193f854d9a79cb86a65dac0866de64051ff96e35bc7ecedfe/statsmodels-0.14.0.tar.gz")
    version("0.14.0-rc0", sha256="645706abb00bc6c762135eff2d337609f4cf537fa14e586385b852b0eb2eb7ec", url="https://pypi.org/packages/13/62/be7ece587e395571988129848658f76ea9a0ba01f7e7e2f4765604c62191/statsmodels-0.14.0rc0.tar.gz")
    version("0.13.5", sha256="593526acae1c0fda0ea6c48439f67c3943094c542fe769f8b90fe9e6c6cc4871", url="https://pypi.org/packages/a4/7d/a919dbad04ec31741eee6a7f7df4a9a9e57e3b863900e48b079a6b832aab/statsmodels-0.13.5.tar.gz")
    version("0.13.4", sha256="8ee5d1b69f64bc0e9379667455ee3585849d5e6bcd3f3e48e58ba6cadadfead5", url="https://pypi.org/packages/89/eb/fee5161d621a23c31b83928614a9f2ee520854688b6bb60fde361a289f94/statsmodels-0.13.4.tar.gz")
    version("0.13.3", sha256="ed71df887334b1d332e71d33215122bdd54494dcb2248606b30bcfa6112e860a", url="https://pypi.org/packages/cf/5b/bd9ec64964c35f0ebdd368743f93d282c8cb42f3de05d4678bac92ac4d3e/statsmodels-0.13.3.tar.gz")
    version("0.13.2", sha256="77dc292c9939c036a476f1770f9d08976b05437daa229928da73231147cde7d4", url="https://pypi.org/packages/e1/4a/0eb4efa49cc352e2721e2aebfe8573264db2add195545ec3979c98040c3b/statsmodels-0.13.2.tar.gz")
    version("0.13.1", sha256="006ec8d896d238873af8178d5475203844f2c391194ed8d42ddac37f5ff77a69", url="https://pypi.org/packages/e7/86/8c95a2f43d8d66837f52fc0a2d9b4ea491e564789ee94d28f642d9d47ebc/statsmodels-0.13.1.tar.gz")
    version("0.13.0", sha256="f2efc02011b7240a9e851acd76ab81150a07d35c97021cb0517887539a328f8a", url="https://pypi.org/packages/9e/5e/4a2ade283411d1f46d6f8dd5fe951b9152062d55a20750cd5d4b556322bf/statsmodels-0.13.0.tar.gz")
    version("0.12.2", sha256="8ad7a7ae7cdd929095684118e3b05836c0ccb08b6a01fe984159475d174a1b10", url="https://pypi.org/packages/10/26/0fd61f95667e56fd597ecca715dff3623ed1122b6f895ed2b4dfb54afc04/statsmodels-0.12.2.tar.gz")
    version("0.12.1", sha256="a271b4ccec190148dccda25f0cbdcbf871f408fc1394a10a7dc1af4a62b91c8e", url="https://pypi.org/packages/e8/0f/473915873d4fe51e94a31c0571def3ea258e8b9f68ff6cf2294c9d58e6ec/statsmodels-0.12.1.tar.gz")
    version("0.10.2", sha256="9cd2194c6642a8754e85f9a6e6912cdf996bebf6ff715d3cc67f65dadfd37cc9", url="https://pypi.org/packages/9c/8f/a28c4f3a4192ea38a6cee092aac1d52ef69dbc65461b5969a296ef5246d5/statsmodels-0.10.2.tar.gz")
    version("0.10.1", sha256="320659a80f916c2edf9dfbe83512d9004bb562b72eedb7d9374562038697fa10", url="https://pypi.org/packages/d3/7d/4f1f18ad782d6b913aeff17d553859fed40751ecf15ef698c69811e622e6/statsmodels-0.10.1.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-numpy@1.22.3:1", when="@0.14.1: platform=windows ^python@3.10:3.10.0")
        depends_on("py-numpy@1.18.0:1", when="@0.14.1:")
        depends_on("py-packaging@21.3:", when="@0.14.1:")
        depends_on("py-pandas@1.0.0:2.1.0-rc0,2.1.1:", when="@0.14.1:")
        depends_on("py-patsy@0.5.4:", when="@0.14.1:")
        depends_on("py-scipy@1.4.0:1.9.1,1.9.3:", when="@0.14.1: platform=windows")
        depends_on("py-scipy@1.4.0:1.9.1,1.9.3:", when="@0.14.1:")

        # marker: os_name == "nt" and extra == "develop"
        # depends_on("py-pywinpty", when="@0.14.1:")
    # END DEPENDENCIES

