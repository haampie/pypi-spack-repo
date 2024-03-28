# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyAwscli(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("1.29.41", sha256="5ba9589869e5be20816ce85688639c3ab65b10eed7f04467cbbfe662656f52d1", url="https://pypi.org/packages/97/b9/c5bfc951bd47f4064b72a74fed2a663c4f80790acea1e820d949740eecb4/awscli-1.29.41-py3-none-any.whl")
    version("1.27.84", sha256="16eae4f4905c554eb8c89483e9ebab4985c76f9ff84569cba6c45458c130b7c2", url="https://pypi.org/packages/24/c7/b848fb5d5565f0a297396486f7d554253b0adc5ac076d966223108ce7912/awscli-1.27.84-py3-none-any.whl")
    version("1.27.56", sha256="79ea472e6d9a33aac4cf95552b837fa88b8849ce9b8c9cc26d70f6851b4130b4", url="https://pypi.org/packages/78/fd/32ab7f9082cf1456c76375edb989b45779b8ce62829fa7e9dbf6b337287a/awscli-1.27.56-py3-none-any.whl")
    version("1.16.308", sha256="23f63c65f967982a54441a2922a631244597dc75ebd99e4053e51ffa81a6fee2", url="https://pypi.org/packages/8f/86/54c770eac9c1dfcc4a223f8b2a275d2412b2c79282eaad0132272f29dc0c/awscli-1.16.308-py2.py3-none-any.whl")
    version("1.16.179", sha256="101ef0bb99b040bc47d26d2b3e1a435fea8205b198932427cf14703f52821fb0", url="https://pypi.org/packages/da/c3/7bfd8a1a84f9ad2acc0fe048d5b685ccc1ba2d18a6c650f5baa1986a1880/awscli-1.16.179-py2.py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-botocore@1.31.41", when="@1.29.41")
        depends_on("py-botocore@1.29.84", when="@1.27.84")
        depends_on("py-botocore@1.29.56", when="@1.27.56")
        depends_on("py-colorama@0.2.5:0.4.4", when="@1.23:")
        depends_on("py-docutils@0.10:0.16", when="@1.24.5:")
        depends_on("py-pyyaml", when="@1.29.4:")
        depends_on("py-pyyaml@:5", when="@1.19.12:1.29.3")
        depends_on("py-rsa@3.1.2:4.7", when="@1.19.13:1.19.27,1.19.41:")
        depends_on("py-s3transfer@0.6", when="@1.25:1.29.54")
    # END DEPENDENCIES

