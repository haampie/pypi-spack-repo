# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPyobjcFrameworkCoreaudio(PythonPackage):
    # BEGIN VERSIONS
    version("10.2", sha256="5e97ae7a65be85aee83aef004b31146c5fbf28325d870362959f7312b303fb67", url="https://pypi.org/packages/df/a8/9a2645bfe7ab310f39a35605911ef1a04a9b8a5224e58244c8edda3e2731/pyobjc-framework-CoreAudio-10.2.tar.gz")
    version("10.1", sha256="713ca82fc363ea6cf373d2db0b183f39058bcadceb8229d9e8839b783104f8e2", url="https://pypi.org/packages/dd/e3/b53c3a20b328319f842ba098fda952038dcf8f64bd95c01bbcbc7ba94d3c/pyobjc-framework-CoreAudio-10.1.tar.gz")
    version("10.0", sha256="6042e9fea80bf5c23a8a3a4a2888243b7152316275ab863ed6bc289eabdef9f1", url="https://pypi.org/packages/94/ac/f1dfe39ee82279b034f52e7bbe1aca3735d0a998ca895e0e7cf2802464f3/pyobjc-framework-CoreAudio-10.0.tar.gz")
    version("9.2", sha256="7b8e32e073b04896850c971a9e4c5afaf9f3343b8e525bb23f50a360c587cf87", url="https://pypi.org/packages/51/43/d15c986e635066db113bd6a1f6d99857bd88ac46bf70f619b2cdff8362f3/pyobjc-framework-CoreAudio-9.2.tar.gz")
    version("9.1.1", sha256="bb825b6f176a2cf6f3159f8bc6e778da8de59951fd4dad1d945334d6462fd691", url="https://pypi.org/packages/0e/38/a05dd8056d92882666090c16d3e7dd534eca749fa6bf8d7eb18a331de10a/pyobjc-framework-CoreAudio-9.1.1.tar.gz")
    version("9.1", sha256="7d00eb0cf9ba6ac56dc0344ed84cba9b2ff1189b4b22d8a6418d9512e215e383", url="https://pypi.org/packages/ed/15/64b728927fcfea06b69829736311c32c8f992352106457827d41f3f73cfb/pyobjc-framework-CoreAudio-9.1.tar.gz")
    version("9.0.1", sha256="f02a1d61296b38d82477cbcbb2ddd4e8585e88b0dabbf8655450690c1bfb7254", url="https://pypi.org/packages/c2/e3/866427f60b7e093afbbc3acbc72c0adbc92128b835868ca6d472af6e96eb/pyobjc-framework-CoreAudio-9.0.1.tar.gz")
    version("9.0", sha256="77430c9117f5710369ce6b15812a969f6cdf561867db52175acd5b29720c9843", url="https://pypi.org/packages/7a/e3/0158176de6329f01a95ce7576956d027e6d85b50f9b5922f8b02f51e4b92/pyobjc-framework-CoreAudio-9.0.tar.gz")
    version("8.5.1", sha256="6dd76697c8ae018a0bbf7eadf26b05ec6da3f2865107a83bfd46d2e7fc557da1", url="https://pypi.org/packages/92/85/9b2b0d264fb97e074eb8fdc0d2c1d52d168faa1345a371a0c0d268a0525b/pyobjc-framework-CoreAudio-8.5.1.tar.gz")
    version("8.5", sha256="2ffe0b6ec3404e092b61ff4a54fe7aebdac2f4c470b215e32596823a361910f3", url="https://pypi.org/packages/15/07/31df7063dbc5a750ba253e51be6fbfa585a0cd2029fbadef053adb10f5cd/pyobjc-framework-CoreAudio-8.5.tar.gz")
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

