##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyDataladMetalad(PythonPackage):
    version("0.14.20", sha256="34363d88fbab936ce7f79f1a8d1156ae2a67d2ecf113a099e9649e4e4319a18c", url="https://pypi.org/packages/a6/99/f26722a6d35e589098e00c4058dc813550ac8f99d6d2ee8d6d42d6626373/datalad_metalad-0.14.20-py3-none-any.whl")
    version("0.4.22", sha256="915200eb7e483d9d45dad07557bf59e6d6e81c5506e21726eda0e5fb6f1383f8", url="https://pypi.org/packages/cf/d1/8dac93b6cab935e222861fe27e1c0235204dcaf072e7d1c88da156037dbf/datalad_metalad-0.4.22-py3-none-any.whl")
    version("0.4.21", sha256="f2df2140a81b9278c30334b9027ed42fcf23bb3e83c0067dffd5a92eb0f81dbf", url="https://pypi.org/packages/ee/71/3c9bad81c07763e10c58c59159822278d21549f815612112f6e05f2ec03f/datalad_metalad-0.4.21-py3-none-any.whl")
    version("0.4.20", sha256="a0eef1991144453a46211cbdc1d333a3166e7a816ec64155034d845ee47a32d8", url="https://pypi.org/packages/e5/05/9353b168d47577c44dae588ec50de9274507940f4f074ae852aba0a1f7e8/datalad_metalad-0.4.20-py3-none-any.whl")
    version("0.4.19", sha256="d2ae06dfd26926c74afda00c0ed89407f3de4790d617f85133e4e0973005f8e5", url="https://pypi.org/packages/12/64/4d16be5763a1c9f1c8ee38a329106ef2392cccd3f89d0953e3b8dee881ce/datalad_metalad-0.4.19-py3-none-any.whl")
    version("0.4.18", sha256="455c93ba5b904cefb63c47cfabf84e4aad79b231429573e4291b97426033e750", url="https://pypi.org/packages/1b/e5/f7cbb5f9192913bbdc6da5d30731918295efd5bb156c87994d7ecfb7b908/datalad_metalad-0.4.18-py3-none-any.whl")
    version("0.4.17", sha256="7b361fb5ce419ba4599f5492a7435bebc306aec85d113ae2e4a3a7babe5a96d0", url="https://pypi.org/packages/08/5b/1606571a8a0a1760904872d51c627e7364c71d18a75890542408e385e590/datalad_metalad-0.4.17-py3-none-any.whl")
    version("0.4.16", sha256="c9533cf7a6066505ac652de1bc93a52072e52710fa6b604a972177cad62ee78e", url="https://pypi.org/packages/17/c7/62f6d5708cd49287227b8d2f6c1e28c7fed0d732fc757c1f3b2575e121db/datalad_metalad-0.4.16-py3-none-any.whl")
    version("0.4.12", sha256="7aacf6736592f3e644e1e98ef9c7cf2b577604b1c1fd1eff4971b82ad089aca9", url="https://pypi.org/packages/ac/e4/ea94f411a3de565dc3780283b75d04d0d1ad4312408e850cfb4194c545d1/datalad_metalad-0.4.12-py3-none-any.whl")
    version("0.4.11", sha256="b46b5cdc959dd8f84015f0f3529e210b0585d98c1608064a294c72b6f908a356", url="https://pypi.org/packages/6e/8a/30adceb4dccb47363a34238ffaec333d618e4e86f0008440ab75f2a7d99e/datalad_metalad-0.4.11-py3-none-any.whl")
    version("0.4.5", sha256="c6a4fec45a3fe33dc59710f61ef5b8d2bee0e5fa601aff6ae810a706776c398e", url="https://pypi.org/packages/e4/a2/5a4622e6afd3df47e2590fe75a934ced626cf3240fc4d464b21489f60174/datalad_metalad-0.4.5-py3-none-any.whl")
    version("0.2.1", sha256="40b072d8fdf97ca6d820e2e4c836b762df1de340f637180ee1fdd8338f2a57c3", url="https://pypi.org/packages/8b/ba/2d7a77a57e6048b2d98acfd40241ca7ff376be20430c764de468784acb9a/datalad_metalad-0.2.1-py2.py3-none-any.whl")

    with default_args(type="run"):
        depends_on("py-datalad@0.18:", when="@0.4.11:")
        depends_on("py-datalad@0.15.6:", when="@0.3:0.4.5")
        depends_on("py-datalad@0.12.3:", when="@0.2.1:0.2")
        depends_on("py-datalad-deprecated", when="@0.4.17:")
        depends_on("py-datalad-metadata-model@0.3.10:", when="@0.4.12:")
        depends_on("py-datalad-metadata-model@0.3.6:", when="@0.4.10:0.4.11")
        depends_on("py-datalad-metadata-model@0.3.5:", when="@0.4.5:0.4.9")
        depends_on("py-pytest", when="@0.4.11:")
        depends_on("py-pyyaml", when="@0.3:")
        depends_on("py-six", when="@0.3.1:0.4.17")

