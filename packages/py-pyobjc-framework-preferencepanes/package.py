# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPyobjcFrameworkPreferencepanes(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("10.2", sha256="4da63d42bc2f2de547b6c817236e902ad6155efa05e5305daa38be830b70a19d", url="https://pypi.org/packages/1d/b8/dbb234ced081a2b92d90538f7061637031823127e529e29f17d523fb73c6/pyobjc_framework_PreferencePanes-10.2-py2.py3-none-any.whl")
    version("10.1", sha256="9b16c93d7f684cbe097932c8260a0b6460ad9fc68230648981340b7e3ee7053e", url="https://pypi.org/packages/da/fb/b60617ab6e7392485a25464e58f6d23d32be6c59922882fe5ccefc9e86d9/pyobjc_framework_PreferencePanes-10.1-py2.py3-none-any.whl")
    version("10.0", sha256="992765158f0cae73957178109338bde94bbac5c91ca6e1ada884c3dc43868e18", url="https://pypi.org/packages/e3/9f/bc04935f3ed97090cd86796a291d52fc414c6d65af64fe662546ad4485c1/pyobjc_framework_PreferencePanes-10.0-py2.py3-none-any.whl")
    version("9.2", sha256="b1416b9eb72dc8e9ded32b326c7fd07356d61d115a269a0909fe1e9520886255", url="https://pypi.org/packages/62/8d/170a1da2b40906e179c61412e75cd74304f16a6099f098c8559e52fcafc6/pyobjc_framework_PreferencePanes-9.2-py2.py3-none-any.whl")
    version("9.1.1", sha256="ad34e358321bf8147f327e562987b15307561f795b90ee8e808c60bc97cdc48e", url="https://pypi.org/packages/2a/50/a06e6e8114e25fbea2c1e2a2047fb448b0ff2b5329f3a746f5d83a2b6fb7/pyobjc_framework_PreferencePanes-9.1.1-py2.py3-none-any.whl")
    version("9.1", sha256="bb643d6ac86cc3f99956e32e9d9bf9bcae887a643658ffb82f999410207c13b6", url="https://pypi.org/packages/a0/b0/9332058571709170edb81dda83a49dcb97a18537efa9508fac8ec3f8fc65/pyobjc_framework_PreferencePanes-9.1-py2.py3-none-any.whl")
    version("9.0.1", sha256="3895ad636420cff1f4f1d7e4bad566e0b918a270e5cca0532f45010a61211fda", url="https://pypi.org/packages/6f/17/a70b7ba918f3a5f118cd151a82b10dcefbcb1d5ab5360ba55c570a465974/pyobjc_framework_PreferencePanes-9.0.1-py2.py3-none-any.whl")
    version("9.0", sha256="f441fa055638b768c57442157da6308b16af46ea420ee50eb531555c9b968497", url="https://pypi.org/packages/c7/19/97165427353b885a59c695d2bd568a680b2ac7c0cf60ec8e62364af74ba8/pyobjc_framework_PreferencePanes-9.0-py2.py3-none-any.whl")
    version("8.5.1", sha256="4008f7580a46a0dcff1aa55916717e7b65b93b159d5b7dcf9c5f7279966cc93e", url="https://pypi.org/packages/43/ca/e0a57777af894c5f99700e0465cf9df2112996ec8354d2afa7c124b3f8ab/pyobjc_framework_PreferencePanes-8.5.1-py2.py3-none-any.whl")
    version("8.5", sha256="d95ad33b484676ae093feddcccd6b65d1c751545ab8a1bde61f8c807a9ab16c9", url="https://pypi.org/packages/6e/43/8890629896ed9e38c353d3d33973df496a5b191f815c5643e76d826bd099/pyobjc_framework_PreferencePanes-8.5-py2.py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-pyobjc-core@10.2:", when="@10.2:")
        depends_on("py-pyobjc-core@10.1:", when="@10.1")
        depends_on("py-pyobjc-core@10:", when="@10:10.0")
        depends_on("py-pyobjc-core@9.2:", when="@9.2:9")
        depends_on("py-pyobjc-core@9.1.1:", when="@9.1.1:9.1")
        depends_on("py-pyobjc-core@9.1:", when="@9.1:9.1.0")
        depends_on("py-pyobjc-core@9.0.1:", when="@9.0.1:9.0")
        depends_on("py-pyobjc-core@9:", when="@9:9.0.0")
        depends_on("py-pyobjc-core@8.5.1:", when="@8.5.1:8")
        depends_on("py-pyobjc-core@8.5:", when="@8.5:8.5.0")
        depends_on("py-pyobjc-framework-cocoa@10.2:", when="@10.2:")
        depends_on("py-pyobjc-framework-cocoa@10.1:", when="@10.1")
        depends_on("py-pyobjc-framework-cocoa@10:", when="@10:10.0")
        depends_on("py-pyobjc-framework-cocoa@9.2:", when="@9.2:9")
        depends_on("py-pyobjc-framework-cocoa@9.1.1:", when="@9.1.1:9.1")
        depends_on("py-pyobjc-framework-cocoa@9.1:", when="@9.1:9.1.0")
        depends_on("py-pyobjc-framework-cocoa@9.0.1:", when="@9.0.1:9.0")
        depends_on("py-pyobjc-framework-cocoa@9:", when="@9:9.0.0")
        depends_on("py-pyobjc-framework-cocoa@8.5.1:", when="@8.5.1:8")
        depends_on("py-pyobjc-framework-cocoa@8.5:", when="@8.5:8.5.0")
    # END DEPENDENCIES

