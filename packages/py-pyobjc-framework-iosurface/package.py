# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPyobjcFrameworkIosurface(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("10.2", sha256="b571335a2150e865828d3e52e2a742531499c88dd85215c14d07e68e9bed70a7", url="https://pypi.org/packages/3d/55/8889d7c137b4acce33f3d3cbc4e0271e78b9176633f073b0ccfce6bd03f0/pyobjc_framework_IOSurface-10.2-py2.py3-none-any.whl")
    version("10.1", sha256="46239320148b82c1f2364d5468999b48fa9c94fc404aff6c5451d23896ece694", url="https://pypi.org/packages/1b/56/0894e4e88ebcb75a2cdd84b80c7d7540333c0cf01590d928c5a6a898c363/pyobjc_framework_IOSurface-10.1-py2.py3-none-any.whl")
    version("10.0", sha256="a3df57071d833c58ca019bf880a54c92aaeb11accc006a1fb4eb7f215cf8a1a1", url="https://pypi.org/packages/c0/60/75f4b9961d9dd394b25b68c8c3e8eb1ffe3d46866f790460d190b137183c/pyobjc_framework_IOSurface-10.0-py2.py3-none-any.whl")
    version("9.2", sha256="c974077ff4c6dda3b81c0e1b631418dfb865693f32fc437cd54f778be0d26973", url="https://pypi.org/packages/ca/7b/7d220c07c63fa70130a3a397755d832a1dc52116e246bc7d642fde738d10/pyobjc_framework_IOSurface-9.2-py2.py3-none-any.whl")
    version("9.1.1", sha256="0bd8b47330a399224899f1730805d68c4a2488656abf23903350a43652bc6a33", url="https://pypi.org/packages/cd/be/d0041ba3c063b964cb426781d3670c3f8bc3a6d053e11303204e78488517/pyobjc_framework_IOSurface-9.1.1-py2.py3-none-any.whl")
    version("9.1", sha256="7d115aac23bc937acdc3ca1ff7aef360064a35b81d8a07e647f319163214f575", url="https://pypi.org/packages/86/6b/ed8853e5bd9c66b0df25fc2308538ca1d6a204434ac01ba283a46b22e9ad/pyobjc_framework_IOSurface-9.1-py2.py3-none-any.whl")
    version("9.0.1", sha256="c06c94b8a69350a9f5d6dfad63b7018387b9d90cb0d2cc90942afad5ed049b34", url="https://pypi.org/packages/be/8c/a0fe726bd888e848e379c241b81a79a2b4178127d180f74d3fdf4da5bfdf/pyobjc_framework_IOSurface-9.0.1-py2.py3-none-any.whl")
    version("9.0", sha256="4a6f29f11d511e60d87dd763f0f88ea9632a1bc8c246aec48cd7a7d60aeb3b46", url="https://pypi.org/packages/59/c1/8b80040433a937fca45f3e917567297ca2de18fbf1b98d46763560dabce9/pyobjc_framework_IOSurface-9.0-py2.py3-none-any.whl")
    version("8.5.1", sha256="4a815299dae4752147f85e2c3d3bcdc14146cdd1c450722c74642f7241745a49", url="https://pypi.org/packages/d0/df/c4546ebbd922e64274486e40cf0d2ac380602ab93de9c309b748d67d0496/pyobjc_framework_IOSurface-8.5.1-py2.py3-none-any.whl")
    version("8.5", sha256="f5809d25b4bc97c03ab694e83151d1fdab5efe2e871f3833a9112fc060c75496", url="https://pypi.org/packages/71/3f/83a1e286eeb06397cbe85737f34fb7c57179c3f6bcc02c9e38b9fc995bc9/pyobjc_framework_IOSurface-8.5-py2.py3-none-any.whl")
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

