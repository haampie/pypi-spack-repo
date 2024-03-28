# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyAwkward(PythonPackage):
    # BEGIN VERSIONS
    version("2.6.2", sha256="c79c293a7f278ba316959b2246f682f338a4e5caff152bd9b4c45cc7ff8dc0e1", url="https://pypi.org/packages/18/9c/02978c408c7f93f3162e0c6b2f94f50fc0c89261277a948b72c693f642b4/awkward-2.6.2-py3-none-any.whl")
    version("2.6.1", sha256="9a48d366a42ad4d54f383c3202395db36472eb426e64ff9f09eaf0286516df36", url="https://pypi.org/packages/68/98/fe8f0108b2ca85f198b54660336c6221018a99eef64522a38c1975e248ba/awkward-2.6.1-py3-none-any.whl")
    version("2.6.0", sha256="715874cb667d0c2071cc35072c21767297020e76722852543322a1d96de42a57", url="https://pypi.org/packages/fe/ee/572155eb9f4a36cc1b0b82b2580c657e445d3e303da097df3bae6aa687f2/awkward-2.6.0-py3-none-any.whl")
    version("2.5.2", sha256="6b6cbb62cdafb65457c4672980735a2b2e635a5eda5570a51459b4e42359ceb5", url="https://pypi.org/packages/40/7f/33f8f1f0c9f55a01b9ab50431163da364355433730a13330f6e2f136936a/awkward-2.5.2-py3-none-any.whl")
    version("2.5.1", sha256="9b7f17557b5c44cbed337829d06797e58b7d5bc142e4e53911f55d7d579707d9", url="https://pypi.org/packages/b4/3f/adcb5df88523767cf6bad04012766239ae373e02f63271abce332e8b6772/awkward-2.5.1-py3-none-any.whl")
    version("2.5.0", sha256="8a97cc97ad662a1130d8481242e732a30cc4809f0298f6443ed86f21aa9fba5c", url="https://pypi.org/packages/2a/3d/75823ab9e30e48d4f38dad23923b858c104041c894184c9760f314507f02/awkward-2.5.0-py3-none-any.whl")
    version("2.4.10", sha256="a0cc863a686bba98d41443daf7f63add8b93f6c34de77a24322e2946ed029d13", url="https://pypi.org/packages/a7/29/4fecdc892ff6a031a643229426945da5144136acf39f02944f219268c391/awkward-2.4.10-py3-none-any.whl")
    version("2.4.9", sha256="1f52226dfca1e4fe9283ed83750084e6a8f2ceaca3c7d0d9f361d87df2408967", url="https://pypi.org/packages/22/1b/0ef7291782c14c03f31b1a14786a86891be17ef5dfac746b036334dda081/awkward-2.4.9-py3-none-any.whl")
    version("2.4.8", sha256="3bb5c505d1ddc78f876d5e2449deedc33e823691bdeaba9a8571284d9f4635e9", url="https://pypi.org/packages/46/6e/94b1f932319a29ca750abb49f36584c97a75b8eb06219d266176a998dbaf/awkward-2.4.8-py3-none-any.whl")
    version("2.4.7", sha256="e7a6034dec908dc4034eb5d9cd9824119c202a0cb212238e60a1094510c69375", url="https://pypi.org/packages/8d/41/72065697d8977eecb1348c976449c2afbd0ff221d9aa8c6b6bc97a7b9df8/awkward-2.4.7-py3-none-any.whl")
    version("2.1.1", sha256="eb37e9b04054442c6637dffa709623c37fe91cd7a4c9eb99c287eb3c2e32d9ca", url="https://pypi.org/packages/00/52/8da2f684ff3eeb4bc51acdceecbbbf98558f944abb3bb8adff411f6d1054/awkward-2.1.1-py3-none-any.whl")
    version("2.1.0", sha256="880dd7e39c73b8ff5fc9f2bd78ce370cd3111e42084d770fa70e3cde60c00d2b", url="https://pypi.org/packages/9b/f0/fcbc163b47b833bd93916164bba868afca8485ba73abef836122ced23b23/awkward-2.1.0-py3-none-any.whl")
    version("2.0.10", sha256="d0870fe300e94a3ede60cd82c0548a37323a4df0b8249452cc1e174989fd314a", url="https://pypi.org/packages/99/8f/6a477f41f561ede3151f5f8476ce51197395e3ddf30e505f8475825b7bc7/awkward-2.0.10-py3-none-any.whl")
    version("2.0.9", sha256="82592837dd774ac83411942f4176808a3671ead611fd45288a5594b14d199be5", url="https://pypi.org/packages/a1/d9/e492456bc0cccc8ce0641a0dce064b7d3ca6c9e43b59b58d8719d5c5f512/awkward-2.0.9-py3-none-any.whl")
    version("2.0.8", sha256="6b5ab68add587b66747e30f609e31a148ec79d7d17572bcb00969b3954be8eec", url="https://pypi.org/packages/42/2f/a137a7f70afb7d810610275946e50f000900dd6f0442b293ac29cd742922/awkward-2.0.8-py3-none-any.whl")
    version("2.0.7", sha256="c5cbf3639c52be40037eedce80d1f50c945d02f705561159f7273c7552dff78e", url="https://pypi.org/packages/1a/c7/97cca33a3185b68ffa9cfee1eb6b5ab2e00e15cc878c13d77c79226cf990/awkward-2.0.7-py3-none-any.whl")
    version("2.0.6", sha256="bd799a95c5e5dbd089bb7db598059f4e57cd232d421d9614d1c9a679a53f18f6", url="https://pypi.org/packages/f1/93/d580668e7d06b286c1cc2c7858d3a8c96f75090a5ebf2343d909be564a9f/awkward-2.0.6-py3-none-any.whl")
    version("2.0.5", sha256="d95354aea90c47d6b467ebadffa1f9d0f16b968fbbc0334d96ae8abe695bc497", url="https://pypi.org/packages/20/3d/910a792eeaa2c751b65f15c1844b2a0a50e47d0f775cdf3b1c32cd183305/awkward-2.0.5-py3-none-any.whl")
    version("2.0.4", sha256="7d1f5d6ba58f90821c78d9866d1d541ad2e0f282ecbd5054ff7f6889fb72aaef", url="https://pypi.org/packages/0c/1e/c3a1796421a9962bba6fae2587cebae5725f8abe9277c4c5e0890092f9f2/awkward-2.0.4-py3-none-any.whl")
    version("2.0.3", sha256="5062d30d60b0b4b2f45dd5c476ca7e374472c4a16f2b165e54e51f477dca0fb1", url="https://pypi.org/packages/e2/92/0f0c968089194e985781875749617190565b5a5eedfa9b9b7cb2454de33f/awkward-2.0.3-py3-none-any.whl")
    version("2.0.2", sha256="74da726390958e7362eaa500bd47c4a82f1c169f923f944a90f07af08e1dc01e", url="https://pypi.org/packages/37/e2/4ce9dbc4648749bf7226a99d041e322e2cf3e595077bf7892b95c458c6f0/awkward-2.0.2-py3-none-any.whl")
    version("2.0.1", sha256="b7055c3b79fea53cab5774409bb26be815a66c5ffac931fb400cca33288783b3", url="https://pypi.org/packages/b7/3a/460d3350da5a11a6f2c29d4e702a77ab8c2ef227593cb12a33f45085d9f2/awkward-2.0.1-py3-none-any.whl")
    version("2.0.0", sha256="5d8961dd4fa6e1c49e80e9fd815c85bc0527bfe4c2ae059560d293fd5fce9220", url="https://pypi.org/packages/cc/90/85431d8c1d356affe6a72a8388b00e37a54b1c37ebbb1e96d32dc873605b/awkward-2.0.0-py3-none-any.whl")
    version("1.10.3", sha256="7e669b1d29da300ed4c4f0d3a14119356037e7cfa8c3aa9d130bf1be6e38f03b", url="https://pypi.org/packages/dd/d4/d813843fbeb70177dd9bc32747c4658986db57e607597348e9b269f61229/awkward-1.10.3.tar.gz")
    version("1.10.2", sha256="303bc0919f0932db3e78a9254c17fcdeb125e4be65cd894b40dfbc3bfddfc054", url="https://pypi.org/packages/54/00/738df8c34175bc366b70098bce1711f774b60f5a50d5cee49bf1e0e8e4ac/awkward-1.10.2.tar.gz")
    version("1.10.1", sha256="c6394ed25fb14a086d63621d9d84fdc228f5d42a64586f215731b36fde17034b", url="https://pypi.org/packages/ba/3a/f5bd821836b2b73850fc464a4b696524c532c518b781fc758c98376f07b9/awkward-1.10.1.tar.gz")
    version("1.10.0", sha256="1d89c7244e6184b35f4bce6bd08ff82eb2ef60be67f572923bc6aaee35dab544", url="https://pypi.org/packages/8c/96/b492f04f6fa92b5e0259ee58484138e677e731956c0e30dbe9652ed56a53/awkward-1.10.0.tar.gz")
    version("1.9.0", sha256="cad799237e4370b50f77e716e78dd3565a7b3fd82fcd5a41a76aa1512d51075d", url="https://pypi.org/packages/13/43/ed24e8394fbdd7d3e47e75f0354433a10f6cec742a098c26891f1e5e05be/awkward-1.9.0.tar.gz")
    version("1.8.0", sha256="6655fa22d1b1d1dcb9ccee0d502350ab90c53467a10b540b7624422b594d2e72", url="https://pypi.org/packages/76/39/8b1feb4bda277f1864ea847d9d2e442d28e4de501a50ae807dd39f375e6f/awkward-1.8.0.tar.gz")
    version("1.7.0", sha256="e4e642dfe496d2acb245c90e37dc18028e25d5e936421e7371ea6ba0fde6435a", url="https://pypi.org/packages/31/fc/832c64ba928b13009d927f1951196f400c0f2c5798eef6041013a3a88b3d/awkward-1.7.0.tar.gz")
    version("1.5.1", sha256="c0357c62223fefcfc7a7565389dbd4db900623bf10eccf2bc8e87586ec59b38d", url="https://pypi.org/packages/c1/66/ebf25c01dbf8b4e892fee8bb9a33f8b7e28c4433665713ead20b4a217a15/awkward-1.5.1.tar.gz")
    version("1.5.0", sha256="3cb1b0e28f420232d894d89665d5c0c8241b99e56d806171f4faf5cdfec08ae1", url="https://pypi.org/packages/eb/86/05088fc5305ff69beace67d784f3b5a566ad2ac1fdd8825dfec13405ed0f/awkward-1.5.0.tar.gz")
    version("1.4.0", sha256="25ae6114d5962c717cb87e3bc30a2f6eaa232b252cf8c51ba805b8f04664ae0d", url="https://pypi.org/packages/92/36/78e8569019febaa660dfd5ce93196c03c100c31cdae5f2bdbe805f75be4a/awkward-1.4.0.tar.gz")
    version("1.3.0", sha256="b6021694adec9813842bad1987b837e439dabaf5b0dff9041201d238fca71fb4", url="https://pypi.org/packages/a7/8d/4a2d66d2ccd7c1fb6cdbf931930d9b12fa9f4503ec69d213fe03002a81a0/awkward-1.3.0.tar.gz")
    version("1.2.3", sha256="7d727542927a926f488fa62d04e2c5728c72660f17f822e627f349285f295063", url="https://pypi.org/packages/4d/7d/6de83e56de46522c6caa1c5e617d91b9f126dbf36fd58ecc7b15cb26ea34/awkward-1.2.3.tar.gz")
    version("1.2.2", sha256="89f126a072d3a6eee091e1afeed87e0b2ed3c34ed31a1814062174de3cab8d9b", url="https://pypi.org/packages/4d/6a/59a260ba06f088a8885d52c9db26a64428831f406bc5770f70c14c23722d/awkward-1.2.2.tar.gz")
    version("1.1.2", sha256="4ae8371d9e6d5bd3e90f3686b433cebc0541c88072655d2c75ec58e79b5d6943", url="https://pypi.org/packages/88/82/f13c3c09b1295d1a4e5d449eb0d27a2d4513429f12059a3ca7c737ebe478/awkward-1.1.2.tar.gz")
    version("1.0.2", sha256="3468cb80cab51252a1936e5e593c7df4588ea0e18dcb6fb31e3d2913ba883928", url="https://pypi.org/packages/21/0a/9988d6c23a2d12d64552f9436bace86e1c6cb441ad3017386a312d4c51c4/awkward-1.0.2.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-awkward-cpp@30", when="@2.6.2")
        depends_on("py-awkward-cpp@29", when="@2.6:2.6.1")
        depends_on("py-awkward-cpp@28", when="@2.5.2:2.5")
        depends_on("py-awkward-cpp@27", when="@2.5.1")
        depends_on("py-awkward-cpp@26", when="@2.5.0:2.5.1-rc1")
        depends_on("py-awkward-cpp@25", when="@2.4.7:2.5.0-rc0")
        depends_on("py-awkward-cpp@12", when="@2.1:2.1.1")
        depends_on("py-awkward-cpp@11", when="@2.0.10:2.0")
        depends_on("py-awkward-cpp@10", when="@2.0.9")
        depends_on("py-awkward-cpp@9", when="@2.0.8")
        depends_on("py-awkward-cpp@8", when="@2.0.7")
        depends_on("py-awkward-cpp@7", when="@2.0.6")
        depends_on("py-awkward-cpp@6", when="@2.0.5")
        depends_on("py-awkward-cpp@5", when="@2.0.3:2.0.4")
        depends_on("py-awkward-cpp@4", when="@2.0.2")
        depends_on("py-awkward-cpp@3", when="@2.0.1")
        depends_on("py-awkward-cpp@2", when="@2.0.0-rc8:2.0.0")
        depends_on("py-fsspec@2022.11:", when="@2.6.1:")
        depends_on("py-fsspec", when="@2.6:2.6.0")
        depends_on("py-importlib-metadata@4.13:", when="@2.4: ^python@:3.11")
        depends_on("py-importlib-resources", when="@1.10.5:1,2.0.0-rc4:2.3 ^python@:3.8")
        depends_on("py-numpy@1.18.0:", when="@2.3:2.6.2")
        depends_on("py-numpy@1.17.0:", when="@2.1:2.2")
        depends_on("py-numpy@1.14.5:", when="@2.0.0-rc5:2.0")
        depends_on("py-packaging", when="@1.10.5:1,2.0.0-rc4:")
        depends_on("py-typing-extensions@4.1:", when="@2.0.0-rc5: ^python@:3.10")
    # END DEPENDENCIES

