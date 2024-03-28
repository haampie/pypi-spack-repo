# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPyobjcFrameworkSecurityfoundation(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("10.2", sha256="296f7f9ff96a35c19e4aef7621a567c0efe584aafd20ac25a2839dd96bf46a04", url="https://pypi.org/packages/9d/3e/fc6f4c09ffc57816b642ac246de563366508ed888e4e1bc50cd3d24151d3/pyobjc_framework_SecurityFoundation-10.2-py2.py3-none-any.whl")
    version("10.1", sha256="bbd67737afec25f2e3d41c8c2e7b4a6f9aae4231242e215b82a950eef6432ce0", url="https://pypi.org/packages/31/46/2002e1c71bc18312720ba71132464ec9d79c9b8e1033c8cbddb5f3dea8cc/pyobjc_framework_SecurityFoundation-10.1-py2.py3-none-any.whl")
    version("10.0", sha256="c7c8bc25d3297eb6c4684ef0c9680b619a1966ddc0cfd33a2122a46cd7963f57", url="https://pypi.org/packages/c2/91/4498d0c3c5879a732f2f0e45cf00977c74fa0f50929e3de82cc66fc78b5e/pyobjc_framework_SecurityFoundation-10.0-py2.py3-none-any.whl")
    version("9.2", sha256="e5868b66905a96429fc6149cee680c027ca530575200ff456cc97c6d9d59c301", url="https://pypi.org/packages/3a/89/7a7cfb0350edc544f215b90d3e8cbeade3bbb58e04397307ae76176ae77b/pyobjc_framework_SecurityFoundation-9.2-py2.py3-none-any.whl")
    version("9.1.1", sha256="cbf21fe7b098c88af63711984c1110d41f320dbb1321aa120a8bb314b8a8a46d", url="https://pypi.org/packages/c0/74/6bff039871d2fe528a93423ded43f40e089cf8dd0b1cf4718ee177e63439/pyobjc_framework_SecurityFoundation-9.1.1-py2.py3-none-any.whl")
    version("9.1", sha256="00d122abd2915be9d520319dfc01107ec2e57d7029cca92e5410704b76dc5bf5", url="https://pypi.org/packages/73/76/770af03a446ad89f926e5ec99826004fbecb5892d456f7798c05e58149b1/pyobjc_framework_SecurityFoundation-9.1-py2.py3-none-any.whl")
    version("9.0.1", sha256="548ffe20222aecafbe8bdb4b838cb9cb4a91b1780b2e88babd42899ecf2b1fd8", url="https://pypi.org/packages/18/f4/b17419b30e6ea801a5c8ab8a11cdda3a670f9f1809382f618414ff6b28f4/pyobjc_framework_SecurityFoundation-9.0.1-py2.py3-none-any.whl")
    version("9.0", sha256="c38024ab0e59d702424e8259a12f9bdc40d3b1926887a67634c16ee9d5cb4cc1", url="https://pypi.org/packages/d8/d4/09260eb0ffbd9cd4b434e27124d0825563ad46b2011218c44c21fd53ce80/pyobjc_framework_SecurityFoundation-9.0-py2.py3-none-any.whl")
    version("8.5.1", sha256="9b790d87d49f3e927a6916e7d42e9aa56493bded4b0d7fd59a4bd7c6ab106479", url="https://pypi.org/packages/e3/71/6497d242a979b56af812a83a8ab61489de7342b476a57d4271f3e3662906/pyobjc_framework_SecurityFoundation-8.5.1-py2.py3-none-any.whl")
    version("8.5", sha256="0d913e7ccc7db7e6adf3a7ed8db296dd28ec865e785f90b4b078eb14bdaeb152", url="https://pypi.org/packages/21/01/1e8cff4f5fcc749e4e180952de7a18ad4b56ef02054e7df6af98fc69e9cf/pyobjc_framework_SecurityFoundation-8.5-py2.py3-none-any.whl")
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
        depends_on("py-pyobjc-framework-security@10.2:", when="@10.2:")
        depends_on("py-pyobjc-framework-security@10.1:", when="@10.1")
        depends_on("py-pyobjc-framework-security@10:", when="@10:10.0")
        depends_on("py-pyobjc-framework-security@9.2:", when="@9.2:9")
        depends_on("py-pyobjc-framework-security@9.1.1:", when="@9.1.1:9.1")
        depends_on("py-pyobjc-framework-security@9.1:", when="@9.1:9.1.0")
        depends_on("py-pyobjc-framework-security@9.0.1:", when="@9.0.1:9.0")
        depends_on("py-pyobjc-framework-security@9:", when="@9:9.0.0")
        depends_on("py-pyobjc-framework-security@8.5.1:", when="@8.5.1:8")
        depends_on("py-pyobjc-framework-security@8.5:", when="@8.5:8.5.0")
    # END DEPENDENCIES

