# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPyobjcFrameworkQuartz(PythonPackage):
    # BEGIN VERSIONS
    version("10.2", sha256="9b947e081f5bd6cd01c99ab5d62c36500d2d6e8d3b87421c1cbb7f9c885555eb", url="https://pypi.org/packages/9d/be/1895258fdac58acfdddb3af29cf80619778689c9254133e82d1a345d42a1/pyobjc-framework-Quartz-10.2.tar.gz")
    version("10.1", sha256="b7439c0a3be9590d261cd2d340ba8dd24a75877b0be3ebce56e022a19cc05738", url="https://pypi.org/packages/db/f1/eb0012e9a0442a5001a0a906de334a6ed5ab638c851de7418edff949d3a1/pyobjc-framework-Quartz-10.1.tar.gz")
    version("10.0", sha256="ff7c938d9c8adff87d577d63e58f9be6e4bc75274384715fa7a20032a1ce8b0e", url="https://pypi.org/packages/3e/be/f2d67b25f6b047139a4b665e369f0db28ae0c64524f86a1f948eaa8ee39f/pyobjc-framework-Quartz-10.0.tar.gz")
    version("9.2", sha256="f586183b9b9ef7f165f0444a7b714ed965d79f6e92617caaf869150dcfd5a72b", url="https://pypi.org/packages/49/52/a56bbd76bba721f49fa07d34ac962414b95eb49a9b941fe4d3761f3e6934/pyobjc-framework-Quartz-9.2.tar.gz")
    version("9.1.1", sha256="8d03bc52bd6d90f00f274fd709b82e53dc5dfca19f3fc744997634e03faaa159", url="https://pypi.org/packages/7e/9d/d65d770d64547a9333c58d882ed5b508ea16203c8f3af090969412a6b77e/pyobjc-framework-Quartz-9.1.1.tar.gz")
    version("9.1", sha256="f6f48990cfb59eb0a3e61cac376b82a6a4f83453040844d97d164ff5086679e9", url="https://pypi.org/packages/5c/44/b3ea7ac62f93a7b236995881c2030633441d4cd8b034f233cc3402daa6b0/pyobjc-framework-Quartz-9.1.tar.gz")
    version("9.1-beta1", sha256="8e0177179f3798cbca24ad43dfe4b465ffd820a5049f1a20b251878b08580cd7", url="https://pypi.org/packages/3d/7f/b87012c558554b4e630a1627a02f04a2c515d444c60e3e230bd3d71a34ec/pyobjc-framework-Quartz-9.1b1.tar.gz")
    version("9.0.1", sha256="7e2e37fc5c01bbdc37c1355d886e6184d1977043d5a05d1d956573fa8503dac3", url="https://pypi.org/packages/ca/6f/64331d1ed37358d71d39423710724c34e943e6da4acaf9f0e73629b34a5d/pyobjc-framework-Quartz-9.0.1.tar.gz")
    version("9.0", sha256="c83639e88d13bec2395a77170a334d2570bf8119c16684c008fd1d0ba34bc290", url="https://pypi.org/packages/23/03/6c7d69c9fe7b479d5114ede4215326428c3fab3f935030f7e774185416c5/pyobjc-framework-Quartz-9.0.tar.gz")
    version("8.5.1", sha256="37ba625b6c240d4f5aea02f1672b16e53e39de07dbaf33751a61b5a0be7dc9fa", url="https://pypi.org/packages/8a/a6/6a4447d1e98606d1737d9fb0a04f0a9893419850c2ccd16990c5ee502424/pyobjc-framework-Quartz-8.5.1.tar.gz")
    version("8.5", sha256="d2bc5467a792ddc04814f12a1e9c2fcaf699a1c3ad3d4264cfdce6b9c7b10624", url="https://pypi.org/packages/26/bb/0118f93b98c3815666fb75e8021e9ba3901c36cc6586a4ca03af1910b777/pyobjc-framework-Quartz-8.5.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-pyobjc-core@10.2:", when="@10.2:")
        depends_on("py-pyobjc-core@10.1:", when="@10.1")
        depends_on("py-pyobjc-core@10:", when="@10:10.0")
        depends_on("py-pyobjc-framework-cocoa@10.2:", when="@10.2:")
        depends_on("py-pyobjc-framework-cocoa@10.1:", when="@10.1")
        depends_on("py-pyobjc-framework-cocoa@10:", when="@10:10.0")
    # END DEPENDENCIES

