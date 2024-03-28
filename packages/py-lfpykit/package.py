# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyLfpykit(PythonPackage):
    # BEGIN VERSIONS
    version("0.5.1", sha256="25509ac8d3692c31231551d30c88720b49141fe6b8ed217efc54b0c59c68a076", url="https://pypi.org/packages/6b/be/5a72ee4deb4f1410e3266874447a38adde6f56cddf3e958506647f2e3ecc/LFPykit-0.5.1-py3-none-any.whl")
    version("0.5", sha256="3f87f12466ec905890ea854eb1444d9709a72218aefe683cb762f10c9df51ea2", url="https://pypi.org/packages/79/c2/3d26ea734e2195e6320fec4a6e50ffa2c3ac3e14b923376ead8c4f62257f/LFPykit-0.5-py3-none-any.whl")
    version("0.5-rc0", sha256="91f6248fb333d5c341a61acb56b4ed6810ff6c0fc6d95eb17a99e7cee9e77b7d", url="https://pypi.org/packages/03/c5/a3e776f46c61b4183cdae8d18751788203ec60b6dafc31403b496442a6cd/LFPykit-0.5rc0-py3-none-any.whl")
    version("0.4", sha256="e32d154585fe6f83e337b12bd1f84b91f6ca16e9407739011b0b667b263cba24", url="https://pypi.org/packages/85/01/25ed6c93bfaac3a2c74bfa315416a0040313c10331c9dbd76eb993dd2c6c/LFPykit-0.4-py3-none-any.whl")
    version("0.3.1", sha256="6bc7b267ce798555a287ce652841cbddf4a649e86bb772084e3328ca57e053ec", url="https://pypi.org/packages/89/b5/6f13c95cee6c8bd8e3167ffe0fd9b6d5f500ae713ab54a0dff9cfe34851d/LFPykit-0.3.1-py3-none-any.whl")
    version("0.3", sha256="f425a57bab49252fa00794394f3068a0bbc612f5619f14b8f377e0dca491b286", url="https://pypi.org/packages/fd/f8/678c0bafa032dae937eab5c8e95c9e1e897797e470193c914b2614bf4843/LFPykit-0.3-py3-none-any.whl")
    version("0.3-rc1", sha256="de1e6a7280739149f64836ee04f11c90c6ca513e301002a649c54b3eb9531296", url="https://pypi.org/packages/90/0b/66cb898f03656f0396c6bedb7f15d23cfe4b4dd61343803eeda4dc1b333b/LFPykit-0.3rc1-py3-none-any.whl")
    version("0.2", sha256="b17d28bf57309f2239388fb0c63558530fda63da31688e9e2d667057c34377e6", url="https://pypi.org/packages/e6/12/d0e5930586104b42e80b676fe1a0b08e5c5ace88faddec595462f6ad6508/LFPykit-0.2-py3-none-any.whl")
    version("0.2-rc3", sha256="4cc277928fc6ade089e70ad1d49f9b1583220729885fae45da087ee6422dcf40", url="https://pypi.org/packages/21/17/54f638ccea264d48eb4e27ef1ef4798cdcb4c7b3d079d13ddee180cf2f57/LFPykit-0.2rc3-py3-none-any.whl")
    version("0.1", sha256="4d8af999ec51838122a2ea1459aae112d77e64d5147b94a66260f16ccc6affe5", url="https://pypi.org/packages/af/66/e7c272580c262b160e1ae72679b82f1ad94a1bfbd74c17cd6dbb8034f42e/LFPykit-0.1.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-meautility", when="@0.2-rc2:")
        depends_on("py-numpy@1.15.2:", when="@0.2-rc2:")
        depends_on("py-scipy", when="@0.2-rc2:")
    # END DEPENDENCIES

