# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyNbconvert(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("7.16.2", sha256="0c01c23981a8de0220255706822c40b751438e32467d6a686e26be08ba784382", url="https://pypi.org/packages/4f/90/a522a41247a2c80289f265890d096821698819a15b12f30ff6e51ac00fe6/nbconvert-7.16.2-py3-none-any.whl")
    version("7.16.1", sha256="3188727dffadfdc9c6a1c7250729063d7bc78b355ad7aa023138afa030d1cd07", url="https://pypi.org/packages/dc/6f/2c4e3dafb36dff2c98a170c1d61275f2e2d6bfd0f07d25771c1c18a6a529/nbconvert-7.16.1-py3-none-any.whl")
    version("7.16.0", sha256="ad3dc865ea6e2768d31b7eb6c7ab3be014927216a5ece3ef276748dd809054c7", url="https://pypi.org/packages/c9/ec/c120b21e7f884a701e12a241992754e719adaf430d0d6b30c6655776bc35/nbconvert-7.16.0-py3-none-any.whl")
    version("7.15.0", sha256="0efd3ca74fd1525560e0312cec235e57dfbf3c5c775c7e61e04c532b28f8da6f", url="https://pypi.org/packages/de/4a/386d194d922546d2afb162cca97761fc9411872a7dc01eff8d25986c65a7/nbconvert-7.15.0-py3-none-any.whl")
    version("7.14.2", sha256="db28590cef90f7faf2ebbc71acd402cbecf13d29176df728c0a9025a49345ea1", url="https://pypi.org/packages/f4/50/275525adbd3dcef9aee708b97f146a094c4f7f24c15c668a6e7cb4120181/nbconvert-7.14.2-py3-none-any.whl")
    version("7.14.1", sha256="aa83e3dd27ea38d0c1d908e3ce9518d15fa908dd30521b6d5040bd23f33fffb0", url="https://pypi.org/packages/17/d3/7d08470a59e591f73afbc685d910886f96a38be86df3ca95398c491b8d23/nbconvert-7.14.1-py3-none-any.whl")
    version("7.14.0", sha256="483dde47facdaa4875903d651305ad53cd76e2255ae3c61efe412a95f2d22a24", url="https://pypi.org/packages/7f/ba/3a8a9870a8b42e63e8f5e770adedd191d5adc2348f3097fc0e7c83a39439/nbconvert-7.14.0-py3-none-any.whl")
    version("7.13.1", sha256="3c50eb2d326478cc90b8759cf2ab9dde3d892c6537cd6a5bc0991db8ef734bcc", url="https://pypi.org/packages/be/80/aa90a9fea4893b6ffb584ce5c61f3497fb76febe5648f9bc257b15a29ded/nbconvert-7.13.1-py3-none-any.whl")
    version("7.13.0", sha256="22521cfcc10ba5755e44acb6a70d2bd8a891ce7aed6746481e10cd548b169e19", url="https://pypi.org/packages/dc/d6/aac1997cd0342b17a2282ee0cc9130507b774cebd213e3f52127c2e08812/nbconvert-7.13.0-py3-none-any.whl")
    version("7.12.0", sha256="5b6c848194d270cc55fb691169202620d7b52a12fec259508d142ecbe4219310", url="https://pypi.org/packages/f4/c8/b2b201d67d8fbe6e33865bf32b84104a77e6ace7f1e12614d686a1130033/nbconvert-7.12.0-py3-none-any.whl")
    version("7.4.0", sha256="af5064a9db524f9f12f4e8be7f0799524bd5b14c1adea37e34e83c95127cc818", url="https://pypi.org/packages/2f/90/79bf16b584f5150550b0c175ca7a6e88334226e9275cf16db13785105d73/nbconvert-7.4.0-py3-none-any.whl")
    version("7.0.0", sha256="26843ae233167e8aae31c20e3e1d91f431f04c9f34363bbe2dd0d247f772641c", url="https://pypi.org/packages/b9/66/67e0a0f9e9cb0172d0d92686166418f69ec702ff7db2acca8c8caf325d0d/nbconvert-7.0.0-py3-none-any.whl")
    version("6.5.4", sha256="d679a947f849a966cbbd0bf6e7fedcfdb64be3b20ce7cef11ad55c13f5820e19", url="https://pypi.org/packages/78/19/e3aa3145650e26936bcbc3bbf1f5fa5e1fb5f9a8b2bfd94063383c315a48/nbconvert-6.5.4-py3-none-any.whl")
    version("6.5.3", sha256="2564bb5125d862949f72475de0c0348392add7ea62cc950985347bfe7bbc2034", url="https://pypi.org/packages/ae/32/98f5e052e81800e44838ab1ed0b884e034bb945d8d934f8ee1062ebe9965/nbconvert-6.5.3-py3-none-any.whl")
    version("6.5.2", sha256="2f2bc01f43a6db5ef0c450b75d3f129448c9b49f9a4205699ceda61e4936784b", url="https://pypi.org/packages/1b/8b/d6d7398a6f5b4d6b11047ec3c07d6e86049f265c496a83d4a8c4f12402a7/nbconvert-6.5.2-py3-none-any.whl")
    version("6.5.1", sha256="0a3e224ee753ac4dceeb0257c4a315c069dcc6f9f4ae0ad15c5ea84713d15e28", url="https://pypi.org/packages/54/d1/c3cc6a8144e9a0b25e2c66ac09a57fb05c01ad2d5f03b671fbe50d8aed81/nbconvert-6.5.1-py3-none-any.whl")
    version("6.5.0", sha256="c56dd0b8978a1811a5654f74c727ff16ca87dd5a43abd435a1c49b840fcd8360", url="https://pypi.org/packages/e8/f9/2de57146b8995d7f1b68d6fd0b4751d68c23f52e6f4ad926a7274184e8f2/nbconvert-6.5.0-py3-none-any.whl")
    version("6.4.5", sha256="e01d219f55cc79f9701c834d605e8aa3acf35725345d3942e3983937f368ce14", url="https://pypi.org/packages/8a/32/31c8101dadc1716198f569f6b77abe8406fc3c283b2974d0c15c802c811b/nbconvert-6.4.5-py3-none-any.whl")
    version("6.4.4", sha256="c0c13d11378e13f72b9cd509c008383dca4051c228e4985f75023b2a5d82fc9f", url="https://pypi.org/packages/16/31/5dcbffe34aeb9dc4760c0b36e21a7a621f0ab776d0fc8d39183fa5e9a77d/nbconvert-6.4.4-py3-none-any.whl")
    version("6.4.3", sha256="5a8eea76af7870d5dfa0197f52d1af85da23d5ad57e5f61d0e2fd1572761ad4e", url="https://pypi.org/packages/a7/4c/891bd3ef5f137c80b51cfcda6dc7d2ea934082f7890de36fb40aa593fcd9/nbconvert-6.4.3-py3-none-any.whl")
    version("6.4.2", sha256="7b006ae9979af56200e7fa3db39d9d12c99e811e8843b05dbe518e5b754bcb2e", url="https://pypi.org/packages/ac/e0/28f63b4dd05fa751b4b10e54f8a7cb15a5086320baad8700be41dc96eac0/nbconvert-6.4.2-py3-none-any.whl")
    version("6.4.1", sha256="fe93bc42485c54c5a49a2324c834aca1ff315f320a535bed3e3c4e085d3eebe3", url="https://pypi.org/packages/d9/62/568fc5c1a425b5cc4741ef2b3fbc545c413f1a236a18571e7faba447aaa6/nbconvert-6.4.1-py3-none-any.whl")
    version("6.3.0", sha256="8f23fbeabda4a500685d788ee091bf22cf34119304314304fb39f16e2fc32f37", url="https://pypi.org/packages/95/45/8d349273c93ca07e433eb561bf03e0d7ae8e0303904371eee2e0fbe0b037/nbconvert-6.3.0-py3-none-any.whl")
    version("6.2.0", sha256="b1b9dc4f1ff6cafae0e6d91f42fb9046fdc32e6beb6d7e2fa2cd7191ad535240", url="https://pypi.org/packages/19/c7/f7d49d1347b87a6c9324688ead2f02e1c119b20e0cc0474e69edfe63ff11/nbconvert-6.2.0-py3-none-any.whl")
    version("6.0.1", sha256="970122eaf3a3ddcfe4e03514b219df4be4af09e70c748faf6ba96f51a25fd09b", url="https://pypi.org/packages/e3/7f/ecd2d1f370c55c09b46deb6d400a0619582e4391e16993fd43487963c916/nbconvert-6.0.1-py3-none-any.whl")
    version("5.6.0", sha256="48d3c342057a2cf21e8df820d49ff27ab9f25fc72b8f15606bd47967333b2709", url="https://pypi.org/packages/f9/df/4505c0a7fea624cac461d0f41051f33456ae656753f65cee8c2f43121cb2/nbconvert-5.6.0-py2.py3-none-any.whl")
    version("5.5.0", sha256="4a978548d8383f6b2cfca4a3b0543afb77bc7cb5a96e8b424337ab58c12da9bc", url="https://pypi.org/packages/35/e7/f46c9d65f149271e47fca6ab084ef5c6e4cb1870f4c5cce6690feac55231/nbconvert-5.5.0-py2.py3-none-any.whl")
    version("4.2.0", sha256="fde887f769d8a727f3496999aa388b07355220b5a7c0479840f41b0c9f0be77f", url="https://pypi.org/packages/55/76/7989c6958ac939324ccc1589cfed0bb1f5cd984e604a24a8ea525b97b7c2/nbconvert-4.2.0-py2.py3-none-any.whl")
    version("4.1.0", sha256="18542116114f4340bbde64204cfb542612dfb6a6dcade3caedf13909834e27b5", url="https://pypi.org/packages/26/98/39e08d99ba3a514203973d2d1c9098f1db5e95652951670962bb6f8e7514/nbconvert-4.1.0-py2.py3-none-any.whl")
    version("4.0.0", sha256="8fbbc2739ce3dd0d893ba2ffd30e719407057e742ecaf0ba260e42f4a9b54c4e", url="https://pypi.org/packages/50/14/eedaf095daeb4bf13c14748c0522aeb5a4989ad67cf42ae56e41ed79086c/nbconvert-4.0.0-py2.py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    variant("serve", default=False)
    # END VARIANTS

    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-beautifulsoup4", when="@6.4.4:")
        depends_on("py-bleach@:4,5.0.1:", when="@7.5:")
        depends_on("py-bleach", when="@5:7.4")
        depends_on("py-defusedxml", when="@5.4:")
        depends_on("py-entrypoints@0.2.2:", when="@5.0.0:7.0.0-rc1")
        depends_on("py-entrypoints", when="@4.2:5.0.0-beta1")
        depends_on("py-importlib-metadata@3.6:", when="@7.0.0-rc2: ^python@:3.9")
        depends_on("py-jinja2@3.0.0:", when="@6.5:")
        depends_on("py-jinja2@2.4:", when="@5.5:6.4")
        depends_on("py-jinja2", when="@4.2:5.4")
        depends_on("py-jupyter-core@4.7.0:", when="@6.5:")
        depends_on("py-jupyter-core", when="@4.2:6.4")
        depends_on("py-jupyterlab-pygments", when="@6:")
        depends_on("py-lxml", when="@6.5.1:6,7.0.0:7.0")
        depends_on("py-markupsafe@2.0.0:", when="@6.4.5:")
        depends_on("py-mistune@2.0.3:", when="@7.6:")
        depends_on("py-mistune@2.0.3:2", when="@7.0.0:7.5")
        depends_on("py-mistune@0.8.1:0", when="@5.6:6")
        depends_on("py-mistune@0.8.1:", when="@5.4:5.5")
        depends_on("py-mistune@:0.5,0.7:", when="@4.2:5.2")
        depends_on("py-nbclient@0.5:", when="@6.5:")
        depends_on("py-nbclient@0.5", when="@6.0.0-rc0:6.4")
        depends_on("py-nbformat@5.7:", when="@7.5:")
        depends_on("py-nbformat@5.1:", when="@6.5:7.4")
        depends_on("py-nbformat@4.4:", when="@5.3:6.4")
        depends_on("py-nbformat", when="@4.2:5.2")
        depends_on("py-packaging", when="@6.5:")
        depends_on("py-pandocfilters@1.4.1:", when="@5.0.0:")
        depends_on("py-pygments@2.4.1:", when="@6:")
        depends_on("py-pygments", when="@4.2:5")
        depends_on("py-testpath", when="@5.0.0:6.4")
        depends_on("py-tinycss2", when="@6.5:")
        depends_on("py-tornado@6.1:", when="@6.5:+serve")
        depends_on("py-tornado@4:", when="@5:6.4+serve")
        depends_on("py-tornado", when="@4.2:4+serve")
        depends_on("py-traitlets@5.1:", when="@7.5:")
        depends_on("py-traitlets@5.0.0:", when="@6.1:7.4")
        depends_on("py-traitlets@4.2:", when="@5:6.0")
        depends_on("py-traitlets", when="@4.2:4")
    # END DEPENDENCIES

