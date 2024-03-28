# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPiper(PythonPackage):
    # BEGIN VERSIONS
    version("0.14.0", sha256="874706b253f159b5546016c8b6a180118d4e64df53b7698a8f39c271d20f93cd", url="https://pypi.org/packages/ad/76/9ccdbf937a57a82cb303b51cefbc8469f98456d5484556e13f055ce34edb/piper-0.14.0-py3-none-any.whl")
    version("0.14.0-alpha2", sha256="fbd117755d56af3d3719a71c44d568e3f050f150d83ac362001f33fb201de01b", url="https://pypi.org/packages/fa/c2/9d3adc4b19235ec85f4c47adff7096e1ca26944803e25ed35add408692ac/piper-0.14.0a2-py3-none-any.whl")
    version("0.14.0-alpha1", sha256="221dbb96bc775680f2c45395711b0df84cecb441f72ac808d03ee6e5e50673ce", url="https://pypi.org/packages/79/71/26836ba428248a5d5b2ddaa46895e06ae2e305c9b411894d428d0efa1163/piper-0.14.0a1-py3-none-any.whl")
    version("0.13.3-alpha1", sha256="f2104ed23244989751cdd9b9fe5f3cdb3bdc82e0ea30cd4142dc50cda08d74be", url="https://pypi.org/packages/a0/d8/e74c1b2db61e34b690c3183f9d2f8949e16a1416c3c66d02bb9783b596e0/piper-0.13.3a1-py3-none-any.whl")
    version("0.13.2", sha256="a39ce65b14af2d1a921269bd1861dcc45254af14b35f010ec126e61bcaa501e6", url="https://pypi.org/packages/d6/8d/d6540efd21b320826ca184c9cba1ba2a2a21c25b14798cc6c99371271205/piper-0.13.2-py3-none-any.whl")
    version("0.13.1", sha256="383cf125cae34f3abbd89db29f803bbba12ebf967fdc17394cfb8a44ad0c26e3", url="https://pypi.org/packages/62/35/f0d4cc6df6ab49eef17f5bdb3fdf2ca3e193a72d94a8bfdd155a97d4ed5e/piper-0.13.1-py3-none-any.whl")
    version("0.13.0", sha256="5e50e87ebdca713282b81bfb9754ab28cb0e99729a623d4183a07d48f77751ed", url="https://pypi.org/packages/29/83/24379dfe0f8f3c8a403164a2285fd34923aad094f65f0d70afbff4f892bb/piper-0.13.0-py3-none-any.whl")
    version("0.12.3", sha256="b7da6286fc883d129bd3456179946bbe8f2f9455b81032ffcc97410b8f4dd572", url="https://pypi.org/packages/a1/ca/c102d69056eb6d3d235e623e801aeda1de509a9cc504b976163def8887ab/piper-0.12.3-py3-none-any.whl")
    version("0.12.2", sha256="60492e0a6a2924040de95f2c993c90d053f538fd56c276fa22f241438a34c01d", url="https://pypi.org/packages/bc/3a/89c79854a9e6580d1512e3cc63fbfdd9d35d7242a01134e9fec027ed43ce/piper-0.12.2.tar.gz")
    version("0.12.1", sha256="d3e292a7383f6011759f0803aeb2f62489ecb457c4e916637a74dbbffdfcb3bd", url="https://pypi.org/packages/4b/6e/d365deaeebb50378dfaddddc34d394b25b38f340604910ea163b483d3546/piper-0.12.1.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-attmap@0.12.5:", when="@0.12.3:0.13")
        depends_on("py-logmuse@0.2.4:", when="@0.12.3:")
        depends_on("py-pandas", when="@0.12.3:")
        depends_on("py-pipestat@0.6.0:", when="@0.14.0:")
        depends_on("py-pipestat@0.6.0-alpha9:", when="@0.14.0-alpha2")
        depends_on("py-pipestat@0.6.0-alpha7:", when="@0.14:0.14.0-alpha1")
        depends_on("py-pipestat@0.6:", when="@0.13.3-alpha1:0.13")
        depends_on("py-pipestat@0.4:", when="@0.13:0.13.2")
        depends_on("py-psutil", when="@0.9.2,0.12.3:")
        depends_on("py-ubiquerg@0.4.5:", when="@0.12.3:")
        depends_on("py-yacman", when="@0.12.3:")
    # END DEPENDENCIES

