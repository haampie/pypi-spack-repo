# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyFasteners(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("0.19", sha256="758819cb5d94cdedf4e836988b74de396ceacb8e2794d21f82d131fd9ee77237", url="https://pypi.org/packages/61/bf/fd60001b3abc5222d8eaa4a204cd8c0ae78e75adc688f33ce4bf25b7fafa/fasteners-0.19-py3-none-any.whl")
    version("0.18", sha256="1d4caf5f8db57b0e4107d94fd5a1d02510a450dced6ca77d1839064c1bacf20c", url="https://pypi.org/packages/bc/a2/7d35ba2c8d9963398fcec49cd814e50a6b920d213928f06fdbbf8aa3289b/fasteners-0.18-py3-none-any.whl")
    version("0.17.3", sha256="cae0772df265923e71435cc5057840138f4e8b6302f888a567d06ed8e1cbca03", url="https://pypi.org/packages/f6/01/274da83334c20dc1ae7a48b1ea4ae50d3571d4e6aea65bb0368f841701ad/fasteners-0.17.3-py3-none-any.whl")
    version("0.17.2", sha256="2a4292ca86cdac2533226a62e7dbf4078d2a561fa615d33dd18921fa1d22a1e4", url="https://pypi.org/packages/39/17/b2ef8f3426b92957848fbed2dc1a11f807edb02d891e02cfc2267ce1ce8d/fasteners-0.17.2-py3-none-any.whl")
    version("0.17.1", sha256="bce18cacf62de17585875db0c5f690cecf5138d20f4b95e35eb56ae50dcc2b53", url="https://pypi.org/packages/64/f4/920a818e0aee493685e8741258dec892dc004a40c5b2eb866335fa1b59a6/fasteners-0.17.1-py3-none-any.whl")
    version("0.16.3", sha256="8408e52656455977053871990bd25824d85803b9417aa348f10ba29ef0c751f7", url="https://pypi.org/packages/31/91/6630ebd169ca170634ca8a10dfcc5f5c11b0621672d4c2c9e40381c6d81a/fasteners-0.16.3-py2.py3-none-any.whl")
    version("0.16.2", sha256="5d6b04bf12802a8bbb88233014b033e851f39470a675d93703412e9c5deac15c", url="https://pypi.org/packages/a2/eb/0e2f9bb76ff799dde0c6c078044506be141ef9442fce3e7b55c5fa2aec26/fasteners-0.16.2-py2.py3-none-any.whl")
    version("0.16.1", sha256="ea0570c5c932acb675ec63c7332ec0ad40ad99c765968319670f740f8c5a0462", url="https://pypi.org/packages/2e/63/b23490eb6cf3928455118ab5f041d6f4b629b82af91871668673d60353cd/fasteners-0.16.1-py2.py3-none-any.whl")
    version("0.16", sha256="74b6847e0a6bb3b56c8511af8e24c40e4cf7a774dfff5b251c260ed338096a4b", url="https://pypi.org/packages/78/20/c862d765287e9e8b29f826749ebae8775bdca50b2cb2ca079346d5fbfd76/fasteners-0.16-py2.py3-none-any.whl")
    version("0.15", sha256="007e4d2b2d4a10093f67e932e5166722d2eab83b77724156e92ad013c6226574", url="https://pypi.org/packages/18/bd/55eb2d6397b9c0e263af9d091ebdb756b15756029b3cededf6461481bc63/fasteners-0.15-py2.py3-none-any.whl")
    version("0.14.1", sha256="564a115ff9698767df401efca29620cbb1a1c2146b7095ebd304b79cc5807a7c", url="https://pypi.org/packages/14/3a/096c7ad18e102d4f219f5dd15951f9728ca5092a3385d2e8f79a7c1e1017/fasteners-0.14.1-py2.py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-monotonic", when="@0.11:0.15")
        depends_on("py-six", when="@:0.16.0,0.16.2:0.16")
    # END DEPENDENCIES

