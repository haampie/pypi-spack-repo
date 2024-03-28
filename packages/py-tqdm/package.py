# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyTqdm(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("4.66.2", sha256="1ee4f8a893eb9bef51c6e35730cebf234d5d0b6bd112b0271e10ed7c24a02bd9", url="https://pypi.org/packages/2a/14/e75e52d521442e2fcc9f1df3c5e456aead034203d4797867980de558ab34/tqdm-4.66.2-py3-none-any.whl")
    version("4.66.1", sha256="d302b3c5b53d47bce91fea46679d9c3c6508cf6332229aa1e7d8653723793386", url="https://pypi.org/packages/00/e5/f12a80907d0884e6dff9c16d0c0114d81b8cd07dc3ae54c5e962cc83037e/tqdm-4.66.1-py3-none-any.whl")
    version("4.66.0", sha256="39d459c7140b7890174e69d4d68d6291bc774a55b4bc5d93c0b760798ac5a03e", url="https://pypi.org/packages/a5/d6/502a859bac4ad5e274255576cd3e15ca273cdb91731bc39fb840dd422ee9/tqdm-4.66.0-py3-none-any.whl")
    version("4.65.2", sha256="6c431f7dee4f57284c8f4bd2eb1d4af00d730d38cc6098bd79880bcbec676276", url="https://pypi.org/packages/c0/ab/bd9ba7f84c509c8b377628bc66696d52623e30c6c0830db3c78748eec4b4/tqdm-4.65.2-py3-none-any.whl")
    version("4.65.1", sha256="16181c62ad2c6f8f6f29876e66322faad1c7fd3cc70aa9cc25ff63e50d1da031", url="https://pypi.org/packages/40/14/63f9a5bc62e8a50585b8a7a6de1ffab8eab09aaa5321b86127919ee7de02/tqdm-4.65.1-py3-none-any.whl")
    version("4.65.0", sha256="c4f53a17fe37e132815abceec022631be8ffe1b9381c2e6e30aa70edc99e9671", url="https://pypi.org/packages/e6/02/a2cff6306177ae6bc73bc0665065de51dfb3b9db7373e122e2735faf0d97/tqdm-4.65.0-py3-none-any.whl")
    version("4.64.1", sha256="6fee160d6ffcd1b1c68c65f14c829c22832bc401726335ce92c52d395944a6a1", url="https://pypi.org/packages/47/bb/849011636c4da2e44f1253cd927cfb20ada4374d8b3a4e425416e84900cc/tqdm-4.64.1-py2.py3-none-any.whl")
    version("4.64.0", sha256="74a2cdefe14d11442cedf3ba4e21a3b84ff9a2dbdc6cfae2c34addb2a14a5ea6", url="https://pypi.org/packages/8a/c4/d15f1e627fff25443ded77ea70a7b5532d6371498f9285d44d62587e209c/tqdm-4.64.0-py2.py3-none-any.whl")
    version("4.63.2", sha256="d647b0cefa04c89241cba1b4755e0bd7d3b3c1c7063f8653ed6c8591aad7e33e", url="https://pypi.org/packages/eb/d9/2fab9a32aface12b5ca96627e75609d1477bf37f1039fc0ca7ff56e7029b/tqdm-4.63.2-py2.py3-none-any.whl")
    version("4.63.1", sha256="6461b009d6792008d0000e1b0c7ca50195ec78c0e808a3a6b668a56a3236c3a5", url="https://pypi.org/packages/a6/73/7780b2c0868bdce1f13ce27b09b239f0eefc975a5c7ebc82a7613b2a2f05/tqdm-4.63.1-py2.py3-none-any.whl")
    version("4.62.3", sha256="8dd278a422499cd6b727e6ae4061c40b48fce8b76d1ccbf5d34fca9b7f925b0c", url="https://pypi.org/packages/63/f3/b7a1b8e40fd1bd049a34566eb353527bb9b8e9b98f8b6cf803bb64d8ce95/tqdm-4.62.3-py2.py3-none-any.whl")
    version("4.59.0", sha256="9fdf349068d047d4cfbe24862c425883af1db29bcddf4b0eeb2524f6fbdb23c7", url="https://pypi.org/packages/f8/3e/2730d0effc282960dbff3cf91599ad0d8f3faedc8e75720fdf224b31ab24/tqdm-4.59.0-py2.py3-none-any.whl")
    version("4.58.0", sha256="2c44efa73b8914dba7807aefd09653ac63c22b5b4ea34f7a80973f418f1a3089", url="https://pypi.org/packages/4e/8c/f1035bd24b0e352ddba7be320abc1603fc4c9976fcda6971ed287be59164/tqdm-4.58.0-py2.py3-none-any.whl")
    version("4.56.2", sha256="a89be573bfddb81bb0b395a416d5e55e3ecc73ce95a368a4f6360bedea33195e", url="https://pypi.org/packages/b3/db/dcda019790a8d989b8b0e7290f1c651a0aaef10bbe6af00032155e04858d/tqdm-4.56.2-py2.py3-none-any.whl")
    version("4.56.1", sha256="ab9b659241d82b8b51b2269ee243ec95286046bf06015c4e15a947cc15914211", url="https://pypi.org/packages/51/c1/2b9a2bf4b47481777c79bf6daad23a621ffc81e15fb0edf23b8ce42e0d61/tqdm-4.56.1-py2.py3-none-any.whl")
    version("4.56.0", sha256="4621f6823bab46a9cc33d48105753ccbea671b68bab2c50a9f0be23d4065cb5a", url="https://pypi.org/packages/80/02/8f8880a4fd6625461833abcf679d4c12a44c76f9925f92bf212bb6cefaad/tqdm-4.56.0-py2.py3-none-any.whl")
    version("4.49.0", sha256="8f3c5815e3b5e20bc40463fa6b42a352178859692a68ffaa469706e6d38342a5", url="https://pypi.org/packages/73/d5/f220e0c69b2f346b5649b66abebb391df1a00a59997a7ccf823325bd7a3e/tqdm-4.49.0-py2.py3-none-any.whl")
    version("4.48.2", sha256="1a336d2b829be50e46b84668691e0a2719f26c97c62846298dd5ae2937e4d5cf", url="https://pypi.org/packages/28/7e/281edb5bc3274dfb894d90f4dbacfceaca381c2435ec6187a2c6f329aed7/tqdm-4.48.2-py2.py3-none-any.whl")
    version("4.48.1", sha256="44b896c38f70f91826a3f83a3195b23c0460322bfc729566ec8e4e89bb5ad713", url="https://pypi.org/packages/43/74/ff00ba1f998684ffc67ea700ed45e5099877906ac36ca6d7b5d9695e6166/tqdm-4.48.1-py2.py3-none-any.whl")
    version("4.48.0", sha256="fcb7cb5b729b60a27f300b15c1ffd4744f080fb483b88f31dc8654b082cc8ea5", url="https://pypi.org/packages/af/88/7b0ea5fa8192d1733dea459a9e3059afc87819cb4072c43263f2ec7ab768/tqdm-4.48.0-py2.py3-none-any.whl")
    version("4.47.0", sha256="7810e627bcf9d983a99d9ff8a0c09674400fd2927eddabeadf153c14a2ec8656", url="https://pypi.org/packages/46/62/7663894f67ac5a41a0d8812d78d9d2a9404124051885af9d77dc526fb399/tqdm-4.47.0-py2.py3-none-any.whl")
    version("4.46.1", sha256="07c06493f1403c1380b630ae3dcbe5ae62abcf369a93bbc052502279f189ab8c", url="https://pypi.org/packages/f3/76/4697ce203a3d42b2ead61127b35e5fcc26bba9a35c03b32a2bd342a4c869/tqdm-4.46.1-py2.py3-none-any.whl")
    version("4.46.0", sha256="acdafb20f51637ca3954150d0405ff1a7edde0ff19e38fb99a80a66210d2a28f", url="https://pypi.org/packages/c9/40/058b12e8ba10e35f89c9b1fdfc2d4c7f8c05947df2d5eb3c7b258019fda0/tqdm-4.46.0-py2.py3-none-any.whl")
    version("4.45.0", sha256="ea9e3fd6bd9a37e8783d75bfc4c1faf3c6813da6bd1c3e776488b41ec683af94", url="https://pypi.org/packages/4a/1c/6359be64e8301b84160f6f6f7936bbfaaa5e9a4eab6cbc681db07600b949/tqdm-4.45.0-py2.py3-none-any.whl")
    version("4.44.1", sha256="be5ddeec77d78ba781ea41eacb2358a77f74cc2407f54b82222d7ee7dc8c8ccf", url="https://pypi.org/packages/1c/1a/cd6ee6b8b06557dcc5590785af2fe90fa10c19c28e567c1e3a299d5081e7/tqdm-4.44.1-py2.py3-none-any.whl")
    version("4.44.0", sha256="f0fc945df434e5e612fb7eb93bf29e924940913590450c3760f198dd75a2cd19", url="https://pypi.org/packages/ee/57/823bec179380e4829021cae90c8519f58d426e4b712d2a50b6651990461a/tqdm-4.44.0-py2.py3-none-any.whl")
    version("4.36.1", sha256="dd3fcca8488bb1d416aa7469d2f277902f26260c45aa86b667b074cd44b3b115", url="https://pypi.org/packages/e1/c1/bc1dba38b48f4ae3c4428aea669c5e27bd5a7642a74c8348451e0bd8ff86/tqdm-4.36.1-py2.py3-none-any.whl")
    version("4.19.9", sha256="782aa84b61a5246c4f9e5b938875009e0b759d9a5c9d16b12e4f8deefdff7892", url="https://pypi.org/packages/b3/c4/b67cf1ab472b770e08e94105a0c7ca7032cd070627c435f5998c9cf6e64f/tqdm-4.19.9-py2.py3-none-any.whl")
    version("4.8.4", sha256="a28f0ee0b8ec63659604c5432291e77147fb0c66e78242ed343aaccf89362f6d", url="https://pypi.org/packages/3a/c0/2653e9a90aef358da8880980c155218791f79b9a1d479a9a00f88ac42aac/tqdm-4.8.4-py2.py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    variant("notebook", default=False)
    variant("telegram", default=False)
    # END VARIANTS

    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-colorama", when="@4.61.2: platform=windows")
        depends_on("py-ipywidgets@6.0.0:", when="@4.59:+notebook")
        depends_on("py-requests", when="@4.55:+telegram")
    # END DEPENDENCIES

