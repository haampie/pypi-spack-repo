##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyMditPyPlugins(PythonPackage):
    version("0.4.0", sha256="b51b3bb70691f57f974e257e367107857a93b36f322a9e6d44ca5bf28ec2def9", url="https://pypi.org/packages/e5/3c/fe85f19699a7b40c8f9ce8ecee7e269b9b3c94099306df6f9891bdefeedd/mdit_py_plugins-0.4.0-py3-none-any.whl")
    version("0.3.5", sha256="ca9a0714ea59a24b2b044a1831f48d817dd0c817e84339f20e7889f392d77c4e", url="https://pypi.org/packages/fe/4c/a9b222f045f98775034d243198212cbea36d3524c3ee1e8ab8c0346d6953/mdit_py_plugins-0.3.5-py3-none-any.whl")
    version("0.3.4", sha256="4f1441264ac5cb39fa40a5901921c2acf314ea098d75629750c138f80d552cdf", url="https://pypi.org/packages/6b/5a/69b3be744aa58aa956fe97a50bfe7488a4b8544cccc907f92ccaa42208fd/mdit_py_plugins-0.3.4-py3-none-any.whl")
    version("0.3.3", sha256="36d08a29def19ec43acdcd8ba471d3ebab132e7879d442760d963f19913e04b9", url="https://pypi.org/packages/33/eb/c358112e8265f827cf8228eda36cf2a720ad933f5ca66f47f808edf4bb34/mdit_py_plugins-0.3.3-py3-none-any.whl")
    version("0.3.2", sha256="01e1c0f5432792d79ef627cd1745ce7c240d88d84b4e9dc6e87529a0f3ebba3e", url="https://pypi.org/packages/e4/92/268849737427f7f9a128d2586e561a7dfac723c02f3aaaaef4d27dd6829c/mdit_py_plugins-0.3.2-py3-none-any.whl")
    version("0.3.1", sha256="606a7f29cf56dbdfaf914acb21709b8f8ee29d857e8f29dcc33d8cb84c57bfa1", url="https://pypi.org/packages/de/d9/20870f611989b8dcfd2395eddefdd4b1983d6c36513cce7fbbe9eb345768/mdit_py_plugins-0.3.1-py3-none-any.whl")
    version("0.3.0", sha256="b1279701cee2dbf50e188d3da5f51fee8d78d038cdf99be57c6b9d1aa93b4073", url="https://pypi.org/packages/5b/c4/1cf60e11b55197fa2e5e8d2f732a229690f5a08b018ae1cf4c00585ca834/mdit_py_plugins-0.3.0-py3-none-any.whl")
    version("0.2.8", sha256="1833bf738e038e35d89cb3a07eb0d227ed647ce7dd357579b65343740c6d249c", url="https://pypi.org/packages/c0/cb/782222da2cc3d543aee662c33cbaf611ec010146ca21c91d5743e8d99603/mdit_py_plugins-0.2.8-py3-none-any.whl")
    version("0.2.7", sha256="2b0cb3ba8b64dfa2ce2f0d6b1d06708fb93426704520944ccefab1c8710da81e", url="https://pypi.org/packages/58/04/d5538523c5aae983c6057e6feba23dccb1da39d022264d7dacac1bfc4cd6/mdit_py_plugins-0.2.7-py3-none-any.whl")
    version("0.2.6", sha256="77fd75dad81109ee91f30eb49146196f79afbbae041f298ae4886c8c2b5e23d7", url="https://pypi.org/packages/0c/31/f0ecaccf7cd2db17332a94852f190840167c3cb7eadf09efe498412f909a/mdit_py_plugins-0.2.6-py3-none-any.whl")
    version("0.2.5", sha256="3c78db5cfdcf8f55f0af2b096de391bffcef0b3600222f434efb016d7c267cec", url="https://pypi.org/packages/66/62/fae9ee5766a7153d571ad732ef514c552efeaa31735fd60e6d9bc07fa9e4/mdit_py_plugins-0.2.5-py3-none-any.whl")
    version("0.2.4", sha256="f13ad035e977db0dd268af4a372716f3b555f1435f9623b4aed10c3c8bbf618c", url="https://pypi.org/packages/9d/df/16e87ebd0bb9d946d3b2d39c1171398f7f71eef5d9ca85adb94131b8c7b5/mdit_py_plugins-0.2.4-py3-none-any.whl")
    version("0.2.3", sha256="a75072d819f45de4b3bdb83178c92bd2e9466f8dc0866fa60f63fd87419d43ba", url="https://pypi.org/packages/97/23/3e017136aefe61b442fee2869fcc7756c814e3cfe551f225e1e085f27217/mdit_py_plugins-0.2.3-py3-none-any.whl")
    version("0.2.2", sha256="953c86ba91f593ace6e7839cd48da1a631160e270baa630519b9cc32a9173f83", url="https://pypi.org/packages/40/fe/0f06e8545ac0578741342cc00305b8d955863b72755af0c3771f339099fb/mdit_py_plugins-0.2.2-py3-none-any.whl")
    version("0.2.1", sha256="9994aa8c03e8a6fbd15b43413bd98521dafdf9d45aeb6213c769befa52ed58da", url="https://pypi.org/packages/64/f2/b477dfb13e6d3db6421cf61cd7b76562f16141e81cb174d837dda519253b/mdit_py_plugins-0.2.1-py3-none-any.whl")

    with default_args(type="run"):
        depends_on("py-markdown-it-py@1.0.0:", when="@0.4:")
        depends_on("py-markdown-it-py@1.0.0:2", when="@0.3")
        depends_on("py-markdown-it-py@1.0.0:1", when="@0.2.7:0.2")
        depends_on("py-markdown-it-py@0.5.8:1", when="@0.2.1:0.2.6")

