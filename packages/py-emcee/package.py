# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyEmcee(PythonPackage):
    # BEGIN VERSIONS
    version("3.1.1", sha256="e01d68a84725f6c0734c3c31394e88a7252b12fddb44efe981e10956a7028a93", url="https://pypi.org/packages/ca/41/62ddfd3847bbf9247dcf163de1ff79d56eaa1ac33bfb382f925ab22ba638/emcee-3.1.1-py2.py3-none-any.whl")
    version("3.0.2", sha256="bffaa2e1830d90f4e2ae42ca8db9bef67b73eefe90bdedacf58c9a1977966184", url="https://pypi.org/packages/97/f4/00151f5f843088337c6a53edd6cbb2df340f1044d23080c662f95219cc3f/emcee-3.0.2-py2.py3-none-any.whl")
    version("2.2.1", sha256="b83551e342b37311897906b3b8acf32979f4c5542e0a25786ada862d26241172", url="https://pypi.org/packages/3f/d3/7635106605dedccd08705beac53be4c43a8da1caad6be667adbf93ed0965/emcee-2.2.1.tar.gz")
    version("2.1.0", sha256="5ce1039a3d78fb9e7d53fcd768517585c5998193743bfcfaac407927d375ca63", url="https://pypi.org/packages/de/00/2358f12c98fa74ab58d78e6a4a4f9a8152fadf6ade2d809d98d771dcc31b/emcee-2.1.0.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-numpy", when="@3.0-rc2:")
    # END DEPENDENCIES

