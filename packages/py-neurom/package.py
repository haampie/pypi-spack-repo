# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyNeurom(PythonPackage):
    # BEGIN VERSIONS
    version("3.2.8", sha256="a9bafa35c4e1d45cd77fc0c4b49310d80e0181dbda977989768f3c07773696cd", url="https://pypi.org/packages/72/8a/de5a50b702a16804cb0f7dd02ca3ee8adc78905d6a027949871f3cb55c3e/neurom-3.2.8-py3-none-any.whl")
    version("3.2.5", sha256="eb0b6f8de92225d997e7172192f09b2c073506d58c48e35421aa9e3a576fcf72", url="https://pypi.org/packages/ae/1c/bdd07d722114c1dd421d92f82c20c3aac1a22a24b5f6d6cb3b735134b2a5/neurom-3.2.5.tar.gz")
    version("3.2.4", sha256="a584e0979b54deee906dd716ea90de20773e20b527d83960d0fe655b0905eb4a", url="https://pypi.org/packages/88/b8/6b89a524f2e13f16ccaed9306088a31fdb1d48756d66aff376e4c91032d4/neurom-3.2.4.tar.gz")
    version("3.2.3", sha256="57b8ccafb092c080d090379d8aad225b8efa14085316112f6bac45a50aee8162", url="https://pypi.org/packages/48/d3/0f4855422805b0871036e402e1440be459f5a8e06ee1e53f51e17e330605/neurom-3.2.3.tar.gz")
    version("3.2.2", sha256="bc442cf5193289b893a66d5e541868f84bb120b03395b03ce2423c19729b92de", url="https://pypi.org/packages/34/95/5a1ba33f88dbc054bf5f9e5db5fb05a5f5d8a5fc63d6b071bd6dfdf036c9/neurom-3.2.2.tar.gz")
    version("3.2.1", sha256="72e1058cf000ecd9cf6531f584a3142d94d355917664f848471914673ba561e5", url="https://pypi.org/packages/41/b2/4720e89b382a48c6364895535553fda9c43028d3ce4fd8b475e48812741a/neurom-3.2.1.tar.gz")
    version("3.2.0", sha256="e8411565473388b76ef28b6bddd451982aa437f685736b6994278bee19b72b0d", url="https://pypi.org/packages/51/09/f9abc856ec5f9ca7fb5f145e48b5f39e5089c76f8913f14c609f812a8c71/neurom-3.2.0.tar.gz")
    version("3.1.0", sha256="1a711c3bd92a55b845f6e26ec6197e9208bf3d91762088eda9cb00ceea992f3a", url="https://pypi.org/packages/bb/aa/ceaed4403b5413a27f29e2e2ad1d436ec396d9e49000b59299dec8b3f32c/neurom-3.1.0.tar.gz")
    version("3.0.2", sha256="6f13e6134e1f5852bc2540e84ada53c6a479e76fb78dd4632f034d0337d3b1a5", url="https://pypi.org/packages/53/f1/b27d2672aa4aaaf0f58892eddce64552bcf6de9c70c92d5ea7953314751f/neurom-3.0.2.tar.gz")
    version("3.0.1", sha256="490dc3992ffe4941ceed44e50da574de637dfc0e0e88a5f1d7b80ff00ba29314", url="https://pypi.org/packages/9a/51/3fdb57d6e934d3aebbfc6cfe0c7cc371d2ea6c1bce7ec036f24960037ed6/neurom-3.0.1.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    variant("plotly", default=False)
    # END VARIANTS

    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-click@7:", when="@3.2.8:")
        depends_on("py-importlib-resources@1.3:", when="@3.2.8: ^python@:3.8")
        depends_on("py-matplotlib@3.2.1:", when="@3.2.8:")
        depends_on("py-morphio@3.3.6:", when="@3.2.8:")
        depends_on("py-numpy@1.8:", when="@3.2.8:")
        depends_on("py-pandas@1.0.5:", when="@3.2.8:")
        depends_on("py-plotly@3.6.0:", when="@3.2.8:+plotly")
        depends_on("py-psutil@5.5.1:", when="@3.2.8:+plotly")
        depends_on("py-pyyaml", when="@3.2.8:")
        depends_on("py-scipy@1.2.0:", when="@3.2.8:")
        depends_on("py-tqdm@4.8.4:", when="@3.2.8:")
    # END DEPENDENCIES

