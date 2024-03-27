##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyDatabricksCli(PythonPackage):
    version("0.18.0", sha256="1176a5f42d3e8af4abfc915446fb23abc44513e325c436725f5898cbb9e3384b", url="https://pypi.org/packages/ae/a3/d56f8382c40899301f327d1c881278b09c9b8bc301c2c111633a0346d06e/databricks_cli-0.18.0-py2.py3-none-any.whl")
    version("0.17.8", sha256="1d5ef6520ea3ed403d58f24538641bd8eeb163621f5054205fcf643578698579", url="https://pypi.org/packages/0b/5f/e032f8679bf4c7f88ac68d285b0caa53bf428127e5e60dd7e6c99585f582/databricks-cli-0.17.8.tar.gz")
    version("0.17.7", sha256="5a545063449f3b9ad904644c0f251058485e29e564dedf8d4e4a7b45caf9549b", url="https://pypi.org/packages/73/22/274c985aaea6617ece986c8c7d458543758a0e28f53ab9f41174ba381f59/databricks-cli-0.17.7.tar.gz")
    version("0.17.6", sha256="7fea8b4e47ac38bd4eaad8a76e38a6916419df930ad1c615a6b43feb427672c4", url="https://pypi.org/packages/f7/e1/248bc0b4400b2b307c54058079cacdc25cca7ceb2a3288b2be7df746ebaa/databricks-cli-0.17.6.tar.gz")
    version("0.17.5", sha256="4cd1c3b152d943db318371139de60f287659cfe938cbf3c31cdd8d5b1925f7c3", url="https://pypi.org/packages/50/93/d8a137ae1a3413feea11657ddba02e72f76114510c73dcb18b20a205e704/databricks-cli-0.17.5.tar.gz")
    version("0.17.4", sha256="bc0c4dd082f033cb6d7978cacaca5261698efe3a4c70f52f98762c38db925ce0", url="https://pypi.org/packages/ca/18/be4b07af8cf405e60b665e8edc9bf310a6328fdbea5aca5504ed26907d12/databricks-cli-0.17.4.tar.gz")
    version("0.17.3", sha256="2f00f3e70e859809f0595885ec76fc73ba60ad0cccd69564f7df5d95b6c90066", url="https://pypi.org/packages/0d/90/c292931799688d2d790f4c738562eb274ad64f7b8dc6aee1cab25c7e590c/databricks-cli-0.17.3.tar.gz")
    version("0.17.2", sha256="16bda8def2fd8e361e8f355a016841bc1b8a87da25047f5339acf559fa55f1fb", url="https://pypi.org/packages/30/aa/098399e3a438ec04a8d0af551f1f55e05ca7265fe2a1d02e4c9439570f22/databricks-cli-0.17.2.tar.gz")
    version("0.17.1", sha256="65f15c3df2ffbaa444c05f332bb28ab889fac0c9da1853b1e96fdefec3c69c0c", url="https://pypi.org/packages/c7/05/283eddcba2b196a7ea532eb7d67ab831776f8cd269112eb42be83cb5d49c/databricks-cli-0.17.1.tar.gz")
    version("0.17.0", sha256="4afa17da73c6e93ca09c5fdf24fa3552965854bbbc3f1428cf4d27edb751b72c", url="https://pypi.org/packages/92/97/582cb36b56b94132d0fefe6e18e77d09168235329f55168c83cc0cf65726/databricks-cli-0.17.0.tar.gz")
    version("0.14.3", sha256="bdf89a3917a3f8f8b99163e38d40e66dc478c7408954747f145cd09816b05e2c", url="https://pypi.org/packages/bc/af/631375abc29e59cedfa4467a5f7755503ba19898890751e1f2636ef02f92/databricks-cli-0.14.3.tar.gz")

    with default_args(type="run"):
        depends_on("py-click@7:", when="@0.18:")
        depends_on("py-oauthlib@3.1:", when="@0.18:")
        depends_on("py-pyjwt@1.7:", when="@0.18:")
        depends_on("py-requests@2.17.3:", when="@0.18:")
        depends_on("py-six@1.10:", when="@0.18:")
        depends_on("py-tabulate@0.7.7:", when="@0.18:")
        depends_on("py-urllib3@1.26.7:", when="@0.18:")

