##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyOptree(PythonPackage):
    version("0.10.0", sha256="dc7e8880f997365083191784d141c790833877af71aec8825c7f2b7f7f43c98e", url="https://pypi.org/packages/02/2f/0cd6aea70fd3058c782e9b4a223121cb3d1a696bc12d376943b37dce60e9/optree-0.10.0.tar.gz")
    version("0.9.2", sha256="ed0e31f787c274da0cb354687030e0ebbe5a98d2a25876c7c114568fc9fc78d4", url="https://pypi.org/packages/cf/12/32c4295a40e886ba4ba4cce8892a326b2b87a48ff54e367705dc48d90453/optree-0.9.2.tar.gz")
    version("0.9.1", sha256="d77262972b0a35ea0b5a91b80bfeeb1aae6abb796537d2ba79581a78247a09e7", url="https://pypi.org/packages/9b/2a/bcff64df1e72f81c9b972bdad0502a1cac76fefe9d5c94180f8ed2c24479/optree-0.9.1.tar.gz")
    version("0.9.0", sha256="ad1657fb84103b54def061ad663c2961150a11e1d3d9cd598fd5f64ac17f9225", url="https://pypi.org/packages/06/0a/1606b793e28006afd77b89a4ab44092491e09cf9f968c3488d0922699885/optree-0.9.0.tar.gz")
    version("0.8.0", sha256="292cb366f221c65ff4e3ed3230fa963da655dc19b51bbac8f018f944ad5d1289", url="https://pypi.org/packages/6e/3c/f2c151c335bbc01192da9a2c2a65a4b173cad2d1e0bfc1a55d0c08a879db/optree-0.8.0.tar.gz")
    version("0.7.0", sha256="d85a9aa0c64ff69146a31f9d5aeed27eb10895e28eac3b20d7c4a65a0161f57e", url="https://pypi.org/packages/4b/e7/807073ea0eace3fb4c3f9017b3eae10b7a9fd415c3884fe9bbf2205b129e/optree-0.7.0.tar.gz")
    version("0.6.0", sha256="4923459626c6b542557cf4e61f9749a6e86fab07a71c8b5de6287d814edb86df", url="https://pypi.org/packages/23/47/f4f3fb6fc55db9219ef6134f8b1257e2053ba08870cc9b3e118db043ce8c/optree-0.6.0.tar.gz")
    version("0.5.1", sha256="bc57a5450362de4bcf6522106ecf33bd2c6339dff95ab92808d15b653b2720bf", url="https://pypi.org/packages/d3/a4/71722d3ffd4a26f4076fd5a13f627f895d80b4206da5a3434238bd32791d/optree-0.5.1.tar.gz")
    version("0.5.0", sha256="709127beddb3826b74f9bcc1f78eec8a3a36a3475b2121b5a41822bd46a227ea", url="https://pypi.org/packages/e6/ea/08a026b72ee762484c2cfd8cc4661cb5eeb29e90d1c562d50a2381535274/optree-0.5.0.tar.gz")
    version("0.4.2", sha256="fe403cfaa24f8126a7fd573e3a3f00e9bc6c07e3f7514f74d6b3b7880f6d4f2a", url="https://pypi.org/packages/0c/2a/5d93c48e15034ead4dd79f914af80991b506c69a1c47f03b1f9a2727cec9/optree-0.4.2.tar.gz")

    with default_args(type="run"):
        depends_on("py-typing-extensions@4:", when="@0.9.2:")

