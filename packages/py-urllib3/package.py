##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyUrllib3(PythonPackage):
    version("2.2.1", sha256="450b20ec296a467077128bff42b73080516e71b56ff59a60a02bef2232c4fa9d", url="https://pypi.org/packages/a2/73/a68704750a7679d0b6d3ad7aa8d4da8e14e151ae82e6fee774e6e0d05ec8/urllib3-2.2.1-py3-none-any.whl")
    version("2.2.0", sha256="ce3711610ddce217e6d113a2732fafad960a03fd0318c91faa79481e35c11224", url="https://pypi.org/packages/88/75/311454fd3317aefe18415f04568edc20218453b709c63c58b9292c71be17/urllib3-2.2.0-py3-none-any.whl")
    version("2.1.0", sha256="55901e917a5896a349ff771be919f8bd99aff50b79fe58fec595eb37bbc56bb3", url="https://pypi.org/packages/96/94/c31f58c7a7f470d5665935262ebd7455c7e4c7782eb525658d3dbf4b9403/urllib3-2.1.0-py3-none-any.whl")
    version("2.0.7", sha256="fdb6d215c776278489906c2f8916e6e7d4f5a9b602ccbcfdf7f016fc8da0596e", url="https://pypi.org/packages/d2/b2/b157855192a68541a91ba7b2bbcb91f1b4faa51f8bae38d8005c034be524/urllib3-2.0.7-py3-none-any.whl")
    version("2.0.6", sha256="7a7c7003b000adf9e7ca2a377c9688bbc54ed41b985789ed576570342a375cd2", url="https://pypi.org/packages/26/40/9957270221b6d3e9a3b92fdfba80dd5c9661ff45a664b47edd5d00f707f5/urllib3-2.0.6-py3-none-any.whl")
    version("2.0.5", sha256="ef16afa8ba34a1f989db38e1dbbe0c302e4289a47856990d0682e374563ce35e", url="https://pypi.org/packages/37/dc/399e63f5d1d96bb643404ee830657f4dfcf8503f5ba8fa3c6d465d0c57fe/urllib3-2.0.5-py3-none-any.whl")
    version("2.0.4", sha256="de7df1803967d2c2a98e4b11bb7d6bd9210474c46e8a0401514e3a42a75ebde4", url="https://pypi.org/packages/9b/81/62fd61001fa4b9d0df6e31d47ff49cfa9de4af03adecf339c7bc30656b37/urllib3-2.0.4-py3-none-any.whl")
    version("2.0.3", sha256="48e7fafa40319d358848e1bc6809b208340fafe2096f1725d05d67443d0483d1", url="https://pypi.org/packages/8a/03/ad9306a50d05c166e3456fe810f33cee2b8b2a7a6818ec5d4908c4ec6b36/urllib3-2.0.3-py3-none-any.whl")
    version("2.0.2", sha256="d055c2f9d38dc53c808f6fdc8eab7360b6fdbbde02340ed25cfbcd817c62469e", url="https://pypi.org/packages/4b/1d/f8383ef593114755429c307449e7717b87044b3bcd5f7860b89b1f759e34/urllib3-2.0.2-py3-none-any.whl")
    version("2.0.1", sha256="d75e5ece05ff170e323303fd924edf29e705f5ae057c489f453a686b639bb68a", url="https://pypi.org/packages/fc/cf/2bbbd8fc9b92b6f5b9eaff7ed0ddde10ecccfaf345f06e55cca99ed77121/urllib3-2.0.1-py3-none-any.whl")
    version("2.0.0", sha256="8f7f917bc6ff1c021c4b7b677229c455a7612878748581f6de39fd45e4fa21ae", url="https://pypi.org/packages/ca/25/fe81738a115a2f1005b19bd69b6253b7b5cd6c9119164f13f02ec627fc41/urllib3-2.0.0-py3-none-any.whl")
    version("1.26.18", sha256="34b97092d7e0a3a8cf7cd10e386f401b3737364026c45e622aa02903dffe0f07", url="https://pypi.org/packages/b0/53/aa91e163dcfd1e5b82d8a890ecf13314e3e149c05270cc644581f77f17fd/urllib3-1.26.18-py2.py3-none-any.whl")
    version("1.26.17", sha256="94a757d178c9be92ef5539b8840d48dc9cf1b2709c9d6b588232a055c524458b", url="https://pypi.org/packages/48/fe/a5c6cc46e9fe9171d7ecf0f33ee7aae14642f8d74baa7af4d7840f9358be/urllib3-1.26.17-py2.py3-none-any.whl")
    version("1.26.16", sha256="8d36afa7616d8ab714608411b4a3b13e58f463aee519024578e062e141dce20f", url="https://pypi.org/packages/c5/05/c214b32d21c0b465506f95c4f28ccbcba15022e000b043b72b3df7728471/urllib3-1.26.16-py2.py3-none-any.whl")
    version("1.26.15", sha256="aa751d169e23c7479ce47a0cb0da579e3ede798f994f5816a74e4f4500dcea42", url="https://pypi.org/packages/7b/f5/890a0baca17a61c1f92f72b81d3c31523c99bec609e60c292ea55b387ae8/urllib3-1.26.15-py2.py3-none-any.whl")
    version("1.26.14", sha256="75edcdc2f7d85b137124a6c3c9fc3933cdeaa12ecb9a6a959f22797a0feca7e1", url="https://pypi.org/packages/fe/ca/466766e20b767ddb9b951202542310cba37ea5f2d792dae7589f1741af58/urllib3-1.26.14-py2.py3-none-any.whl")
    version("1.26.13", sha256="47cc05d99aaa09c9e72ed5809b60e7ba354e64b59c9c173ac3018642d8bb41fc", url="https://pypi.org/packages/65/0c/cc6644eaa594585e5875f46f3c83ee8762b647b51fc5b0fb253a242df2dc/urllib3-1.26.13-py2.py3-none-any.whl")
    version("1.26.12", sha256="b930dd878d5a8afb066a637fbb35144fe7901e3b209d1cd4f524bd0e9deee997", url="https://pypi.org/packages/6f/de/5be2e3eed8426f871b170663333a0f627fc2924cc386cd41be065e7ea870/urllib3-1.26.12-py2.py3-none-any.whl")
    version("1.26.11", sha256="c33ccba33c819596124764c23a97d25f32b28433ba0dedeb77d873a38722c9bc", url="https://pypi.org/packages/d1/cb/4783c8f1a90f89e260dbf72ebbcf25931f3a28f8f80e2e90f8a589941b19/urllib3-1.26.11-py2.py3-none-any.whl")
    version("1.26.10", sha256="8298d6d56d39be0e3bc13c1c97d133f9b45d797169a0e11cdd0e0489d786f7ec", url="https://pypi.org/packages/68/47/93d3d28e97c7577f563903907912f4b3804054e4877a5ba6651f7182c53b/urllib3-1.26.10-py2.py3-none-any.whl")
    version("1.26.9", sha256="44ece4d53fb1706f667c9bd1c648f5469a2ec925fcf3a776667042d645472c14", url="https://pypi.org/packages/ec/03/062e6444ce4baf1eac17a6a0ebfe36bb1ad05e1df0e20b110de59c278498/urllib3-1.26.9-py2.py3-none-any.whl")
    version("1.26.6", sha256="39fb8672126159acb139a7718dd10806104dec1e2f0f6c88aab05d17df10c8d4", url="https://pypi.org/packages/5f/64/43575537846896abac0b15c3e5ac678d787a4021e906703f1766bfb8ea11/urllib3-1.26.6-py2.py3-none-any.whl")
    version("1.25.11", sha256="f5321fbe4bf3fefa0efd0bfe7fb14e90909eb62a48ccda331726b4319897dd5e", url="https://pypi.org/packages/56/aa/4ef5aa67a9a62505db124a5cb5262332d1d4153462eb8fd89c9fa41e5d92/urllib3-1.25.11-py2.py3-none-any.whl")
    version("1.25.10", sha256="e7983572181f5e1522d9c98453462384ee92a0be7fac5f1413a1e35c56cc0461", url="https://pypi.org/packages/9f/f0/a391d1463ebb1b233795cabfc0ef38d3db4442339de68f847026199e69d7/urllib3-1.25.10-py2.py3-none-any.whl")
    version("1.25.9", sha256="88206b0eb87e6d677d424843ac5209e3fb9d0190d0ee169599165ec25e9d9115", url="https://pypi.org/packages/e1/e5/df302e8017440f111c11cc41a6b432838672f5a70aa29227bf58149dc72f/urllib3-1.25.9-py2.py3-none-any.whl")
    version("1.25.8", sha256="2f3db8b19923a873b3e5256dc9c2dedfa883e33d87c690d9c7913e1f40673cdc", url="https://pypi.org/packages/e8/74/6e4f91745020f967d09332bb2b8b9b10090957334692eb88ea4afe91b77f/urllib3-1.25.8-py2.py3-none-any.whl")
    version("1.25.7", sha256="a8a318824cc77d1fd4b2bec2ded92646630d7fe8619497b142c84a9e6f5a7293", url="https://pypi.org/packages/b4/40/a9837291310ee1ccc242ceb6ebfd9eb21539649f193a7c8c86ba15b98539/urllib3-1.25.7-py2.py3-none-any.whl")
    version("1.25.6", sha256="3de946ffbed6e6746608990594d08faac602528ac7015ac28d33cee6a45b7398", url="https://pypi.org/packages/e0/da/55f51ea951e1b7c63a579c09dd7db825bb730ec1fe9c0180fc77bfb31448/urllib3-1.25.6-py2.py3-none-any.whl")
    version("1.25.5", sha256="9c6c593cb28f52075016307fc26b0a0f8e82bc7d1ff19aaaa959b91710a56c47", url="https://pypi.org/packages/81/b7/cef47224900ca67078ed6e2db51342796007433ad38329558f56a15255f5/urllib3-1.25.5-py2.py3-none-any.whl")
    version("1.25.4", sha256="8a8090dd02b145256534c205e624eb20161080428ffa14408f6f283c0d0c356e", url="https://pypi.org/packages/91/0d/7777358f672a14b7ae0dfcd29f949f409f913e0578190d6bfa68eb55864b/urllib3-1.25.4-py2.py3-none-any.whl")
    version("1.25.3", sha256="b246607a25ac80bedac05c6f282e3cdaf3afb65420fd024ac94435cabe6e18d1", url="https://pypi.org/packages/e6/60/247f23a7121ae632d62811ba7f273d0e58972d75e58a94d329d51550a47d/urllib3-1.25.3-py2.py3-none-any.whl")
    version("1.25.2", sha256="d363e3607d8de0c220d31950a8f38b18d5ba7c0830facd71a1c6b1036b7ce06c", url="https://pypi.org/packages/39/ec/d93dfc69617a028915df914339ef66936ea976ef24fa62940fd86ba0326e/urllib3-1.25.2-py2.py3-none-any.whl")
    version("1.24.3", sha256="a637e5fae88995b256e3409dc4d52c2e2e0ba32c42a6365fee8bbd2238de3cfb", url="https://pypi.org/packages/01/11/525b02e4acc0c747de8b6ccdab376331597c569c42ea66ab0a1dbd36eca2/urllib3-1.24.3-py2.py3-none-any.whl")
    version("1.24.2", sha256="4c291ca23bbb55c76518905869ef34bdd5f0e46af7afe6861e8375643ffee1a0", url="https://pypi.org/packages/df/1c/59cca3abf96f991f2ec3131a4ffe72ae3d9ea1f5894abe8a9c5e3c77cfee/urllib3-1.24.2-py2.py3-none-any.whl")
    version("1.24.1", sha256="61bf29cada3fc2fbefad4fdf059ea4bd1b4a86d2b6d15e1c7c0b582b9752fe39", url="https://pypi.org/packages/62/00/ee1d7de624db8ba7090d1226aebefab96a2c71cd5cfa7629d6ad3f61b79e/urllib3-1.24.1-py2.py3-none-any.whl")
    version("1.24", sha256="8819bba37a02d143296a4d032373c4dd4aca11f6d4c9973335ca75f9c8475f59", url="https://pypi.org/packages/8c/4b/5cbc4cb46095f369117dcb751821e1bef9dd86a07c968d8757e9204c324c/urllib3-1.24-py2.py3-none-any.whl")
    version("1.23", sha256="b5725a0bd4ba422ab0e66e89e030c806576753ea3ee08554382c14e685d117b5", url="https://pypi.org/packages/bd/c9/6fdd990019071a4a32a5e7cb78a1d92c53851ef4f56f62a3486e6a7d8ffb/urllib3-1.23-py2.py3-none-any.whl")
    version("1.22", sha256="06330f386d6e4b195fbfc736b297f58c5a892e4440e54d294d7004e3a9bbea1b", url="https://pypi.org/packages/63/cb/6965947c13a94236f6d4b8223e21beb4d576dc72e8130bd7880f600839b8/urllib3-1.22-py2.py3-none-any.whl")
    version("1.21.1", sha256="8ed6d5c1ff9d6ba84677310060d6a3a78ca3072ce0684cb3c645023009c114b1", url="https://pypi.org/packages/24/53/f397db567de0aa0e81b211d81c13c41a779f14893e42189cf5bdb97611b2/urllib3-1.21.1-py2.py3-none-any.whl")
    version("1.20", sha256="b64c0faa183e9e9e76193146c4147e82a734982c6b6719dca851d6cc4ec90c01", url="https://pypi.org/packages/67/87/67be08389f8df83c9ba4c12e618a4ad93546e234a1e9530618735cd9b73d/urllib3-1.20-py2.py3-none-any.whl")
    version("1.14", sha256="ffe8859ca4fdfb021c2e8e0d3033f6c5eb372f8d4c3fd5455523055a2806a437", url="https://pypi.org/packages/73/55/63deba73d82dfa39974ca3903110c3e3557ff8758a3a79482810915b385d/urllib3-1.14-py2.py3-none-any.whl")

    variant("secure", default=False)
    variant("socks", default=False)

    with default_args(type="run"):
        depends_on("py-certifi", when="@1.13:2.0+secure")
        depends_on("py-cryptography@1.9:", when="@2.0.0-alpha2:2.0+secure")
        depends_on("py-cryptography@1.3.4:", when="@1.24:1.24.1,1.24.3:2.0.0-alpha1+secure")
        depends_on("py-idna@2:", when="@1.24:1.24.1,1.24.3:2.0+secure")
        depends_on("py-ipaddress", when="@1.24:1.24.1,1.24.3:1.24+secure")
        depends_on("py-pyopenssl@17.1:", when="@2.0.0-alpha2:2.0+secure")
        depends_on("py-pyopenssl@0.14:", when="@1.24:1.24.1,1.24.3:2.0.0-alpha1+secure")
        depends_on("py-pysocks@1.5.6,1.6:", when="@1.17:+socks")
        depends_on("py-urllib3-secure-extra", when="@1.26.12:2.0+secure")

        # marker: extra == "secure;python-version<="2-7""
        # depends_on("py-certifi", when="@1.11:1.12")

        # marker: extra == "secure;python-version>"2-7""
        # depends_on("py-certifi", when="@1.11:1.12")

