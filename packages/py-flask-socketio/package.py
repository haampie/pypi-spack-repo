# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyFlaskSocketio(PythonPackage):
    # BEGIN VERSIONS
    version("5.3.6", sha256="9e62d2131842878ae6bfdd7067dfc3be397c1f2b117ab1dc74e6fe74aad7a579", url="https://pypi.org/packages/56/c8/dc0be9e26272dc89342868ecc2d9ddb9e31002b4b8e49fdb754aa0f9ecbf/Flask_SocketIO-5.3.6-py3-none-any.whl")
    version("5.3.5", sha256="04d42f2b7c2c3bdfea83b62e53f999374c573c698eddb53c468fca2bf75c1d3c", url="https://pypi.org/packages/21/d2/b068376f4c6cdb9737083e569e38c9612ea842b93297cc4f501ebe7eac93/Flask_SocketIO-5.3.5-py3-none-any.whl")
    version("5.3.4", sha256="564acfb24dcc9545cdae536cde0323653d9b547069a925f11eeb132338aa71c0", url="https://pypi.org/packages/08/4d/a2f07873367e8916e0bae32df1d3cb9b39ea2141d7a5fdfab8c9d6818d71/Flask_SocketIO-5.3.4-py3-none-any.whl")
    version("5.3.3", sha256="1f6a5afd68a4bf01140ef891c24f04ad0c52487d4829281a42eca0a35a204acf", url="https://pypi.org/packages/fd/0b/066d20aaa289d5a2e3058972ba3af5cb13934d0bbade62981e2c4edc3ce4/Flask_SocketIO-5.3.3-py3-none-any.whl")
    version("5.3.2", sha256="04093e3ca144467f9731c376796aff105d182ac4cccfcb056d05d567a675f306", url="https://pypi.org/packages/5d/10/5b3b69c51e88868e9a3ef97ae311a8daa8a4dd7200d887109a51f9cb3d9b/Flask_SocketIO-5.3.2-py3-none-any.whl")
    version("5.3.1", sha256="ff0c721f20bff1e2cfba77948727a8db48f187e89a72fe50c34478ce6efb3353", url="https://pypi.org/packages/a0/39/6899b61349cbcb19e84c948fbc8fc216c20d113e0e1ea996cf8fe5d50ee5/Flask_SocketIO-5.3.1-py3-none-any.whl")
    version("5.3.0", sha256="77b71d69c0b62ac2ce091efa53ed3ff0498d00059bb171a9ab69a395eb127207", url="https://pypi.org/packages/64/bf/7340f548c7f7eb16e1d46720a37555d8dc286c889367517cdce0a06e62c5/Flask_SocketIO-5.3.0-py3-none-any.whl")
    version("5.2.0", sha256="c82672b843fa271ec2961d356c608bc94a730660ac73a623bddb66c4b3d72215", url="https://pypi.org/packages/b2/ab/12484901c7597790081ae840f9a528a4812fa798cb2a97266d54df36ff23/Flask_SocketIO-5.2.0-py3-none-any.whl")
    version("5.1.2", sha256="eb0a1b9924bf899a20311326601e1c659fc9779175f778e495ddc5a438108c54", url="https://pypi.org/packages/21/05/2845470412f8432b921aa59e93b6d8f86aa27247691ee92650c9f70e62e5/Flask_SocketIO-5.1.2-py3-none-any.whl")
    version("5.1.1", sha256="07e1899e3b4851978b2ac8642080156c6294f8d0fc5212b4e4bcca713830306a", url="https://pypi.org/packages/70/73/b30d4448b64e877c4f75a916bdad0070c92570b8913c8e4893faf8c69850/Flask_SocketIO-5.1.1-py3-none-any.whl")
    version("2.9.6", sha256="be85842328f7847f511cf8cd828739884403b86ab5b0d576dae4241dd920b415", url="https://pypi.org/packages/cd/70/ae4a055477ecad475eec4990eb3474b152ff525ed10690afdcf180aee06c/Flask_SocketIO-2.9.6-py2.py3-none-any.whl")
    version("2.9.5", sha256="e45665e6ddab07b1c92cadc21c656b95635abc87ddb89a5fe1050c17588afffd", url="https://pypi.org/packages/de/71/c0d7c5d3f465464e38ef97d48851ec5cbd86c15a732c99ef6dc689deae39/Flask_SocketIO-2.9.5-py2.py3-none-any.whl")
    version("2.9.4", sha256="10939c523b63add65bdce3a431323685f61c1115d08122c49f8c4ecd53741bcc", url="https://pypi.org/packages/38/3c/8f45c5b309cc809b82bd9d7dd79a686429eeffac221c1acdff84a13e9daf/Flask_SocketIO-2.9.4-py2.py3-none-any.whl")
    version("2.9.3", sha256="b53e8f90430f251453ac50a4c46425e595f26398341f56131b77e5f8a288cf90", url="https://pypi.org/packages/2f/a1/e000535dbfc64602bcceea0d31474fa3adf0430b67c55c3fa24f33dba9ca/Flask_SocketIO-2.9.3-py2.py3-none-any.whl")
    version("2.9.2", sha256="11874b64dfb0769f32485170be73abd63d80edbdd209d876a7620575cbbd4ce1", url="https://pypi.org/packages/63/76/5aac107e14c5d680b60a312345502ddea101011218492c6d65b919051add/Flask_SocketIO-2.9.2-py2.py3-none-any.whl")
    version("2.9.1", sha256="62b86dc61515f9ef346cc36c371665457628a2ef3bae4323dca218f4514ee488", url="https://pypi.org/packages/a7/e3/5eaee362f75b20894fdee7dc8081631bcfa701c422b071c86fa83681bff2/Flask-SocketIO-2.9.1.tar.gz")
    version("2.9.0", sha256="2132a9d1e14f5fca894805d228a23fa575bb42ad85137360d35f5c517147337b", url="https://pypi.org/packages/64/2b/da19c1357ed7f93ec6900f7de15e7ec45bc34a7182a5976354688dcdccb3/Flask-SocketIO-2.9.0.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-flask@0.9:", when="@3.0.1:")
        depends_on("py-python-socketio@5.0.2:", when="@5:")
    # END DEPENDENCIES

