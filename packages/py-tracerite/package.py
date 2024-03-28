# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyTracerite(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("1.1.1", sha256="3a787a9ecb1a136ea9ce17e6328e414ec414a4f644130af4e1e330bec2dece29", url="https://pypi.org/packages/4e/71/127927fdd41dd577fd946c319cf9c012366f3ff9f048d0b0689dc72819ef/tracerite-1.1.1-py3-none-any.whl")
    version("1.1.0", sha256="4cccac04db05eeeabda45e72b57199e147fa2f73cf64d89cfd625df321bd2ab6", url="https://pypi.org/packages/6f/17/5cb3c7062752665f75b2bb32df59a5dd13ac535edaa65e1c23b929c165d8/tracerite-1.1.0-py3-none-any.whl")
    version("1.0.1", sha256="6b9a49c45674efab6f3a3b601eb881d2537c2742973caeb8f13916b9d508628c", url="https://pypi.org/packages/6d/9b/4c57d3b1883b94f8ddcd3742593d1fecff686da5a76ac9d4ea0d44f3e313/tracerite-1.0.1-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-html5tagger@1.2.1:")
    # END DEPENDENCIES

