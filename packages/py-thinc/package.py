# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyThinc(PythonPackage):
    # BEGIN VERSIONS
    version("7.4.1", sha256="0139fa84dc9b8d88af15e648fc4ae13d899b8b5e49cb26a8f4a0604ee9ad8a9e", url="https://pypi.org/packages/17/5d/4343b3a79565af88ba2d53818d97995c3c239288f2565b826865f376d271/thinc-7.4.1.tar.gz")
    version("7.4.0", sha256="523e9be1bfaa3ed1d03d406ce451b6b4793a9719d5b83d2ea6b3398b96bc58b8", url="https://pypi.org/packages/f3/0b/10bbd6c847ea4cf2c54f6857ac3d4d0dda269ecb75ec37630ac860280571/thinc-7.4.0.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-blis@0.4:0.4.0.0,0.4.1:0.4", when="@:7.1.0,7.2:7.2.0.0,7.3:7.3.0.0,7.3.1:7.4.1,8.0.0.dev:8.0.0.dev0")
        depends_on("py-catalogue@0.0.7:1", when="@7.4:7.4.1,8.0.0.dev:8.0.0.dev0")
        depends_on("py-cymem@2:", when="@:7.1.0,7.2:7.2.0.0,7.3:7.3.0.0,7.3.1:7.4.1,8:8.0.0-alpha18,8.0.0.dev:8.0.0,8.2.1:8,9.0.0.dev4:")
        depends_on("py-murmurhash@0.28:1.0", when="@:7.1.0,7.2:7.2.0.0,7.3:7.3.0.0,7.3.1:7.4.1,8:8.0.0-alpha18,8.0.0.dev:8.0.0")
        depends_on("py-numpy@1.7:", when="@:7.1.0,7.2:7.2.0.0,7.3:7.3.0.0,7.3.1:7.4.1,8:8.0.0-alpha18,8.0.0.dev:8.0.0")
        depends_on("py-plac@0.9.6:1.1", when="@7.3.1:7.4.1")
        depends_on("py-preshed@1.0.1:3", when="@7.2:7.2.0.0,7.3:7.3.0.0,7.3.1:7.4.1")
        depends_on("py-srsly@0.0.6:1", when="@:7.1.0,7.2:7.2.0.0,7.3:7.3.0.0,7.3.1:7.4.1")
        depends_on("py-tqdm@4.10:", when="@:7.1.0,7.2:7.2.0.0,7.3:7.3.0.0,7.3.1:7.4.1")
        depends_on("py-wasabi@0.0.9:0", when="@:7.1.0,7.2:7.2.0.0,7.3:7.3.0.0,7.3.1:7.4.1")
    # END DEPENDENCIES

