##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyEarthengineApi(PythonPackage):
    version("0.1.394", sha256="d6b1bd4fc9cab98aaefd3355b1b0cdbd355f8b92643104e42a6fffe698bc4191", url="https://pypi.org/packages/04/95/5ec43d7b4322367e4f24f0a16e34189c8e5ab1aed0ec3e1fca65b71b1ba3/earthengine_api-0.1.394-py3-none-any.whl")
    version("0.1.393", sha256="54b4bf3f13c2570887a2bb72f1a3a0f8547e628894d922b9819168899cd70769", url="https://pypi.org/packages/de/af/e25ec4ef904d939127a35af2ecf2dc6dcffa0708bd91198985b74c14db05/earthengine_api-0.1.393-py3-none-any.whl")
    version("0.1.392", sha256="8a26ce06d429fdde61b811199ff5c125501b2019843dda7aff1b34d4c6693c6f", url="https://pypi.org/packages/97/e4/43420d5bd093f29d6f4e13f9e940543e28d5c840900ecd365f744e0fa063/earthengine_api-0.1.392-py3-none-any.whl")
    version("0.1.391", sha256="c005ef8aabb1f34ba5b90a25475b955bb150d66e3d2a71c0390b9b2e1fa2e182", url="https://pypi.org/packages/3b/ea/4e8e2947fe50cf6c0de850a33487b7b8e10112cbf89e9c22765ff91fe341/earthengine_api-0.1.391-py3-none-any.whl")
    version("0.1.390", sha256="35352fdd7cd06c6a811bce0b236be7e63b0d7983df830228860a8094078db66d", url="https://pypi.org/packages/3a/67/57b971fa989283f1c1599ff42dec0bb8e6b5ad0a4ccc2f0ac29c8aac062a/earthengine_api-0.1.390-py3-none-any.whl")
    version("0.1.389", sha256="9a93d087e87f6cfe92d80b6b1663aa01a760bf6f92d365ea6d8a2b97246af467", url="https://pypi.org/packages/47/a5/dc50c3b011839487cf01ea9977bfd1e2519cb9ceed9de86815685d054f80/earthengine_api-0.1.389-py3-none-any.whl")
    version("0.1.388", sha256="c5c6ed7613e7d43eb18691c35a48840025473b1deae5351d3b703785bba916c4", url="https://pypi.org/packages/c3/31/4f7e9ea03e96a223a834d952ea0468867cf8e89aa5ac326473f2b899eb73/earthengine_api-0.1.388-py3-none-any.whl")
    version("0.1.386", sha256="b62c214fd1a44eeca795d919473b0aa578e68699d687646f601f64ce6c76ca24", url="https://pypi.org/packages/ea/5e/973fde11441125767acd36fe433079e03437f8d3831a3cea8b52dad3ff05/earthengine-api-0.1.386.tar.gz")
    version("0.1.385", sha256="ad6d45980ac0aa6b155cb8a9b04584944ed5da1c2f8a8e71b5c29956449d7a30", url="https://pypi.org/packages/3b/33/4393cf689cee8d742394f98a7ca510fb934dc95ec5c80472f6820fa7a6cd/earthengine-api-0.1.385.tar.gz")
    version("0.1.384", sha256="b2ed22d5fa9a930f6b97c439b99e51fea75f4d8e911ead740d3bce540dabdf6b", url="https://pypi.org/packages/96/62/b7651eeedacbbaae1840f1ae902269160bd40ea4861fc99ca0d4eab57115/earthengine-api-0.1.384.tar.gz")
    version("0.1.344", sha256="bc5a270b8296aaae8574e68dfd93fe878bc5fbe77d1c41f90bcb5e5b830ca5c8", url="https://pypi.org/packages/7c/69/6daf01496661727964e217ef4e67fa077112d41d3b1c747d593e246ec0b1/earthengine-api-0.1.344.tar.gz")

    with default_args(type="run"):
        depends_on("py-google-api-python-client@1.12.1:", when="@0.1.388:")
        depends_on("py-google-auth@1.4.1:", when="@0.1.388:")
        depends_on("py-google-auth-httplib2@0.0.3:", when="@0.1.388:")
        depends_on("py-google-cloud-storage", when="@0.1.388:")
        depends_on("py-httplib2@0.9.2:", when="@0.1.388:")
        depends_on("py-requests", when="@0.1.388:")

