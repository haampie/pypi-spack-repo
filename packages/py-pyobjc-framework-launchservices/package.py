# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPyobjcFrameworkLaunchservices(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("10.2", sha256="15b7c96e3059550c218ed5cb5de11dddc7aae21c67c0808b130a5d49b8f4cc0f", url="https://pypi.org/packages/a3/e8/9323d5032ada2465e2dbdd06ea40db8ac5a52bdb1c8735caaec0810c6b3d/pyobjc_framework_LaunchServices-10.2-py2.py3-none-any.whl")
    version("10.1", sha256="b792a863427a2c59c884952737041e25ef05bdb541471ce94fb26a05b48abbbc", url="https://pypi.org/packages/e9/0b/e837529b81b847e1342943b39714448b9fe8150531827094890f5b166bda/pyobjc_framework_LaunchServices-10.1-py2.py3-none-any.whl")
    version("10.0", sha256="f86c70574c7d7c9586fd1908e15fff9df297ab285d7067759337c8e03955427c", url="https://pypi.org/packages/9f/de/e6a3d660da1382458a7c53f3304c78598de780bd048648036b445e1924b9/pyobjc_framework_LaunchServices-10.0-py2.py3-none-any.whl")
    version("9.2", sha256="9fb1156c275bc2bcd4bbe9941c9bd2f47ad7c7d8ce096a4bd23d693440438469", url="https://pypi.org/packages/3f/f7/690044acdcb1538eedde33603ba15fd4825a9b00f61a43c18d8541f383d8/pyobjc_framework_LaunchServices-9.2-py2.py3-none-any.whl")
    version("9.1.1", sha256="7cf2612b713a59806772fd42673874f7fd652c21907fa1e103261315daeb110f", url="https://pypi.org/packages/17/e8/adb2e32a07948a37730fddc30ed146495f7ad6f4ee2caf3eda8343b82751/pyobjc_framework_LaunchServices-9.1.1-py2.py3-none-any.whl")
    version("9.1", sha256="85eeb76bed91686803e1bd48eadec75dad4f7d42a130500869794e138a964e20", url="https://pypi.org/packages/58/7a/99a37970f3f308f8557cb1bcf7ec74dbfe65b94cd77034198129af7c5554/pyobjc_framework_LaunchServices-9.1-py2.py3-none-any.whl")
    version("9.0.1", sha256="81513cb767669ff432e062c41fecef87531a006b9efd534026f63515cd94ecf2", url="https://pypi.org/packages/d9/13/451f5a3733bf283b5c4d41dbfcd741bdda2394e311d5795c7726cfbce4e8/pyobjc_framework_LaunchServices-9.0.1-py2.py3-none-any.whl")
    version("9.0", sha256="e946fe2dabdcd007049c2dd30b7b37379da1805446c7db3b9fcb5bc7244f6a70", url="https://pypi.org/packages/c7/d1/eae3c4e9e55f58b4f9c4ae2715dea10a5bdd90b295336cffee7218b8dec7/pyobjc_framework_LaunchServices-9.0-py2.py3-none-any.whl")
    version("8.5.1", sha256="8a22a3e730383f7ba5d51d065ab273f1a8671f610638359854d3a749ba8ab4da", url="https://pypi.org/packages/90/9e/7dc1968a2a14c9a4c11a9cdb42960b21a0bb54133aa4519e9ffc23f110ce/pyobjc_framework_LaunchServices-8.5.1-py2.py3-none-any.whl")
    version("8.5", sha256="f8d0c8577db3f4a7223a4c18e6453d3431d97c3041462a234492a08da1cde010", url="https://pypi.org/packages/61/4e/d76fb692139870b33c3c07a7205c32061521f292e4a8dae8faf8736d7332/pyobjc_framework_LaunchServices-8.5-py2.py3-none-any.whl")
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
        depends_on("py-pyobjc-framework-coreservices@10.2:", when="@10.2:")
        depends_on("py-pyobjc-framework-coreservices@10.1:", when="@10.1")
        depends_on("py-pyobjc-framework-coreservices@10:", when="@10:10.0")
        depends_on("py-pyobjc-framework-coreservices@9.2:", when="@9.2:9")
        depends_on("py-pyobjc-framework-coreservices@9.1.1:", when="@9.1.1:9.1")
        depends_on("py-pyobjc-framework-coreservices@9.1:", when="@9.1:9.1.0")
        depends_on("py-pyobjc-framework-coreservices@9.0.1:", when="@9.0.1:9.0")
        depends_on("py-pyobjc-framework-coreservices@9:", when="@9:9.0.0")
        depends_on("py-pyobjc-framework-coreservices@8.5.1:", when="@8.5.1:8")
        depends_on("py-pyobjc-framework-coreservices@8.5:", when="@8.5:8.5.0")
    # END DEPENDENCIES

