##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPyobjcFrameworkLocalauthenticationembeddedui(PythonPackage):
    version("10.2", sha256="eafbbc321082ff012cdb14e38abae7ced94c6d962cb64af43d6d515da976e175", url="https://pypi.org/packages/19/16/b0f47c5ee7e4fc102fcfc58679a2f156982682b431af5f8d22657c4f90ea/pyobjc_framework_LocalAuthenticationEmbeddedUI-10.2-py2.py3-none-any.whl")
    version("10.1", sha256="a8e8101ca74441a862ffb8e2309fe382789c759d0951fb7b7b4e46652b4cb068", url="https://pypi.org/packages/37/c4/9e92c02bb511255158209f6367c403a5dde20e4763414726b186c3ba2319/pyobjc_framework_LocalAuthenticationEmbeddedUI-10.1-py2.py3-none-any.whl")
    version("10.0", sha256="136725e321929fd840905751adf158b4bba561951984ec75a4e534ef0be76c30", url="https://pypi.org/packages/85/e7/936eebeead13b07f84a9c10eae70d8c953286bdbd03f2841acdef53c1a88/pyobjc_framework_LocalAuthenticationEmbeddedUI-10.0-py2.py3-none-any.whl")
    version("9.2", sha256="f1ac1b35393e826f5eda00a8065207f9689470579b7d3eb25a4f478bd758bf3f", url="https://pypi.org/packages/cc/12/6997716b3f3ddf86ef17f54e313e558bf74d4359b4fa8e2be782b3f7219c/pyobjc_framework_LocalAuthenticationEmbeddedUI-9.2-py2.py3-none-any.whl")
    version("9.1.1", sha256="85883c615ea71674c5df61df071a7eebdd6db8f27c7898bd339b24bce4311632", url="https://pypi.org/packages/e3/ef/c6c5c9a3a27c21c2a52b319078292746013ebf37dd299cab2ca44d10eef1/pyobjc_framework_LocalAuthenticationEmbeddedUI-9.1.1-py2.py3-none-any.whl")
    version("9.1", sha256="5dce3c83687d1e8c85532138cecd101165c511bc28470d9397edd57b6784553e", url="https://pypi.org/packages/09/59/d0ff6b994c93372868ed580b30d8245c5ccd3a5ffee2406bf1e6dc3ba38c/pyobjc_framework_LocalAuthenticationEmbeddedUI-9.1-py2.py3-none-any.whl")
    version("9.0.1", sha256="ed8e3ee8330ae973d76297b37476358e45b0e8e47129c2839a52e3393e9ccd79", url="https://pypi.org/packages/10/3a/aa7af2f351e533663e1de147d9e046dfecd66f21e81545ae6795a56f20b4/pyobjc_framework_LocalAuthenticationEmbeddedUI-9.0.1-py2.py3-none-any.whl")
    version("9.0", sha256="9d1ea04cb4a22eacb98713a517f5db760b1b7ea82fcbfa13f10140f751ca9d46", url="https://pypi.org/packages/a8/f2/8752ff1b125f312b13f607fb3d26b5e07d58a793a8a7c9b37d526ef76ed0/pyobjc_framework_LocalAuthenticationEmbeddedUI-9.0-py2.py3-none-any.whl")
    version("8.5.1", sha256="4a829f05f2c089cfb4e6435548d700dc2fdabbd5fd71d2daff83f4e8cda1b870", url="https://pypi.org/packages/f5/de/7fe5df187df2277db357602241f0f5ce0bd0b8ced38391c3667814bd4124/pyobjc_framework_LocalAuthenticationEmbeddedUI-8.5.1-py2.py3-none-any.whl")
    version("8.5", sha256="168ea2e0c0871393734459169f289103c608d137140e7a24637745d47aca6b73", url="https://pypi.org/packages/30/38/d1e38bfea6a05f0fd089401a32a94960fe18d5fe6c312cec48d2369d837a/pyobjc_framework_LocalAuthenticationEmbeddedUI-8.5-py2.py3-none-any.whl")

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
        depends_on("py-pyobjc-framework-localauthentication@10.2:", when="@10.2:")
        depends_on("py-pyobjc-framework-localauthentication@10.1:", when="@10.1")
        depends_on("py-pyobjc-framework-localauthentication@10:", when="@10:10.0")
        depends_on("py-pyobjc-framework-localauthentication@9.2:", when="@9.2:9")
        depends_on("py-pyobjc-framework-localauthentication@9.1.1:", when="@9.1.1:9.1")
        depends_on("py-pyobjc-framework-localauthentication@9.1:", when="@9.1:9.1.0")
        depends_on("py-pyobjc-framework-localauthentication@9.0.1:", when="@9.0.1:9.0")
        depends_on("py-pyobjc-framework-localauthentication@9:", when="@9:9.0.0")
        depends_on("py-pyobjc-framework-localauthentication@8.5.1:", when="@8.5.1:8")
        depends_on("py-pyobjc-framework-localauthentication@8.5:", when="@8.5:8.5.0")

