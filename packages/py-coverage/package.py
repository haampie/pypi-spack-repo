##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyCoverage(PythonPackage):
    version("7.4.4", sha256="c901df83d097649e257e803be22592aedfd5182f07b3cc87d640bbb9afd50f49", url="https://pypi.org/packages/bf/d5/f809d8b630cf4c11fe490e20037a343d12a74ec2783c6cdb5aee725e7137/coverage-7.4.4.tar.gz")
    version("7.4.3", sha256="276f6077a5c61447a48d133ed13e759c09e62aff0dc84274a68dc18660104d52", url="https://pypi.org/packages/d2/e2/f2d313169e0ecf1b46295b3ddf28a6818d02c1b047413f38b6325823cb2b/coverage-7.4.3.tar.gz")
    version("7.4.2", sha256="1a5ee18e3a8d766075ce9314ed1cb695414bae67df6a4b0805f5137d93d6f1cb", url="https://pypi.org/packages/bf/4f/a873791c3caa6c064a05332a5954f73b7ad6cfd6c1a1368aef1dd4ff1cfe/coverage-7.4.2.tar.gz")
    version("7.4.1", sha256="1ed4b95480952b1a26d863e546fa5094564aa0065e1e5f0d4d0041f293251d04", url="https://pypi.org/packages/ca/41/e2ba20f090d0d16b73ad1f6fc542eb31b0db20662576583fb4f02554891f/coverage-7.4.1.tar.gz")
    version("7.4.0", sha256="707c0f58cb1712b8809ece32b68996ee1e609f71bd14615bd8f87a1293cb610e", url="https://pypi.org/packages/67/8a/a8aebe8c70fadb1ad8bdadfc8fb97ce9a518ca406cb6eece0ed17122bfa4/coverage-7.4.0.tar.gz")
    version("7.3.4", sha256="020d56d2da5bc22a0e00a5b0d54597ee91ad72446fa4cf1b97c35022f6b6dbf0", url="https://pypi.org/packages/42/02/088c18e25b23bf9958afe305083617ebe103dd5294a4ed4e1ef734c46b9b/coverage-7.3.4.tar.gz")
    version("7.3.3", sha256="df04c64e58df96b4427db8d0559e95e2df3138c9916c96f9f6a4dd220db2fdb7", url="https://pypi.org/packages/cf/79/b8ed9dbd011d2c9c7e0273f59daae4645469ab4ab09a23e1033e352978a6/coverage-7.3.3.tar.gz")
    version("7.3.2", sha256="be32ad29341b0170e795ca590e1c07e81fc061cb5b10c74ce7203491484404ef", url="https://pypi.org/packages/57/44/ecd5442163c53f333bfcd2e7f428457a68b008a4b65d436a64b1db362451/coverage-7.3.2.tar.gz")
    version("7.3.1", sha256="6cb7fe1581deb67b782c153136541e20901aa312ceedaf1467dcb35255787952", url="https://pypi.org/packages/29/73/f584ffd3acea29a2f2330bb8fd0c14af3f0efd03f73c696a6f229199198e/coverage-7.3.1.tar.gz")
    version("7.3.0", sha256="49dbb19cdcafc130f597d9e04a29d0a032ceedf729e41b181f51cd170e6ee865", url="https://pypi.org/packages/4e/87/c0163d39ac70cab62ebcaee164c988215cd312919a78940c2251a2fcfabb/coverage-7.3.0.tar.gz")
    version("7.2.6", sha256="2025f913f2edb0272ef15d00b1f335ff8908c921c8eb2013536fcaf61f5a683d", url="https://pypi.org/packages/fc/6d/e8658433ce675a34ac82167ce8b890b1c020dcb6bacc7a0e4505af82bfaa/coverage-7.2.6.tar.gz")
    version("6.4.4", sha256="e16c45b726acb780e1e6f88b286d3c10b3914ab03438f32117c4aa52d7f30d58", url="https://pypi.org/packages/79/f3/8c1af7233f874b5df281397e2b96bedf58dc440bd8c6fdbf93a4436c517a/coverage-6.4.4.tar.gz")
    version("6.3.1", sha256="6c3f6158b02ac403868eea390930ae64e9a9a2a5bbfafefbb920d29258d9f2f8", url="https://pypi.org/packages/4f/9c/fd040e3291e6b123fb35474c8c685b9afa8f14abd4efba3fe2fa2b71ea2c/coverage-6.3.1.tar.gz")
    version("6.1.2", sha256="d9a635114b88c0ab462e0355472d00a180a5fbfd8511e7f18e4ac32652e7d972", url="https://pypi.org/packages/56/45/6917f6de0b18a4d3b465c5b35c95df4cf1e440de37c7584275412f11f637/coverage-6.1.2.tar.gz")
    version("5.5", sha256="ebe78fe9a0e874362175b02371bdfbee64d8edc42a044253ddf4ee7d3c15212c", url="https://pypi.org/packages/38/df/d5e67851e83948def768d7fb1a0fd373665b20f56ff63ed220c6cd16cb11/coverage-5.5.tar.gz")
    version("5.4", sha256="6d2e262e5e8da6fa56e774fb8e2643417351427604c2b177f8e8c5f75fc928ca", url="https://pypi.org/packages/29/83/9429871de6c7ec9ff113e12246af75aad4f0a7f31c66d0a499a0b7443a71/coverage-5.4.tar.gz")
    version("5.3.1", sha256="38f16b1317b8dd82df67ed5daa5f5e7c959e46579840d77a67a4ceb9cef0a50b", url="https://pypi.org/packages/40/05/2c1d1405edeec38114abcd404f15a35a41029b89d0514aa8ad11ffcbde81/coverage-5.3.1.tar.gz")
    version("5.3", sha256="280baa8ec489c4f542f8940f9c4c2181f0306a8ee1a54eceba071a449fb870a0", url="https://pypi.org/packages/da/50/4c0c93ea67c8b42aa700cfbdedd64ea5ac5e7108ba14e3e744f57309304b/coverage-5.3.tar.gz")
    version("5.2.1", sha256="a34cb28e0747ea15e82d13e14de606747e9e484fb28d63c999483f5d5188e89b", url="https://pypi.org/packages/20/c0/0df91b7bde75063316f0aa5fa699f76b2bbb4514f190a2f68580b18d2f31/coverage-5.2.1.tar.gz")
    version("5.2", sha256="1874bdc943654ba46d28f179c1846f5710eda3aeb265ff029e0ac2b52daae404", url="https://pypi.org/packages/23/ca/c722303813a4ab9bbaee2c2639aebbfd47cc542081c56608a31a9fa3cf7d/coverage-5.2.tar.gz")
    version("5.1", sha256="f90bfc4ad18450c80b024036eaf91e4a246ae287701aaa88eaebebf150868052", url="https://pypi.org/packages/fe/4d/3d892bdd21acba6c9e9bec6dc93fbe619883a0967c62f976122f2c6366f3/coverage-5.1.tar.gz")
    version("5.0.4", sha256="1b60a95fc995649464e0cd48cecc8288bac5f4198f21d04b8229dc4097d76823", url="https://pypi.org/packages/d1/7d/ac53d7350a5178c1f59ddf0f17552bf68e4bb3a202543f9a30bbaa46cf80/coverage-5.0.4.tar.gz")
    version("5.0.3", sha256="77afca04240c40450c331fa796b3eab6f1e15c5ecf8bf2b8bee9706cd5452fef", url="https://pypi.org/packages/6d/1d/d44ed71d9a254453f4dd296cadf497957454995a35defcc7a7424caec89d/coverage-5.0.3.tar.gz")
    version("5.0.2", sha256="b251c7092cbb6d789d62dc9c9e7c4fb448c9138b51285c36aeb72462cad3600e", url="https://pypi.org/packages/a7/58/e406d5ae5181b32ce784ab143a4bb7f0831bb3cfb95bcf7e04f0b4c67783/coverage-5.0.2.tar.gz")
    version("4.5.4", sha256="e07d9f1a23e9e93ab5c62902833bf3e4b1f65502927379148b6622686223125c", url="https://pypi.org/packages/85/d5/818d0e603685c4a613d56f065a721013e942088047ff1027a632948bdae6/coverage-4.5.4.tar.gz")
    version("4.5.3", sha256="9de60893fb447d1e797f6bf08fdf0dbcda0c1e34c1b06c92bd3a363c0ea8c609", url="https://pypi.org/packages/82/70/2280b5b29a0352519bb95ab0ef1ea942d40466ca71c53a2085bdeff7b0eb/coverage-4.5.3.tar.gz")
    version("4.5.2", sha256="ab235d9fe64833f12d1334d29b558aacedfbca2356dfb9691f2d0d38a8a7bfb4", url="https://pypi.org/packages/fb/af/ce7b0fe063ee0142786ee53ad6197979491ce0785567b6d8be751d2069e8/coverage-4.5.2.tar.gz")
    version("4.5.1", sha256="56e448f051a201c5ebbaa86a5efd0ca90d327204d8b059ab25ad0f35fbfd79f1", url="https://pypi.org/packages/35/fe/e7df7289d717426093c68d156e0fd9117c8f4872b6588e8a8928a0f68424/coverage-4.5.1.tar.gz")
    version("4.5", sha256="b7a06a523dfeaf417da630d46ad4f4e11ca1bae6202c9312c4cb987dde5792fc", url="https://pypi.org/packages/11/24/6c0503ffe54c639d9b56f037daf723f7f09853d8efa668a836ee54ae0b2a/coverage-4.5.tar.gz")
    version("4.4.2", sha256="309d91bd7a35063ec7a0e4d75645488bfab3f0b66373e7722f23da7f5b0f34cc", url="https://pypi.org/packages/0b/e1/190ef1a264144c9b073b7353c259ca5431b5ddc8861b452e858fcbd0e9de/coverage-4.4.2.tar.gz")
    version("4.4.1", sha256="7a9c44400ee0f3b4546066e0710e1250fd75831adc02ab99dda176ad8726f424", url="https://pypi.org/packages/36/db/690ee79312bb60f121c0da1c973856ddb751afe09cc10caec1452208eaf4/coverage-4.4.1.tar.gz")
    version("4.4", sha256="b52e45af6992d6c1b733a54b60fc96a371a5d5d7ef3efa14ad34f884bf1738d6", url="https://pypi.org/packages/09/5f/be950b85b95abe63ae7817214bd2b19f10ce20a93991456018f24b73c55b/coverage-4.4.tar.gz")
    version("4.3.4", sha256="eaaefe0f6aa33de5a65f48dd0040d7fe08cac9ac6c35a56d0a7db109c3e733df", url="https://pypi.org/packages/6e/33/01cb50da2d0582c077299651038371dba988248058e03c7a7c4be0c84c40/coverage-4.3.4.tar.gz")
    version("4.3.3", sha256="688baf4f54a3c73f3c6609b70c7b7516de11bd11e5796a6a72aad9a652097c22", url="https://pypi.org/packages/ea/93/dbb8e58e56edc255bcea554cd2f14df0e0726bce634c407925ab34b19894/coverage-4.3.3.tar.gz")
    version("4.0-alpha6", sha256="afb4e6f0795c3ca233ba8130921b18b1d169427ced80f1240135d3b711230fa1", url="https://pypi.org/packages/d1/4c/87136ba38cc99e188e6288de24c4065cf96e3998453e13158c9965aaf43b/coverage-4.0a6.zip")

    variant("toml", default=False)

    with default_args(type="run"):
        depends_on("py-toml", when="@5.0-beta1:5.2.0+toml")
        depends_on("py-tomli", when="@7.3.2:+toml ^python@:3.10")

