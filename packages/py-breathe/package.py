##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyBreathe(PythonPackage):
    version("4.35.0", sha256="52c581f42ca4310737f9e435e3851c3d1f15446205a85fbc272f1f97ed74f5be", url="https://pypi.org/packages/eb/61/faddc25913de74e60e175bcfd962ec83532653c5895c0a06a83a6b5bbf3d/breathe-4.35.0-py3-none-any.whl")
    version("4.34.0", sha256="48804dcf0e607a89fb6ad88c729ef12743a42db03ae9489be4ef8f7c4011774a", url="https://pypi.org/packages/e8/6b/1385608a27653b6f02047d23f365f5dde7a54a266a0b3358b578c9a747b9/breathe-4.34.0-py3-none-any.whl")
    version("4.33.1", sha256="553aeffb00efc2cf96c4c9ed388d6ee8036ecd6d1bd9bd0c656fc25ca271bd3c", url="https://pypi.org/packages/04/e2/9d835c6f7fa0a575a005fa920506f07085fbf71651d1d1b1e8dd4f75b7af/breathe-4.33.1-py3-none-any.whl")
    version("4.33.0", sha256="9f2d517e350224d48a5790911cb028e2e9fafaf0e0eb89d684cbe1268933d4cc", url="https://pypi.org/packages/39/71/406a7b67477dd46700b4f7673e4a6e241d89d64979594dd696ebcd0333d8/breathe-4.33.0-py3-none-any.whl")
    version("4.32.0", sha256="47101b15b83495bf0e557aca3193b03ecf47f3787a89b9904067dea24164e84a", url="https://pypi.org/packages/90/44/d772e38b06366d48b742adcffe78c020f28247799d27b133d4bf2060d149/breathe-4.32.0-py3-none-any.whl")
    version("4.21.0", sha256="7660afa86f1dae3b19415a41d2a85c9b4a9d8f5cf26d0faa2f98c0715553333e", url="https://pypi.org/packages/57/ea/f7cb70ca71dac563591baf3f1fc740cbdf689f841ca1a1ffe837227425be/breathe-4.21.0.tar.gz")
    version("4.11.1", sha256="9b7a94122039ad61383551a696d9c1fa5c16b423a28dadf113389a481d03fad6", url="https://pypi.org/packages/0a/6f/d9ae3b6f8a2cb80856489f7aacdfa375f448e98d6e73fc69c66586a17060/breathe-4.11.1.tar.gz")
    version("4.11.0", sha256="ca91bbee1b0040cc4566b6d3be055e7ddf232efcb62f728165c0c7ac77c6a317", url="https://pypi.org/packages/b2/5a/108ac169fdf11252372e6713d926eb8c402b3c28509ae9350b115978b6cf/breathe-4.11.0.tar.gz")
    version("4.10.0", sha256="e94370b8b607a32d9611ed8246e635f02c21dc6847f04e888a00f66a12694eff", url="https://pypi.org/packages/2d/41/b3799f304116bdc5bce9016861afd676853f18d8222e1f1a057d79a70272/breathe-4.10.0.tar.gz")
    version("4.9.1", sha256="76e1f3706efeda2610d9a8e7b421d2877ff0654a3fe6d3190a8686536111a684", url="https://pypi.org/packages/c8/d6/c223ee6386c8aaf3b5d596fa15831cc31b4750526e39d9173df1e945d58c/breathe-4.9.1.tar.gz")
    version("4.9.0", sha256="dc664e4b573b29efd071f3feb52b0704c2fb644a5b8ec985527f8719aff8a16e", url="https://pypi.org/packages/f5/74/6dbabb6d93dfaf437aba9f0d4b4624dbfc975cbdc7adddd4da63daf07fa5/breathe-4.9.0.tar.gz")
    version("4.8.0", sha256="2a549639fd7186579809bc4c143df4c89e0dfd287da134e1f1a1ea032badbb29", url="https://pypi.org/packages/60/e4/6194c61b92d900110ed99ecd3e74673dce563294c53db57db3e4e96c2d77/breathe-4.8.0.tar.gz")
    version("4.7.3", sha256="9aa7927c0dcecdbc1663f5d5ce0c83e2e538021267b56db880d3b47ff8f744dc", url="https://pypi.org/packages/1c/7a/7a0f6c8367c96542d01fc1de8cedce8d93c8e3d9ded4e5b03eaefdcbcc82/breathe-4.7.3-py2.py3-none-any.whl")
    version("4.7.2", sha256="6d7eaeed9c54f3b92fe80acbbc224da21a3201cca6528f624d10dd639c34a7db", url="https://pypi.org/packages/82/c5/0220a19b26f2e4bdf7b3b762c05d3591f02092d0bcf4cfc2a4a6cd0f70dc/breathe-4.7.2-py2.py3-none-any.whl")
    version("4.7.1", sha256="01603def2e9f19a18a25744480aaf88e9cf0a00e778c15984813d2b20621a1d7", url="https://pypi.org/packages/52/e5/f28e9ab2d59b3731b82230797e694c77b4424080656bada4e5b3ed98fd88/breathe-4.7.1-py2.py3-none-any.whl")
    version("4.7.0", sha256="d90c309ca44811f0cc3fe45b99ef7de1418ab7ba7d9897b14671c7352d761f65", url="https://pypi.org/packages/da/a7/19fab4d5d2224b3bf8ac7b76d09c43a51e9448ed97a1892bb747d8f11bba/breathe-4.7.0-py2.py3-none-any.whl")

    with default_args(type="run"):
        depends_on("py-docutils@0.12:", when="@4.28:")
        depends_on("py-docutils@0.5:", when="@4.7")
        depends_on("py-six@1.4:", when="@4.7")
        depends_on("py-sphinx@4.0.0:5.0.0-beta1,5.0.1:", when="@4.35:")
        depends_on("py-sphinx@4.0.0:5.0.0-beta1,5.0.1:5", when="@4.34")
        depends_on("py-sphinx@3.0.0:4", when="@4.29.1:4.33")
        depends_on("py-sphinx@1.4:", when="@4.7")

