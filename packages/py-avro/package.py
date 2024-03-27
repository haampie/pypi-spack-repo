##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyAvro(PythonPackage):
    version("1.11.1", sha256="f123623ecc648d0e20ce14f8ed85162140c13cc4b108865d1b2529fbfa06c008", url="https://pypi.org/packages/f2/90/c8ad84cfe84895be0f9d883b8154174866db352c32ff19826d2ed1f722db/avro-1.11.1.tar.gz")
    version("1.11.0", sha256="1206365cc30ad561493f735329857dd078533459cee4e928aec2505f341ce445", url="https://pypi.org/packages/82/d2/c8d425dcfed3427a580cbdfddd43ed0300821ea804e3e0a72f213a7cd273/avro-1.11.0.tar.gz")
    version("1.10.2", sha256="381b990cc4c4444743c3297348ffd46e0c3a5d7a17e15b2f4a9042f6e955c31a", url="https://pypi.org/packages/09/28/04d55db3488d65b4d22c3ba55878a418722d586129555b89a811d58c22d6/avro-1.10.2.tar.gz")
    version("1.8.2", sha256="8f9ee40830b70b5fb52a419711c9c4ad0336443a6fba7335060805f961b04b59", url="https://pypi.org/packages/eb/27/143f124a7498f841317a92ced877150c5cb8d28a4109ec39666485925d00/avro-1.8.2.tar.gz")


