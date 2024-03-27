##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPyobjcFrameworkAdsupport(PythonPackage):
    version("10.2", sha256="4883ac30f1d78d764b57aacb46af78018f2302b9f7e8f4e1fccb25c3cb44ab74", url="https://pypi.org/packages/cb/c4/d6a27d9775d060f2e9c81d8ac8730dd8ba3ef595c3e50484eafa652b5e62/pyobjc_framework_AdSupport-10.2-py2.py3-none-any.whl")
    version("10.1", sha256="d61f2e44f6c2ed5c33b6520754ef8ea22470f8ac3154912aa44bee4fb792255c", url="https://pypi.org/packages/4d/d3/08779d7bd4846acb19dbe7ff5629e53cb61cc1c01d48b3c16d72530a1c06/pyobjc_framework_AdSupport-10.1-py2.py3-none-any.whl")
    version("10.0", sha256="9fe3295892d2906f46ee36c982cf1b41a94dc9c5a316937174966512d61a7939", url="https://pypi.org/packages/a1/08/489ff746a853c92d069e219e3720c16d8131411c07de461661c44a94b392/pyobjc_framework_AdSupport-10.0-py2.py3-none-any.whl")
    version("9.2", sha256="ee2faf9e667210fc54e661b2134764f55d94a3f5275e776680486f7d5b6d794b", url="https://pypi.org/packages/0b/fc/f9935f12bf15b44ad58c183082f9bf8d8bd845677cc6ed5e20cb145351f0/pyobjc_framework_AdSupport-9.2-py2.py3-none-any.whl")
    version("9.1.1", sha256="7777aaf53c281bb5f3ee3f26988609570ed2103836d708e7dde72014d02d4863", url="https://pypi.org/packages/9e/0a/1a99555c745031b3a4bd476849474caa8cb3ac1cb21cf702e236ddd51311/pyobjc_framework_AdSupport-9.1.1-py2.py3-none-any.whl")
    version("9.1", sha256="99a71205dc87ceadca1e64307dabf4ade99ca71c319eba1c847f597303cb3df0", url="https://pypi.org/packages/fb/b5/a02c0a7a87c719b47a74834369323f01b32bd6148e0fc3b98c96a3bb6704/pyobjc_framework_AdSupport-9.1-py2.py3-none-any.whl")
    version("9.0.1", sha256="290dccba0b234ec3a635ddbe3f3095816e2a76783b69e96c4d0799a1922d694b", url="https://pypi.org/packages/da/c0/c96149e84016d133a5da76c30c639088229b67074e281e8a9b40ce292060/pyobjc_framework_AdSupport-9.0.1-py2.py3-none-any.whl")
    version("9.0", sha256="291bf5e562d3ccce252d6c7d885191368bc251b65287abf93571a8447ad33d29", url="https://pypi.org/packages/14/ff/4ca78700f289c78c25ed4f9ac877f9bb25e3d952d187011cfeb011d8f82f/pyobjc_framework_AdSupport-9.0-py2.py3-none-any.whl")
    version("8.5.1", sha256="d30aed801ad3889b1370630f67f9066a309632f4258c41bc5678916093cb0c79", url="https://pypi.org/packages/86/4c/01c7416f61025ed5b973f2e68eb828a6d3b670ac6f11964336b79b2df631/pyobjc_framework_AdSupport-8.5.1-py2.py3-none-any.whl")
    version("8.5", sha256="fe562dc1ff04e73c4cf5995f5ba959410b3772743dc63425849572886229b384", url="https://pypi.org/packages/9e/93/19ff6ce39851f966ec526ccf09a43f104072b27a698f4b5b43df04e8ff94/pyobjc_framework_AdSupport-8.5-py2.py3-none-any.whl")

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

