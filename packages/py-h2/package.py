##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyH2(PythonPackage):
    version("4.1.0", sha256="03a46bcf682256c95b5fd9e9a99c1323584c3eec6440d379b9903d709476bc6d", url="https://pypi.org/packages/2a/e5/db6d438da759efbb488c4f3fbdab7764492ff3c3f953132efa6b9f0e9e53/h2-4.1.0-py3-none-any.whl")
    version("4.0.0", sha256="ac9e293a1990b339d5d71b19c5fe630e3dd4d768c620d1730d355485323f1b25", url="https://pypi.org/packages/bd/c2/5ffec707d0022208787908d9657f782ce35b653baa1e87abecf22a7cf513/h2-4.0.0-py3-none-any.whl")
    version("3.2.0", sha256="61e0f6601fa709f35cdb730863b4e5ec7ad449792add80d1410d4174ed139af5", url="https://pypi.org/packages/25/de/da019bcc539eeab02f6d45836f23858ac467f584bfec7a526ef200242afe/h2-3.2.0-py2.py3-none-any.whl")
    version("3.1.1", sha256="ac377fcf586314ef3177bfd90c12c7826ab0840edeb03f0f24f511858326049e", url="https://pypi.org/packages/fb/e3/823a574b33aac578c3a171b1a2225ee8e1ad0c3842f3871bdc34e270f352/h2-3.1.1-py2.py3-none-any.whl")
    version("3.1.0", sha256="c8f387e0e4878904d4978cd688a3195f6b169d49b1ffa572a3d347d7adc5e09f", url="https://pypi.org/packages/a6/b2/0348a08cce9980b15ef8607adc7f0534193fe25b9269daa0c327dc74f026/h2-3.1.0-py2.py3-none-any.whl")
    version("3.0.1", sha256="4be613e35caad5680dc48f98f3bf4e7338c7c429e6375a5137be7fbe45219981", url="https://pypi.org/packages/30/2b/833e258072d47865b99dc0810475481d6371e3d3bfede9251ca27035e30f/h2-3.0.1-py2.py3-none-any.whl")
    version("3.0.0", sha256="e35364b8560d408638a463491670ea0302311a30a64c61ccac7d6ea7488b33b5", url="https://pypi.org/packages/10/f6/bf83b9f8ce32ec52217d9079fbec63b5466e8a62c65dd7965cb66020a37d/h2-3.0.0-py2.py3-none-any.whl")

    with default_args(type="run"):
        depends_on("py-hpack@4:", when="@4:")
        depends_on("py-hpack@3", when="@3.2:3")
        depends_on("py-hpack@2.3:3", when="@3.0.1:3.1")
        depends_on("py-hpack@2.3:2", when="@3:3.0.0")
        depends_on("py-hyperframe@6:", when="@4:")
        depends_on("py-hyperframe@5.2:5", when="@3.1:3")
        depends_on("py-hyperframe@5", when="@3:3.0")

