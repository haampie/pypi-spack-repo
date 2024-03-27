##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPyobjcFrameworkApplicationservices(PythonPackage):
    version("10.2", sha256="f83d6ed3320afb6648be6defafe0f05bac00d0281fc84ee4766ff977309b659f", url="https://pypi.org/packages/87/cf/9445914f4daa0c7a335a24e443107da9c3c726e6c4220a261f5d6b23ad24/pyobjc-framework-ApplicationServices-10.2.tar.gz")
    version("10.1", sha256="bb780eabadad0fbf36a128041dccfd71e30bbeb6b110852d37fd5c98f4a2ec04", url="https://pypi.org/packages/5e/9b/e30c8394c046f3d52aea968182ec25d91a4afd904e44184a7e425e57efc1/pyobjc-framework-ApplicationServices-10.1.tar.gz")
    version("10.0", sha256="8a667da95c09202def58746c42d5093f90be5762a52e6f5ad8beb334b51dca20", url="https://pypi.org/packages/92/99/3a32664089b07eaef3ff0d8f95be9ef5dce390a9957f257b51656850995c/pyobjc-framework-ApplicationServices-10.0.tar.gz")
    version("9.2", sha256="568c95dd1899b49f88af9d4a2da1e979b369f808c6854cf52c0035df09a2528a", url="https://pypi.org/packages/1f/0d/55aa1ed3b641675992991c1f353d076ddbcb779baccb297292531740dd51/pyobjc-framework-ApplicationServices-9.2.tar.gz")
    version("9.1.1", sha256="50c613bee364150bbd6cd992ca32b0848a780922cb57d112f6a4a56e29802e19", url="https://pypi.org/packages/a5/77/a02b908bc7d443ca73895b278cd48f43c29daab216e4bbafbc29f1d14f11/pyobjc-framework-ApplicationServices-9.1.1.tar.gz")
    version("9.1", sha256="4c60ecb9c3c450feeb11ba6036f5001fe809b135ff8c5d2db9f205625bade01b", url="https://pypi.org/packages/3f/f5/f87477917a221b103027955069878d2c589d06ed04be9576019eaa72314e/pyobjc-framework-ApplicationServices-9.1.tar.gz")
    version("9.0.1", sha256="e3a350781fdcab6c1da4343dfc54ae3c0523e59e61147432f61dcfb365752fde", url="https://pypi.org/packages/04/8d/7413bb658fae85ac99fc11ddc351678ab477edf4cdf1e13007e28e12c065/pyobjc-framework-ApplicationServices-9.0.1.tar.gz")
    version("9.0", sha256="bed332b53f2429219df4ba43a99e85b3305f82dcee0bd370849f84c3d786fd69", url="https://pypi.org/packages/f3/f5/be7c3704767c49cfab9f82951247a138a6fc0f0d6b93a8e994ebb003ce0b/pyobjc-framework-ApplicationServices-9.0.tar.gz")
    version("8.5.1", sha256="9cc5118c4c6db4c1ae349ee286b4c45c469f677afc6850d1d8d86af0e103e3df", url="https://pypi.org/packages/6a/4d/f820ff207905c5d1094cfa2cc3abbb306c532ea1f801f2320eabf73423fc/pyobjc-framework-ApplicationServices-8.5.1.tar.gz")
    version("8.5", sha256="fa3015ef8e3add90af3447d7fdcc7f8dd083cc2a1d58f99a569480a2df10d2b1", url="https://pypi.org/packages/1e/40/186f708bf77a4b674da8bf610edc678e296778b372cba0b4d18c2143b490/pyobjc-framework-ApplicationServices-8.5.tar.gz")

    with default_args(type="run"):
        depends_on("py-pyobjc-core@10.2:", when="@10.2:")
        depends_on("py-pyobjc-core@10.1:", when="@10.1")
        depends_on("py-pyobjc-core@10:", when="@10:10.0")
        depends_on("py-pyobjc-framework-cocoa@10.2:", when="@10.2:")
        depends_on("py-pyobjc-framework-cocoa@10.1:", when="@10.1")
        depends_on("py-pyobjc-framework-cocoa@10:", when="@10:10.0")
        depends_on("py-pyobjc-framework-coretext@10.2:", when="@10.2:")
        depends_on("py-pyobjc-framework-coretext@10.1:", when="@10.1")
        depends_on("py-pyobjc-framework-quartz@10.2:", when="@10.2:")
        depends_on("py-pyobjc-framework-quartz@10.1:", when="@10.1")
        depends_on("py-pyobjc-framework-quartz@10:", when="@10:10.0")

