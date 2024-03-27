##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyStackData(PythonPackage):
    version("0.6.3", sha256="d5558e0c25a4cb0853cddad3d77da9891a08cb85dd9f9f91b9f8cd66e511e695", url="https://pypi.org/packages/f1/7b/ce1eafaf1a76852e2ec9b22edecf1daa58175c090266e9f6c64afcd81d91/stack_data-0.6.3-py3-none-any.whl")
    version("0.6.2", sha256="cbb2a53eb64e5785878201a97ed7c7b94883f48b87bfb0bbe8b623c74679e4a8", url="https://pypi.org/packages/6a/81/aa96c25c27f78cdc444fec27d80f4c05194c591465e491a1358d8a035bc1/stack_data-0.6.2-py3-none-any.whl")
    version("0.6.1", sha256="960cb054d6a1b2fdd9cbd529e365b3c163e8dabf1272e02cfe36b58403cff5c6", url="https://pypi.org/packages/e7/f1/a1f2fd4a75d371412650b3ddc16741e0de383fe701953566c9288f678a5b/stack_data-0.6.1-py3-none-any.whl")
    version("0.6.0", sha256="b92d206ef355a367d14316b786ab41cb99eb453a21f2cb216a4204625ff7bc07", url="https://pypi.org/packages/0b/d3/87a41424a1d24d2cb9f5ae4ef4a97c7437ad81eb37d21049ce5decd13d70/stack_data-0.6.0-py3-none-any.whl")
    version("0.5.1", sha256="5120731a18ba4c82cefcf84a945f6f3e62319ef413bfc210e32aca3a69310ba2", url="https://pypi.org/packages/57/dc/9367ef8074e2331706fbad14d749157341fbffd21339c43820e07664ec94/stack_data-0.5.1-py3-none-any.whl")
    version("0.5.0", sha256="66d2ebd3d7f29047612ead465b6cae5371006a71f45037c7e2507d01367bce3b", url="https://pypi.org/packages/9d/ad/22b5d86e421b2786aeb166cf51d519ce5a2a8878c7542d3e58e75aac02b5/stack_data-0.5.0-py3-none-any.whl")
    version("0.4.0", sha256="b94fed36d725cfabc6d09ed5886913e35eed9009766a1af1d5941b9da3a94aaa", url="https://pypi.org/packages/0d/c3/10a5a5731867c3e0337ebba1827006a937cccfadb6575911d750fd6d8eeb/stack_data-0.4.0-py3-none-any.whl")
    version("0.3.0", sha256="aa1d52d14d09c7a9a12bb740e6bdfffe0f5e8f4f9218d85e7c73a8c37f7ae38d", url="https://pypi.org/packages/f3/99/9e6a7eea1618eecf8767dc7970722003761403893fa978fa30be6f3846eb/stack_data-0.3.0-py3-none-any.whl")
    version("0.2.0", sha256="999762f9c3132308789affa03e9271bbbe947bf78311851f4d485d8402ed858e", url="https://pypi.org/packages/6b/25/9a454b432df53ffbbb4f03198c3347f393c34f4de07fb652563bdbdf91e8/stack_data-0.2.0-py3-none-any.whl")
    version("0.1.4", sha256="02cc0683cbc445ae4ca8c4e3a0e58cb1df59f252efb0aa016b34804a707cf9bc", url="https://pypi.org/packages/42/0b/d09b87028bf9ddc249bf0885367f679cc1a0cc5c9996bbef37eb849b3ee7/stack_data-0.1.4-py3-none-any.whl")

    with default_args(type="run"):
        depends_on("py-asttokens@2.1:", when="@0.6:")
        depends_on("py-asttokens", when="@0.0.7:0.5")
        depends_on("py-executing@1.2:", when="@0.6:")
        depends_on("py-executing", when="@0.0.7:0.5")
        depends_on("py-pure-eval", when="@0.0.7:")

