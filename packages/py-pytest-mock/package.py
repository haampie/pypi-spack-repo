# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPytestMock(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("3.12.0", sha256="0972719a7263072da3a21c7f4773069bcc7486027d7e8e1f81d98a47e701bc4f", url="https://pypi.org/packages/b9/25/b29fd10dd062cf41e66787a7951b3842881a2a2d7e3a41fcbb58a8466046/pytest_mock-3.12.0-py3-none-any.whl")
    version("3.11.1", sha256="21c279fff83d70763b05f8874cc9cfb3fcacd6d354247a976f9529d19f9acf39", url="https://pypi.org/packages/da/85/80ae98e019a429445bfb74e153d4cb47c3695e3e908515e95e95c18237e5/pytest_mock-3.11.1-py3-none-any.whl")
    version("3.11.0", sha256="9f732204aff799161cea6f818366bd254b41dbdfb6fd8fee4e04d332aba011d4", url="https://pypi.org/packages/a6/cf/9e166752dc2ed70ee865eb6f6eeb1cbe02d4ff3d9aafc2ce9c328d994fbb/pytest_mock-3.11.0-py3-none-any.whl")
    version("3.10.0", sha256="f4c973eeae0282963eb293eb173ce91b091a79c1334455acfac9ddee8a1c784b", url="https://pypi.org/packages/91/84/c951790e199cd54ddbf1021965b62a5415b81193ebdb4f4af2659fd06a73/pytest_mock-3.10.0-py3-none-any.whl")
    version("3.9.0", sha256="1a1b9264224d026932d6685a0f9cef3b61d91563c3e74af9fe5afb2767e13812", url="https://pypi.org/packages/e2/d7/a8e6c7bcd5f896eecf13446dfb46b73f3493ac5592fa8564e118a0923020/pytest_mock-3.9.0-py3-none-any.whl")
    version("3.8.2", sha256="8a9e226d6c0ef09fcf20c94eb3405c388af438a90f3e39687f84166da82d5948", url="https://pypi.org/packages/64/ec/e21d6a5c31df566847de2dc7e7c1870c67cf10cb97cb0a1ea0e389446e60/pytest_mock-3.8.2-py3-none-any.whl")
    version("3.8.1", sha256="d989f11ca4a84479e288b0cd1e6769d6ad0d3d7743dcc75e460d1416a5f2135a", url="https://pypi.org/packages/c3/ab/76e3a40f0faea13806d0ac8e69b3903cfb7d76e49905a259c0465470963f/pytest_mock-3.8.1-py3-none-any.whl")
    version("3.8.0", sha256="537c6da22e2a2a4622d5f4056abfd6e7e88a953b8e4db4c027f091601a562365", url="https://pypi.org/packages/a5/85/a666c7993840ffb2027daccf9b7f2488dc0162797c9147d7cbcdc0562db7/pytest_mock-3.8.0-py3-none-any.whl")
    version("3.7.0", sha256="6cff27cec936bf81dc5ee87f07132b807bcda51106b5ec4b90a04331cba76231", url="https://pypi.org/packages/11/40/8fcb3c0f72e11dc44e1102b2adf5f160b8a00e84d915798c60aabcd9257a/pytest_mock-3.7.0-py3-none-any.whl")
    version("3.6.1", sha256="30c2f2cc9759e76eee674b81ea28c9f0b94f8f0445a1b87762cadf774f0df7e3", url="https://pypi.org/packages/fd/be/ce7e79a7bf68ff6630f662f58a8dc68e2a602d8649a1c0e05c8e6b9a2177/pytest_mock-3.6.1-py3-none-any.whl")
    version("1.11.1", sha256="34520283d459cdf1d0dbb58a132df804697f1b966ecedf808bbf3d255af8f659", url="https://pypi.org/packages/ca/04/c530b2e4d61f99c524dcac0a9002563955370622f70fe4771cd4e56e217b/pytest_mock-1.11.1-py2.py3-none-any.whl")
    version("1.2", sha256="2911668c5ea518a07e2da53a170e2f86eaccf1245ec9605c37eadf6578dec468", url="https://pypi.org/packages/6a/40/d5f2fbef42f85b8c53ddb2bb1db847ef46c86e6204abfeaa605b3ed07307/pytest_mock-1.2-py2.py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-pytest@5:", when="@3.3:")
        depends_on("py-pytest@2.7:", when="@1.6.1,1.6.3:3.2")
    # END DEPENDENCIES

