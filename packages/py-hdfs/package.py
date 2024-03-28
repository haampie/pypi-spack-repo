# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyHdfs(PythonPackage):
    # BEGIN VERSIONS
    version("2.7.3", sha256="752a21e43f82197dce43697c73f454ba490838108c73a57a9247efb66d1c0479", url="https://pypi.org/packages/29/c7/1be559eb10cb7cac0d26373f18656c8037553619ddd4098e50b04ea8b4ab/hdfs-2.7.3.tar.gz")
    version("2.7.2", sha256="829b659f4ed8f114923690f5b1aa51d295e590bb25eb59ffee00acc1ce493a93", url="https://pypi.org/packages/a8/9f/723bf4d4c92e85562430b21b096fb8baa87ff39cd5d784ddd17df2b0146f/hdfs-2.7.2.tar.gz")
    version("2.7.1", sha256="9cd8ac73e03c83f9e588a5ee6ec9b1e953fb652ad8dd03da337a17de34a4c2cb", url="https://pypi.org/packages/22/df/9de81af7a3aaf0a6cc413d96b4879cf117c71df0076bdda7dce64a079771/hdfs-2.7.1.tar.gz")
    version("2.7.0", sha256="3428078ad1e83a2e2a11801c536ac2aa5094f5fabde5d1e7145bacbf4a599c1e", url="https://pypi.org/packages/fd/49/34f26fae99c5ebbfcdd81d6bd4aae21d42f018e1e14fa6301c227e45b24d/hdfs-2.7.0-py3-none-any.whl")
    version("2.6.0", sha256="05912125cfc68075387f271654dac185dc1aba8b347519f6a14d1395e39d7749", url="https://pypi.org/packages/08/f7/4c3fad73123a24d7394b6f40d1ec9c1cbf2e921cfea1797216ffd0a51fb1/hdfs-2.6.0-py3-none-any.whl")
    version("2.5.8", sha256="1be117549fc1285571bc51aedc15df5a203138dba02f9adfa26761b69a949370", url="https://pypi.org/packages/82/39/2c0879b1bcfd1f6ad078eb210d09dbce21072386a3997074ee91e60ddc5a/hdfs-2.5.8.tar.gz")
    version("2.5.7", sha256="ba512cc8d5e3f0452b7feb196174a0394e733078fe8dcb82572c66ba309dfe9d", url="https://pypi.org/packages/a0/a5/1433f90ac909e259c5fd38d75d8b730be93e40cf44a0d0f5ae2742aa1d7c/hdfs-2.5.7-py2-none-any.whl")
    version("2.5.6", sha256="7ac9c9ef7a24f6275b41c003ae9808542ecf1a696a13e1ad337664e8ebb40a48", url="https://pypi.org/packages/fc/2f/c25777cbc9eb31c8f5faf07ca016cd724963ada3781a0c02f29636a7cea2/hdfs-2.5.6.tar.gz")
    version("2.5.5", sha256="32a432c6d628ded09330a7475d8540ea3cba1bc890959859cf9b1e2565a2b7ba", url="https://pypi.org/packages/67/53/d9460f7b9c948f620543ddbcd0ea93bf9bcaa33d1ece3361d6a75a8c1b04/hdfs-2.5.5-py2-none-any.whl")
    version("2.5.4", sha256="51cf602f2c4bc19026139addafa005a4086df0b15fa75bea4444758c89f56095", url="https://pypi.org/packages/6f/f1/d1b86fc910dca68e3eb21c6bf555f6f2cbbeb07c5c7ff2a22d2a6a891eae/hdfs-2.5.4-py2-none-any.whl")
    version("2.1.0", sha256="a40fe99ccb03b5c3247b33a4110eb21b57405dd7c3f1b775e362e66c19b44bc6", url="https://pypi.org/packages/bb/ef/35af4764ea6c60bd14195ca78d4e831d154183f35cc4af4a0b3e01aa28ce/hdfs-2.1.0.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-docopt", when="@2.5.3:2.5.5,2.5.7,2.6:2.7.0")
        depends_on("py-requests@2.7:", when="@2.5.3:2.5.5,2.5.7,2.6:2.7.0")
        depends_on("py-six@1.9:", when="@2.5.3:2.5.5,2.5.7,2.6:2.7.0")
    # END DEPENDENCIES

