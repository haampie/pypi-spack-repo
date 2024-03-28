# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyFalcon(PythonPackage):
    # BEGIN VERSIONS
    version("3.1.3", sha256="23335dbccd44f29e85ec55f2f35d5a0bc12bd7a509f641ab81f5c64b65626263", url="https://pypi.org/packages/3b/30/a7bc770025b6a7a36d0508e3d735dca239df7c27b862856e54d661f24632/falcon-3.1.3.tar.gz")
    version("3.1.3-rc1", sha256="3d292d9dea157ae43a313d86d2ccc2a1bd2fde900c01c15243e04c9b2a3505f3", url="https://pypi.org/packages/67/74/eccf026a1c5a9a09f25b97f7b69a643ace5d61cf13b3bdbe303a7b227eeb/falcon-3.1.3rc1.tar.gz")
    version("3.1.2", sha256="dadb4964fbcba712b0f5af02b30f921fb5e502d172cb869f99a768678bb78506", url="https://pypi.org/packages/ee/5c/af5ee294dfa813c6010b578e891ea410107452d7518b2fb24dbcfb100f11/falcon-3.1.2.tar.gz")
    version("3.1.1", sha256="5dd393dbf01cbaf99493893de4832121bd495dc49a46c571915b79c59aad7ef4", url="https://pypi.org/packages/29/bc/c11c9a14bb5b4d18a024ee51da15b793d1c869d151bb4101e324e0d055a8/falcon-3.1.1.tar.gz")
    version("3.1.0", sha256="f2760bd18c16393a6fb5e55f371f67921edb72febe693a82b3c5e82195d087b7", url="https://pypi.org/packages/36/53/4fd90c6c841bc2e4be29ab92c65e5406df9096c421f138bef9d95d43afc9/falcon-3.1.0.tar.gz")
    version("3.0.1", sha256="c41d84db325881a870e8b7129d5ecfd972fa4323cf77b7119a1d2a21966ee681", url="https://pypi.org/packages/63/22/6a9009c53ad78e65d88a44db8eccc7f39c6f54fc05fb43b1e9cbbc481d06/falcon-3.0.1.tar.gz")
    version("3.0.0", sha256="8d7c3d52ae4590ddfa0b3d9c75d44ab573340a5e78d72ee687712e757ac53929", url="https://pypi.org/packages/f1/59/2748d63922a46e040be06cd175a6242a33ade7839aac37f441544bb6d651/falcon-3.0.0.tar.gz")
    version("3.0.0-alpha2", sha256="075e847af427b66dc246b759af108293ed06fd9d340143cab68c3a72cb405cce", url="https://pypi.org/packages/db/5d/dea25ca06745dbb2c9724cbc7e85a6597a533849dffe6b41e635aa7ee416/falcon-3.0.0a2-py2.py3-none-any.whl")
    version("3.0.0-alpha1", sha256="1147049bf4ebe4779fe4e43b04d6a99681fc45806710c77aef444a142a7c0010", url="https://pypi.org/packages/9d/b5/7e2575062c833928aa63f3e535632686709e6dc478a6fc5bf70c5c31fd6a/falcon-3.0.0a1-py2.py3-none-any.whl")
    version("2.0.0", sha256="eea593cf466b9c126ce667f6d30503624ef24459f118c75594a69353b6c3d5fc", url="https://pypi.org/packages/19/30/edff5a1fea7a8e9876c8391e170263e1bb207875b6a65cd619818487b27b/falcon-2.0.0.tar.gz")
    version("2.0.0-rc4", sha256="093a6a275d72fb5e2551eddf133a40214fb3c5c8df91d24ef61ed3f381bfe51a", url="https://pypi.org/packages/38/9f/610913e457e922578cf2e5e4843fa32f3cd8f6d4fb7e44b2e8d31809d156/falcon-2.0.0rc4.tar.gz")
    version("2.0.0-rc3", sha256="9410b4ea9068c27dc53a335b14c8f4705983c1eb6882dbdbf07f523728dfdd64", url="https://pypi.org/packages/0f/40/a842f16a42d8e97a686e1abee9c7d23ae4668094e4d77fada8418f98faa9/falcon-2.0.0rc3.tar.gz")
    version("2.0.0-rc2", sha256="65ea1b37b74f7b09e1e0831b1f477d9c3e1d7c63fc8fee03bcb849c6eabd34c4", url="https://pypi.org/packages/3d/4e/09ea27cb5364db30cfad78ef5178e7aa3e5365a24a343384b6282cca8e6d/falcon-2.0.0rc2.tar.gz")
    version("2.0.0-rc1", sha256="aec454344f19cdb0c9fab91a0da6f3f22e19829a7b554adb5c4539258f3737a9", url="https://pypi.org/packages/dd/d3/c7cdbb344218ad984797886858837aec8e600f9881c6c19ce8a71e20d231/falcon-2.0.0rc1-py2.py3-none-any.whl")
    version("2.0.0-beta2", sha256="8421bf8a0b24c359bc4010b6803f168bd0acfa6f7d40f7067ac6e84d2cbaa179", url="https://pypi.org/packages/23/4b/69b5fc67ee2417186e5e0fda86ba2de40000a7562228bb6eeaa1cf6108e3/falcon-2.0.0b2-py2.py3-none-any.whl")
    version("2.0.0-beta1", sha256="0ead81121347ee4e1556f36460a93b2bdbae6c381d91f4d548b96b50e9b678a4", url="https://pypi.org/packages/88/e9/8c9f383541331f592f023c712c1674769be1d1740c0db98e5d738b796d86/falcon-2.0.0b1-py2.py3-none-any.whl")
    version("2.0.0-alpha2", sha256="55b5c2c601e31d702c987eb7d7dc9f1e5d94f501fa7e52e784ce84ee8d4f94cd", url="https://pypi.org/packages/c7/03/1485420df73f80f66f6f77d1083fd8e2c33f04be0e84f6ee87a9e5cdb0a5/falcon-2.0.0a2-py2.py3-none-any.whl")
    version("1.4.1", sha256="0a66b33458fab9c1e400a9be1a68056abda178eb02a8cb4b8f795e9df20b053b", url="https://pypi.org/packages/e8/d0/20bb807dee65f1f163754670557b128eafce1710f6c9c363a38e357f3783/falcon-1.4.1-py2.py3-none-any.whl")
    version("1.4.0", sha256="5a343d9bb47b233b8efa91e76a4080db753c4cccfc8f1aba0e86f1f7453e3df0", url="https://pypi.org/packages/e7/ee/99d8ad2d779c827826115c0a6c70d602aaa65dc42bf76d16466d28c0a4e0/falcon-1.4.0-py2.py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-python-mimeparse@1.5.2:", when="@1.1:1")
        depends_on("py-six@1.4:", when="@1")
    # END DEPENDENCIES

