##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPyobjcFrameworkAvkit(PythonPackage):
    version("10.2", sha256="6497a5109a29235a7fd8bddcb6d79bd495ccd9373b41e84ca3f012a642e5b880", url="https://pypi.org/packages/34/cc/4413f44b57f0a95165701ecc62089a4bb463585b6f6c71957f931818b01f/pyobjc-framework-AVKit-10.2.tar.gz")
    version("10.1", sha256="15779995d4bb3b231a09d9032cf42e8f2681e4271ee677076a08c60a1b45fac7", url="https://pypi.org/packages/d2/db/03b1cfa2973a97b1e482ac81e0ca8ea7e03a9dbfacb571d0a9dfdbbcd476/pyobjc-framework-AVKit-10.1.tar.gz")
    version("10.0", sha256="53f8b74a76c948c0d9a96f331d99e1a6ab7a1ce87af7d9bbfffd267532bea98c", url="https://pypi.org/packages/7c/6f/62ce1f1d64edeaacd56b6b59d5016ee72c5623b41aa477f9182711257d06/pyobjc-framework-AVKit-10.0.tar.gz")
    version("9.2", sha256="788be2abee6c1df6862189a25baa25416d8aa49304f76b95c5ee2240fe96d1d2", url="https://pypi.org/packages/dd/78/e7766c8683e544c8a0ab2cbad8e302942d59d287fab10f8a538140289926/pyobjc-framework-AVKit-9.2.tar.gz")
    version("9.1.1", sha256="41e0d8dcf456ad25cbf4ef0bacbbaa88f85d60255668c438d4334805be8f57b3", url="https://pypi.org/packages/ac/f7/6133ad7a4ee8895ea44bbf1c02f6c3cea1fac46738a305608690464a8895/pyobjc-framework-AVKit-9.1.1.tar.gz")
    version("9.1", sha256="a9452d1bd20f9f6240daf01d6c39358a6db8edc699bb68cf17326e136b416cbe", url="https://pypi.org/packages/c8/e0/3275bad298b16cd10f91d6b14fdcfb9134d39d5adbc65c9ee06995698337/pyobjc-framework-AVKit-9.1.tar.gz")
    version("9.0.1", sha256="382815a5ffab7444cade994cc3335898eaf25fd627af2adf7a5a9d982a62a273", url="https://pypi.org/packages/2f/5d/06960370c2ec0245a8685c1c0680679302fd00b8e94d8bb83c8211502a2c/pyobjc-framework-AVKit-9.0.1.tar.gz")
    version("9.0", sha256="fcdd4f3652e19a0b27e2686c105e0c7e8fa3a5dd2acc6a46ca86206e81cd9180", url="https://pypi.org/packages/d2/85/bc997c4f0a8dbaf4f1bc9daf66f793c0d8c087f24a1295400c5feaa0f6fc/pyobjc-framework-AVKit-9.0.tar.gz")
    version("8.5.1", sha256="fc6a92cf236e5e2693f0d0484094ad6b020821160076f4ef75034b666c2a9931", url="https://pypi.org/packages/97/dc/faf75e2dc6f49d6c165f100048e677406851b05b86194146c77be1645864/pyobjc-framework-AVKit-8.5.1.tar.gz")
    version("8.5", sha256="ec1283fe4f805ab156d04f6cdc76a03c99235e1989026bea0aa97532c1510ebc", url="https://pypi.org/packages/ab/a9/984eeda3d461670e1c1de33b7ccd97b0f4323e8b94dcb47f46727a522231/pyobjc-framework-AVKit-8.5.tar.gz")

    with default_args(type="run"):
        depends_on("py-pyobjc-core@10.2:", when="@10.2:")
        depends_on("py-pyobjc-core@10.1:", when="@10.1")
        depends_on("py-pyobjc-core@10:", when="@10:10.0")
        depends_on("py-pyobjc-framework-cocoa@10.2:", when="@10.2:")
        depends_on("py-pyobjc-framework-cocoa@10.1:", when="@10.1")
        depends_on("py-pyobjc-framework-cocoa@10:", when="@10:10.0")
        depends_on("py-pyobjc-framework-quartz@10.2:", when="@10.2:")
        depends_on("py-pyobjc-framework-quartz@10.1:", when="@10.1")
        depends_on("py-pyobjc-framework-quartz@10:", when="@10:10.0")

