# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyIsal(PythonPackage):
    # BEGIN VERSIONS
    version("1.6.1", sha256="7b64b75d260b544beea3f59cb25a6f520c04768818ef4ac316ee9a1f2ebf18f5", url="https://pypi.org/packages/50/a8/25887c43941b2a6ca85529e242fd8e57906e6047fde51ee36510f9d525fa/isal-1.6.1.tar.gz")
    version("1.6.0", sha256="d9bd3697177afdf65286c6804ef4ad2735dcf0f000f97a182a2333a20667ee27", url="https://pypi.org/packages/8c/e9/31ba563f7a7c2fc56271f4847151a4d136fcc712d17c3e0b2f61f10376ce/isal-1.6.0.tar.gz")
    version("1.5.3", sha256="01d9b76db3535374d720a06f5d66031f74e609698f0382fdd6ab3a0351210b72", url="https://pypi.org/packages/08/07/228b14e3a58f5d1294a54120f82efeadf1d5ebf39af43d93ba71f1e7e74c/isal-1.5.3.tar.gz")
    version("1.5.2", sha256="38f4e04b9f5a9577a7b16362a4d38b413e6978852d0c94c2cd7a3964e4794f28", url="https://pypi.org/packages/60/3c/5affdb3e64e75038ac63b55d4aec2bdf200e8f92917778a8b01dd7d7d125/isal-1.5.2.tar.gz")
    version("1.5.1", sha256="c96f3f9a8aed66a9e28b68a3b04a0852e8a06a5493a2fab57b963d9c0ee97fac", url="https://pypi.org/packages/55/44/ebbcbfe7efa1ff468415e1386d0cfdba988e235dcd8a2c34e2faf7fe9f02/isal-1.5.1.tar.gz")
    version("1.5.0", sha256="eadb48eb7dc161ac73afe36b18980b3b34ac224f2172302e301717aa40748b54", url="https://pypi.org/packages/be/ec/1fafcd81275d87a1512b02f75b71e82132eebee5ee2b14ee6e2a06d12f9a/isal-1.5.0.tar.gz")
    version("1.5.0.dev0", sha256="586dd53aaa237917b966668dc1c8406aca77f3ad82fe7285fa300ef3e3092a68", url="https://pypi.org/packages/4f/59/519c06df0d1bfdd8c9e339ff246fff123368475a98d5e56aef44abefddbc/isal-1.5.0.dev0.tar.gz")
    version("1.4.1", sha256="3211a032436af58a902b5ccb754f6be219a730ee3c6d3a8fc6b79429c24fc13c", url="https://pypi.org/packages/83/d9/ee4e6f71e0c6a66f07abca8521d3260b63521a84df9a6c8f56a89ad09781/isal-1.4.1.tar.gz")
    version("1.4.0", sha256="5e94c033651ae4950d0e115f4138938c671c38c8bcf78b7a1e5fef094376522d", url="https://pypi.org/packages/1b/20/b018dc291db34ade6c19cf44916eb79b16bf521a67ff7da6f607f75c0995/isal-1.4.0.tar.gz")
    version("1.3.0", sha256="4d5ffce8b65b1ff9fa5c84dca79c49f163656ff5463bc0a078c6cdb3500f6bfc", url="https://pypi.org/packages/87/67/2d445484eec933f4484ccdadbfddeb97c44c90389abc9b9613989c2100ba/isal-1.3.0.tar.gz")
    version("1.2.0", sha256="7e968efcb628a69ea990894d2b6cd8cc8afc4e86fb648001ae0ba6dd2e79042a", url="https://pypi.org/packages/7b/94/123cd2aa9632824ccd5d2bb45ec391de78c34cf9b1aaf2ebc045881802a3/isal-1.2.0.tar.gz")
    version("1.1.0", sha256="1364f4e3255a57d51c01422ab3ae785a43c076d516ebf49f6a25adecf8232105", url="https://pypi.org/packages/72/21/885d092e829e454700eb8acd1b086acb35d9c2756882afc0d22f4cec2ae5/isal-1.1.0.tar.gz")
    version("1.0.0", sha256="a30369de6852109eef8ca1bdd46d7e4b5c4517846a25acfc707cbb19db66ac80", url="https://pypi.org/packages/4f/0a/e500ff6f277d93649bf8d24d9043b0b9c080fe26c50bae7dcd39ba1ba7e1/isal-1.0.0.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    # END DEPENDENCIES

