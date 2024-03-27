##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyBcbioGff(PythonPackage):
    version("0.7.1", sha256="98b18c797fbabd27f47c2edc2a5c5e75d37a353cc2286684c4650728e66ff8fd", url="https://pypi.org/packages/4d/fc/fb0ad7988b7db0bd88c2764fd6b82657786e61cd5ab7f051e823c1aa1d4a/bcbio_gff-0.7.1-py3-none-any.whl")
    version("0.7.0", sha256="9f1bc9629ef1be13e713971c208223e1812ba1a6119979e9ce80b25212120d65", url="https://pypi.org/packages/65/ca/a662629e1b030af679d228aed5c813f0a8ceedec69f30885f1ec5571ea8a/bcbio_gff-0.7.0-py3-none-any.whl")
    version("0.6.9", sha256="34dfa970e14f4533dc63c0a5512b7b5221e4a06449e6aaa344162ed5fdd7a1de", url="https://pypi.org/packages/cd/de/13a70a7a158fc9d61ea18b9dadd2ef07584c44a912708b6d29de0185fc1d/bcbio-gff-0.6.9.tar.gz")
    version("0.6.8", sha256="8578d3c917a81e39898fa588e969c934fb942c2f3e11c275fa492c679a5f36a1", url="https://pypi.org/packages/ff/84/7b5fd81fab0ce826c048bea363d2e27179031bbfb8c289e9924ecb639f96/bcbio-gff-0.6.8.tar.gz")
    version("0.6.7", sha256="6e6f70639149612272a3b298a93ac50bba6f9ecece934f2a0ea86d4abde975da", url="https://pypi.org/packages/36/ea/43b0b78123aa89b352c401339be0a560c46f3d11b42ad3156a927761037d/bcbio-gff-0.6.7.tar.gz")
    version("0.6.6", sha256="74c6920c91ca18ed9cb872e9471c0be442dad143d8176345917eb1fefc86bc37", url="https://pypi.org/packages/ba/93/34156e0ed3eff9dbd52035f53a48b2ff7ae6bd877cda23ea9fce26cac9fc/bcbio-gff-0.6.6.tar.gz")
    version("0.6.5", sha256="a9e30fa8918f34427e1b99fcf40afb2e71f4e3f94a4a8ea490b506706eb8d5f6", url="https://pypi.org/packages/58/b3/4d2a1c146a9cdb2e5a0c80ae8a39cd1fc2daf4b990084f4cc1fe084d518d/bcbio-gff-0.6.5.tar.gz")
    version("0.6.4", sha256="e0efddc2376ed11b8f9682029b58bfd523a9aa62199f870b4ce64509ff99820b", url="https://pypi.org/packages/94/df/e2d75cc688ac6eb53f5fb4e2cffd240596bbcd5be28bab8d4f6404a6f86c/bcbio-gff-0.6.4.tar.gz")
    version("0.6.2", sha256="c682dc46a90e9fdb124ab5723797a5f71b2e3534542ceff9f6572b64b9814e68", url="https://pypi.org/packages/d2/02/722db105394093e107c6d4aeb7b8526909a2580b984e9b4f90202e9db1ab/bcbio-gff-0.6.2.tar.gz")
    version("0.6.1", sha256="7ba2e69ddf1956b93750062592026cbfebad28176bcc79ad0e82d6a06ca8cba5", url="https://pypi.org/packages/26/ff/e3f26bad87926bd397173ddafed4b0a6e30394ed7d1717879bdc19142ceb/bcbio-gff-0.6.1.tar.gz")

    with default_args(type="run"):
        depends_on("py-biopython", when="@0.7:")
        depends_on("py-six", when="@0.7:")

