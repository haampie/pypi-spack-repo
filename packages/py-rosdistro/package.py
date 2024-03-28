# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyRosdistro(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("0.9.0", sha256="1e22e084f9bc45960c4c0614df813b51991680b133e8e18ddd93d3b14f52d2b6", url="https://pypi.org/packages/af/7f/644ccbd6218a6ec36c4a478f5607ff3fa36e1b250d6187d97b3393a332b2/rosdistro-0.9.0-py3-none-any.whl")
    version("0.8.3", sha256="4d61b3d5a3c0661767ecb947c75fa3fd4be06d7f5788ec7d75d0fb734049c921", url="https://pypi.org/packages/8e/d2/9edf2b1ee6d9e762ca136eff03c9f4883d5d00d330946cbb2897adb3395f/rosdistro-0.8.3-py3-none-any.whl")
    version("0.8.2", sha256="17de781a7af83ffaf07316a886a556b22b13ca1a3171aa1b844e57ccb65c5d5d", url="https://pypi.org/packages/87/83/9c348b16a6b27364123f4f777f2d502e1bd59f9b39e43641f4db8b9cbc84/rosdistro-0.8.2-py3-none-any.whl")
    version("0.8.1", sha256="410ee277db4e41ce820c729174fa5df631458a1259258d82e214336260c6d9df", url="https://pypi.org/packages/6e/42/3e09940d333620ebda4d07431014521092910de753782b00138aa37a35af/rosdistro-0.8.1-py3-none-any.whl")
    version("0.8.0", sha256="f344e35cf5f4c27e885379dc9b819d226270fbc3caae4175316af3c73c46b03a", url="https://pypi.org/packages/ef/ef/b655c9734b38a97fa706891ea888bfb377eff5ff15179c15546f99a4967d/rosdistro-0.8.0-py3-none-any.whl")
    version("0.7.5", sha256="abc84ff15a01407ac29e4d28c6407017a768d6ce243e2232747f8388436d3b05", url="https://pypi.org/packages/e4/64/14eb0e9c18a790dbaed85ae832dcf8e722543526fdda20f0a4d1a3f044ca/rosdistro-0.7.5-py3-none-any.whl")
    version("0.7.4", sha256="65e523f9c28694f1b64f4ca82f289871cf479ef6930752cde4a1414981e8c344", url="https://pypi.org/packages/a7/ec/448c490f3695cd5448280ed74620e0dba629ecb7fd4de519fd037be78a9d/rosdistro-0.7.4-py3-none-any.whl")
    version("0.7.3", sha256="63c57d5342615844108d160e0765c4b2bff3d9860e962bcfd98c7a5b41a938f9", url="https://pypi.org/packages/64/ac/b639706f07e085ad1da46f6f084d9315f52c5ce03f5e53a44f1bef10a146/rosdistro-0.7.3-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-catkin-pkg", when="@0.6.9:")
        depends_on("py-pyyaml", when="@0.6.9:")
        depends_on("py-rospkg", when="@0.6.9:")
        depends_on("py-setuptools", when="@0.6.9:")
    # END DEPENDENCIES

