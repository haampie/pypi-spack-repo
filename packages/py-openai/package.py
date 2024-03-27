##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyOpenai(PythonPackage):
    version("1.14.3", sha256="7a465994a7ccf677a110c6cc2ef9d86229bad42c060b585b67049aa749f3b774", url="https://pypi.org/packages/83/30/f4c71038833912e3e3cd4083b0277d3a0e568e621cfb5c99f28b7c53dae1/openai-1.14.3-py3-none-any.whl")
    version("1.14.2", sha256="a48b3c4d635b603952189ac5a0c0c9b06c025b80eb2900396939f02bb2104ac3", url="https://pypi.org/packages/c5/e7/5254c1c37a475d68b9ec11397a2fa967a06ef5e58e41755857f35b26511b/openai-1.14.2-py3-none-any.whl")
    version("1.14.1", sha256="f9322b0bf3b82bbd06930fad535369a023f35a3a96d3ef0b827644a15d7aae97", url="https://pypi.org/packages/b3/05/4e1b778f3e261076354148e7716d14b95a279381e0a246e1fa7a5f574732/openai-1.14.1-py3-none-any.whl")
    version("1.14.0", sha256="5c9fd3a59f5cbdb4020733ddf79a22f6b7a36d561968cb3f3dd255cdd263d9fe", url="https://pypi.org/packages/75/d1/06a969e3b15429873d52cb2ca8ad9b2c3b28bcf977ba6796dbaef13f5b95/openai-1.14.0-py3-none-any.whl")
    version("1.13.4", sha256="379643b24ded980948794bc8092b01ed7ef35e7915c55ef47fa628e61a96ae1a", url="https://pypi.org/packages/f6/2a/09109ceaba91fd2b3b775aa0f73b58d21451ba913004ca01531f4989447b/openai-1.13.4-py3-none-any.whl")
    version("1.13.3", sha256="5769b62abd02f350a8dd1a3a242d8972c947860654466171d60fb0972ae0a41c", url="https://pypi.org/packages/a9/cc/f2bbce0ad52e09cd1aecb724af06385021b42a7317cd5938ba9c8581509d/openai-1.13.3-py3-none-any.whl")
    version("1.12.0", sha256="a54002c814e05222e413664f651b5916714e4700d041d5cf5724d3ae1a3e3481", url="https://pypi.org/packages/26/a1/75474477af2a1dae3a25f80b72bbaf20e8296191ece7fff2f67984206f33/openai-1.12.0-py3-none-any.whl")
    version("1.11.1", sha256="e0f388ce499f53f58079d0c1f571f356f2b168b84d0d24a412506b6abc714980", url="https://pypi.org/packages/37/34/f3c3d6bdc3eebf1b6a7c696dd6f934630af6cf5250cec099edf117cd3b53/openai-1.11.1-py3-none-any.whl")
    version("1.11.0", sha256="05abd618db093be1d2a16d3281136c163ddf57d7fe8fdf82c8b1edda6099c0b0", url="https://pypi.org/packages/91/00/6bafbbbb989a86af017960b8650f748e1091036f454b0ce406ad7ab7d981/openai-1.11.0-py3-none-any.whl")
    version("1.10.0", sha256="aa69e97d0223ace9835fbf9c997abe9ee95318f684fd2de6d02c870700c71ebc", url="https://pypi.org/packages/46/85/8681046cd9cc13a36ac76e4a1b047338c90dbeab2e9b14fb36de7f314c93/openai-1.10.0-py3-none-any.whl")
    version("0.27.8", sha256="e0a7c2f7da26bdbe5354b03c6d4b82a2f34bd4458c7a17ae1a7092c3e397e03c", url="https://pypi.org/packages/67/78/7588a047e458cb8075a4089d721d7af5e143ff85a2388d4a28c530be0494/openai-0.27.8-py3-none-any.whl")

    with default_args(type="run"):
        depends_on("py-aiohttp", when="@0.27:0.27.0,0.27.2:0")
        depends_on("py-anyio@3.5:", when="@1.3.8:")
        depends_on("py-distro@1.7:", when="@1:")
        depends_on("py-httpx@0.23:0", when="@1:")
        depends_on("py-pydantic@1.9.0:", when="@1:")
        depends_on("py-requests@2.20:", when="@0.27:0.27.0,0.27.2:0")
        depends_on("py-sniffio", when="@1.3.6:")
        depends_on("py-tqdm@4:", when="@1:")
        depends_on("py-tqdm", when="@0.27:0.27.0,0.27.2:0")
        depends_on("py-typing-extensions@4.7.0:", when="@1.6:")

