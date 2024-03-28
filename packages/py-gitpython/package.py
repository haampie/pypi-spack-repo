# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyGitpython(PythonPackage):
    # BEGIN VERSIONS
    version("3.1.42", sha256="1bf9cd7c9e7255f77778ea54359e54ac22a72a5b51288c457c881057b7bb9ecd", url="https://pypi.org/packages/67/c7/995360c87dd74e27539ccbfecddfb58e08f140d849fcd7f35d2ed1a5f80f/GitPython-3.1.42-py3-none-any.whl")
    version("3.1.41", sha256="c36b6634d069b3f719610175020a9aed919421c87552185b085e04fbbdb10b7c", url="https://pypi.org/packages/45/c6/a637a7a11d4619957cb95ca195168759a4502991b1b91c13d3203ffc3748/GitPython-3.1.41-py3-none-any.whl")
    version("3.1.40", sha256="cf14627d5a8049ffbf49915732e5eddbe8134c3bdb9d476e6182b676fc573f8a", url="https://pypi.org/packages/8d/c4/82b858fb6483dfb5e338123c154d19c043305b01726a67d89532b8f8f01b/GitPython-3.1.40-py3-none-any.whl")
    version("3.1.39", sha256="a149403bbe7f8c5c6069cb50c1a5761a9449a8e90ab603196a33d7ec7b5e0c94", url="https://pypi.org/packages/1c/25/866c4ee2bce18128f2ff02dc06afbc9be30f990af1f14461d5540c31e5fc/GitPython-3.1.39-py3-none-any.whl")
    version("3.1.38", sha256="9e98b672ffcb081c2c8d5aa630d4251544fb040fb158863054242f24a2a2ba30", url="https://pypi.org/packages/3c/ae/044453eacd5a526d3f242ccd77e38ee8219c65e0b132562b551bd67c61a4/GitPython-3.1.38-py3-none-any.whl")
    version("3.1.37", sha256="5f4c4187de49616d710a77e98ddf17b4782060a1788df441846bddefbb89ab33", url="https://pypi.org/packages/8a/7e/20f7e45878b5aed34320fbeeae8f78acc806e7bd708d00b1c6e64b016f5b/GitPython-3.1.37-py3-none-any.whl")
    version("3.1.36", sha256="8d22b5cfefd17c79914226982bb7851d6ade47545b1735a9d010a2a4c26d8388", url="https://pypi.org/packages/f9/94/1877b88fa3a0a30bedb43757a14f548c3b2719c8d83c16012f89564c0f3b/GitPython-3.1.36-py3-none-any.whl")
    version("3.1.35", sha256="c19b4292d7a1d3c0f653858db273ff8a6614100d1eb1528b014ec97286193c09", url="https://pypi.org/packages/0f/c6/bb9e2276b6fed126aa21e292493b45a3df4cfba7cbfcf2ab8809a6b0e718/GitPython-3.1.35-py3-none-any.whl")
    version("3.1.34", sha256="5d3802b98a3bae1c2b8ae0e1ff2e4aa16bcdf02c145da34d092324f599f01395", url="https://pypi.org/packages/38/fb/1a372b2a6be38501c66f714c07077cf9d9b84bfbf539f2c20639339a7f03/GitPython-3.1.34-py3-none-any.whl")
    version("3.1.33", sha256="11f22466f982211ad8f3bdb456c03be8466c71d4da8774f3a9f68344e89559cb", url="https://pypi.org/packages/cb/43/3aa8dfeff60bcfec7b4860acde4bef3cd2b85aac6e65fe24240fc51cb1b8/GitPython-3.1.33-py3-none-any.whl")
    version("3.1.27", sha256="5b68b000463593e05ff2b261acff0ff0972df8ab1b70d3cdbd41b546c8b8fc3d", url="https://pypi.org/packages/83/32/ce68915670da6fd6b1e3fb4b3554b4462512f6441dddd194fc0f4f6ec653/GitPython-3.1.27-py3-none-any.whl")
    version("3.1.24", sha256="dc0a7f2f697657acc8d7f89033e8b1ea94dd90356b2983bca89dc8d2ab3cc647", url="https://pypi.org/packages/fd/05/4b2e29f82f40d3add50956bdb9c868b3608381810b630ea439bb588f558d/GitPython-3.1.24-py3-none-any.whl")
    version("3.1.23", sha256="de2e2aff068097b23d6dca5daf588078fd8996a4218f6ffa704a662c2b54f9ac", url="https://pypi.org/packages/a1/94/c1a820262d9f98377e070756c77f8c4b6c20575aa9fd1966f2aea1dc4f6b/GitPython-3.1.23-py3-none-any.whl")
    version("3.1.22", sha256="5ca38c42f5c9d6dc233e790013ca19d88b9703339a625bd385166a7a12a3b8b1", url="https://pypi.org/packages/0f/40/77d9d79442c3efc850daef498572fd2a16dee6cc08cc54069f31dcb34673/GitPython-3.1.22-py3-none-any.whl")
    version("3.1.20", sha256="b1e1c269deab1b08ce65403cf14e10d2ef1f6c89e33ea7c5e5bb0222ea593b8a", url="https://pypi.org/packages/55/60/f884f01eef2a7255875862ec1b12d57d74113ec6e8d9e16c4d254cd6aa3c/GitPython-3.1.20-py3-none-any.whl")
    version("3.1.19", sha256="17690588e36bd0cee21921ce621fad1e8be45a37afa486ff846fb8efcf53c34c", url="https://pypi.org/packages/b7/f7/1687fc522bc7a7f7cdacd3854ac749bcadca44c257897843de60d1fad8fe/GitPython-3.1.19-py3-none-any.whl")
    version("3.1.18", sha256="fce760879cd2aebd2991b3542876dc5c4a909b30c9d69dfc488e504a8db37ee8", url="https://pypi.org/packages/bc/91/b38c4fabb6e5092ab23492ded4f318ab7299b19263272b703478038c0fbc/GitPython-3.1.18-py3-none-any.whl")
    version("3.1.17", sha256="29fe82050709760081f588dd50ce83504feddbebdc4da6956d02351552b1c135", url="https://pypi.org/packages/27/da/6f6224fdfc47dab57881fe20c0d1bc3122be290198ba0bf26a953a045d92/GitPython-3.1.17-py3-none-any.whl")
    version("3.1.16", sha256="37ac36cacf2e2be5e88f0810187c5833e71c1a2a8cf81588f5699d1b70183baa", url="https://pypi.org/packages/f3/2b/92c1bab288255e6bf3ec9e11218eb19ce507f374e7f253029a46e3c1cb1e/GitPython-3.1.16-py3-none-any.whl")
    version("3.1.15", sha256="a77824e516d3298b04fb36ec7845e92747df8fcfee9cacc32dd6239f9652f867", url="https://pypi.org/packages/d7/6d/0528adaff6229c5cd85feb84366e1cf3130d86c69d0acea02fe12b5d79c4/GitPython-3.1.15-py3-none-any.whl")
    version("3.1.14", sha256="3283ae2fba31c913d857e12e5ba5f9a7772bbc064ae2bb09efafa71b0dd4939b", url="https://pypi.org/packages/a6/99/98019716955ba243657daedd1de8f3a88ca1f5b75057c38e959db22fb87b/GitPython-3.1.14-py3-none-any.whl")
    version("3.1.13", sha256="c5347c81d232d9b8e7f47b68a83e5dc92e7952127133c5f2df9133f2c75a1b29", url="https://pypi.org/packages/fb/67/47a04d8a9d7f94645676fe683f1ee3fe9be01fe407686c180768a92abaac/GitPython-3.1.13-py3-none-any.whl")
    version("3.1.12", sha256="867ec3dfb126aac0f8296b19fb63b8c4a399f32b4b6fafe84c4b10af5fa9f7b5", url="https://pypi.org/packages/d7/cb/ec98155c501b68dcb11314c7992cd3df6dce193fd763084338a117967d53/GitPython-3.1.12-py3-none-any.whl")
    version("3.1.11", sha256="6eea89b655917b500437e9668e4a12eabdcf00229a0df1762aabd692ef9b746b", url="https://pypi.org/packages/24/d1/a7f8fe3df258549b303415157328bfcc63e9b11d06a7ad7a3327f3d32606/GitPython-3.1.11-py3-none-any.whl")
    version("3.1.10", sha256="58483ad99811321e3c0b52c8b2229ff517499229a4854752b7d128005986e409", url="https://pypi.org/packages/08/5c/2edb73fec5bf7e0bc4507c548ce408655c9ad03ffc6a66c7e278d75cfb5d/GitPython-3.1.10-py3-none-any.whl")
    version("3.1.9", sha256="138016d519bf4dd55b22c682c904ed2fd0235c3612b2f8f65ce218ff358deed8", url="https://pypi.org/packages/c0/d7/b2b0672e0331567157adf9281f41ee731c412ee518ca5e6552c27fa73c91/GitPython-3.1.9-py3-none-any.whl")
    version("3.1.8", sha256="1858f4fd089abe92ae465f01d5aaaf55e937eca565fb2c1fce35a51b5f85c910", url="https://pypi.org/packages/09/bc/ae32e07e89cc25b9e5c793d19a1e5454d30a8e37d95040991160f942519e/GitPython-3.1.8-py3-none-any.whl")
    version("3.1.7", sha256="fa3b92da728a457dd75d62bb5f3eb2816d99a7fe6c67398e260637a40e3fafb5", url="https://pypi.org/packages/f9/1e/a45320cab182bf1c8656107b3d4c042e659742822fc6bff150d769a984dd/GitPython-3.1.7-py3-none-any.whl")
    version("3.1.6", sha256="b742bc5010d9b69fc027f1be21443bc2ad87ffc81a365e958dbc275f3fe0475b", url="https://pypi.org/packages/24/74/4ce5de2e0182da3c90a29dc1ee44871ec3926abe6e3b2a99b5474985a30d/GitPython-3.1.6-py3-none-any.whl")
    version("3.1.5", sha256="39ae158ee8c360ee5a872fc411705430d4875cbe894654edbe39e246e38e4d64", url="https://pypi.org/packages/ef/bc/574a066bd8b61ae3c01ce5cd3eeb89aa0b1b4c0eb9fb137cd5b1cf8596be/GitPython-3.1.5-py3-none-any.whl")
    version("3.1.4", sha256="c23663f44f05d8a54d6623c70b4b3a831afbde892128b932eace35eb3fad8f99", url="https://pypi.org/packages/14/9c/b08d717ca4361d5e3e778beb88d3eb3a723aa4671446a14eaa6895aebeed/GitPython-3.1.4-py3-none-any.whl")
    version("3.1.3", sha256="ef1d60b01b5ce0040ad3ec20bc64f783362d41fa0822a2742d3586e1f49bb8ac", url="https://pypi.org/packages/8c/f9/c315aa88e51fabdc08e91b333cfefb255aff04a2ee96d632c32cb19180c9/GitPython-3.1.3-py3-none-any.whl")
    version("3.1.2", sha256="da3b2cf819974789da34f95ac218ef99f515a928685db141327c09b73dd69c09", url="https://pypi.org/packages/44/33/917e6fde1cad13daa7053f39b7c8af3be287314f75f1b1ea8d3fe37a8571/GitPython-3.1.2-py3-none-any.whl")
    version("3.1.1", sha256="71b8dad7409efbdae4930f2b0b646aaeccce292484ffa0bc74f1195582578b3d", url="https://pypi.org/packages/19/1a/0df85d2bddbca33665d2148173d3281b290ac054b5f50163ea735740ac7b/GitPython-3.1.1-py3-none-any.whl")
    version("3.1.0", sha256="43da89427bdf18bf07f1164c6d415750693b4d50e28fc9b68de706245147b9dd", url="https://pypi.org/packages/d3/2f/6a366d56c9b1355b0880be9ea66b166cb3536392638d8d91413ec66305ad/GitPython-3.1.0-py3-none-any.whl")
    version("3.0.9", sha256="ecf785b0b23bb6d28f5fff3d67cc4a07cb607e94476495d2a943d2e57d9fd473", url="https://pypi.org/packages/b5/b6/b56e9fa46e592769b00ba5402e570474829736db6ae869c70a1f7fa36d96/GitPython-3.0.9-py3-none-any.whl")
    version("0.3.6", sha256="f3f42ca085eedbd3a9956b5e639de58bbe77a119f6b3d5c3af27669a2322c4a9", url="https://pypi.org/packages/e9/d5/807cea9ffbfa398a23bbaff35d3fd37aa330c8c264c9489ed104b6192f74/GitPython-0.3.6.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-gitdb@4:", when="@3.1:")
        depends_on("py-gitdb2@3", when="@3.0.9:3.0")
        depends_on("py-typing-extensions@3.7.4.3:", when="@3.1.19:3.1.24 ^python@:3.9")
        depends_on("py-typing-extensions@3.7.4:", when="@3.1.15")
    # END DEPENDENCIES

