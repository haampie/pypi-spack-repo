# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPyobjcFrameworkModelio(PythonPackage):
    # BEGIN VERSIONS
    version("10.2", sha256="8ae1444375260a346d1c77838f84e2c04dfabaf2769b2970a3588becb670431e", url="https://pypi.org/packages/2e/bf/b3def866d117da921fc64eb15d94dc949da497f60c6f9b22cc3628ec9b6b/pyobjc-framework-ModelIO-10.2.tar.gz")
    version("10.1", sha256="75fe5405165264a5059c16bfd492593e3becba50811a47dedbfc699ff73d4bfb", url="https://pypi.org/packages/db/a4/9f6dcce71c7de1ee97e6b2feecc90e5c64fcd237ffd250d0f6692641df8c/pyobjc-framework-ModelIO-10.1.tar.gz")
    version("10.0", sha256="1629db056d3bebdd79c582637e48c9da5c5aa76a073439dcb3820e00e3f75227", url="https://pypi.org/packages/79/4e/82b19c9c91e1a49d236c48d17b369cc037f047066a125bc9fe8df2090014/pyobjc-framework-ModelIO-10.0.tar.gz")
    version("9.2", sha256="8a5752c4d23997c2c82f9567da4c9616f54b961269ab79f0aff47287cc0c386a", url="https://pypi.org/packages/2e/ff/9a38dcb560e3323d81a14308b3fcd198b8bf3b292a1c1896c6bcf92a4237/pyobjc-framework-ModelIO-9.2.tar.gz")
    version("9.1.1", sha256="398a3c6ca82ac08b4b5cb63fb6e362269bd18a28fc0b3b2528846cc8b6777fed", url="https://pypi.org/packages/d1/eb/6fcea4efa21f6cfa6e984ee8b52188c4f95667ab1e25bd681b4711b195b0/pyobjc-framework-ModelIO-9.1.1.tar.gz")
    version("9.1", sha256="9aaf8f3c038a4d5a8bfba33618556795dac7ca6cfd6d3747528b59008e30767f", url="https://pypi.org/packages/ac/55/ec36d4a8665e59e9aba5bc3e7768474067437f4a77398a7abbc5220e44f5/pyobjc-framework-ModelIO-9.1.tar.gz")
    version("9.0.1", sha256="3ab77928b28497bcd1fd4b17bf32fb9b16dbe385344c2ed33ea259770c6b2709", url="https://pypi.org/packages/3c/a1/cd81d38f32fa49b78ea3d48bd6d9b187193ed662b9299ff9cec37fdb88d4/pyobjc-framework-ModelIO-9.0.1.tar.gz")
    version("9.0", sha256="af7c689ee63a09c146d610e08e90969fce9b578bbbc6059380a341e2b5e7b5e5", url="https://pypi.org/packages/51/1a/442c6c2be3dd7b0ee7d7ff67ed7018c88f1b773599616432e0a24f843e11/pyobjc-framework-ModelIO-9.0.tar.gz")
    version("8.5.1", sha256="1d38fc43a65f0f248eb2480973ccd2608cec1c92527baccbcd62bdd34a45e56e", url="https://pypi.org/packages/4c/fc/01752d7cad0373ede575169c37f70524d3610e5db022f0ee8a831ab04099/pyobjc-framework-ModelIO-8.5.1.tar.gz")
    version("8.5", sha256="9db7f7992f71ecdef3b03a0006d4988fc661dde0fe049c04d9c6a8e040d3af4d", url="https://pypi.org/packages/d0/7d/599d4c0ce9a730c81dde4415a66672fbefc517e123562492572fa9a53999/pyobjc-framework-ModelIO-8.5.tar.gz")
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
        depends_on("py-pyobjc-framework-quartz@10.2:", when="@10.2:")
        depends_on("py-pyobjc-framework-quartz@10.1:", when="@10.1")
        depends_on("py-pyobjc-framework-quartz@10:", when="@10:10.0")
    # END DEPENDENCIES

