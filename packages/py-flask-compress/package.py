# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyFlaskCompress(PythonPackage):
    # BEGIN VERSIONS
    version("1.14", sha256="b86c9808f0f38ea2246c9730972cf978f2cdf6a9a1a69102ba81e07891e6b26c", url="https://pypi.org/packages/3f/d2/23fd656d38d4c896fa14371990b9978722c48a30d0edcf6b5f7054775a07/Flask_Compress-1.14-py3-none-any.whl")
    version("1.13", sha256="1128f71fbd788393ce26830c51f8b5a1a7a4d085e79a21a5cddf4c057dcd559b", url="https://pypi.org/packages/20/80/8cdb28e467d3ffdc221992145114a709c1e7c011b84c66bc250e27596286/Flask_Compress-1.13-py3-none-any.whl")
    version("1.12", sha256="9f4e40211755e86f85e5eb7d414856ef1e8751912caa78d62853169400335f0c", url="https://pypi.org/packages/d5/08/91ffc9506cb569f45cc4781ac8d35c6be19b9c3c8b1f8bc77aed56a46b53/Flask_Compress-1.12-py3-none-any.whl")
    version("1.11", sha256="7ccc4102104a63e6207f39eb307f99aebbfbaf4e70992d727440cff29119a0a0", url="https://pypi.org/packages/b2/95/581bc6018dcef72593ebbbb0ac84050ce97ee36fa174014145d66765552b/Flask_Compress-1.11-py3-none-any.whl")
    version("1.10.1", sha256="a6c2d1ff51771e9b39d7a612754f4cb4e8af20cebe16b02fd19d98d8dd6966e5", url="https://pypi.org/packages/75/fa/a3c96f3f367ad1d6532fa8394c9a6f5879513868207096f6b41f4168b342/Flask_Compress-1.10.1-py3-none-any.whl")
    version("1.10.0", sha256="0d0ac484e3b0bd58351fc387ace0c9c4c6ed2f8102cef203cb572175baf82b94", url="https://pypi.org/packages/ba/78/41627459e46db2434ed5196b1f7a210ed3c162d7e4a24e6dbdc172765989/Flask_Compress-1.10.0-py3-none-any.whl")
    version("1.9.0", sha256="6dc80e18b0304ff3155461fb4b155eb8be3e929e6f7bbdd90c723e1c554e2368", url="https://pypi.org/packages/c6/d5/69b13600230d24310b98a52da561113fc01a5c17acf77152761eef3e50f1/Flask_Compress-1.9.0-py3-none-any.whl")
    version("1.8.0", sha256="fda1b8a834176c485c7018a4b9326599311afbaaa08a715771c1fd9021f871fa", url="https://pypi.org/packages/b2/7a/9c4641f975fb9daaf945dc39da6a52fd5693ab3bbc2d53780eab3b5106f4/Flask_Compress-1.8.0-py3-none-any.whl")
    version("1.7.0", sha256="965e832684160871b5268f97879c5e85a88569cc6e3e353a7779215664eefdad", url="https://pypi.org/packages/de/eb/6bb0f8cb872167752eab8b06b67724566342de873dcfd85faaf7761944d9/Flask-Compress-1.7.0.tar.gz")
    version("1.6.0", sha256="2d551211eca86e684c170491c857692b6c4c94a147ab6b41995decac8ee63567", url="https://pypi.org/packages/2f/83/dfac4e00a20b094a6c7870e97fc30e3e9e2eedc41c1d02c13d0539810dc2/Flask-Compress-1.6.0.tar.gz")
    version("1.4.0", sha256="468693f4ddd11ac6a41bca4eb5f94b071b763256d54136f77957cfee635badb3", url="https://pypi.org/packages/0e/2a/378bd072928f6d92fd8c417d66b00c757dc361c0405a46a0134de6fd323d/Flask-Compress-1.4.0.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-brotli", when="@1.8:")
        depends_on("py-flask", when="@1.8:")
    # END DEPENDENCIES

