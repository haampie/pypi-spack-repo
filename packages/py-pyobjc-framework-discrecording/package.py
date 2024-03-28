# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPyobjcFrameworkDiscrecording(PythonPackage):
    # BEGIN VERSIONS
    version("10.2", sha256="9670018a0970553882feb10e066585ad791c502539712f4117bad4a6647c79b3", url="https://pypi.org/packages/c4/a1/0cdd58c3180fd705f1a206991b0eb3d0f3dde17dc246d2d5e786d310ab77/pyobjc-framework-DiscRecording-10.2.tar.gz")
    version("10.1", sha256="321c69b6494c57d75d4a0ecf5d90ceac3800441bf877eac8196ab25dcf15ebde", url="https://pypi.org/packages/2d/73/39878ea9187e75969fe3e5745db2d6ca59a1ea3f0bed7b78684da15c2579/pyobjc-framework-DiscRecording-10.1.tar.gz")
    version("10.0", sha256="1b4a9a702f0695ed87392693ab916cc120c179547d6fa7bf3e59708fe218ec22", url="https://pypi.org/packages/b8/06/3d9b70e91537d57b68b469ddbf2f5d2b26eab83e23f36bb57aef485204fd/pyobjc-framework-DiscRecording-10.0.tar.gz")
    version("9.2", sha256="253c6772b6541739cbc11c1e44001d8b16fd6d36946e55b738c110e42978ba4c", url="https://pypi.org/packages/55/ca/ba7ba6ef509dbc6c7ea8dc7b4e79df921cf4b9f75485382c7ea52a99a9e0/pyobjc-framework-DiscRecording-9.2.tar.gz")
    version("9.1.1", sha256="63a3e94786faac3623070393bcc12813e2ae0a8af404ea907143d7fb1162d482", url="https://pypi.org/packages/1b/c8/78931be3b49cd2471a82d3836b3d9a46b539499cab11f1a60adcae332236/pyobjc-framework-DiscRecording-9.1.1.tar.gz")
    version("9.1", sha256="2da9cbb38f761a66c90f482f8ba7931a1e172c5b22b97a9fa6ff4f0f407b5c64", url="https://pypi.org/packages/b1/3b/3c1ff22f025bb04bb3e224f6c94ca003abd8b018bbebd5122bdf1d556ca4/pyobjc-framework-DiscRecording-9.1.tar.gz")
    version("9.1-beta1", sha256="06e075ef1d84419c17abd4f455605caaa553a7b5be76ef07607cb0450e609562", url="https://pypi.org/packages/56/18/a398d8a0ce3e0b95a4823ad2129216e6ab5a55068bf2df6924d44bdde6e1/pyobjc-framework-DiscRecording-9.1b1.tar.gz")
    version("9.0.1", sha256="06def981e8c25e6c51e8918eedfb56fa983f2b71f1c7ae43a54f84416dc75d69", url="https://pypi.org/packages/76/e7/ff52a1c1bb86027e717841a3412d17f1261f5352f331075eae0be838f74c/pyobjc-framework-DiscRecording-9.0.1.tar.gz")
    version("9.0", sha256="1a908dc93bc6dbba39c77656d6e17d665a2a0103b4a1ef980250aa0782af2b85", url="https://pypi.org/packages/77/85/8edd3d7323fe3bb445fbd88ca156e20f62f4ebe9a5b42da7298486305ff7/pyobjc-framework-DiscRecording-9.0.tar.gz")
    version("8.5.1", sha256="9bfb437878885023b3b6951aaaebd4b5f992c5e75347364dd07a8d7126c19eb4", url="https://pypi.org/packages/8d/63/ee9eab9d3b1ac5be97b65ffd2ad71dfafa9fe7c1538f88c4fde0149c5a50/pyobjc-framework-DiscRecording-8.5.1.tar.gz")
    version("8.5", sha256="dc3f3fa26d482a5a470e4f09fe909647f5125df241a27ed8eb5c6a71c534a01e", url="https://pypi.org/packages/35/b2/e73f5f4ed69f1914fbeabfaaad16501c34e9876b2dee63487c53c10a500e/pyobjc-framework-DiscRecording-8.5.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-pyobjc-core@10.2:", when="@10.2:")
        depends_on("py-pyobjc-core@10.1:", when="@10.1")
        depends_on("py-pyobjc-core@10:", when="@10:10.0")
        depends_on("py-pyobjc-framework-cocoa@10.2:", when="@10.2:")
        depends_on("py-pyobjc-framework-cocoa@10.1:", when="@10.1")
        depends_on("py-pyobjc-framework-cocoa@10:", when="@10:10.0")
    # END DEPENDENCIES

