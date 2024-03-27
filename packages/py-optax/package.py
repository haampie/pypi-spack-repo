##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyOptax(PythonPackage):
    version("0.2.1", sha256="fe1adcf2157ecfd83af05110b4ac0de142aa52baecc4e51c42490ac6d2867cd2", url="https://pypi.org/packages/dd/89/7e91e9ecf3bf1e4d0cdb7ffa3fc61e422968a9df0c38d66f6b564a8be336/optax-0.2.1-py3-none-any.whl")
    version("0.2.0", sha256="68673a95b8a18231b86879e317281869c005ef11a901209aaf25aee30be079cf", url="https://pypi.org/packages/d7/62/5072ef01f30959b726cf995e4c612138acfc3e7e149bf5496c5bb2aac680/optax-0.2.0-py3-none-any.whl")
    version("0.1.9", sha256="3cbcfac6e70dff9484cd7560dc92e43a50df1eac0d4af2a1f7c2e1fd116bf972", url="https://pypi.org/packages/bb/c6/ca58ae4ed7283c65ab53318096cd53a3ab78462d0488a185eef3cf2f2d04/optax-0.1.9-py3-none-any.whl")
    version("0.1.8", sha256="9a76a895511a1d9b50078c55e9fffd7f095e5e947d4c804eead7f3dc51c5c270", url="https://pypi.org/packages/95/f6/36933cf75cb37e21d3de2dc6195306aa1cc30250e29e55c10cc5a84c1ce6/optax-0.1.8-py3-none-any.whl")
    version("0.1.7", sha256="2b85115f2ae7adafe5fd9abf4b275e53057765361511c8ccc868e70158458494", url="https://pypi.org/packages/13/71/787cc24c4b606f3bb9f1d14957ebd7cb9e4234f6d59081721230b2032196/optax-0.1.7-py3-none-any.whl")
    version("0.1.5", sha256="4057461448abd1fccdefd5e6c7ebc6ea8daa3105041f2631d6efd506544ecde0", url="https://pypi.org/packages/04/16/93f5a15951c5cb71d43c6440efc7d9e2d3dca1f4783dc364a0c1891a086e/optax-0.1.5-py3-none-any.whl")
    version("0.1.4", sha256="12fcf33bd682f9a162a3deb097f864130c3224d76771af2ba09410de80399a9b", url="https://pypi.org/packages/2e/7a/53ab156dd30acd9b4039603ebe623e81783de33b33ed14bcd52a29c2eeef/optax-0.1.4-py3-none-any.whl")
    version("0.1.3", sha256="33ac3b36bc8f6e087e112fd3a14ab054b99d1c26867aae552db80e234916e522", url="https://pypi.org/packages/d8/d3/de0f96c03c9e55549bbd46629b4a379609b2d426551ab04811d19aef7f23/optax-0.1.3-py3-none-any.whl")
    version("0.1.2", sha256="4e3cb24b70e87acd65700da77c570c468e701d32a2393ae4a5ec35719d90ade6", url="https://pypi.org/packages/6e/76/430128410afff80dce25b620c0dbc89b07ed559cc8475945ea3384e8d3c3/optax-0.1.2-py3-none-any.whl")
    version("0.1.1", sha256="c03a143527624d626a8157a26fd8e7ad05fcec746bb44352b71394554e835ce6", url="https://pypi.org/packages/ca/9d/a374b8bd6a2ca59dcb42df71f32bce3ebc6a6559417eb154e3b7964be290/optax-0.1.1-py3-none-any.whl")

    with default_args(type="run"):
        depends_on("python@3.9:", when="@0.1.9:")
        depends_on("py-absl-py@0.7.1:")
        depends_on("py-chex@0.1.7:", when="@0.1.8:")
        depends_on("py-chex@0.1.5:", when="@0.1.4:0.1.7")
        depends_on("py-chex@0.0.4:", when="@0.0.3:0.1.3")
        depends_on("py-jax@0.1.55:")
        depends_on("py-jaxlib@0.1.37:")
        depends_on("py-numpy@1.18.0:")
        depends_on("py-typing-extensions@3.10:", when="@0.1.1:0.1.4")

