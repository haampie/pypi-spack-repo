# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PySmartOpen(PythonPackage):
    # BEGIN VERSIONS
    version("7.0.1", sha256="9507e38b43d1fd515c2085b9db2e41b592bb754b0e31395a085eb0d61d2410e5", url="https://pypi.org/packages/ad/08/dcd19850b79f72e3717c98b2088f8a24b549b29ce66849cd6b7f44679683/smart_open-7.0.1-py3-none-any.whl")
    version("7.0.0", sha256="ea2b7a8fc7d766689cacba3b425ef5cea6038180e4878142657baa86ed6b6264", url="https://pypi.org/packages/c8/f5/039b836c58f9b2739c3ee7856dbcad67dc7e32037b303e95a37e783c72a6/smart_open-7.0.0-py3-none-any.whl")
    version("6.4.0", sha256="8d3ef7e6997e8e42dd55c74166ed21e6ac70664caa32dd940b26d54a8f6b4142", url="https://pypi.org/packages/fc/d9/d97f1db64b09278aba64e8c81b5d322d436132df5741c518f3823824fae0/smart_open-6.4.0-py3-none-any.whl")
    version("6.3.0", sha256="b4c9ae193ad6d3e7add50944b86afa0d150bd821ab8ec21edb26d9a06b66f6a8", url="https://pypi.org/packages/47/80/c2d1bdd36c6b64ae566d9a29724291510e4f3796ce99639d3c2999286284/smart_open-6.3.0-py3-none-any.whl")
    version("6.2.0", sha256="088bf00f9327c71e549bc2f86567d3320df5d89667f009ce1c16568976068ef7", url="https://pypi.org/packages/3e/07/36678c6ff0dfa6cf445d0e00bf4f013de3b86ec1a2e8bfd1e5df69b2d91d/smart_open-6.2.0-py3-none-any.whl")
    version("6.1.0", sha256="1a5315659844085a1ba7ec40d080c1d084ba8535ec113160d692fe8a0e032417", url="https://pypi.org/packages/91/15/0ded056b0f19d88b88422c477e29b6d60ffabafb29d46da100c53434f8ad/smart_open-6.1.0-py3-none-any.whl")
    version("6.0.0", sha256="94afbd5058a45d4fdc4f859ed158b46054cb5ca1c019d76f6f8a60495f662129", url="https://pypi.org/packages/09/db/fab79b619923e26cecc5fb460c80f71f99666fe19182d5bb600ec4d6ff10/smart_open-6.0.0-py3-none-any.whl")
    version("5.2.1", sha256="71d14489da58b60ce12fc3ecb823facc59a8b23cd1b58edb97175640350d3a62", url="https://pypi.org/packages/cd/11/05f68ea934c24ade38e95ac30a38407767787c4e3db1776eae4886ad8c95/smart_open-5.2.1-py3-none-any.whl")
    version("5.2.0", sha256="c670c977cd4c66e91097fc3cda57ceec09f1d660019225b6bd870523c02ef516", url="https://pypi.org/packages/36/fd/3880dea47d6fe06d1cea561c93e077f0b131caf8193801d20a0a16d5e774/smart_open-5.2.0-py3-none-any.whl")
    version("1.11.1", sha256="221cc08ae926af6ad72d141f208d228e1e801b1ee9b15f3e466eecf89d931002", url="https://pypi.org/packages/5d/13/a2db017db801d0157fdc41814658396e6ae398d06adf69d73df1c8175b5d/smart_open-1.11.1.tar.gz")
    version("1.10.0", sha256="bea5624c0c2e49987c227bdf3596573157eccd96fd1d53198856c8d53948fa2c", url="https://pypi.org/packages/6e/14/47cf88d290e4681be35f3b6e8889ba26ed809a0ba14336dc8ae46ffcfda8/smart_open-1.10.0.tar.gz")
    version("1.8.4", sha256="788e07f035defcbb62e3c1e313329a70b0976f4f65406ee767db73ad5d2d04f9", url="https://pypi.org/packages/37/c0/25d19badc495428dec6a4bf7782de617ee0246a9211af75b302a2681dea7/smart_open-1.8.4.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    variant("azure", default=False)
    variant("gcs", default=False)
    variant("http", default=False)
    variant("s3", default=False)
    # END VARIANTS

    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-azure-common", when="@5:+azure")
        depends_on("py-azure-core", when="@5:+azure")
        depends_on("py-azure-storage-blob", when="@5:+azure")
        depends_on("py-boto3", when="@5:+s3")
        depends_on("py-google-cloud-storage@2.6:", when="@6.3:+gcs")
        depends_on("py-google-cloud-storage@1.31:", when="@6:6.2+gcs")
        depends_on("py-google-cloud-storage", when="@5+gcs")
        depends_on("py-requests", when="@5:+http")
        depends_on("py-wrapt", when="@7:")
    # END DEPENDENCIES

