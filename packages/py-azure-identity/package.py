# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyAzureIdentity(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("1.16.0-beta2", sha256="a888764f16212daf1b7c64cb6b422ba04b348c2eeea3960f935f46a70b34c595", url="https://pypi.org/packages/f4/1c/d6b402cca049f61943874bfadb670dbcbea75da93b3f260ce0212fd8e3bf/azure_identity-1.16.0b2-py3-none-any.whl")
    version("1.16.0-beta1", sha256="d9d5af5b1c78755c771c4dbe17af0dccc7db7521a8da641e667ce3845f38e83d", url="https://pypi.org/packages/57/13/39f82fcf5f98f5b0e2e586e72e83394bf166ccc187a2b60a0c54c7c3554a/azure_identity-1.16.0b1-py3-none-any.whl")
    version("1.15.0", sha256="a14b1f01c7036f11f148f22cd8c16e05035293d714458d6b44ddf534d93eb912", url="https://pypi.org/packages/30/10/5dbf755b368d10a28d55b06ac1f12512a13e88874a23db82defdea9a8cd9/azure_identity-1.15.0-py3-none-any.whl")
    version("1.15.0-beta2", sha256="e6444ffd6283fecd0b7fbee95e341a5ec9eb171bd563f9819862faeb58d4ddff", url="https://pypi.org/packages/48/82/d00b5eea9e8e7c6fa7d3533c4976f4d23ee7293a40fa634460747c8b9d4b/azure_identity-1.15.0b2-py3-none-any.whl")
    version("1.15.0-beta1", sha256="153736db01345ef48afc9b77d0c80552d2059845a644ad1f1bdc62ca0b6659fe", url="https://pypi.org/packages/10/3c/6f28707bb7de2e3f7908ed28e83e76af692c9b73a4f2b467cabf4917434e/azure_identity-1.15.0b1-py3-none-any.whl")
    version("1.14.1", sha256="3a5bef8e9c3281e864e869739be8d67424bff616cddae96b546ca2a5168d863d", url="https://pypi.org/packages/42/b6/e2757da4800e0f402b23d0ca6f1e88726263a501c198729cd865f45f3e22/azure_identity-1.14.1-py3-none-any.whl")
    version("1.14.0", sha256="edabf0e010eb85760e1dd19424d5e8f97ba2c9caff73a16e7b30ccbdbcce369b", url="https://pypi.org/packages/42/8d/7701695ca568e373e6b8fa5193733b173ee8630f9b64843164b65a20f8c2/azure_identity-1.14.0-py3-none-any.whl")
    version("1.13.0", sha256="bd700cebb80cd9862098587c29d8677e819beca33c62568ced6d5a8e5e332b82", url="https://pypi.org/packages/33/16/fa96a5e057d6842e95d94fc410896e061b3d3a2584d57e13fc58268df45f/azure_identity-1.13.0-py3-none-any.whl")
    version("1.12.0", sha256="2a58ce4a209a013e37eaccfd5937570ab99e9118b3e1acf875eed3a85d541b92", url="https://pypi.org/packages/ce/96/942f03d8a80e30e2289496c10d99e3a8b71f10c0b70b5337fd8ec2ae85e5/azure_identity-1.12.0-py3-none-any.whl")
    version("1.11.0", sha256="f5eb0035ac9ceca26658b30bb2a375755c4cda61d0e3fd236b0e52ade2cb0995", url="https://pypi.org/packages/d8/44/47d8af284ed2e6fa066b669f1f72dab09aeb230d52291bb26a964fd2b20b/azure_identity-1.11.0-py3-none-any.whl")
    version("1.10.0", sha256="b386f1ccbea6a48b9ab7e7f162adc456793c345193a7c1a713959562b08dcbbd", url="https://pypi.org/packages/84/d4/56eeaa097dd15123aaed85346e9ab3701c62650cf81e83d56600f5f30113/azure_identity-1.10.0-py3-none-any.whl")
    version("1.9.0", sha256="2e75bbf0a72309b8f95f6769214b90bf271f3662d28d962bcddf4d2406157b51", url="https://pypi.org/packages/c8/ae/0aed0af4d9f78c6a38ce07a3dbbb55c6be3f87a261193ff8996e22b166d6/azure_identity-1.9.0-py3-none-any.whl")
    version("1.8.0", sha256="8d87aff09b8dabe3c99bb934798dcdeb2f2d49614ecc4f0425cc888faafd64ae", url="https://pypi.org/packages/fe/a8/6289b84a371e061010fcbbbdaa50e448e83ec8ebe2d8430f7c9355458ee6/azure_identity-1.8.0-py3-none-any.whl")
    version("1.7.1", sha256="454e16ed1152b4fd3fb463f4b4e2f7a3fc3a862b0ca28010bff6d5c6b2b0c50f", url="https://pypi.org/packages/38/97/126125151456b93e9eb2a22419864237dc0539fa1badbe4da867567b3b5a/azure_identity-1.7.1-py2.py3-none-any.whl")
    version("1.4.1", sha256="6f95b3505fc134ad16bd16da053456e1933188ac43161704d48ddb4edebf72c9", url="https://pypi.org/packages/93/97/0e57f9d0bb0e9aee5cce0007616f6d3c2e09931fd24ad140c9cc3b06b7ef/azure_identity-1.4.1-py2.py3-none-any.whl")
    version("1.4.0", sha256="92ccea6c6ac7724d186cb73422d1ad8f525202dce2bdc17f35c695948fadf222", url="https://pypi.org/packages/68/d8/b2c5fb855983b6e1cfabe1c7105e15562430eabf592d51754ec8924d1f0a/azure_identity-1.4.0-py2.py3-none-any.whl")
    version("1.4.0-beta7", sha256="ed10bf597f3e624a90de221fffc1ce339064eeb80437c9c81916be6b614b4caf", url="https://pypi.org/packages/c6/48/5f9a4aaa9fb185430f2c5338f03146f0c2fb6fb9f96ca771a189eb8ae2af/azure_identity-1.4.0b7-py2.py3-none-any.whl")
    version("1.4.0-beta6", sha256="d3da802ad76fabcca320e755a26c4f1f6379900b4e3f4b01d2238ed959d4009d", url="https://pypi.org/packages/e6/ce/514116545449c38fa590220061411a8878e343c3598e5cb9efe74ff070a0/azure_identity-1.4.0b6-py2.py3-none-any.whl")
    version("1.4.0-beta5", sha256="87cff332a4fbc48bd865220f3a108ef4a5f6ad5bda6b37f0c6c646831dac9ae6", url="https://pypi.org/packages/36/21/ccbb2cf3b81aa1b2f0a5467fa30aa704b49f03e20491841212849f704c09/azure_identity-1.4.0b5-py2.py3-none-any.whl")
    version("1.4.0-beta4", sha256="90e2b67fb2a228c4c0ea49a3f129d55c85c9a8467df076c32656edd9327f97b2", url="https://pypi.org/packages/07/16/06b48bf0d28f0711b472caed3a6f1cc3cd5fc457117ee960ee869ad96bc5/azure_identity-1.4.0b4-py2.py3-none-any.whl")
    version("1.4.0-beta3", sha256="7b23eafb657e38b56ad70bd3b94a0c72d6d5e9f4f502be2d11d716fc56352363", url="https://pypi.org/packages/cd/46/befebe7f01492ed4d2a3b3e093731d61ab45260390ce649020c138152e49/azure_identity-1.4.0b3-py2.py3-none-any.whl")
    version("1.3.1", sha256="3775d5d244d65bde19d9ba76b95b1c82484a7a09f8b13140b106bc84df601d35", url="https://pypi.org/packages/dc/55/9b89cd436c145bc11cfb5ebabf2d4a7468a996104a2c26f2674eb3a7bb05/azure_identity-1.3.1-py2.py3-none-any.whl")
    version("1.3.0", sha256="7e9c85e3f82f1e29e5edfc7beb3030b25e8b8fd02b65d5ea1c67f13cde01da0f", url="https://pypi.org/packages/9b/c9/3ca9cdb73e72329907348dd1fcd34eb03d4d49f9b14e078b6d0e6f8fabc0/azure_identity-1.3.0-py2.py3-none-any.whl")
    version("1.2.0", sha256="4ce65058461c277991763ed3f121efc6b9eb9c2edefb62c414dfa85c814690d3", url="https://pypi.org/packages/c4/7a/9372cd51fc3408ede0fab950ef9a6518cad34ef36e199982bb1ddfa18512/azure_identity-1.2.0-py2.py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-azure-core@1.23:", when="@1.15.0:")
        depends_on("py-azure-core@1.11:", when="@1.7.0-beta2:1.15.0-beta2")
        depends_on("py-azure-core@1.0.0:", when="@1.0.0:1.7.0-beta1")
        depends_on("py-cryptography@2.5:", when="@1.7.0-beta4:")
        depends_on("py-cryptography@2.1.4:", when="@:1.7.0-beta3")
        depends_on("py-msal@1.24.0:", when="@1.15.0-beta2:")
        depends_on("py-msal@1.20.0:", when="@1.13:1.15.0-beta1")
        depends_on("py-msal@1.12:", when="@1.7.0-beta2:1.12")
        depends_on("py-msal@1.3:", when="@1.4.0-beta6:1.4")
        depends_on("py-msal@1.1:", when="@1.4.0-beta4:1.4.0-beta5")
        depends_on("py-msal@1:", when="@1.0.1:1.4.0-beta3")
        depends_on("py-msal-extensions@0.3:", when="@1.10.0:")
        depends_on("py-msal-extensions@0.3:0", when="@1.5.0-beta2:1.10.0-beta1")
        depends_on("py-msal-extensions@0.2.2:0.2", when="@1.4.0-beta4:1.5.0-beta1")
        depends_on("py-msal-extensions@0.1.3:0.1", when="@1.0.1:1.4.0-beta3")
        depends_on("py-six@1.12:", when="@1.6:1.13")
        depends_on("py-six@1.6:", when="@1.0.0-beta2:1.5")
    # END DEPENDENCIES

