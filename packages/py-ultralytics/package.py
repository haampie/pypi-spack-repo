# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyUltralytics(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("8.0.50", sha256="60c409292cab97ba9893cf7a60a0b2a385f82c7a7f007206a53c0075737dda57", url="https://pypi.org/packages/07/d0/97e48941aa91f5c87f576e4268e190d585d011a5a0afd54171522d1bc37f/ultralytics-8.0.50-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("python@3.7:", when="@:8.0.151")
        depends_on("py-certifi@2022.12:", when="@8.0.47:8.0.50")
        depends_on("py-matplotlib@3.2.2:", when="@:8.0.128,8.0.130:8.0.180")
        depends_on("py-numpy@1.18.5:", when="@:8.0.53")
        depends_on("py-opencv-python@4.6:", when="@:8.0.128,8.0.130:")
        depends_on("py-pandas@1.1.4:", when="@:8.0.128,8.0.130:")
        depends_on("py-pillow@7.1.2:", when="@:8.0.128,8.0.130:")
        depends_on("py-psutil", when="@:8.0.128,8.0.130:")
        depends_on("py-pyyaml@5.3.1:", when="@:8.0.128,8.0.130:")
        depends_on("py-requests@2.23:", when="@:8.0.128,8.0.130:")
        depends_on("py-scipy@1.4.1:", when="@:8.0.128,8.0.130:")
        depends_on("py-seaborn@0.11.0:", when="@:8.0.128,8.0.130:")
        depends_on("py-sentry-sdk", when="@:8.0.109")
        depends_on("py-tensorboard@2.4.1:", when="@:8.0.50")
        depends_on("py-thop@0.1.1:", when="@:8.0.103,8.0.190:")
        depends_on("py-torch@1.7:", when="@:8.0.128,8.0.130:8.0.151")
        depends_on("py-torchvision@0.8.1:", when="@:8.0.128,8.0.130:8.0.151")
        depends_on("py-tqdm@4.64:", when="@:8.0.128,8.0.130:")
    # END DEPENDENCIES

