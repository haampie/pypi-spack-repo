# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyOnnx(PythonPackage):
    # BEGIN VERSIONS
    version("1.15.0", sha256="b18461a7d38f286618ca2a6e78062a2a9c634ce498e631e708a8041b00094825", url="https://pypi.org/packages/f4/6e/2b2963f9e3a7201c8c3a30656f9c81bc9d32d198a88a747456ab2874166a/onnx-1.15.0.tar.gz")
    version("1.13.1", sha256="0bdcc25c2c1ce4a8750e4ffbd93ae945442e7fac6e51176f38e366b74a97dfd9", url="https://pypi.org/packages/56/b5/f5889d518276061f999d7cda5714f288b1718cbbc3f538e943822626eead/onnx-1.13.1.tar.gz")
    version("1.13.0", sha256="410b39950367857f97b65093681fe2495a2e23d63777a8aceaf96c56a16d166e", url="https://pypi.org/packages/6c/f6/215ba9e8d2587755df363170e3be54892b087bad0a99935fe456f7555255/onnx-1.13.0.tar.gz")
    version("1.12.0", sha256="13b3e77d27523b9dbf4f30dfc9c959455859d5e34e921c44f712d69b8369eff9", url="https://pypi.org/packages/2c/6a/39b0580858589a67c3322aabc2634f158391ffbf98fa410127533e7f1495/onnx-1.12.0.tar.gz")
    version("1.11.0", sha256="eca224c7c2c8ee4072a0743e4898a84a9bdf8297b5e5910a2632e4c4182ffb2a", url="https://pypi.org/packages/fd/b7/fccddff4d1873074605ff08acc812202b4a849cf4925b1f6ed5eeba575c4/onnx-1.11.0.tar.gz")
    version("1.10.1", sha256="9d941ba76cab55db8913ecad9dc50cefeb368460f6338a91783a5d7643f3a044", url="https://pypi.org/packages/18/ec/d1d74c6355a139a633d1335620e6d891e3a3556889b3d0ede878ab53fc11/onnx-1.10.1.tar.gz")
    version("1.8.1", sha256="9d65c52009a90499f8c25fdfe5acda3ac88efe0788eb1d5f2575a989277145fb", url="https://pypi.org/packages/2b/8d/c924f54e19ec71543c18658d86e8337579d5a784bd524b7f18e2e2cd6f17/onnx-1.8.1.tar.gz")
    version("1.6.0", sha256="3b88c3fe521151651a0403c4d131cb2e0311bd28b753ef692020a432a81ce345", url="https://pypi.org/packages/81/a9/a14c3bc32908c37b46b19a89eb6185b0c90fd9c03ef12379d51940b8fc71/onnx-1.6.0.tar.gz")
    version("1.5.0", sha256="1a584a4ef62a6db178c257fffb06a9d8e61b41c0a80bfd8bcd8a253d72c4b0b4", url="https://pypi.org/packages/1a/a7/a7aecbfe51f01f754b579ab3fbefaa53f03abdd8cc205cc9b0996089df34/onnx-1.5.0.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-numpy", when="@1.6:1.7,1.15")
        depends_on("py-protobuf@3.20.2:", when="@1.15:")
        depends_on("py-protobuf", when="@1.6:1.7")
        depends_on("py-six", when="@1.6:1.7")
        depends_on("py-typing-extensions@3.6.2.1:", when="@1.6:1.7")
    # END DEPENDENCIES

