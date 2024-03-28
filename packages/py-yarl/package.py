# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyYarl(PythonPackage):
    # BEGIN VERSIONS
    version("1.9.2", sha256="04ab9d4b9f587c06d801c2abfe9317b77cdf996c65a90d5e84ecc45010823571", url="https://pypi.org/packages/5f/3f/04b3c5e57844fb9c034b09c5cb6d2b43de5d64a093c30529fd233e16cf09/yarl-1.9.2.tar.gz")
    version("1.8.1", sha256="af887845b8c2e060eb5605ff72b6f2dd2aab7a761379373fd89d314f4752abbf", url="https://pypi.org/packages/d6/04/255c68974ec47fa754564c4abba8f61f9ed68b869bbbb854198d6259c4f7/yarl-1.8.1.tar.gz")
    version("1.7.2", sha256="45399b46d60c253327a460e99856752009fcee5f5d3c80b2f7c0cae1c38d56dd", url="https://pypi.org/packages/f6/da/46d1b3d69a9a0835dabf9d59c7eb0f1600599edd421a4c5a15ab09f527e0/yarl-1.7.2.tar.gz")
    version("1.4.2", sha256="58cd9c469eced558cd81aa3f484b2924e8897049e06889e8ff2510435b7ef74b", url="https://pypi.org/packages/d6/67/6e2507586eb1cfa6d55540845b0cd05b4b77c414f6bca8b00b45483b976e/yarl-1.4.2.tar.gz")
    version("1.3.0", sha256="024ecdc12bc02b321bc66b41327f930d1c2c543fa9a561b39861da9388ba7aa9", url="https://pypi.org/packages/fb/84/6d82f6be218c50b547aa29d0315e430cf8a23c52064c92d0a8377d7b7357/yarl-1.3.0.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-idna@2:", when="@0.17:1.2.5-alpha0,1.2.5-alpha3,1.2.5-alpha5:1.4,1.9.3:")
        depends_on("py-multidict@4:", when="@1:1.2.5-alpha0,1.2.5-alpha3,1.2.5-alpha5:1.4,1.9.3:")
    # END DEPENDENCIES

