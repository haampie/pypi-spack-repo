# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPyobjcFrameworkCallkit(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("10.2", sha256="f3f26c877743a340718e0647ccee4604f9d87aa8ad5c3268c794d94f6f9246ee", url="https://pypi.org/packages/e0/fd/23c66b686280caa062c399cfc8d371e1f57f4625e77f7cd6d16abad5c13d/pyobjc_framework_CallKit-10.2-py2.py3-none-any.whl")
    version("10.1", sha256="f82e791b2dbae4adfcc596949975573309a0127ba02d4c35743501f6665ec610", url="https://pypi.org/packages/d1/20/5e81811ba046920563facdceb0a4f26ce7b5f57783b7cef7829d3fc30c7e/pyobjc_framework_CallKit-10.1-py2.py3-none-any.whl")
    version("10.0", sha256="3c431115a3d3c826268a9c4272c0b261e5a15206e9468915a859cde52f32d190", url="https://pypi.org/packages/ee/be/250854d5a51ca461f594d178b2e1ceba0e6af64a3ef0a5e7aca67e6662de/pyobjc_framework_CallKit-10.0-py2.py3-none-any.whl")
    version("9.2", sha256="b76c92e34e0c43244fc40e84fc2c8d0df718770aea19a993775e59ead9bbb073", url="https://pypi.org/packages/60/af/f88718068b6e5907a9b37b86f675983fc1d7222c6cb546218a624a136d6c/pyobjc_framework_CallKit-9.2-py2.py3-none-any.whl")
    version("9.1.1", sha256="b942a3473b4494dd2d678fc57bbc4eac4e0729f011cd456ea791b27a3471835c", url="https://pypi.org/packages/9a/bb/c9b33fffbed33c57f7bbc56b4b35aacbe97fd993592c144a7ce4a2413420/pyobjc_framework_CallKit-9.1.1-py2.py3-none-any.whl")
    version("9.1", sha256="c9f01da84f5121651f2ec126f2bd35b39f0adaa08fd4e9336c1ca66c74b92538", url="https://pypi.org/packages/03/6a/6ea706793f28e249c82253a0bebd1aa1c348ff864c2dba2a576dc1b07395/pyobjc_framework_CallKit-9.1-py2.py3-none-any.whl")
    version("9.0.1", sha256="b80104ef5d94b5f7545ff378a7f1e67afcd248cff37a1cf4490e6e24817c7103", url="https://pypi.org/packages/ec/36/d2b1d5781217e53592d592256b20b53f97fc211102569efb6344024b35f8/pyobjc_framework_CallKit-9.0.1-py2.py3-none-any.whl")
    version("9.0", sha256="b7bf0fa1fd4a36d324240de5ab868a61d936ae776f487faa48f51a51181e1c68", url="https://pypi.org/packages/8f/fc/4dd4bb8c26d8caaaff8a85ad08537c968451a68e24532c7f23510ad6d324/pyobjc_framework_CallKit-9.0-py2.py3-none-any.whl")
    version("8.5.1", sha256="cc28ac314c97f0bc1c233baf7c81c6566c72ddd03c32476d0cda5d512338f187", url="https://pypi.org/packages/98/65/5cc8f7ce012fabf6fe12c1da31569962f4540e91c28bf912c4b5a7e49346/pyobjc_framework_CallKit-8.5.1-py2.py3-none-any.whl")
    version("8.5", sha256="f3cccdb264aac23b9241c838c09b8a4e3ec3ebc1c8d76eb2b7a18d0a21dcc23c", url="https://pypi.org/packages/5b/37/301f43748cf497c9085596c9c9a7ce3b0de5e92f721419cac0ef0180cefc/pyobjc_framework_CallKit-8.5-py2.py3-none-any.whl")
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
    # END DEPENDENCIES

