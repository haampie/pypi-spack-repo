##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPyobjcFrameworkUsernotificationsui(PythonPackage):
    version("10.2", sha256="b0909b11655a7ae14e54ba6f80f1c6d34d46de5e8b565d0a51c22f87604ad3d3", url="https://pypi.org/packages/9e/11/facf4e8c84a65c16f04a7c6fbdd4bf4d30889b5c174c7a17f6904387fd3b/pyobjc_framework_UserNotificationsUI-10.2-py2.py3-none-any.whl")
    version("10.1", sha256="6640c6d04f459b6927096696dac98ce5fcb702a507a757d6d1b909b341bb8a0d", url="https://pypi.org/packages/bb/3e/09f634b82f7e6ca935b2bb201e0b6646e698c45a93ce1f10f26a8eef1009/pyobjc_framework_UserNotificationsUI-10.1-py2.py3-none-any.whl")
    version("10.0", sha256="3732661248a507a61ec551846b5f03d136d719ee402a434f9e77cee044983d75", url="https://pypi.org/packages/2b/b0/901d5933879732b9cc4f6ffcb40b73a64acae2ea3b301278cdda5b07ebe0/pyobjc_framework_UserNotificationsUI-10.0-py2.py3-none-any.whl")
    version("9.2", sha256="8dede553a3aebf4c5d5ea86537120ad8f65071bcbd20a0ecb127e06643596bef", url="https://pypi.org/packages/4d/90/96954c855c098ea33df1f0b2a65a45054644e8816c9b5d16f3ac691f924c/pyobjc_framework_UserNotificationsUI-9.2-py2.py3-none-any.whl")
    version("9.1.1", sha256="dca9926267cdb0dd06389bec894bc5e6a16efe948f7a194d71cfe6103bbb9f3d", url="https://pypi.org/packages/9b/e7/6cbcf14f5dcf6101cf172de9f06ed3f653366ccd7e32529f3fe03be25eaf/pyobjc_framework_UserNotificationsUI-9.1.1-py2.py3-none-any.whl")
    version("9.1", sha256="8fb0a19f03ef59d6cd24e8900c86a47bb0a568e7c472148a32b8e41f208af8e1", url="https://pypi.org/packages/9a/c2/3c52b26ae404cd6d58d1e9389aa2af91ac64743b9743ddb516ee67dda0b1/pyobjc_framework_UserNotificationsUI-9.1-py2.py3-none-any.whl")
    version("9.0.1", sha256="6fb9f16e74893fde59bd2323cfd24764acc74a5fa3652c79b52aea4e62896b65", url="https://pypi.org/packages/fd/a2/bc2b3f25b581ddf533c62afd260d91e3dfb0007f5b0c62e4239211302968/pyobjc_framework_UserNotificationsUI-9.0.1-py2.py3-none-any.whl")
    version("9.0", sha256="6aa5745983c8414c44f48cd30bc5437206f92170cb482368d5341651ca06f299", url="https://pypi.org/packages/a0/e8/8c27a57011438372bbc71a05c04823e1460b3fb9c7e867bd4dc26b9d7d7e/pyobjc_framework_UserNotificationsUI-9.0-py2.py3-none-any.whl")
    version("8.5.1", sha256="4c73307f376656b282f50cab56642a60165b0671a7d9cc640f07f617db92c0b7", url="https://pypi.org/packages/7f/53/129300067f8ee3595a92160d6106c34ab09a89b2997ab9378c9815540357/pyobjc_framework_UserNotificationsUI-8.5.1-py2.py3-none-any.whl")
    version("8.5", sha256="41b65dae32691b0aea32ba4f27dd73756cc4254117a438447f20984134787750", url="https://pypi.org/packages/ff/7c/e12faa24bd1fac5485bbe35c15e28b771f313bae7bffc785b96c2024138c/pyobjc_framework_UserNotificationsUI-8.5-py2.py3-none-any.whl")

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
        depends_on("py-pyobjc-framework-usernotifications@10.2:", when="@10.2:")
        depends_on("py-pyobjc-framework-usernotifications@10.1:", when="@10.1")
        depends_on("py-pyobjc-framework-usernotifications@10:", when="@10:10.0")
        depends_on("py-pyobjc-framework-usernotifications@9.2:", when="@9.2:9")
        depends_on("py-pyobjc-framework-usernotifications@9.1.1:", when="@9.1.1:9.1")
        depends_on("py-pyobjc-framework-usernotifications@9.1:", when="@9.1:9.1.0")
        depends_on("py-pyobjc-framework-usernotifications@9.0.1:", when="@9.0.1:9.0")
        depends_on("py-pyobjc-framework-usernotifications@9:", when="@9:9.0.0")
        depends_on("py-pyobjc-framework-usernotifications@8.5.1:", when="@8.5.1:8")
        depends_on("py-pyobjc-framework-usernotifications@8.5:", when="@8.5:8.5.0")

