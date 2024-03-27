##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyZipp(PythonPackage):
    version("3.18.1", sha256="206f5a15f2af3dbaee80769fb7dc6f249695e940acca08dfb2a4769fe61e538b", url="https://pypi.org/packages/c2/0a/ba9d0ee9536d3ef73a3448e931776e658b36f128d344e175bc32b092a8bf/zipp-3.18.1-py3-none-any.whl")
    version("3.18.0", sha256="c1bb803ed69d2cce2373152797064f7e79bc43f0a3748eb494096a867e0ebf79", url="https://pypi.org/packages/39/ab/b6f4d44df331bf15f1bdae6a839563eeaad6c006a6c4e289acdd7db1ebe3/zipp-3.18.0-py3-none-any.whl")
    version("3.17.0", sha256="0e923e726174922dce09c53c59ad483ff7bbb8e572e00c7f7c46b88556409f31", url="https://pypi.org/packages/d9/66/48866fc6b158c81cc2bfecc04c480f105c6040e8b077bc54c634b4a67926/zipp-3.17.0-py3-none-any.whl")
    version("3.16.2", sha256="679e51dd4403591b2d6838a48de3d283f3d188412a9782faadf845f298736ba0", url="https://pypi.org/packages/8c/08/d3006317aefe25ea79d3b76c9650afabaf6d63d1c8443b236e7405447503/zipp-3.16.2-py3-none-any.whl")
    version("3.16.1", sha256="0b37c326d826d5ca35f2b9685cd750292740774ef16190008b00a0227c256fe0", url="https://pypi.org/packages/a1/3b/385e3b43200af0b9a13d03c234efbd9d40c6d73ab63fde1c097a2daacdea/zipp-3.16.1-py3-none-any.whl")
    version("3.16.0", sha256="5dadc3ad0a1f825fe42ce1bce0f2fc5a13af2e6b2d386af5b0ff295bc0a287d3", url="https://pypi.org/packages/ad/be/a6c11f5e0c042fb97e6b567730f55c56b2fe4089304ae66207a54fa49d7e/zipp-3.16.0-py3-none-any.whl")
    version("3.15.0", sha256="48904fc76a60e542af151aded95726c1a5c34ed43ab4134b597665c86d7ad556", url="https://pypi.org/packages/5b/fa/c9e82bbe1af6266adf08afb563905eb87cab83fde00a0a08963510621047/zipp-3.15.0-py3-none-any.whl")
    version("3.14.0", sha256="188834565033387710d046e3fe96acfc9b5e86cbca7f39ff69cf21a4128198b7", url="https://pypi.org/packages/a8/7d/90189265f0a9bcdf79b1143b77b0ef6dca0a5f13783f1e1efa4d7d7eafca/zipp-3.14.0-py3-none-any.whl")
    version("3.13.0", sha256="e8b2a36ea17df80ffe9e2c4fda3f693c3dad6df1697d3cd3af232db680950b0b", url="https://pypi.org/packages/95/7b/1608a7344743f54a8c072d64d2a279934fd204d6d015278b0a0ed4ce104b/zipp-3.13.0-py3-none-any.whl")
    version("3.12.1", sha256="6c4fe274b8f85ec73c37a8e4e3fa00df9fb9335da96fb789e3b96b318e5097b3", url="https://pypi.org/packages/37/7d/4a5221043904612db108bbe7d0ad7409015fb143bae137c72d9dfd7b75e1/zipp-3.12.1-py3-none-any.whl")
    version("3.8.1", sha256="47c40d7fe183a6f21403a199b3e4192cca5774656965b0a4988ad2f8feb5f009", url="https://pypi.org/packages/f0/36/639d6742bcc3ffdce8b85c31d79fcfae7bb04b95f0e5c4c6f8b206a038cc/zipp-3.8.1-py3-none-any.whl")
    version("3.6.0", sha256="9fe5ea21568a0a70e50f273397638d39b03353731e6cbbb3fd8502a33fec40bc", url="https://pypi.org/packages/bd/df/d4a4974a3e3957fd1c1fa3082366d7fff6e428ddb55f074bf64876f8e8ad/zipp-3.6.0-py3-none-any.whl")
    version("0.6.0", sha256="f06903e9f1f43b12d371004b4ac7b06ab39a44adc747266928ae6debfa7b3335", url="https://pypi.org/packages/74/3d/1ee25a26411ba0401b43c6376d2316a71addcc72ef8690b101b4ea56d76a/zipp-0.6.0-py2.py3-none-any.whl")
    version("0.5.1", sha256="8c1019c6aad13642199fbe458275ad6a84907634cc9f0989877ccc4a2840139d", url="https://pypi.org/packages/a0/0f/9bf71d438d2e9d5fd0e4569ea4d1a2b6f5a524c234c6d221b494298bb4d1/zipp-0.5.1-py2.py3-none-any.whl")

    with default_args(type="run"):
        depends_on("py-more-itertools", when="@0.6:1.0,2:2.0")

