##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyNbclassic(PythonPackage):
    version("1.0.0", sha256="f99e4769b4750076cd4235c044b61232110733322384a94a63791d2e7beacc66", url="https://pypi.org/packages/84/ae/eaa71c0ed64e8ddc426a4c902e83d31c4925e9d3418d6b240dd5752b6e71/nbclassic-1.0.0-py3-none-any.whl")
    version("0.5.6", sha256="e3c8b7de80046c4a36a74662a5e325386d345289906c618366d8154e03dc2322", url="https://pypi.org/packages/8b/24/63cd9d8b11fb3778ac11de109558e5f2bcd2eed5be01a14ab3162bc95b68/nbclassic-0.5.6-py3-none-any.whl")
    version("0.5.5", sha256="47791b04dbcb89bf7fde910a3d848fd4793a4248a8936202453631a87da37d51", url="https://pypi.org/packages/e4/cd/c980bc2da7b46431e2a6f9c42522528a2a6d18fb24c6ec07f8abd14fbd13/nbclassic-0.5.5-py3-none-any.whl")
    version("0.5.4", sha256="df78e4ba143f35084ad060deec16cb1d4839dde47bfdbc4232beb7071a6d70ea", url="https://pypi.org/packages/33/88/8b97740df1487e01fa89e636ba70404ef166312882182f33a5c9f0754fc6/nbclassic-0.5.4-py3-none-any.whl")
    version("0.5.3", sha256="e849277872d9ffd8fe4b39a8038d01ba82d6a1def9ce11b1b3c26c9546ed5131", url="https://pypi.org/packages/ff/73/c64228a1f88ef6352a3839a866cc8951b16d0db653ec8d9c5160e6a11dac/nbclassic-0.5.3-py3-none-any.whl")
    version("0.5.2", sha256="6403a996562dadefa7fee9c49e17b663b5fd508241de5df655b90011cf3342d9", url="https://pypi.org/packages/df/4a/ea941b1a6f2cf8f5d928e6ed4c72013cb85a24629be2e3496647ed8d8a22/nbclassic-0.5.2-py3-none-any.whl")
    version("0.5.1", sha256="32c235e1f22f4048f3b877d354c198202898797cf9c2085856827598cead001b", url="https://pypi.org/packages/f8/bb/a037a02aef224cd09041a79fba23257322255f93798fe7bd10c45e796b63/nbclassic-0.5.1-py3-none-any.whl")
    version("0.5.0", sha256="7317255221a76ca9e6a28c6760afc19c6f5c48225eaa5bf9f9f3fd5f30986f7d", url="https://pypi.org/packages/57/d9/14edb05c5cf699e2def8865e07ca9d31e3bb955e42c93d842d006b1b0e9d/nbclassic-0.5.0-py3-none-any.whl")
    version("0.4.8", sha256="cbf05df5842b420d5cece0143462380ea9d308ff57c2dc0eb4d6e035b18fbfb3", url="https://pypi.org/packages/a6/85/2a240df7326b7311ebd926c12d7df5394aef2f9f76ffbb294079cc43960e/nbclassic-0.4.8-py3-none-any.whl")
    version("0.4.7", sha256="d71d18aa6605eaf59e9b99b34c96360af45847f2a30ee2fefbe2f7bed4bc3df2", url="https://pypi.org/packages/b5/e8/eff73eb3b3424bd698ec919a3653b579f4253badaa579f477f769aa772ce/nbclassic-0.4.7-py3-none-any.whl")
    version("0.4.6", sha256="b19d00c90a706a301db58c4ec1936db6ec0a8d99b91590550a50e91bb14b5571", url="https://pypi.org/packages/ed/e9/db86d7cd479441c543ac3251b4645d7ff9a6c2337655982ea2fe15c14fe0/nbclassic-0.4.6-py3-none-any.whl")
    version("0.4.5", sha256="07fba5a9e52a6ed7e795b45d300629b2a07a69e5a47398833b7977a7ecc8a3c1", url="https://pypi.org/packages/e6/fc/e3d71e00ca66f644da449c64ef564a10880b7df74267d479753065100ac1/nbclassic-0.4.5-py3-none-any.whl")
    version("0.3.5", sha256="012d18efb4e24fe9af598add0dcaa621c1f8afbbbabb942fb583dd7fbb247fc8", url="https://pypi.org/packages/6f/45/21eaa314a406e2ba5c000ad755d1153b3269d338800674b5ff5f62f1f0fb/nbclassic-0.3.5-py3-none-any.whl")
    version("0.3.1", sha256="a7437c90a0bffcce172a4540cc53e140ea5987280c87c31a0cfa6e5d315eb907", url="https://pypi.org/packages/11/68/217ab6d4e4676dcfa4e855bb435469164a361a58e1856872cb06277f14b5/nbclassic-0.3.1-py3-none-any.whl")

    with default_args(type="run"):
        depends_on("py-argon2-cffi", when="@0.4:")
        depends_on("py-ipykernel", when="@0.4:")
        depends_on("py-ipython-genutils", when="@0.4:")
        depends_on("py-jinja2", when="@0.4:")
        depends_on("py-jupyter-client@6.1.1:", when="@0.4:")
        depends_on("py-jupyter-core@4.6.1:", when="@0.4:")
        depends_on("py-jupyter-server@1.17:", when="@0.5:0.5.1")
        depends_on("py-jupyter-server@1.8:", when="@0.3.7:")
        depends_on("py-jupyter-server@1.8:1", when="@0.3.1:0.3.6")
        depends_on("py-nbconvert@5.0.0:", when="@0.4:")
        depends_on("py-nbformat", when="@0.4:")
        depends_on("py-nest-asyncio@1.5:", when="@0.4:")
        depends_on("py-notebook@:6", when="@0.0.3:0.2.0,0.2.2:0.3")
        depends_on("py-notebook-shim@0.2.3:", when="@0.5.6:")
        depends_on("py-notebook-shim@0.1:", when="@0.3.6:0.5.5")
        depends_on("py-prometheus-client", when="@0.4:")
        depends_on("py-pyzmq@17.0.0:", when="@0.4:")
        depends_on("py-send2trash@1.8:", when="@0.4:")
        depends_on("py-terminado@0.8.3:", when="@0.4:")
        depends_on("py-tornado@6.1:", when="@0.4:")
        depends_on("py-traitlets@4.2.1:", when="@0.4:")

