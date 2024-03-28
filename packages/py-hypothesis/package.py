# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyHypothesis(PythonPackage):
    # BEGIN VERSIONS
    version("6.99.9", sha256="1b19bca587d8ead95875d30a38f38211d5a8de72f4df86953cc6fc060aff740e", url="https://pypi.org/packages/3a/5b/677e216d890db363b68c296f4202bd088c0ec233c9225334cc3d5dcd7457/hypothesis-6.99.9-py3-none-any.whl")
    version("6.99.8", sha256="8b5175a906c0a11967c3a04eeb17c42b4b395cacd02a246ce926613189a14279", url="https://pypi.org/packages/6a/87/102586821543e55e4d1885ce5303b6990d2a182c22aaefd699dc0c0c3267/hypothesis-6.99.8-py3-none-any.whl")
    version("6.99.7", sha256="d6fe9518613ef2c292007e059a49422c90413370cd955d3c99d4f31a47ac927e", url="https://pypi.org/packages/87/ed/da48c79788030c09e8c114577b66a7c685c6caf11661bf39a4247fef021d/hypothesis-6.99.7-py3-none-any.whl")
    version("6.99.6", sha256="f5287e0ca8be94b2129483e1268639f8675c8c041d1b1756561a374575659940", url="https://pypi.org/packages/1e/66/169602c24f9fbe5c4f64102acf2a1623f539bec591bec309f57ca81b6a25/hypothesis-6.99.6-py3-none-any.whl")
    version("6.99.5", sha256="0ab4968fa4c38ba6d3cd9f54f3d637e3c72fe136bff11373355f2e06416c6a7d", url="https://pypi.org/packages/ab/42/ab93044758baf2a303376f35408ce02783b7af6a553e991c578f21946483/hypothesis-6.99.5-py3-none-any.whl")
    version("6.99.4", sha256="20ca59622b002b3b4d6c5913c37149e233240e7d7ea632e8da7f77629b2f7040", url="https://pypi.org/packages/aa/3b/b3c46849e967a56519c5d1dfbdcb0069034e8616bbdddefed65bcb991bae/hypothesis-6.99.4-py3-none-any.whl")
    version("6.99.3", sha256="cd211270c21fc2f4eb76e1e7052cb3d46450cdec5660a16973ae218f84eb4d73", url="https://pypi.org/packages/c8/16/acc95d4ad0546dfb87019c2db520a9764f5b16e28488903a5439f2aca9ea/hypothesis-6.99.3-py3-none-any.whl")
    version("6.99.2", sha256="f277f6ccb074f39d51c7f32ba5a0ff640dba9b71ef69ea1e1e09b6f7c25302f5", url="https://pypi.org/packages/7c/b6/3a4fda35a8abbd0af32b1bf52fb79b54ccaef05e70a76709fd1b903162d8/hypothesis-6.99.2-py3-none-any.whl")
    version("6.99.1", sha256="6521173a51a3b4b3970aa96669df44443c6b742fbd56a478af8cd1eb925114a1", url="https://pypi.org/packages/90/6d/2bb0aeda3d177e1fe35d01cfd741202f6bbd2c9ee59a500b0c7a8718a9ad/hypothesis-6.99.1-py3-none-any.whl")
    version("6.99.0", sha256="6e59b66322ff9d066e39c511af40d107c1d944891bbf608a7f03c5e7c8dfaef4", url="https://pypi.org/packages/df/4a/529fc7aae0044f994669bf14fec5b5d8d7f24d635c371a46c98d0d9582f0/hypothesis-6.99.0-py3-none-any.whl")
    version("6.23.1", sha256="e1c5c4a7e1f9a1a1da03cf6a148703333c468fb036f3cd785da1210c23648a4f", url="https://pypi.org/packages/d2/46/dd7c1999679942dddf83cc8aa6d0769500c05c7d2cdd5f992900ad977d88/hypothesis-6.23.1-py3-none-any.whl")
    version("5.3.0", sha256="bfdac4e9ca4c6f9850be67699293dba3016f9c0521a73f5210f3d647888d6256", url="https://pypi.org/packages/a1/7e/75407f8633f20e4254effc8209b52b93197fa2ddf000e20fff8edccb0e1c/hypothesis-5.3.0-py3-none-any.whl")
    version("4.57.1", sha256="94f0910bc87e0ae8c098f4ada28dfdc381245e0c8079c674292b417dbde144b5", url="https://pypi.org/packages/f3/3b/16830a2b289079c5e8933344bde6326adf1fa4fbe4b4510083fab750eba9/hypothesis-4.57.1-py3-none-any.whl")
    version("4.41.2", sha256="acd47600deb55e9c2c98de6deef23384160ed0fdaafb6753146e556c077d3c78", url="https://pypi.org/packages/bc/af/392c2f90d69c6d3c5214a9c25fc7d336e1e600adf7ff80638139f12f7ae5/hypothesis-4.41.2-py3-none-any.whl")
    version("4.24.3", sha256="a2daa11895e1b93a0d11efd15bbc95b56309233a39e0ab6981df207199ed6a04", url="https://pypi.org/packages/ee/4b/717286b878b4f16a1bea68281612f82763a7472b3e1021f76e968872c7db/hypothesis-4.24.3-py3-none-any.whl")
    version("4.7.2", sha256="e3894dcda1f044c560882afe8485235c9e86736363a2c4658f7c13a5fc3f1aa8", url="https://pypi.org/packages/51/f3/d2522da59a8578ca58866bc873b92d5e7cc7a6a822af9947914613587762/hypothesis-4.7.2-py3-none-any.whl")
    version("3.7.0", sha256="0fea49d08f2d5884f014151a5af6fb48d862f6ad567ffc4a2e84abf2f186c423", url="https://pypi.org/packages/e1/cb/a444d3e96721240a86c7acc243b55355bf3b7161286e10184f57d30c51dc/hypothesis-3.7.0.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    variant("django", default=False)
    variant("numpy", default=False)
    variant("pandas", default=False)
    # END VARIANTS

    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-attrs@22.2:", when="@6.91.1:")
        depends_on("py-attrs@19.2:", when="@4.38.2:6.91.0")
        depends_on("py-django@3.2:", when="@6.54.2:+django")
        depends_on("py-django@2.2:", when="@5.8.1:6.54.1+django")
        depends_on("py-django@1.11:", when="@4.24.6:5.8.0+django")
        depends_on("py-exceptiongroup@1.0.0:", when="@6.56.4: ^python@:3.10")
        depends_on("py-numpy@1.17.3:", when="@6.79.4:+numpy")
        depends_on("py-numpy@1.9:", when="@3.19,4.24.6:6.72,6.74:6.74.0+numpy")
        depends_on("py-pandas@1.1.0:", when="@6.73,6.74.1:+pandas")
        depends_on("py-pandas@0.25.0:", when="@5.41.3:6.52+pandas")
        depends_on("py-pandas@0.19.0:", when="@4.24.6:5.41.2+pandas")
        depends_on("py-pytz@2014:", when="@4.56.1:6.30+django")
        depends_on("py-pytz", when="@3.19,4.24.6:4.56.0+django")
        depends_on("py-sortedcontainers@2.1:", when="@4.55:")
    # END DEPENDENCIES

