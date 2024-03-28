# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyAnnotatedTypes(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("0.6.0", sha256="0641064de18ba7a25dee8f96403ebc39113d0cb953a01429249d5c7564666a43", url="https://pypi.org/packages/28/78/d31230046e58c207284c6b2c4e8d96e6d3cb4e52354721b944d3e1ee4aa5/annotated_types-0.6.0-py3-none-any.whl")
    version("0.5.0", sha256="58da39888f92c276ad970249761ebea80ba544b77acddaa1a4d6cf78287d45fd", url="https://pypi.org/packages/d8/f0/a2ee543a96cc624c35a9086f39b1ed2aa403c6d355dfe47a11ee5c64a164/annotated_types-0.5.0-py3-none-any.whl")
    version("0.4.0", sha256="ac27bcccc7a1447efe9a9bd1145766cc14a841b107a6040a799c260e83adf67d", url="https://pypi.org/packages/72/06/228244d7bc5db85719963cb957abd097ecc0e412053c70a4d3d5ef7cd5f3/annotated_types-0.4.0-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-typing-extensions@4:", when="@0.4: ^python@:3.8")
    # END DEPENDENCIES

