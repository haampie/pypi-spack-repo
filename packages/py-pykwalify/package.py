# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPykwalify(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("1.8.0", sha256="731dfa87338cca9f559d1fca2bdea37299116e3139b73f78ca90a543722d6651", url="https://pypi.org/packages/1f/fd/ac2161cce19fd67a18c269073f8e86292b5511acec6f8ef6eab88615d032/pykwalify-1.8.0-py2.py3-none-any.whl")
    version("1.7.0", sha256="428733907fe5c458fbea5de63a755f938edccd622c7a1d0b597806141976f00e", url="https://pypi.org/packages/36/9f/612de8ca540bd24d604f544248c4c46e9db76f6ea5eb75fb4244da6ebbf0/pykwalify-1.7.0-py2.py3-none-any.whl")
    version("1.6.1", sha256="0959032cf185c168256a623b80ff3d2ca57d704f78ca286b4155ebcd9fae9d49", url="https://pypi.org/packages/ce/d2/550d30b645425fd11e503d6e04fc19e91719941faf0e4e08a58d278b6345/pykwalify-1.6.1-py2.py3-none-any.whl")
    version("1.6.0", sha256="d382481b3829d057931a1a6c708f03f80e2d7ebc0123a78b267fc626e796fd68", url="https://pypi.org/packages/6e/59/55c32d59b462a9c3fae2ab25f179f91d61617c0215e9f8ba3f4966b2b8b1/pykwalify-1.6.0-py2.py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-docopt@0.6.2:", when="@1.7:")
        depends_on("py-python-dateutil@2.8:", when="@1.8:")
        depends_on("py-python-dateutil@2.4.2:", when="@1.7")
        depends_on("py-pyyaml@3.11:", when="@1.7")
        depends_on("py-ruamel-yaml@0.16:", when="@1.8:")
    # END DEPENDENCIES

