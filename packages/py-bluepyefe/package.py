# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyBluepyefe(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("2.3.6", sha256="3b49fe8306910bb0a1f537a6bb0e145e61211f12796427fdd1d02858040a6ff9", url="https://pypi.org/packages/2e/da/39a31517235c7370b098c3635623b0653366daf609a77dcad3dd2765aef8/bluepyefe-2.3.6-py3-none-any.whl")
    version("2.2.18", sha256="9b5ceee89c9b94bfe39bb116afae93a0fb2952d4579c45b15fbbd3cb8c845a06", url="https://pypi.org/packages/be/05/cd88b95bdacababe014740bfb8983bfc554ef6719b4609190fbf7b29a9f7/bluepyefe-2.2.18-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-efel", when="@0.3.123:0,2.1.26:")
        depends_on("py-h5py", when="@2.1.26:")
        depends_on("py-igor", when="@0.3.123:0,2.1.26:2.2.25")
        depends_on("py-igor2", when="@2.2.30:")
        depends_on("py-matplotlib", when="@0.3.123:0,2.1.26:")
        depends_on("py-neo", when="@0.3.123:0,2.1.26:")
        depends_on("py-numpy@:1.23", when="@2.2.11:2.2.25")
        depends_on("py-numpy", when="@0.4.7:0,2.1.26:2.2.2,2.2.30:")
        depends_on("py-scipy", when="@0.3.123:0,2.1.26:")
    # END DEPENDENCIES

