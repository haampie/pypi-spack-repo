# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyAsdfTransformSchemas(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("0.5.0", sha256="9f91bfd964b905d0deff269b057a75b2b3745c462c3b9e7897242844fbc4cfe8", url="https://pypi.org/packages/ad/66/4332d3d13c205a7d95f89c0fba3f6aaf5c0b549189d6d04ba72f95c17b87/asdf_transform_schemas-0.5.0-py3-none-any.whl")
    version("0.4.0", sha256="fed6cab061ee759c97a30bfe4ec06fdea7af72268b355301082e97994e4313e8", url="https://pypi.org/packages/53/0a/4fc758de9a49065c4d147d9b8772b8bdc988108a774ea64d0a35aa22e196/asdf_transform_schemas-0.4.0-py3-none-any.whl")
    version("0.3.0", sha256="b0dbcae1bd15afea52d67209d8a75533c0ad3713e7e0eb55d968ff70393cc7fc", url="https://pypi.org/packages/2a/f2/b184f660552be16a3bd00b5c70eeb3abff9d154ccfbb1c868482a9559de0/asdf_transform_schemas-0.3.0-py3-none-any.whl")
    version("0.2.2", sha256="03425e67ce48b3c783d29ba2b6e19fa6055cd0146d779e4ffab117ae6dfbe322", url="https://pypi.org/packages/c5/74/e50775e69b43bc248ffcf1b05ce322d5ae0362165a9772ca35e0e231fdeb/asdf_transform_schemas-0.2.2-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("python@3.9:", when="@0.5:")
        depends_on("py-asdf-standard@1.1:", when="@0.5:")
        depends_on("py-asdf-standard@1.0.1:", when="@0.2.1:0.4")
        depends_on("py-importlib-resources@3:", when="@0.2.1:0.4 ^python@:3.8")
    # END DEPENDENCIES

