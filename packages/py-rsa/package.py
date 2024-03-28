# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyRsa(PythonPackage):
    # BEGIN VERSIONS
    version("4.9", sha256="90260d9058e514786967344d0ef75fa8727eed8a7d2e43ce9f4bcf1b536174f7", url="https://pypi.org/packages/49/97/fa78e3d2f65c02c8e1268b9aba606569fe97f6c8f7c2d74394553347c145/rsa-4.9-py3-none-any.whl")
    version("4.8", sha256="95c5d300c4e879ee69708c428ba566c59478fd653cc3a22243eeb8ed846950bb", url="https://pypi.org/packages/30/ab/8fd9e88e6fa5ec41afca995938bbefb72195278e0cfc5bd76a4f29b23fb2/rsa-4.8-py3-none-any.whl")
    version("4.7.2", sha256="78f9a9bf4e7be0c5ded4583326e7461e3a3c5aae24073648b4bdfa797d78c9d2", url="https://pypi.org/packages/e9/93/0c0f002031f18b53af7a6166103c02b9c0667be528944137cc954ec921b3/rsa-4.7.2-py3-none-any.whl")
    version("4.7.1", sha256="74ba16e7ef58920b80b5c54c1c1066d391a2c1e812c466773f74c634eb12253b", url="https://pypi.org/packages/a0/c6/f6f92e055213860a39c98e51a10a51af473bc799a889fe8edac11108245b/rsa-4.7.1-py3-none-any.whl")
    version("4.7", sha256="a8774e55b59fd9fc893b0d05e9bfc6f47081f46ff5b46f39ccf24631b7be356b", url="https://pypi.org/packages/bf/87/dc7a6ebf0afbc602548627fa48e9c1147fa187233bf71d4c51c76a2cfb27/rsa-4.7-py3-none-any.whl")
    version("4.6", sha256="6166864e23d6b5195a5cfed6cd9fed0fe774e226d8f854fcb23b7bbef0350233", url="https://pypi.org/packages/1c/df/c3587a667d6b308fadc90b99e8bc8774788d033efcc70f4ecaae7fad144b/rsa-4.6-py3-none-any.whl")
    version("4.5", sha256="35c5b5f6675ac02120036d97cf96f1fde4d49670543db2822ba5015e21a18032", url="https://pypi.org/packages/26/f8/8127fdda0294f044121d20aac7785feb810e159098447967a6103dedfb96/rsa-4.5-py2.py3-none-any.whl")
    version("4.4.1", sha256="0ddc7ab19b5781148e405a4de7f1e9929e8c1e015d11a53b81e9a6242ee8e098", url="https://pypi.org/packages/5e/8e/d31e64657fb184e7c0136f0af382b396c8f0362f577c7e55e7ee0a68d93b/rsa-4.4.1-py2.py3-none-any.whl")
    version("4.4", sha256="4afbaaecc3e9550c7351fdf0ab3fea1857ff616b85bab59215f00fb42e0e9582", url="https://pypi.org/packages/6c/d5/8523e9a849ca91bb498badfbca159af6db1a9b41e84ab539ab6cdea2268f/rsa-4.4-py2.py3-none-any.whl")
    version("4.3", sha256="d111bb8b92767d68c153cb248da8465c28ccdec449a266b76ac7ada0b48d6bbe", url="https://pypi.org/packages/72/18/c309bed1b3d06c82e0c0d5004537cd72b52b9fdd049482119b6b3d868e1a/rsa-4.3-py2.py3-none-any.whl")
    version("4.2", sha256="aaefa4b84752e3e99bd8333a2e1e3e7a7da64614042bd66f775573424370108a", url="https://pypi.org/packages/68/69/854f072529f9e0ed2cc97b81adc5f20a18dab60bc84dd0eec7446d2166df/rsa-4.2.tar.gz")
    version("4.1.1", sha256="1a7245638fa914ed6196b5e88fa5064cd95c7e65df800ec5d4f288e2b19fb4af", url="https://pypi.org/packages/2a/77/eb06a2d3bade230edee25812c16b83b820518f848ec7dd47fd73097fd207/rsa-4.1.1.tar.gz")
    version("4.0", sha256="14ba45700ff1ec9eeb206a2ce76b32814958a98e372006c8fb76ba820211be66", url="https://pypi.org/packages/02/e5/38518af393f7c214357079ce67a317307936896e961e35450b70fad2a9cf/rsa-4.0-py2.py3-none-any.whl")
    version("3.4.2", sha256="43f682fea81c452c98d09fc316aae12de6d30c4b5c84226642cf8f8fd1c93abd", url="https://pypi.org/packages/e1/ae/baedc9cb175552e95f3395c43055a6a5e125ae4d48a1d7a924baca83e92e/rsa-3.4.2-py2.py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-pyasn1@0.1.3:", when="@4.1:4.1.0,4.3:4.7.0,4.7.2:")
    # END DEPENDENCIES

