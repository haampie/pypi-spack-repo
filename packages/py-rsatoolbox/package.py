# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyRsatoolbox(PythonPackage):
    # BEGIN VERSIONS
    version("0.1.2", sha256="2d091cbaa33373bf9da4df5ca8d127f0e427431a3db726076090ab2d54fe1213", url="https://pypi.org/packages/80/53/2aeb853fa5bc3b921d9b3851528182518acb5b9f7fec34a343ddbcb79727/rsatoolbox-0.1.2.tar.gz")
    version("0.1.0", sha256="245f909d31909ba896b765fa51ea019510dd690c6bb8d04b178a9c76ec36dce9", url="https://pypi.org/packages/ff/e2/73b6433c3d0485b9b119774730b5799606d34b2a25742fd84c5d7f3d9b43/rsatoolbox-0.1.0.tar.gz")
    version("0.0.5", sha256="7ede9309755a6173c26f08fd36fa436a11993c7ae0fa9fce05f38be7af0dc6eb", url="https://pypi.org/packages/21/f2/9422df26f21c887e06e2dc07da8de8a3f0801cd96bd5f11ac84271e262a3/rsatoolbox-0.0.5.tar.gz")
    version("0.0.4", sha256="105174ab6da86ac3c3afdcc632addb031c30f351ca012cf15f4b7852dbbbf604", url="https://pypi.org/packages/7f/7f/e0ff526af80dd94ed5546a94dd56a1e4452a9c081359dbc8e3618e35889b/rsatoolbox-0.0.4-py3-none-any.whl")
    version("0.0.3", sha256="1a778b45c694f8d305c9ca19b309770da0bd24e16501218d2a51d1d93e26ad61", url="https://pypi.org/packages/fb/e6/ff89bfc9573c35c5b156219efef078a0c9fd1882a2b56f31e86e2b1e74d8/rsatoolbox-0.0.3-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("python@:3.11", when="@0.1.3:0.1.4,0.1.5.dev:0.1.5.dev46")
        depends_on("python@:3.10", when="@0.0.5:0.1.2,0.1.3.dev:0.1.3.dev32")
        depends_on("py-coverage", when="@:0.0.4")
        depends_on("py-h5py", when="@:0.0.4,0.1.5:")
        depends_on("py-joblib", when="@:0.0.4,0.1.5:")
        depends_on("py-matplotlib", when="@:0.0.4,0.1.5:")
        depends_on("py-numpy@1.21.2:", when="@0.0.3:0.0.4,0.1.5:")
        depends_on("py-pandas", when="@0.0.4,0.1.5:")
        depends_on("py-petname@2.2", when="@0.0.4")
        depends_on("py-scikit-image", when="@:0.0.4,0.1.5:")
        depends_on("py-scikit-learn", when="@:0.0.4,0.1.5:")
        depends_on("py-scipy", when="@:0.0.4,0.1.5:")
        depends_on("py-tqdm", when="@:0.0.4,0.1.5:")
    # END DEPENDENCIES

