# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyLightgbm(PythonPackage):
    # BEGIN VERSIONS
    version("4.3.0", sha256="006f5784a9bcee43e5a7e943dc4f02de1ba2ee7a7af1ee5f190d383f3b6c9ebe", url="https://pypi.org/packages/74/d1/2e4b02e4611ab36647639c4eea8c4520bb90f948563e00a3bec583a9f9f5/lightgbm-4.3.0.tar.gz")
    version("4.2.0", sha256="8a4d051df2ab2218998a16f7712e843ee9e96d8b09ffbfcc18533da127e0da02", url="https://pypi.org/packages/92/3d/209b257b7bcfaa39d54b9ab22db5097ff110c6a2f2399d5244c76c43aba2/lightgbm-4.2.0.tar.gz")
    version("4.1.0", sha256="bee59dd269a93b093f2c610d4a6683a7ea87c63d3ea35c622123ce2c020b2abc", url="https://pypi.org/packages/98/a9/01f50aee85949ba713733b69a3f0b42d39719a414a0e29bdf2a9f05ecc53/lightgbm-4.1.0.tar.gz")
    version("4.0.0", sha256="03d1b3903aa51cd9a5e3965941236f2a7bf5a69d7a76059dbf68fd9b4fc92d8f", url="https://pypi.org/packages/d8/61/4165b1caf07d661c4f0241534bbc18748e49e1ddb849fd9908c36c1d622c/lightgbm-4.0.0.tar.gz")
    version("3.3.5", sha256="10b8fbdcf851e4f68a1f02f38d99bdc44c7c7fb9b1a62dcf924a0d29ff73395c", url="https://pypi.org/packages/98/1f/fc5c183012f5fdd23e65d54ee09312d8b4dc9e4e39c227236f61942ef293/lightgbm-3.3.5.tar.gz")
    version("3.3.4", sha256="d6fa4d5b2a6f38d588434193f366757b20b301300b7385ca6924e2e402fc9063", url="https://pypi.org/packages/5d/aa/b82b32474a66da1234e4e8452f8448583d341692dc0575659586ba8b6673/lightgbm-3.3.4.tar.gz")
    version("3.3.3", sha256="857e559ae84a22963ce2b62168292969d21add30bc9246a84d4e7eedae67966d", url="https://pypi.org/packages/35/46/3c4ba33302ed23e741b1c7a9c0f50520dae5f71b20c899932e770dc974cb/lightgbm-3.3.3.tar.gz")
    version("3.3.2", sha256="5d25d16e77c844c297ece2044df57651139bc3c8ad8c4108916374267ac68b64", url="https://pypi.org/packages/8f/51/d272fa065be3be615d279be915705fa3824b86155e36c974cfb8d3ceec1e/lightgbm-3.3.2.tar.gz")
    version("3.3.1", sha256="5b9f31759ab4e94d9409deb03104c55b0a40058a6ccea804022046d926bc4904", url="https://pypi.org/packages/b7/31/dc662e3850e101008d8d87a0c4e82ee1e7818b7f403948d2575e7f3b0119/lightgbm-3.3.1.tar.gz")
    version("3.3.0", sha256="107ae7babbbda2c2f0e07484f0c53cdeb455e9219235f79dc4e1685d7541e505", url="https://pypi.org/packages/fe/a2/cf319c151fe2cd863c57bca972c837ea5bf2aa01fd2313aa39ee478a46e5/lightgbm-3.3.0.tar.gz")
    version("3.1.1", sha256="babece2e3613e97748a67ed45387bb0e984bdb1f4126e39f010fbfe7503c7b20", url="https://pypi.org/packages/cf/65/368931f1f234149e14fc6075dbeb1ad8a8aebb105aa11fe8631c72c1bdcf/lightgbm-3.1.1.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    variant("mpi", default=False)
    # END VARIANTS

    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-numpy", when="@2.0.6:2,4:")
        depends_on("py-scipy", when="@2.0.6:2,4:")
    # END DEPENDENCIES

