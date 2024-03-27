##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyYarl(PythonPackage):
    version("1.9.4", sha256="566db86717cf8080b99b58b083b773a908ae40f06681e87e589a976faf8246bf", url="https://pypi.org/packages/e0/ad/bedcdccbcbf91363fd425a948994f3340924145c2bc8ccb296f4a1e52c28/yarl-1.9.4.tar.gz")
    version("1.9.3", sha256="4a14907b597ec55740f63e52d7fee0e9ee09d5b9d57a4f399a7423268e457b57", url="https://pypi.org/packages/ca/f7/2af788563995eeec32b920c0640a6bc54777c89c780030a7754f95166b7f/yarl-1.9.3.tar.gz")
    version("1.9.2", sha256="04ab9d4b9f587c06d801c2abfe9317b77cdf996c65a90d5e84ecc45010823571", url="https://pypi.org/packages/5f/3f/04b3c5e57844fb9c034b09c5cb6d2b43de5d64a093c30529fd233e16cf09/yarl-1.9.2.tar.gz")
    version("1.9.1", sha256="5ce0bcab7ec759062c818d73837644cde567ab8aa1e0d6c45db38dfb7c284441", url="https://pypi.org/packages/ed/02/695dd9ec40214fbad98ffc82e97bbe15d99cb798b837c5af38b5649a20cd/yarl-1.9.1.tar.gz")
    version("1.8.2", sha256="49d43402c6e3013ad0978602bf6bf5328535c48d192304b91b97a3c6790b1562", url="https://pypi.org/packages/c4/1e/1b204050c601d5cd82b45d5c8f439cb6f744a2ce0c0a6f83be0ddf0dc7b2/yarl-1.8.2.tar.gz")
    version("1.8.1", sha256="af887845b8c2e060eb5605ff72b6f2dd2aab7a761379373fd89d314f4752abbf", url="https://pypi.org/packages/d6/04/255c68974ec47fa754564c4abba8f61f9ed68b869bbbb854198d6259c4f7/yarl-1.8.1.tar.gz")
    version("1.8.0", sha256="8e4c9beebb829d244d315cbe1575022d33652fc7b02105c40d8188cb63135077", url="https://pypi.org/packages/37/99/a872464316f791ff59e83cb99c6a0224ee93498455a8f0080eb05f3f8cc6/yarl-1.8.0.tar.gz")
    version("1.7.2", sha256="45399b46d60c253327a460e99856752009fcee5f5d3c80b2f7c0cae1c38d56dd", url="https://pypi.org/packages/f6/da/46d1b3d69a9a0835dabf9d59c7eb0f1600599edd421a4c5a15ab09f527e0/yarl-1.7.2.tar.gz")
    version("1.7.0", sha256="8e7ebaf62e19c2feb097ffb7c94deb0f0c9fab52590784c8cd679d30ab009162", url="https://pypi.org/packages/7f/5c/a4ce6d4f46413afe49734bf901939105f4ce7fcfbcf87d0777cc39501060/yarl-1.7.0.tar.gz")
    version("1.6.3", sha256="8a9066529240171b68893d60dca86a763eae2139dd42f42106b03cf4b426bf10", url="https://pypi.org/packages/97/e7/af7219a0fe240e8ef6bb555341a63c43045c21ab0392b4435e754b716fa1/yarl-1.6.3.tar.gz")
    version("1.4.2", sha256="58cd9c469eced558cd81aa3f484b2924e8897049e06889e8ff2510435b7ef74b", url="https://pypi.org/packages/d6/67/6e2507586eb1cfa6d55540845b0cd05b4b77c414f6bca8b00b45483b976e/yarl-1.4.2.tar.gz")
    version("1.3.0", sha256="024ecdc12bc02b321bc66b41327f930d1c2c543fa9a561b39861da9388ba7aa9", url="https://pypi.org/packages/fb/84/6d82f6be218c50b547aa29d0315e430cf8a23c52064c92d0a8377d7b7357/yarl-1.3.0.tar.gz")

    with default_args(type="run"):
        depends_on("py-idna@2:", when="@0.17:1.2.5-alpha0,1.2.5-alpha3,1.2.5-alpha5:1.4,1.9.3:")
        depends_on("py-multidict@4:", when="@1:1.2.5-alpha0,1.2.5-alpha3,1.2.5-alpha5:1.4,1.9.3:")

