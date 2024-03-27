##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyTransformers(PythonPackage):
    version("4.38.2", sha256="c4029cb9f01b3dd335e52f364c52d2b37c65b4c78e02e6a08b1919c5c928573e", url="https://pypi.org/packages/b6/4d/fbe6d89fde59d8107f0a02816c4ac4542a8f9a85559fdf33c68282affcc1/transformers-4.38.2-py3-none-any.whl")
    version("4.38.1", sha256="a7a9265fb060183e9d975cbbadc4d531b10281589c43f6d07563f86322728973", url="https://pypi.org/packages/3e/6b/1b589f7b69aaea8193cf5bc91cf97410284aecd97b6312cdb08baedbdffe/transformers-4.38.1-py3-none-any.whl")
    version("4.38.0", sha256="a6d7ae9afcfcc0773d8b9ef20940344bd1cae54fe49175ddea61c7c8d11fb52a", url="https://pypi.org/packages/91/89/5416dc364c7ef0711c564fd61a69b03d1e40eeb5c506c38e53ba8a969e79/transformers-4.38.0-py3-none-any.whl")
    version("4.37.2", sha256="595a8b12a1fcc4ad0ced49ce206c58e17be68c85d7aee3d7546d04a32c910d2e", url="https://pypi.org/packages/85/f6/c5065913119c41ecad148c34e3a861f719e16b89a522287213698da911fc/transformers-4.37.2-py3-none-any.whl")
    version("4.37.1", sha256="05e4c4bf94f74addeb716bc83517f49d55df1e9022db3d5b027c801e9a410ebf", url="https://pypi.org/packages/ad/67/b4d6a51dcaf988cb45b31e26c6e33fb169fe34ba5fb168b086309bd7c028/transformers-4.37.1-py3-none-any.whl")
    version("4.37.0", sha256="669d4e2c12661e71c464eb18d6a9b9a2c74d4cba0f4648bb9323896bdd046826", url="https://pypi.org/packages/3c/45/52133ce6bce49a099cc865599803bf1fad93de887276f728e56848d77a70/transformers-4.37.0-py3-none-any.whl")
    version("4.36.2", sha256="462066c4f74ee52516f12890dcc9ec71d1a5e97998db621668455117a54330f6", url="https://pypi.org/packages/20/0a/739426a81f7635b422fbe6cb8d1d99d1235579a6ac8024c13d743efa6847/transformers-4.36.2-py3-none-any.whl")
    version("4.36.1", sha256="0e309d03634885f02d46801ec4f2c3fc1d614a5b9ebde608181f3e842bac53b8", url="https://pypi.org/packages/fc/04/0aad491cd98b09236c54ab849863ee85421eeda5138bbf9d33ecc594652b/transformers-4.36.1-py3-none-any.whl")
    version("4.36.0", sha256="e5a9d9424bcbc5008782ddd79ecbc3a50991e168cc730a14c4c89e80c61f419d", url="https://pypi.org/packages/0f/12/d8e27a190ca67811f81deea3183b528d9169f10b74d827e0b9211520ecfa/transformers-4.36.0-py3-none-any.whl")
    version("4.35.2", sha256="9dfa76f8692379544ead84d98f537be01cd1070de75c74efb13abcbc938fbe2f", url="https://pypi.org/packages/12/dd/f17b11a93a9ca27728e12512d167eb1281c151c4c6881d3ab59eb58f4127/transformers-4.35.2-py3-none-any.whl")
    version("4.31.0", sha256="8487aab0195ce1c2a5ae189305118b9720daddbc7b688edb09ccd79e3b149f6b", url="https://pypi.org/packages/21/02/ae8e595f45b6c8edee07913892b3b41f5f5f273962ad98851dc6a564bbb9/transformers-4.31.0-py3-none-any.whl")
    version("4.24.0", sha256="b7ab50039ef9bf817eff14ab974f306fd20a72350bdc9df3a858fd009419322e", url="https://pypi.org/packages/a4/df/3248eac2923ceffdf55686ff318e002b558e7c51f6a909dd870cf3185949/transformers-4.24.0-py3-none-any.whl")
    version("4.6.1", sha256="9d6569e31e5a4b7ab399eaf224f46ddcbb957e18a7c58cc7d469cb70e96467ea", url="https://pypi.org/packages/d5/43/cfe4ee779bbd6a678ac6a97c5a5cdeb03c35f9eaebbb9720b036680f9a2d/transformers-4.6.1-py3-none-any.whl")
    version("2.8.0", sha256="2b64cfe0033a47ba664837758cd9750196666ea1306e5c40ad5617353c3dc2fc", url="https://pypi.org/packages/a3/78/92cedda05552398352ed9784908b834ee32a0bd071a9b32de287327370b7/transformers-2.8.0-py3-none-any.whl")

    with default_args(type="run"):
        depends_on("py-boto3", when="@2:2.8")
        depends_on("py-filelock", when="@2.4:")
        depends_on("py-huggingface-hub@0.19.3:", when="@4.36:")
        depends_on("py-huggingface-hub@0.16.4:", when="@4.34:4.35")
        depends_on("py-huggingface-hub@0.14.1:", when="@4.29.1:4.31")
        depends_on("py-huggingface-hub@0.10.0:", when="@4.23:4.25")
        depends_on("py-huggingface-hub@0.0.8", when="@4.6:4.7")
        depends_on("py-numpy@1.17.0:", when="@4.3:")
        depends_on("py-numpy", when="@2:4.2")
        depends_on("py-packaging@20:", when="@4.11:")
        depends_on("py-packaging", when="@2.11:4.10")
        depends_on("py-protobuf", when="@3.4:3")
        depends_on("py-pyyaml@5.1:", when="@4.9:")
        depends_on("py-regex@:2019.12.9,2019.12.18:", when="@2.3:")
        depends_on("py-requests", when="@2:")
        depends_on("py-sacremoses", when="@2:4.18")
        depends_on("py-safetensors@0.4.1:", when="@4.37.2:")
        depends_on("py-safetensors@0.3.1:", when="@4.30:4.37.1")
        depends_on("py-sentencepiece@0.1.91", when="@3.5:3")
        depends_on("py-sentencepiece", when="@2:3.0.0")
        depends_on("py-tokenizers@0.14.0:", when="@4.35.2:")
        depends_on("py-tokenizers@0.11.1:0.11.2,0.11.4:0.13", when="@4.23:4.33")
        depends_on("py-tokenizers@0.10.1:0.10", when="@4.3.0:4.15")
        depends_on("py-tokenizers@0.5.2:0.5", when="@2.5.1:2.8")
        depends_on("py-tqdm@4.27:", when="@2.4:")

