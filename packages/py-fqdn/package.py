##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyFqdn(PythonPackage):
    version("1.5.1", sha256="3a179af3761e4df6eb2e026ff9e1a3033d3587bf980a0b1b2e1e5d08d7358014", url="https://pypi.org/packages/cf/58/8acf1b3e91c58313ce5cb67df61001fc9dcd21be4fadb76c1a2d540e09ed/fqdn-1.5.1-py3-none-any.whl")
    version("1.5.0", sha256="4445552e29069c2955b83d7fb0cefb075d3eecb7d15ad7555088fd4ca8ad6048", url="https://pypi.org/packages/38/26/cd4b592e7b019c1f6f966cb7075656c543d654a3aa4d31ee91ed765f1fdd/fqdn-1.5.0-py3-none-any.whl")
    version("1.4.0", sha256="e935616ae81c9c60a22267593fe8e6af68cecc68549cc71bb9bfbcbbcb383386", url="https://pypi.org/packages/59/b4/db61c647f16c44a39b02b6d82aadad424a273d548f855d43d2317ef862b2/fqdn-1.4.0-py3-none-any.whl")
    version("1.3.1", sha256="d2df73b4cfebb9c9d7b544c99954493541dcbbc1e1a31b62bf9fe23746f42e2a", url="https://pypi.org/packages/1d/78/43bd38c602863dcf4959b9f3c404b4257a1715f99f685b3830dc8e04108d/fqdn-1.3.1-py3-none-any.whl")
    version("1.3.0", sha256="9ba7806f4d45c1312bcbdd9cb8550b532b3b4f3d4c1ac2cd2f067730d5e0c624", url="https://pypi.org/packages/6d/aa/a598368c0a1c26eecea4f17e77bf4280c66df0d5bdb2426c179edb16798d/fqdn-1.3.0-py3-none-any.whl")
    version("1.2.0", sha256="c4267e53fe717b4e45ea1ad2bb743d329f296862209ada55e1a937eb46f3d301", url="https://pypi.org/packages/09/09/33258e150a9971e2524bfa5e40bea23135b351f715a9a80762ab9a636e38/fqdn-1.2.0-py3-none-any.whl")
    version("1.1.0", sha256="0823229ec0be52904c43a3be5a3c1a43e8562b5ea50912a73bb757bd406b8aeb", url="https://pypi.org/packages/1e/9c/d27ecdcf967bcf98bf851f3eb5e29749d6e85ee834d0be9060451a671ba4/fqdn-1.1.0.tar.gz")
    version("1.0.2", sha256="2fb16cf5e00e2b0a8ece3080f98b60ebed544a35be443f1b9fc91ad0d8ad05c1", url="https://pypi.org/packages/7a/56/eabb3b0a5ad7c2a2d4a93b0da5897874e2724acf30d02c8e0e598ac89a80/fqdn-1.0.2.tar.gz")
    version("1.0.1", sha256="7534e596286c31590b7b139f93421e7ad900b8792d882d100ff8da7079155c9a", url="https://pypi.org/packages/da/1a/63c33c666c47e2a7e2425fa93c687a8486e14878de3ab6df0699fb8d436e/fqdn-1.0.1.tar.gz")
    version("1.0.0", sha256="ca26c7e182bdc205c4913747f3432d7b0e30aaeb32b327cba0bd33662eb698c7", url="https://pypi.org/packages/d1/9a/7bd74c3fc317895fa85cca0763456e26847478d7a76f80f2cdc5490d5ce1/fqdn-1.0.0.tar.gz")

    with default_args(type="run"):
        depends_on("py-cached-property@1.3:", when="@1.2:1.3")

