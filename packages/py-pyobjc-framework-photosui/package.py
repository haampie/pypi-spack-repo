# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPyobjcFrameworkPhotosui(PythonPackage):
    # BEGIN VERSIONS
    version("10.2", sha256="d0bbcae82b4cc652bb60d3221c557cc19be62ff430575ec8e6d233beb936f73b", url="https://pypi.org/packages/f5/ad/d727d4eca6a4222f50bb1fb706ec3bb6977b315d929dd889365277cd8c27/pyobjc-framework-PhotosUI-10.2.tar.gz")
    version("10.1", sha256="4b90755c6c62a0668782cf05d92fca6277485f2cb3473981760c0dc0e40de1d8", url="https://pypi.org/packages/96/89/1c03f20542731769d1dd549744246ff07a2345bbfcbd09da4aedab04b698/pyobjc-framework-PhotosUI-10.1.tar.gz")
    version("10.0", sha256="aa521325e7c86d1c739306cd5a14f3f7f69f5db654dc8884f1630001ad72aa7c", url="https://pypi.org/packages/cc/35/8f822d54d133e78ac5b5b47de425d42c922e6f527699e739e680d6dc3324/pyobjc-framework-PhotosUI-10.0.tar.gz")
    version("9.2", sha256="8006112e9aaafd4517ec1d6fb36eb5b0d4bd0d92db410b11c1772d7d664cfb04", url="https://pypi.org/packages/24/aa/d53fa6451864bce4b759f0d6a8bff469e39ab7744d6194bffa7203af0d8e/pyobjc-framework-PhotosUI-9.2.tar.gz")
    version("9.1.1", sha256="a008450e11c9276debcdc050110d3412fd917650997edb23c1da0a9b6a7f5e2a", url="https://pypi.org/packages/c4/43/e6f64336515df3082f5104df46ce437cf04e722b0022f6233df1958335e8/pyobjc-framework-PhotosUI-9.1.1.tar.gz")
    version("9.1", sha256="54e2217374e10ab79532d212a68d2879813bb19f7dfc3016454cf038dad3e40d", url="https://pypi.org/packages/93/7f/2aed05093f9fc26cbe79d4732468df51ba18e7a7e5584ae09ca6766da8dc/pyobjc-framework-PhotosUI-9.1.tar.gz")
    version("9.0.1", sha256="9fe98cb87dc2547612ae339f7d239c62eec7736e0cc24de2bb572adb3c5df2a8", url="https://pypi.org/packages/0c/37/059038329c09403dacb11c3790512df6e5ea4a6e326c33fd76dec016d1a2/pyobjc-framework-PhotosUI-9.0.1.tar.gz")
    version("9.0", sha256="235fa1bcafe062bb1b6fe6bbd507387931cf11d2fa91dd48a643ffc53a8e257d", url="https://pypi.org/packages/f7/be/b11c9365d360b2199fda62f479dacde1bc75792d366473cd41d12bec4903/pyobjc-framework-PhotosUI-9.0.tar.gz")
    version("8.5.1", sha256="b33e3282c42df70c929153221e5361817f95542f19d561843f7bd57550dd1fe5", url="https://pypi.org/packages/ae/d6/52af982a08f776253a3b96e79cc7ec3173d2041c10001dab5daf107e87d2/pyobjc-framework-PhotosUI-8.5.1.tar.gz")
    version("8.5", sha256="4ad65e684f4d2d1738a3b981cecc741cc26914ac69c000bbe18ebf27b98a1e4a", url="https://pypi.org/packages/b5/f9/830292ecbb81c449fe47712c28e1bb4f64b5e8879c67c6fdeeb0e498068d/pyobjc-framework-PhotosUI-8.5.tar.gz")
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

