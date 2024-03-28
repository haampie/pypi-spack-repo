# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyDeap(PythonPackage):
    # BEGIN VERSIONS
    version("1.4.1", sha256="cc01de9892dfa7d1bc9803dab28892fead177f0182c81db47360a240ead778ff", url="https://pypi.org/packages/0c/4c/350b7a2a16a4ed3b547172a7d2ca328e5376466a419bf90102ceb290ac5c/deap-1.4.1.tar.gz")
    version("1.4.0", sha256="ffef2921932a0edbe634fcb6d156189e7a364bf638a2af4ae5d59931a9a4c8cc", url="https://pypi.org/packages/c6/62/8ffbdb48215659ce5dce0b15e9a1cab17583d98092833c96a80f7a0707f7/deap-1.4.0.tar.gz")
    version("1.3.3", sha256="8772f1b0fff042d5e516b0aebac2c706243045aa7d0de8e0b8658f380181cf31", url="https://pypi.org/packages/9a/a1/8c5ad42e78abdd7d2174baace0bd864ef6fd9a86c1cf72d410945669d784/deap-1.3.3.tar.gz")
    version("1.3.2", sha256="359f9441af0ce3e59a4688ae90cace0a1a4861f0b901545bf850a6fa571a90fd", url="https://pypi.org/packages/eb/c8/3b0bb045716795b93133ab6c53b6df205de0e69e7b8fb8cb6adef714bbef/deap-1.3.2.tar.gz")
    version("1.3.1", sha256="11f54493ceb54aae10dde676577ef59fc52d52f82729d5a12c90b0813c857a2f", url="https://pypi.org/packages/85/1e/5f707798f8f05616c03079f02b63568b2b91f8136891a2eeffd9f78f6d8b/deap-1.3.1.tar.gz")
    version("1.3.0", sha256="cd0fd7bccf7837b9e6a666b75e1c3a629fa3f5bc346cb90a9edd8cd56f085980", url="https://pypi.org/packages/f7/d2/ca7c4ebbd2c30a017c188b72da98dab3ab54648c3b0aaa7a2efa772d6147/deap-1.3.0.tar.gz")
    version("1.2.2", sha256="95c63e66d755ec206c80fdb2908851c0bef420ee8651ad7be4f0578e9e909bcf", url="https://pypi.org/packages/af/29/e7f2ecbe02997b16a768baed076f5fc4781d7057cd5d9adf7c94027845ba/deap-1.2.2.tar.gz")
    version("1.2.1", sha256="bbdd135cfbe728d817044367e562d6d7bed7dc3626942362d1434b26b628a664", url="https://pypi.org/packages/b0/9c/a7404777a4cdf5857224051f2ae363d76c3d3b17d27b2caf12ed9bbe6d94/deap-1.2.1.tar.gz")
    version("1.2.1-rc3", sha256="5e9bf92f8bf6ff4476f117714b9f4472179369e75d116fcefeb50664bc33ed02", url="https://pypi.org/packages/dd/6f/4611020289cf6961e969720c975b9c3a6c06b8ac7e64877269789790a9b1/deap-1.2.1rc3.tar.gz")
    version("1.2.0", sha256="c40018506cac749d42a813eb132dd8b03e501b3bcc4cd96e494991b8fed4aee7", url="https://pypi.org/packages/b5/63/ea195522c9e987d0b497bbbd8c1c7183f6c39c886637a6eaa8c6b33519f7/deap-1.2.0.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-numpy", when="@1.3.1")
    # END DEPENDENCIES

