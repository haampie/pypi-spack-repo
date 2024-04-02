# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyNumba(PythonPackage):
    # BEGIN VERSIONS
    version("0.58.1", sha256="487ded0633efccd9ca3a46364b40006dbdaca0f95e99b8b83e778d1195ebcbaa", url="https://pypi.org/packages/13/2b/0f750d451fd961fd91d6bc86c512781fa46f9ef64813007e501482522ff9/numba-0.58.1.tar.gz")
    version("0.57.0", sha256="2af6d81067a5bdc13960c6d2519dbabbf4d5d597cf75d640c5aeaefd48c6420a", url="https://pypi.org/packages/7e/cf/aa289fc5d668c368b2c7655e6ac916dbee34df96dc6eae9ad70993b169cb/numba-0.57.0.tar.gz")
    version("0.56.4", sha256="32d9fef412c81483d7efe0ceb6cf4d3310fde8b624a9cecca00f790573ac96ee", url="https://pypi.org/packages/e2/1e/de917b683bb5f0b6078fb1397293eab84c4eaa825fbf94d73d6488eb354f/numba-0.56.4.tar.gz")
    version("0.56.0", sha256="87a647dd4b8fce389869ff71f117732de9a519fe07663d9a02d75724eb8e244d", url="https://pypi.org/packages/b3/23/fd8e7aa70f6c0b41c99de6aae7afc6850ebac2477687e68c6529bfaa41ba/numba-0.56.0.tar.gz")
    version("0.55.2", sha256="e428d9e11d9ba592849ccc9f7a009003eb7d30612007e365afe743ce7118c6f4", url="https://pypi.org/packages/39/dd/7109030bb584e8f0c4c8796bfd39fc5811cb77368a8c5db335f99c1fec9e/numba-0.55.2.tar.gz")
    version("0.55.1", sha256="03e9069a2666d1c84f93b00dbd716fb8fedde8bb2c6efafa2f04842a46442ea3", url="https://pypi.org/packages/69/df/bd36068b2c1d0d34794f8ac0c222f9c4ad88dc710b400e65dbb3b59ea57e/numba-0.55.1.tar.gz")
    version("0.54.0", sha256="bad6bd98ab2e41c34aa9c80b8d9737e07d92a53df4f74d3ada1458b0b516ccff", url="https://pypi.org/packages/24/66/4720b6f70b42c74f10296a9803f8ba28c284f55cee6839f457bc67588277/numba-0.54.0.tar.gz")
    version("0.51.1", sha256="1e765b1a41535684bf3b0465c1d0a24dcbbff6af325270c8f4dad924c0940160", url="https://pypi.org/packages/a0/25/118cfd7d323abf3e353710e2ff7fe12b1470c302103ad9675cd794f2988e/numba-0.51.1.tar.gz")
    version("0.50.1", sha256="89e81b51b880f9b18c82b7095beaccc6856fcf84ba29c4f0ced42e4e5748a3a7", url="https://pypi.org/packages/62/17/d42c2bb47cab6668cb2e47ee44b86556f4fb95fd6e8105ed55211c89c8dd/numba-0.50.1.tar.gz")
    version("0.48.0", sha256="9d21bc77e67006b5723052840c88cc59248e079a907cc68f1a1a264e1eaba017", url="https://pypi.org/packages/c3/81/453926761dc00b02b22d1cd6935aaa8a736fca011d33615315bc7c132788/numba-0.48.0.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    variant("tbb", default=False, description="tbb")
    # END VARIANTS

    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("python@3.8:", when="@0.57:0.58")
        depends_on("python@3.7:", when="@0.56")
        depends_on("python@3.7:3.10", when="@0.55")
        depends_on("python@3.7:3.9", when="@0.54")
        depends_on("py-llvmlite@0.33", when="@0.50")
        depends_on("py-llvmlite@0.31", when="@0.48")
        depends_on("py-numpy@1.15.0:", when="@0.48:0.50")
        depends_on("py-setuptools", when="@0.47:0.50")
    # END DEPENDENCIES

