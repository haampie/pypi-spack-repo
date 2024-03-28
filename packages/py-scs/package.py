# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyScs(PythonPackage):
    # BEGIN VERSIONS
    version("3.2.2", sha256="7206a2ad27ca031d693d65cbcbcfc661498f3983838079a66579bcc784b25293", url="https://pypi.org/packages/27/b7/c42972975cfc21d6d28c08442f7738274219aef9ca8a7adef35b00827ad7/scs-3.2.2.tar.gz")
    version("2.1.1.post2", sha256="f816cfe3d4b4cff3ac2b8b96588c5960ddd2a3dc946bda6b09db04e7bc6577f2", url="https://pypi.org/packages/f2/6e/dbdd778c64c1920ae357a2013ea655d65a1f8b60f397d6e5549e4aafe8ec/scs-2.1.1-2.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    variant("blas64", default=False)
    variant("cuda", default=False)
    variant("cuda_arch", default=False)
    variant("extra_verbose", default=False)
    variant("float32", default=False)
    variant("int32", default=False)
    # END VARIANTS

    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-numpy@1.7:", when="@2:2.1.2")
        depends_on("py-scipy@0.13.2:", when="@2:2.1.2")
    # END DEPENDENCIES

