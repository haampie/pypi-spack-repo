# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyOnnxconverterCommon(PythonPackage):
    # BEGIN VERSIONS
    version("1.14.0", sha256="9723e4a9b47f283e298605dce9f357d5ebd5e5e70172fca26e282a1b490916c4", url="https://pypi.org/packages/6d/6a/9ed9fd4da34cb41fda35bc5cc9e990c605689db7de63ed84fedbca5a77f6/onnxconverter_common-1.14.0-py2.py3-none-any.whl")
    version("1.13.0", sha256="5ee1c025ef6c3b4abaede8425bc6b393248941a6cf8c21563d0d0e3f04634a0a", url="https://pypi.org/packages/51/a4/4439174c879c33557eab08e4dd480c1e096bc26c487c85a62e4c0d8f78ff/onnxconverter_common-1.13.0-py2.py3-none-any.whl")
    version("1.12.2", sha256="29b7caade27aeda1b827232554cec352db8afc6e16c3e3ea8c4264449f9ff3a6", url="https://pypi.org/packages/c5/59/63a053e30e9f8bdaefbd6628fb71b7c705a76e5ce528599f431078ae84d9/onnxconverter_common-1.12.2-py2.py3-none-any.whl")
    version("1.12.1", sha256="4c6d552f134f48a49eafb2f0ab06a1d2dd27c174b2b0c249e2d6f349e7e22feb", url="https://pypi.org/packages/11/30/c58e8d46976f8049e9a820f723efc9a983da0d9a4d73fe28a6cd33631739/onnxconverter_common-1.12.1-py2.py3-none-any.whl")
    version("1.12", sha256="b0585e87718d6265dfd58a9c57b4ecf7f4acae6818728fee063ce8672b6848f8", url="https://pypi.org/packages/5d/6c/2c306831df14340e5fec4117d49c3c1a142765afa47ae6d5e8bd4f67982f/onnxconverter_common-1.12-py2.py3-none-any.whl")
    version("1.9.0", sha256="02b58ca3351fba4eddf8503e1421cfecd4ddcf2074aea4d58e3b2410e6f67ce5", url="https://pypi.org/packages/cc/51/de4e3d84282a6649f4fb73c29b33d96ac1b5e6d30217ed0fff74cc404467/onnxconverter_common-1.9.0-py2.py3-none-any.whl")
    version("1.8.1", sha256="cea0c17a79446640d4523494ff0ac3e5043e65da6dea1e5c82949a65c84ab461", url="https://pypi.org/packages/42/f5/82c29029a643dd4de8e0374fe2d5831f50ca58623dd1ee41e0b8df8a7d71/onnxconverter_common-1.8.1-py2.py3-none-any.whl")
    version("1.8.0", sha256="8aa440190a98997a851236b3fc8b5148a9043a63df9dd4ecafa7606acf843ffa", url="https://pypi.org/packages/c4/5b/e4b49fec47a4219251fb7dd74e88f620825df2678e0f812c38f68b923e2e/onnxconverter-common-1.8.0.tar.gz")
    version("1.7.0", sha256="6d371047186aa6bd419d4a5de7155d0d4aa5d24925af2ffe69069218d9eeeed5", url="https://pypi.org/packages/fe/7a/7e30c643cd7d2ad87689188ef34ce93e657bd14da3605f87bcdbc19cd5b1/onnxconverter_common-1.7.0-py2.py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-numpy", when="@:1.7,1.8.1:")
        depends_on("py-onnx", when="@:1.7,1.8.1:")
        depends_on("py-packaging", when="@1.13:")
        depends_on("py-protobuf@3.20.2", when="@1.14:")
        depends_on("py-protobuf", when="@:1.7,1.8.1:1.13")
    # END DEPENDENCIES

