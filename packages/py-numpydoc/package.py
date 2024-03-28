# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyNumpydoc(PythonPackage):
    # BEGIN VERSIONS
    version("1.6.0", sha256="b6ddaa654a52bdf967763c1e773be41f1c3ae3da39ee0de973f2680048acafaa", url="https://pypi.org/packages/9c/94/09c437fd4a5fb5adf0468c0865c781dbc11d399544b55f1163d5d4414afb/numpydoc-1.6.0-py3-none-any.whl")
    version("1.6.0-rc2", sha256="02e4c5f4482024d3b7dc6761dfd4dd465626d97329fe723fb69087fbd7ab3ab4", url="https://pypi.org/packages/f8/e2/466982438e459a828b665679336dc8804bacb4a8f709452915db8eeeca04/numpydoc-1.6.0rc2-py3-none-any.whl")
    version("1.6.0-rc1", sha256="5e33489d64f0227e87dafec3928295091a16c96bf5b95cdc8a2d4ea409acf48c", url="https://pypi.org/packages/5f/a1/3f3aa22550780f74256e7254cf17bb502aa4a747414497468bffefa5980b/numpydoc-1.6.0rc1-py3-none-any.whl")
    version("1.5.0", sha256="c997759fb6fc32662801cece76491eedbc0ec619b514932ffd2b270ae89c07f9", url="https://pypi.org/packages/c4/81/ad9b8837442ff451eca82515b41ac425f87acff7e2fc016fd1bda13fc01a/numpydoc-1.5.0-py3-none-any.whl")
    version("1.4.0", sha256="fd26258868ebcc75c816fe68e1d41e3b55bd410941acfb969dee3eef6e5cf260", url="https://pypi.org/packages/e7/1a/9e3c2a34aae5bd1ab8988b238aafeb4c8d3ab312b8aa5a8c37be6c6d869d/numpydoc-1.4.0-py3-none-any.whl")
    version("1.3.1", sha256="a49822cb225e71b7ef7889dd42576b5aa14c56ce62e0bc030f97abc8a3ae240f", url="https://pypi.org/packages/38/66/04aa44cdc48010317f473b47003045078b083201af68b9c5a110e19444e3/numpydoc-1.3.1-py3-none-any.whl")
    version("1.3", sha256="60f94b4f8879f0fa6bb02feba42620352017f662ae8ca1a456fca398bca8c10c", url="https://pypi.org/packages/c6/ec/f6f7067a673d7cf8c005c3b387fa63649597235249560e5ba9b56c9c50e2/numpydoc-1.3-py3-none-any.whl")
    version("1.2.1", sha256="2d317df5fd9404a5199bb993c1b6627436b2804582d2775bf9ccf3c5912ebe99", url="https://pypi.org/packages/fb/2c/b8ea78c28367808278e6a61885384dce4157e700db4aac655f7c2e509a08/numpydoc-1.2.1-py3-none-any.whl")
    version("1.2", sha256="3ecbb9feae080031714b63128912988ebdfd4c582a085d25b8d9f7ac23c2d9ef", url="https://pypi.org/packages/61/25/499ff2b2b73c79de971f9dbafe5f188b751c834d9565b123f484b7247fba/numpydoc-1.2-py3-none-any.whl")
    version("1.1.0", sha256="c53d6311190b9e3b9285bc979390ba0257ba9acde5eca1a7065fc8dfca9d46e8", url="https://pypi.org/packages/60/1d/9e398c53d6ae27d5ab312ddc16a9ffe1bee0dfdf1d6ec88c40b0ca97582e/numpydoc-1.1.0-py3-none-any.whl")
    version("1.0.0", sha256="99e9c4ec51ff0dc17f7e15afcb26ba77a2f8ccc85a19dede40006a2b93cc903f", url="https://pypi.org/packages/3a/43/2402fd1f63992a52f88e3b169d59674617013bf7f1ad0cd7d842eafd0c58/numpydoc-1.0.0-py3-none-any.whl")
    version("0.9.2", sha256="9140669e6b915f42c6ce7fef704483ba9b0aaa9ac8e425ea89c76fe40478f642", url="https://pypi.org/packages/b0/70/4d8c3f9f6783a57ac9cc7a076e5610c0cc4a96af543cafc9247ac307fbfe/numpydoc-0.9.2.tar.gz")
    version("0.6.0", sha256="974584a8293182ae995113ee2dce9f4be939c3f40c6c2daf11f9df33f961b5cb", url="https://pypi.org/packages/a9/22/e2069cf728e84dc0c7b80fc5021a4f878688e08f093a470ce4a1540cce45/numpydoc-0.6.0.zip")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-jinja2@2.10:3.0", when="@1.2.1:1.2")
        depends_on("py-jinja2@2.10:", when="@1.2-rc1:1.2.0,1.3-rc1:")
        depends_on("py-jinja2@2.3:", when="@1:1.1")
        depends_on("py-sphinx@5.0.0:", when="@1.6:")
        depends_on("py-sphinx@4.2:", when="@1.5")
        depends_on("py-sphinx@3.0.0:", when="@1.3-rc1:1.4")
        depends_on("py-sphinx@1.8.0:", when="@1.2-rc1:1.2")
        depends_on("py-sphinx@1.6.5:", when="@1:1.1")
        depends_on("py-tabulate@0.8.10:", when="@1.6:")
        depends_on("py-tomli@1.1:", when="@1.6: ^python@:3.10")
    # END DEPENDENCIES

