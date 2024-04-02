# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PySpacy(PythonPackage):
    # BEGIN VERSIONS
    version("2.3.7", sha256="c0f2315fea23497662e28212f89af3a03667f97c867c597b599c37ab84092e22", url="https://pypi.org/packages/79/1c/7c5f7541eb883181b564a8c8ba15d21b2d7b8a38ae32f31763575cf8857d/spacy-2.3.7.tar.gz")
    version("2.3.2", sha256="818de26e0e383f64ccbe3db185574920de05923d8deac8bbb12113b9e33cee1f", url="https://pypi.org/packages/18/db/499f374339b522b6618234b93f25d2990692795ccce3152519ccc508586c/spacy-2.3.2.tar.gz")
    version("2.2.4", sha256="f0f3a67c5841e6e35d62c98f40ebb3d132587d3aba4f4dccac5056c4e90ff5b9", url="https://pypi.org/packages/92/1b/a982be17aa65d61121718f0309a2d8a56a04d6babee4c1a6882965f0d56d/spacy-2.2.4.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-blis@0.4:0.4.0.0,0.4.1:0.4", when="@2.2.4:2.3.2,3:3.0.0-alpha0,3.0.0.dev:3.0.0")
        depends_on("py-catalogue@0.0.7:1", when="@2.2.4:2.3.2,3:3.0.0-alpha0,3.0.0.dev:3.0.0")
        depends_on("py-cymem@2:", when="@2.1.8,2.2.4:2.3.2,3:3.0.0-alpha0,3.0.0.dev:3.0.0,3.7:3.7.0.0,3.7.1:3,4.0.0.dev2:")
        depends_on("py-murmurhash@0.28:1.0", when="@2.1.8,2.2.4:2.3.2,3:3.0.0-alpha0,3.0.0.dev:3.0.0,3.7:3.7.0.0,3.7.1:3,4.0.0.dev2:")
        depends_on("py-numpy@1.15.0:", when="@2.1.8,2.2.4:2.3.2,3:3.0.0-alpha0,3.0.0.dev:3.0.0")
        depends_on("py-plac@0.9.6:1.1", when="@2.2.4:2.3.2,3.0.0.dev:3.0.0.dev8")
        depends_on("py-preshed@3.0.2:3", when="@2.2.4:2.3.2,3:3.0.0-alpha0,3.0.0.dev:3.0.0,3.7:3.7.0.0,3.7.1:3,4.0.0.dev2:")
        depends_on("py-requests@2.13:", when="@2.1.8,2.2.4:2.3.2,3:3.0.0-alpha0,3.0.0.dev:3.0.0,3.7:3.7.0.0,3.7.1:3,4.0.0.dev2:")
        depends_on("py-setuptools", when="@2.2.4:2.3.2,3:3.0.0-alpha0,3.0.0.dev:3.0.0,3.7:3.7.0.0,3.7.1:3,4.0.0.dev2:")
        depends_on("py-srsly@1.0.2:1", when="@2.2.4:2.3.2")
        depends_on("py-thinc@7.4.1", when="@2.3:2.3.2")
        depends_on("py-thinc@7.4:7.4.0.0", when="@2.2.4:2.2")
        depends_on("py-tqdm@4.38:", when="@2.2.4:2.3.2,3:3.0.0-alpha0,3.0.0.dev:3.0.0,3.7:3.7.0.0,3.7.1:3,4.0.0.dev2:")
        depends_on("py-wasabi@0.4:0", when="@2.2.4:2.3.2,3.0.0.dev:3.0.0.dev8")
    # END DEPENDENCIES

