##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPyobjcFrameworkInputmethodkit(PythonPackage):
    version("10.2", sha256="294cf2c50cdbb4cdc8f06946924a01faf45a7356ef86652d73c1f310fc1ce99f", url="https://pypi.org/packages/9d/3c/377c35aab6ae237d95b345f533191c43fdb4c7a4d9daca364bbeb23d4072/pyobjc-framework-InputMethodKit-10.2.tar.gz")
    version("10.1", sha256="b995f43a8859016474098c894c966718afe9fbcc18996ce3c6bebfc6a64cfad7", url="https://pypi.org/packages/1a/b1/f3d42ad9f5b4e91ec8130319849da53e0e6bee7e47a7d0aee6d890a1a0cf/pyobjc-framework-InputMethodKit-10.1.tar.gz")
    version("10.0", sha256="dc2f10752ab62e4c7b2306938d617d83bef6d52752862a0998ed57db472e36ae", url="https://pypi.org/packages/0c/fe/3792b6a27b10786153cbe773f96ba09530beafa1f5b4916ffa0e7f240a1e/pyobjc-framework-InputMethodKit-10.0.tar.gz")
    version("9.2", sha256="d06836f07b8c947d3d18cf29415c346c52b9076861fada068b1d82e6ee1bc026", url="https://pypi.org/packages/1f/50/d6db496e2df9872f7ad76af08ef99e11fee59f633e0499a686bcb3e8973e/pyobjc-framework-InputMethodKit-9.2.tar.gz")
    version("9.1.1", sha256="a1d652e5a02a804b4a07159c0f49b2b1d2ba857272d2aeb45c597166b97e4314", url="https://pypi.org/packages/21/b0/92ddeccde32286f6a075ce9fc53aa5bb5c6056364f40530a805efd7542cd/pyobjc-framework-InputMethodKit-9.1.1.tar.gz")
    version("9.1", sha256="851e9cc1f58edd98e1e712fdfc4bc67678e32fed7b3278e2683956857e6dec0b", url="https://pypi.org/packages/9d/b5/5f4b690f59b846b52ce5b5eae1099c9bb476e0585b50bdac7212144d1fd6/pyobjc-framework-InputMethodKit-9.1.tar.gz")
    version("9.0.1", sha256="c948359e0abcfd3a2287edc35b149afa7b490e74a32bf08c6020b13e54107e82", url="https://pypi.org/packages/b4/32/c580e6b3fac9a4e3114bac3821631e7b7aae8a3970d92bbd7fdb40aed0d3/pyobjc-framework-InputMethodKit-9.0.1.tar.gz")
    version("9.0", sha256="98c3ffc397edb5e4947deef05cae89ba277c4ffa896b0831b6c9c6a5a521ea10", url="https://pypi.org/packages/36/39/a1f0d2f029bc6b93d7f69d5db393e232bd7821ee2f30965e3999898c3630/pyobjc-framework-InputMethodKit-9.0.tar.gz")
    version("8.5.1", sha256="3b55569c2b70a941a3e125c2533dc724a7a8cc31f248d1e9acfc42b0b85fde81", url="https://pypi.org/packages/bf/95/60bcbc9f005eb13ed14fec7c98c6c759fc8e9248cce5c8bb4111ffe0fcb3/pyobjc-framework-InputMethodKit-8.5.1.tar.gz")
    version("8.5", sha256="dfe85508af982fca673803404fec623c4aa0bc3a77488cf29b9bc83d31a36ed1", url="https://pypi.org/packages/85/e9/0f3a6bd92276cd8d97488f27adf300ae996a13796c908874bf93423e45b5/pyobjc-framework-InputMethodKit-8.5.tar.gz")

    with default_args(type="run"):
        depends_on("py-pyobjc-core@10.2:", when="@10.2:")
        depends_on("py-pyobjc-core@10.1:", when="@10.1")
        depends_on("py-pyobjc-core@10:", when="@10:10.0")
        depends_on("py-pyobjc-framework-cocoa@10.2:", when="@10.2:")
        depends_on("py-pyobjc-framework-cocoa@10.1:", when="@10.1")
        depends_on("py-pyobjc-framework-cocoa@10:", when="@10:10.0")

