# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyApeye(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("1.4.1", sha256="44e58a9104ec189bf42e76b3a7fe91e2b2879d96d48e9a77e5e32ff699c9204e", url="https://pypi.org/packages/89/7b/2d63664777b3e831ac1b1d8df5bbf0b7c8bee48e57115896080890527b1b/apeye-1.4.1-py3-none-any.whl")
    version("1.4.0", sha256="32f10f5629c39a0d2a4bc00b16827b43b912c56510395329cb4cc823954ec2be", url="https://pypi.org/packages/d1/10/16f0e76276a3dde7e8b72850cb961ae8e99846d0bbbc92ffc137fd35a2df/apeye-1.4.0-py3-none-any.whl")
    version("1.3.0", sha256="8ce991a5c7d1ccedd46f067fcd53eccfa4b0b62a50d8802340b427941603b839", url="https://pypi.org/packages/08/a2/2108ec0cfa670cc65aafab8cb316f6a5910816c5baf805b543af0a1c06c8/apeye-1.3.0-py3-none-any.whl")
    version("1.2.0", sha256="d6b08c96457e4e0457088c247417fc336ebf83ab88645c508562aaeaf3077954", url="https://pypi.org/packages/57/b8/a035854ec2b791ee59a179a339dc9c53e9d7f5ee952f36982ba264ced364/apeye-1.2.0-py3-none-any.whl")
    version("1.1.0", sha256="8c6d31a5e6de7b355fb6d40ce75215c06d6b434f11f2c2813e5712198ff8cf85", url="https://pypi.org/packages/7d/53/e1b8b822c7f2946655d64357ab05924de0f1183e2d888a97b27dd2449e12/apeye-1.1.0-py3-none-any.whl")
    version("1.0.1", sha256="e7da07880e87630959cc0c459c97a61a41bab0548af02db76adc52ce261f4a37", url="https://pypi.org/packages/f4/f2/a25da34dea75c7c500b30293d6eb8f8f923d88206380907817757270929a/apeye-1.0.1-py3-none-any.whl")
    version("1.0.0", sha256="46a7d3d7882d5d834f969c31d2d328df7212b96f6dca336ff91ac3cdd1d39405", url="https://pypi.org/packages/62/fc/0e882334def1749e5114243f02d16759d2399f2395abff69213e821e150e/apeye-1.0.0-py3-none-any.whl")
    version("0.9.1", sha256="b8838468a1a26e965046956742421f92db922c3585032582f10146f5fffef18a", url="https://pypi.org/packages/4e/98/67252ee13909929bcd4585d696ed0a6d49d9b3f62b4e4f21879323ad550b/apeye-0.9.1-py3-none-any.whl")
    version("0.9.0", sha256="4903a37b48bc59621a3115dbd96da4d1883586e08737ec8187a75d99b30ed7fb", url="https://pypi.org/packages/2e/dd/15964df406cfc7cbf57dace7d2117faae3c8d7720d30fad533f2971c26c1/apeye-0.9.0-py3-none-any.whl")
    version("0.8.0", sha256="119f99d78d34c2e6b5f8dfee0d5258a91fe53321682f696a9bd18d8006b85048", url="https://pypi.org/packages/b2/83/23b47af65d3033848bca147db4c408e06d2b6083055f3499a4ac0d94f3da/apeye-0.8.0-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-apeye-core@1.0.0-beta2:", when="@1.3:")
        depends_on("py-appdirs@1.4.4:", when="@0.0.4:1.1")
        depends_on("py-cachecontrol@0.12.6:+filecache", when="@:0.8")
        depends_on("py-domdf-python-tools@2.6:", when="@1.2:")
        depends_on("py-domdf-python-tools@2.3:", when="@1.0.1:1.1")
        depends_on("py-domdf-python-tools@0.9:", when="@0.2:1.0.0")
        depends_on("py-idna@2.5:", when="@1.0.1:1.2")
        depends_on("py-idna@2.9:", when="@1:1.0.0")
        depends_on("py-lockfile@0.12:", when="@0.0.4:0.8")
        depends_on("py-platformdirs@2.3:", when="@1.2:")
        depends_on("py-requests@2.24:")
        depends_on("py-tldextract@2.2:", when="@0.1:0")
    # END DEPENDENCIES

