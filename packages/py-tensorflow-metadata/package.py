##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyTensorflowMetadata(PythonPackage):
    version("1.14.0", sha256="5ff79bf96f98c800fc08270b852663afe7e74d7e1f92b50ba1487bfc63894cdb", url="https://pypi.org/packages/41/23/3705c7139886c079ef4c0e3be56a5a1fb90e9ee413a4b7caaee0ee0ea6fe/tensorflow_metadata-1.14.0-py3-none-any.whl")
    version("1.13.1", sha256="8abdead4cae3d7258f815d9f63a146ae1e31853ac07ba271db0ea9dfb0a6b317", url="https://pypi.org/packages/6e/b7/41ed520712c659dee0653dbd1ae71ed991bc51c7622e3e4dafbbf208faaa/tensorflow_metadata-1.13.1-py3-none-any.whl")
    version("1.13.0", sha256="d79ef85bcb5cfc8a7b860573f5f81618fba11a43f04c56d608ec1fb86a3452c2", url="https://pypi.org/packages/1d/7a/29b68133e47b46c960d3bcdfdc3bc9e479303d0ce827867006908c2320c1/tensorflow_metadata-1.13.0-py3-none-any.whl")
    version("1.12.0", sha256="4b86df305e5c8252df4c99a25074958f3772db57276fa6bd6a4d14fe482d8bc9", url="https://pypi.org/packages/7e/cb/1a1dd9e8495d3932c056120127d18695bca50c2f754013b6bf0d51557c47/tensorflow_metadata-1.12.0-py3-none-any.whl")
    version("1.11.0", sha256="76894d9804abab98b3cff324406b06d502cc2b8661fe7d23d12360280cc528d0", url="https://pypi.org/packages/6f/f2/6ccc170dce02d80a52879107dec9ec5d5155cba98316e1d70495c894833d/tensorflow_metadata-1.11.0-py3-none-any.whl")
    version("1.10.0", sha256="e3ff528496105c0d73b2a402877525b1695635378fbe5c1b47ac7b3780816bb3", url="https://pypi.org/packages/3a/86/2b3251bb560068f31817d9b678588098e28f396c1f6b88c57cf5d28670af/tensorflow_metadata-1.10.0-py3-none-any.whl")
    version("1.9.0", sha256="a147801b1d91debdea81940a78221af10940f0174529d48075c774a9b46f86d5", url="https://pypi.org/packages/22/42/6ebb03aef0cb37f2ea98f1bf04ed21450fec73941e8421ba3fa37f94ffaf/tensorflow_metadata-1.9.0-py3-none-any.whl")
    version("1.8.0", sha256="65c47207efeaff6b514196d2d420dbb7762f0a07336e1798731f90c81541ab11", url="https://pypi.org/packages/20/e7/b4dcc898ca1c250ff1f1e431a3fdd2b347663283e8aea282704d59e92ad9/tensorflow_metadata-1.8.0-py3-none-any.whl")
    version("1.7.0", sha256="d05600bf0f42371d3ebf12e4a431a16836c039918d24c4b9634235c9b8fc686a", url="https://pypi.org/packages/ed/c4/e4fa9d2725eff8eeed00f2c959d1cbb0a7f027f46ea36b9987b99d4e0d8c/tensorflow_metadata-1.7.0-py3-none-any.whl")
    version("1.6.0", sha256="44ef4279a83d13ff59557edb477edb4abc2a32b3c33188f5aa8061494d28594c", url="https://pypi.org/packages/c7/4d/c1a509ea79857e5f4da30acbe6bf55294a24ad7388ab2842ba68192ca69c/tensorflow_metadata-1.6.0-py3-none-any.whl")
    version("1.5.0", sha256="982aa5715a306c5fcce0817da49ad0892f5d977db37e1811c34013ba4da06207", url="https://pypi.org/packages/81/e6/193d9637b844f88797199fced0e3baa893dd110bdca34b5708b49120ae30/tensorflow_metadata-1.5.0-py3-none-any.whl")

    with default_args(type="run"):
        depends_on("py-absl-py@0.9:1", when="@1.6:")
        depends_on("py-absl-py@0.9:0.12", when="@0.29:1.5")
        depends_on("py-googleapis-common-protos@1.52:", when="@0.24:")
        depends_on("py-protobuf@3.20.3:4.0", when="@1.14:")
        depends_on("py-protobuf@3.20.3:4", when="@1.13.1:1.13")
        depends_on("py-protobuf@3.13.0:3", when="@1.1:1.13.0")

