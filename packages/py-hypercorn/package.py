# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyHypercorn(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("0.16.0", sha256="929e45c4acde3fbf7c58edf55336d30a009d2b4cb1f1eb96e6a515d61b663f58", url="https://pypi.org/packages/17/9e/700d764316399c20fbe8e98c6fff903b5d3f950043cc2fcbd0831a42c953/hypercorn-0.16.0-py3-none-any.whl")
    version("0.15.0", sha256="5008944999612fd188d7a1ca02e89d20065642b89503020ac392dfed11840730", url="https://pypi.org/packages/75/01/454a0127f2e554502fca9aca2a3b39ab850c7962dbabf32ce5ab113f229f/hypercorn-0.15.0-py3-none-any.whl")
    version("0.14.4", sha256="f956200dbf8677684e6e976219ffa6691d6cf795281184b41dbb0b135ab37b8d", url="https://pypi.org/packages/f8/aa/0632f628205f09ec7daa5875e4142db519bfa7a161d48a6417b0f9ab5e08/hypercorn-0.14.4-py3-none-any.whl")
    version("0.14.3", sha256="7c491d5184f28ee960dcdc14ab45d14633ca79d72ddd13cf4fcb4cb854d679ab", url="https://pypi.org/packages/be/8b/e856965857137bc594e8fd52fef1d00b79913a6a01033cba772276aff10b/Hypercorn-0.14.3-py3-none-any.whl")
    version("0.14.2", sha256="1e1807291efdb515c10d28f5bc818b5b1e8e57281bf19fe69160035bf6f762c3", url="https://pypi.org/packages/80/f5/5b87771cc14e416ff3ef2e5f0ebeeb869699b39edff146bc38ec6f09a738/Hypercorn-0.14.2-py3-none-any.whl")
    version("0.14.1", sha256="b71b61698a9fb498564762cef0d18e52e416ab7301e2e55744c92ccaded11b2c", url="https://pypi.org/packages/4e/41/9687e24af6de469b397a06eb78ba58ef9d1564cfe136f784578676d7dc74/Hypercorn-0.14.1-py3-none-any.whl")
    version("0.14.0", sha256="6f9cbde54222e5969ac0022812e71ebc0c84f0c74f75a8465680868cd711b2aa", url="https://pypi.org/packages/fb/57/8afcccdbaa51aecff31bcbcae7e6cfe5451e56039279d5513e443d5b82d0/Hypercorn-0.14.0-py3-none-any.whl")
    version("0.13.2", sha256="ca18f91ab3fa823cbe9e949738f9f2cc07027cd647c80d8f93e4b1a2a175f112", url="https://pypi.org/packages/c9/28/79bbca7d9218d37f8888a0f3215e7ba03851d1c77c11d841542e33cc3190/Hypercorn-0.13.2-py3-none-any.whl")
    version("0.13.1", sha256="fcbfd5b691176cfcbf558cfa536909b2ef249af5528c99fcf941405c1c9aba74", url="https://pypi.org/packages/61/82/c5314147d03fbf772ecf8e6bc008af7907c656290b8a53e57196a3dcf36b/Hypercorn-0.13.1-py3-none-any.whl")
    version("0.13.0", sha256="eafbed8b1cb9827552c0066386d3e693c16d3977dd60896bfa07dca4c9d92a20", url="https://pypi.org/packages/d7/1b/2178b4ad64713570b465f1670a019abc01e30353c3af83adb40577f69a2e/Hypercorn-0.13.0-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-h11", when="@0.3:")
        depends_on("py-h2@3.1:", when="@0.5:")
        depends_on("py-priority", when="@0.8:")
        depends_on("py-taskgroup", when="@0.15: ^python@:3.10")
        depends_on("py-toml", when="@0.7:0.14.3")
        depends_on("py-tomli", when="@0.14.4: ^python@:3.10")
        depends_on("py-wsproto@0.14:", when="@0.5.4:")
    # END DEPENDENCIES

