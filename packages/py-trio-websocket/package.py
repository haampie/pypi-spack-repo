# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyTrioWebsocket(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("0.11.1", sha256="520d046b0d030cf970b8b2b2e00c4c2245b3807853ecd44214acd33d74581638", url="https://pypi.org/packages/48/be/a9ae5f50cad5b6f85bd2574c2c923730098530096e170c1ce7452394d7aa/trio_websocket-0.11.1-py3-none-any.whl")
    version("0.11.0", sha256="2e96d26b382e6ce279504a82215e6dac4e55c53287a0b065cc3dac755a13df22", url="https://pypi.org/packages/42/a4/793db8aecf563efc06ce0b195af4fab4513eca961bb5e1d9a56d25a42148/trio_websocket-0.11.0-py3-none-any.whl")
    version("0.10.4", sha256="c7a620c4013c34b7e4477d89fe76695da1e455e4510a8d7ae13f81c632bdce1d", url="https://pypi.org/packages/f2/25/868488d8b05104e3d1bf162565bbadd5fe6d62bf903710e6402c3aaceb1e/trio_websocket-0.10.4-py3-none-any.whl")
    version("0.10.3", sha256="a9937d48e8132ebf833019efde2a52ca82d223a30a7ea3e8d60a7d28f75a4e3a", url="https://pypi.org/packages/a5/a6/06e2373f95c12e9e8f6b910a76c86e375348ead77ab476230640666310fb/trio_websocket-0.10.3-py3-none-any.whl")
    version("0.10.2", sha256="0908435e4eecc49d830ae1c4d6c47b978a75f00594a2be2104d58b61a04cdb53", url="https://pypi.org/packages/ea/20/fbfa99f222b0aa298d4de6c20a65acf0ed18cab9a4392cea3f34c936a41a/trio_websocket-0.10.2-py3-none-any.whl")
    version("0.10.1", sha256="7e18d64d6cfa0d5dd49a49a0cfc38ea999aafa475ee194bf636da0998dee8294", url="https://pypi.org/packages/29/88/ec3be5629cad8bc496a96272a6617443d0801c5434a4afcdaac4a6d1b68d/trio_websocket-0.10.1-py3-none-any.whl")
    version("0.10.0", sha256="ae0a8bab4b0014510aca37fb67a6eaaa77e64aba372a7333845d2eb991989ae2", url="https://pypi.org/packages/3e/7d/b34fc53268a54f5cb731456c35a28b0b08e0ee2687968c977813445c0b5e/trio_websocket-0.10.0-py3-none-any.whl")
    version("0.9.2", sha256="5b558f6e83cc20a37c3b61202476c5295d1addf57bd65543364e0337e37ed2bc", url="https://pypi.org/packages/db/c5/b5e8bc1f40568a354f2a9cc296b8892605a9d2f22e725290fc33836dd2a3/trio_websocket-0.9.2-py3-none-any.whl")
    version("0.9.1", sha256="6a1e152dcaa73264d398328ff474f3cfcfc7660c02b826b03012414014e9170b", url="https://pypi.org/packages/1e/3f/4ca34c5ec2c670ffcaed093fae999516e8d975c44fa6e2ac2ee6b293fda6/trio_websocket-0.9.1-py3-none-any.whl")
    version("0.9.0", sha256="0c82515fd7dbef5e9f115fae24b2e690902ee7e8cd7d58cdbba1670758b048fb", url="https://pypi.org/packages/d1/c7/dcbc4e7ee949e401914fa3b36af0805df8cdd713cff8047b01c9aae56a97/trio_websocket-0.9.0-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-async-generator@1.10:", when="@0.9")
        depends_on("py-exceptiongroup", when="@0.11.1: ^python@:3.10")
        depends_on("py-exceptiongroup", when="@0.10:0.11.0")
        depends_on("py-trio@0.11:", when="@0.9:")
        depends_on("py-wsproto@0.14:", when="@0.9:")
    # END DEPENDENCIES

