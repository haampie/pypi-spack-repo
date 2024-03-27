##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPythonFsutil(PythonPackage):
    version("0.14.1", sha256="0d45e623f0f4403f674bdd8ae7aa7d24a4b3132ea45c65416bd2865e6b20b035", url="https://pypi.org/packages/4f/e6/c8a2cdf34316bb96a7601ed47778818da266d4917bd9575d3a9ba46aedb7/python_fsutil-0.14.1-py3-none-any.whl")
    version("0.14.0", sha256="babad39e4134e8b1859fe4478c6bd585911de6b919b49a7f08d4dcddcb1822aa", url="https://pypi.org/packages/62/e0/d7da4d52780ce34fcc8cf8a7438f5c7ea77fe8c61e0d198357096cae013b/python_fsutil-0.14.0-py3-none-any.whl")
    version("0.13.1", sha256="b4ad4c57c243ba46ee5aacebe58ce7a6f62ddeff20ea53e52afc420884b5e544", url="https://pypi.org/packages/5b/e4/1c3cdd3417103f2b750c5d13e19d0776bb297ca4506bd31b805972a264fc/python_fsutil-0.13.1-py3-none-any.whl")
    version("0.13.0", sha256="8cc999d9594da083eb59e6b4d10835ee331bde3658de48bda3202e5298a3ee59", url="https://pypi.org/packages/f2/b4/7c5b0a1b1cbcd5cc72fb733d472a434e0a6701d95fc55f74e1c6b161469c/python_fsutil-0.13.0-py3-none-any.whl")
    version("0.12.0", sha256="06064971f73a982a9abb52d1407f35dbca2d3d03c2e16ecc49409293b7e654db", url="https://pypi.org/packages/fa/3a/3f35f54de9e36f293737b832ab56dfcd7a7c7ad153b49c7a676ff76a1a31/python_fsutil-0.12.0-py3-none-any.whl")
    version("0.11.0", sha256="b86f16edfc15babaa4073266436bb700d4453a122db0ce79d63d4922a2e7953b", url="https://pypi.org/packages/ef/9f/09df98000a73d5d76d8c845f60bf10a58990be41c7cee67969fcf62e1b13/python_fsutil-0.11.0-py3-none-any.whl")
    version("0.10.0", sha256="e0421440b5763d08129dcc469364105f3b434fc9736c3bc6ed181b1c623148ee", url="https://pypi.org/packages/37/d6/024690ccbca9ba074610db3ccb0cd3cfeda12fed67020f9ff025691c05e2/python_fsutil-0.10.0-py3-none-any.whl")
    version("0.9.3", sha256="4e205b9ace96008f161c33f8e3c9586dc5531b34a31115a0607ce7522162aed1", url="https://pypi.org/packages/06/e6/c69df77927b77e09479655060a90bc0fd77382595bb1828551279d0adf97/python_fsutil-0.9.3-py3-none-any.whl")
    version("0.9.2", sha256="6415f479277e6ca62fc31bd2f2f58c203847090836574f70fc4025599f0e7530", url="https://pypi.org/packages/88/68/676343d1c0ea59db1ff85113c56b0d32ec1e59cde6b83a3b40fd6f2f26b6/python_fsutil-0.9.2-py3-none-any.whl")
    version("0.9.1", sha256="e982b872abb6d4ed6ac86b647ec5c4d1c1fa0a4f8116794e6cdc9dd12bdee276", url="https://pypi.org/packages/8e/83/41bee2dc8ca4a6d0b8a5385eb0a71d565ef8e84dfefdcb56d93bcf8db1a8/python_fsutil-0.9.1-py3-none-any.whl")
    version("0.4.0", sha256="3e93c919b96a146de78900b644c9d9f957b1d50ae67c510a39f866d30ab626c7", url="https://pypi.org/packages/4b/b1/d9cd591b718300a3c45d959bd71c87cbac932a906d5efc20892e5d152e67/python_fsutil-0.4.0-py3-none-any.whl")

    with default_args(type="run"):
        depends_on("py-requests", when="@0.4:0.5")

