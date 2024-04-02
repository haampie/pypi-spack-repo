# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyTorchvision(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("0.2.2.post3", sha256="4911188843c10a2c66e8f3d0c3989647e626a7a75b8387e2dbbb3e5aa96887ad", url="https://pypi.org/packages/fb/01/03fd7e503c16b3dc262483e5555ad40974ab5da8b9879e164b56c1f4ef6f/torchvision-0.2.2.post3-py2.py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    variant("ffmpeg", default=False, description="ffmpeg")
    variant("jpeg", default=False, description="jpeg")
    variant("nvjpeg", default=False, description="nvjpeg")
    variant("png", default=False, description="png")
    variant("video_codec", default=False, description="video_codec")
    # END VARIANTS

    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-numpy", when="@0.1.7:")
        depends_on("py-pillow@4.1.1:", when="@0.2:")
        depends_on("py-six", when="@0.1.7:")
        depends_on("py-torch", when="@0.1.7:")
    # END DEPENDENCIES

