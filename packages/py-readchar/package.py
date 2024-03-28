# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyReadchar(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("4.1.0.dev1", sha256="e2205d4485f71d244a9ee2bd56cb03e3a36fc2b02febb09b638946174542d4d4", url="https://pypi.org/packages/5e/24/183972db4b1ff6567813b8b099eee2f230197d8c02e20cbbae67548cfeb9/readchar-4.1.0.dev1-py3-none-any.whl")
    version("4.0.6", sha256="b4b31dd35de4897be738f27e8f9f62426b5fedb54b648364987e30ae534b71bc", url="https://pypi.org/packages/86/db/aca9e5e6a53a499d61cbd78b3594d700f1e48a50ab6970a92a4d1251f8db/readchar-4.0.6-py3-none-any.whl")
    version("4.0.5", sha256="76ec784a5dd2afac3b7da8003329834cdd9824294c260027f8c8d2e4d0a78f43", url="https://pypi.org/packages/cd/14/730280df294e52e395a70111f4d9b07be94f5ba7a69db7eba3c324f113b2/readchar-4.0.5-py3-none-any.whl")
    version("4.0.4", sha256="274e08aebb64542362ebf0b06cfa8e7ba7595dc419b812c19d6bc17c2d4fa4bb", url="https://pypi.org/packages/ac/f7/c9697f8f9105659bb0cf74d13af4ff58e1370149e77f01ba0118e3978f15/readchar-4.0.4-py3-none-any.whl")
    version("4.0.3", sha256="3d4351c563aba4ae7d4e0b821a234d48bc748f45b74e3f38b50cba3857b57acb", url="https://pypi.org/packages/76/3a/fd9d3558ae0df9aaa8d9468c391a8d510c4658a17cee3474a44c0bbc43aa/readchar-4.0.3-py3-none-any.whl")
    version("4.0.2", sha256="71d929823ba272cf96ba5dbe2896330f704d71ad33ea6b19cbf1322c203d9950", url="https://pypi.org/packages/cc/05/ad64b25fb05de4a8bb35f4e2243f9c9710dc935899c9c0e84c6b78e111b6/readchar-4.0.2-py3-none-any.whl")
    version("4.0.1", sha256="ab31a7bb626c2780d1c5e1e691fd3c03f00b40afea9f7b5633232c1b98c273ae", url="https://pypi.org/packages/09/82/2455fd1737ccf90b42f6edcaa2d7a55f172b38a6d63f416ae6893547ff26/readchar-4.0.1-py3-none-any.whl")
    version("4.0.0", sha256="49dfb240662d057c028b1597ee80413262d39f3415fd120b3385319b6e494a72", url="https://pypi.org/packages/4f/aa/a1403909bcb0c0c7c88c559cf1e103b52a127d42cdf19e893bebc215b000/readchar-4.0.0-py3-none-any.whl")
    version("3.1.0", sha256="16059b8beb1f525182de193fade8ca314cc4c32f62956a9a50268909103cdaa8", url="https://pypi.org/packages/8f/99/244bd917d70e77fd784320b639cfe5318b89693582943edb4a1c2bc67806/readchar-3.1.0-py3-none-any.whl")
    version("3.0.6", sha256="98e26e62732a7de83ff42b422734157a9cc949bbf73c9d7a6b915a4e49f6ab51", url="https://pypi.org/packages/8f/ea/3d4df4e781ae1237563c989e093c02a1f2b0d5d1c7882580480e72dfb6d4/readchar-3.0.6-py3-none-any.whl")
    version("3.0.5", sha256="4c31210edfdf3e706d042c58feba2e8b6d5768b7f37002c5579fc473552f8fbb", url="https://pypi.org/packages/40/0d/d3819ead63911f2ff3f4ef6608c48b32bbc5f9d2d3934d520c7ab958be73/readchar-3.0.5-py3-none-any.whl")
    version("2.0.1", sha256="ed00b7a49bb12f345319d9fa393f289f03670310ada2beb55e8c3f017c648f1e", url="https://pypi.org/packages/e9/63/9e8c21d675871c60377dbad2e3a3e44135d1bfd25aeb48f0f392a9f09bfd/readchar-2.0.1-py2-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-setuptools@41:", when="@4.0.3:")
        depends_on("py-setuptools", when="@4:4.0.2")
        depends_on("py-wheel", when="@4:4.0.2")
    # END DEPENDENCIES

