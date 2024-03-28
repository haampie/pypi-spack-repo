# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyAwsParallelcluster(PythonPackage):
    # BEGIN VERSIONS
    version("2.11.9", sha256="261754a1ef4e0cfbd47cc8fc466b7b252ff62148d6baf903a66276ce184846e2", url="https://pypi.org/packages/8b/cf/154355f046c01fd88d71c972d03c1ef4aa5cf3f4a0ac010563c08a66f648/aws_parallelcluster-2.11.9-py3-none-any.whl")
    version("2.11.8", sha256="ef8d5aac1abb8b6236673c55d2293523cee142e97a99e3af20481bdd4c276ebc", url="https://pypi.org/packages/05/47/9a04812dadbd0af188f1735ea90319c4f883ea08caf09cd19716ed779abd/aws_parallelcluster-2.11.8-py3-none-any.whl")
    version("2.11.7", sha256="3bcb43479b0495e7d93cc0eea68f071ec9ec8740298dba960643b98b32bf6e1c", url="https://pypi.org/packages/00/cf/f647f35cc5cf6a076812b8c90a0aeb9f9e824e4f9c7a6733c3ccd48463bf/aws_parallelcluster-2.11.7-py3-none-any.whl")
    version("2.11.6", sha256="4c84bed46a8d15de7789849b09154a1fe74fab9af2976952e3b2ee95e02ace93", url="https://pypi.org/packages/9d/33/96eaefb24350deb9962ea021446dd88e5b886dd83718c9f32982bd306c1e/aws_parallelcluster-2.11.6-py3-none-any.whl")
    version("2.11.5", sha256="2498d98c91fd6479d0854e0e9b4aedace8b1ef8fcce31414a3e5fd2d70b88c8a", url="https://pypi.org/packages/22/82/4f8daaa7a870c916f95951852d59fc3be9d064daf1a68a4ce5933072b5ef/aws_parallelcluster-2.11.5-py3-none-any.whl")
    version("2.11.4", sha256="e0b71e5b53949b15f1076ae98cfd53513ba097b51bb730ef8e33f3fd761d7df0", url="https://pypi.org/packages/ac/d6/42796b2eaf8e5af82f93e65dcaa5dae9586661e5a5fc850f16fa9b5084da/aws_parallelcluster-2.11.4-py3-none-any.whl")
    version("2.11.3", sha256="5ad3bfa666c6994d3c2be00318de63e5c30749ecf093ac828f07877d1ab5444e", url="https://pypi.org/packages/0b/43/d87b9d704f3947c1bf7182c7f785c7cf729e8653773b9b54dde1a8e28ea9/aws_parallelcluster-2.11.3-py3-none-any.whl")
    version("2.11.2", sha256="981bce581adbb2d4ffcd8640329984eb09dcc05a2e980d45a0a559358708f36f", url="https://pypi.org/packages/8c/01/977f81d59c16711c4be184f3576b074891126ed46f342848234588f4ae07/aws_parallelcluster-2.11.2-py3-none-any.whl")
    version("2.11.1", sha256="72f0c0d0e3e3c84167c24cc227fb56c2d5d0e3a9e6505b14160a3062781362b6", url="https://pypi.org/packages/eb/08/48361133a700b100715089c388991be4ff97007c773b8221a4ecb318ce66/aws_parallelcluster-2.11.1-py3-none-any.whl")
    version("2.11.0", sha256="851e5c569c9db8ed4bb850c11e422ab65927f77f1aa6a18d331e3c76b65bf20f", url="https://pypi.org/packages/93/d3/2545c03ea67fbdd18c63dc35496287b14a1e6461f979b68eba871032b954/aws_parallelcluster-2.11.0-py3-none-any.whl")
    version("2.10.4", sha256="ce749a555f9883c1472f865e15e7e280884bca5ffe82da1f25f4bff0b45a5c69", url="https://pypi.org/packages/8e/4c/15eac591e692d82040c533f76c083fd3dfa396fd12eed7181c79c4e338fe/aws_parallelcluster-2.10.4-py3-none-any.whl")
    version("2.10.3", sha256="02016358932375c1abb566c6b7f1c891fa617fc4a4ec4ce9969f87758d4039c7", url="https://pypi.org/packages/8b/a2/d59c402e1befa8bb0bba0b60ac95cfacf276fda07170c41c8b78ef0f85b8/aws-parallelcluster-2.10.3.tar.gz")
    version("2.10.2", sha256="95853535b82e8087c6635a946556ed886e68d3a77d67a375830c57d80f2bbd6e", url="https://pypi.org/packages/fb/a6/54a24afbd7fd95012f0ef932dc50081a7a2ed2a657e9b73bb991f182e467/aws-parallelcluster-2.10.2.tar.gz")
    version("2.10.1", sha256="b3d2ea836c08c9be1667d55a8999aae412d7c2b20f958ca5842e8fa440eb24e0", url="https://pypi.org/packages/f4/00/0c1be2aa6b1970424ae40a931e7841459339cb0896165496e09560288748/aws-parallelcluster-2.10.1.tar.gz")
    version("2.10.0", sha256="a7a27871b4f54cb913b0c1233e675131e9b2099549af0840d32c36b7e91b104b", url="https://pypi.org/packages/20/79/f83a62d33f37a9e262b75ef774e8ef9bac700b41a06fadb30e20429b8090/aws-parallelcluster-2.10.0.tar.gz")
    version("2.9.1", sha256="12dc22286cd447a16931f1f8619bdd47d4543fd0de7905d52b6c6f83ff9db8a3", url="https://pypi.org/packages/86/51/106935859c488450ce570dc0166991027f61dc764c2f091e77346554c665/aws-parallelcluster-2.9.1.tar.gz")
    version("2.9.0", sha256="e98a8426bc46aca0860d9a2be89bbc4a90aab3ed2f60ca6c385b595fbbe79a78", url="https://pypi.org/packages/81/97/7efa3d699d14569fe08c63a854ea19455ed291237ef128d7c29e759e2c13/aws-parallelcluster-2.9.0.tar.gz")
    version("2.8.1", sha256="c183dc3f053bc2445db724e561cea7f633dd5e7d467a7b3f9b2f2f703f7d5d49", url="https://pypi.org/packages/82/a8/0083dec45c11987fd61013a2fcb0ca6bf2c99e68e1ad79d59330979f58f9/aws-parallelcluster-2.8.1.tar.gz")
    version("2.8.0", sha256="4e67539d49fe987884a3ed7198dc13bc8a3a1778f0b3656dfe0ae899138678f2", url="https://pypi.org/packages/fb/06/46f3d1717920d7a77db753c6e0fa055fb4a484fab7c8d06a9340576871bb/aws-parallelcluster-2.8.0.tar.gz")
    version("2.7.0", sha256="7c34995acfcc256a6996541d330575fc711e1fd5735bf3d734d4e96c1dc8df60", url="https://pypi.org/packages/78/bc/e2c5703c1823696dd0dda173842a5d524fc035dcab6ae4fa131a23465c45/aws-parallelcluster-2.7.0.tar.gz")
    version("2.6.1", sha256="2ce9015d90b5d4dc88b46a44cb8a82e8fb0bb2b4cca30335fc5759202ec1b343", url="https://pypi.org/packages/7d/98/d02f00e6837a71c60ce411000725938c453eefa013890fc5c28c42dfb839/aws-parallelcluster-2.6.1.tar.gz")
    version("2.6.0", sha256="aaed6962cf5027206834ac24b3d312da91e0f96ae8607f555e12cb124b869f0c", url="https://pypi.org/packages/a1/2e/b9648aedb476fca241accec1051393510685409fc325555c759a9ba9eea9/aws-parallelcluster-2.6.0.tar.gz")
    version("2.5.1", sha256="4fd6e14583f8cf81f9e4aa1d6188e3708d3d14e6ae252de0a94caaf58be76303", url="https://pypi.org/packages/d0/c5/9b1c3ac4861fa239c884eeb688fb6ca097e5a2be124b3d45dfbbd78111e4/aws-parallelcluster-2.5.1.tar.gz")
    version("2.5.0", sha256="3b0209342ea0d9d8cc95505456103ad87c2d4e35771aa838765918194efd0ad3", url="https://pypi.org/packages/d5/f9/c6bd79c75ad4bb92461af81111aad3b8f14aa1e9463d76f8e806d81fafd5/aws-parallelcluster-2.5.0.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-boto3@1.16.14:", when="@2.10.4:")
        depends_on("py-future@0.16:0.18.2", when="@2.10.4:2.10")
        depends_on("py-ipaddress@1.0.22:", when="@2.10.4:2")
        depends_on("py-jinja2@2.11:", when="@2.10.4:3.0")
        depends_on("py-pyyaml@5.3.1:", when="@2.10.4:3.1.0,3.2:3.2.0-beta1")
        depends_on("py-setuptools", when="@2.10.4:")
        depends_on("py-tabulate@0.8.8:0.8", when="@2.11.8:2,3.4:")
        depends_on("py-tabulate@0.8.2:0.8.9", when="@2.11:2.11.7")
        depends_on("py-tabulate@0.8.2:0.8.7", when="@2.10.4:2.10")
    # END DEPENDENCIES

