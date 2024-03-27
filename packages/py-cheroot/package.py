##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyCheroot(PythonPackage):
    version("10.0.0", sha256="8f65dd38ad3d56419cfe2d1b5e4b4e3282b1d58758ca2a336231641a80cf0717", url="https://pypi.org/packages/81/52/ca26d1964531e823961f761026138189f630aaf49fb959c8ab6e1262dc74/cheroot-10.0.0-py3-none-any.whl")
    version("9.0.0", sha256="fa4231fdb42d7720df118ff62a79371e406369f49e6f867c63ad649cfb4e466c", url="https://pypi.org/packages/3b/15/38d6b098fe874406b7de0fa6dec300e233f6d321ee74e8150e23438adf3f/cheroot-9.0.0-py2.py3-none-any.whl")
    version("8.6.0", sha256="62cbced16f07e8aaf512673987cd6b1fc5ad00073345e9ed6c4e2a5cc2a3a22d", url="https://pypi.org/packages/d3/87/8c5a471a82dfd1c82b4cb6605fcad90e1f0e938b14c0516da3504701a2b4/cheroot-8.6.0-py2.py3-none-any.whl")
    version("8.5.2", sha256="7ba11294a83468a27be6f06066df8a0f17d954ad05945f28d228aa3f4cd1b03c", url="https://pypi.org/packages/46/95/86fe6480af78fea7b0e7e1bf02e6acd4cb9e561ea200bd6d6e1398fe5426/cheroot-8.5.2-py2.py3-none-any.whl")
    version("8.5.1", sha256="262097e089ac9d38f21a25ca25fd272fde2b9d5a9950756262c1fb898f5c292b", url="https://pypi.org/packages/9e/10/066754a30b24c8b0d4b502d56b5b91d11d458d7cda81fac019f52c70dc67/cheroot-8.5.1-py2.py3-none-any.whl")
    version("8.5.0", sha256="6c5547b340379cad1bf3e53bcaa8d028e83532b2d86839c72e1008a9312cc09e", url="https://pypi.org/packages/d2/41/7c29d3b35740dbb6da2a89c1536a73a14bdb0efcb39c2cf5414b90633fbb/cheroot-8.5.0-py2.py3-none-any.whl")
    version("8.4.8", sha256="8134fe93ea2fdd9ab394bf21dd18cf4f51b7f2302b309fcab5bdf434c5048a6c", url="https://pypi.org/packages/85/80/f202e6d6543104d61729312b0797f507987e9bdbc534d16ef0c0ddd75ba0/cheroot-8.4.8-py2.py3-none-any.whl")
    version("8.4.7", sha256="df0a7bf2f941695754f150c576abb7254103db75d902ccf7a872acd48a446c74", url="https://pypi.org/packages/df/78/1a56288191b20190002d23bc7026e3858148aa858a20c5a67bae64143429/cheroot-8.4.7-py2.py3-none-any.whl")
    version("8.4.6", sha256="5323e3141df612d7ea47424914518960b03bec8ea64b834b3e88ec4f71ccec4e", url="https://pypi.org/packages/24/dd/3d93c981f5983993e54c096366b09a3279f3602604f4d6859fae2c4cf437/cheroot-8.4.6-py2.py3-none-any.whl")
    version("8.4.5", sha256="ab342666c8e565a55cd2baf2648be9b379269a89d47e60862a087cff9d8b33ce", url="https://pypi.org/packages/bd/39/942862090e73344fc60461449ae2755c71de4a8ce735174474dc283bfda7/cheroot-8.4.5-py2.py3-none-any.whl")
    version("8.3.0", sha256="2b48c88959b5b80a79aca627ae5212acb398becaa70b576b8b89bec1ad0d1367", url="https://pypi.org/packages/20/b0/4e156a205a624bc929673dfa6bcebe4aa6fa00b080dca4dc7b6b50850277/cheroot-8.3.0-py2.py3-none-any.whl")
    version("6.5.5", sha256="1593fa2a42b18744ac485aadf5fec4a29ebfee00ba3937a2269b8ffc94447879", url="https://pypi.org/packages/3e/50/840039a5350b54fb8efbc3b26c6e4244c9ca24c49ad84fe1f57b1f79ff7d/cheroot-6.5.5-py2.py3-none-any.whl")

    with default_args(type="run"):
        depends_on("py-backports-functools-lru-cache", when="@6.2:6.2.2,6.2.4:6.5")
        depends_on("py-jaraco-functools", when="@7:")
        depends_on("py-more-itertools@2.6:", when="@6:")
        depends_on("py-six@1.11:", when="@5.9.2:9")

