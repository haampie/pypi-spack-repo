# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyMultiqc(PythonPackage):
    # BEGIN VERSIONS
    version("1.15", sha256="2f20ed1dd15e9b7c94621f26f93192d0dd5eaae85ffe2d2be423f2f6fbb8c99b", url="https://pypi.org/packages/65/cd/ef0884f0abb38c9662b11f212f463cdb022ef504c512719ccf13d4c728eb/multiqc-1.15-py3-none-any.whl")
    version("1.14", sha256="077a8854a7c906383e10dedd6f14feb6cc949b96a94dbe18a4114b65d92bbbf7", url="https://pypi.org/packages/11/4c/0f85a278cd37406f195115e38281478e9933c50f389b7c4d989af42cb9d1/multiqc-1.14-py3-none-any.whl")
    version("1.13", sha256="7a4d0fbcf8e82e45f71bb6ef16a29788abf0a9ef9c99a9429582a2114cfd5dec", url="https://pypi.org/packages/1a/37/35f769e2be82ba3760a62a1cb39af42beee5334efa40cc7e151626e03c91/multiqc-1.13-py3-none-any.whl")
    version("1.7", sha256="02e6a7fac7cd9ed036dcc6c92b8f8bcacbd28983ba6be53afb35e08868bd2d68", url="https://pypi.org/packages/6b/c7/817d8ef024866e00625d94bbfa26e7a4131eedc166b3d65d7f54ebc90ed6/multiqc-1.7.tar.gz")
    version("1.5", sha256="fe0ffd2b0d1067365ba4e54ae8991f2f779c7c684b037549b617020ea883310a", url="https://pypi.org/packages/fa/3e/fbdcbaebadad2110eed3b4212ced58617cbd9badbfc728c5eabc53916b84/multiqc-1.5.tar.gz")
    version("1.3", sha256="cde17845680131e16521ace04235bb9496c78c44cdc7b5a0fb6fd93f4ad7a13b", url="https://pypi.org/packages/2c/af/1183857d4f2ade150fb2e22282ff11e6f5355419d129ca4ee7200022177f/multiqc-1.3.tar.gz")
    version("1.0", sha256="1a49331a3d3f2e591a6e9902bc99b16e9205731f0cd2d6eaeee0da3d0f0664c9", url="https://pypi.org/packages/61/79/92c1b7d04f87bf70405cbcd24ae059abd509b19b13b469934125311dbf9f/multiqc-1.0.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-click", when="@1.4,1.10:")
        depends_on("py-coloredlogs", when="@1.10:")
        depends_on("py-future@0.14.1:", when="@1.4,1.10:1.19")
        depends_on("py-jinja2@3.0.0:", when="@1.14:")
        depends_on("py-jinja2@2.9:", when="@1.4,1.10:1.13")
        depends_on("py-lzstring", when="@1.4,1.10:1.16")
        depends_on("py-markdown", when="@1.4,1.10:")
        depends_on("py-matplotlib@2.1.1:", when="@1.10:")
        depends_on("py-networkx@2.5.1:", when="@1.11:1.20")
        depends_on("py-numpy", when="@1.4,1.10:")
        depends_on("py-pyyaml@4:", when="@1.10:")
        depends_on("py-requests", when="@1.4,1.10:")
        depends_on("py-rich@10:", when="@1.11:")
        depends_on("py-rich-click", when="@1.13:")
        depends_on("py-simplejson", when="@1.4,1.10:1.15")
        depends_on("py-spectra@0.0.10:", when="@1.4,1.10:")
    # END DEPENDENCIES

