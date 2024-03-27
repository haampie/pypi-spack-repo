##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyEtils(PythonPackage):
    version("1.8.0", sha256="f31d7f27a889457eaa44eab18ce836d24fd6d40dbbb167d38879b7296f6456ea", url="https://pypi.org/packages/d0/3c/784b5f94bcad62a4167f2347fe1095b627433c22a54aecc4504237494b81/etils-1.8.0-py3-none-any.whl")
    version("1.7.0", sha256="61af8f7c242171de15e22e5da02d527cb9e677d11f8bcafe18fcc3548eee3e60", url="https://pypi.org/packages/37/10/dd5b124f037a636783e416a2fe839edd7ec63c0dce7ce4f3c1da029aeb80/etils-1.7.0-py3-none-any.whl")
    version("1.6.0", sha256="3da192b057929f2511f9ef713cee7d9c498e741740f8b2a9c0f6392d787201d4", url="https://pypi.org/packages/cf/10/55adb8074b0211f8cfad76e73da86d4306e45567a5e6a905b4444fd7a751/etils-1.6.0-py3-none-any.whl")
    version("1.5.2", sha256="6dc882d355e1e98a5d1a148d6323679dc47c9a5792939b9de72615aa4737eb0b", url="https://pypi.org/packages/0f/6a/d2aaebacf73d5da7126c632ec0d9dc2df99cc4bbd259bad48904a034fc1b/etils-1.5.2-py3-none-any.whl")
    version("1.5.1", sha256="2c1bfa2817eb4881cb509097f1e65ac6160126ba74ec47b3bb47ee678628d8c8", url="https://pypi.org/packages/1f/ea/523f2ca226b9f06f57e4c564123b551874ce6268c1e581c4006bc4ad2eae/etils-1.5.1-py3-none-any.whl")
    version("1.5.0", sha256="e28bf37a0ee20e81d6cf301ce64574763cc4ade8580a2b3276b790993c167d12", url="https://pypi.org/packages/db/b1/094f147d77178d7a3553b40b6bc13fc9dd1ba4ef5425abe94d07ad2447dc/etils-1.5.0-py3-none-any.whl")
    version("1.4.1", sha256="9134111a01872af7014cf3e8ee7496484abdc94fc5ce992800dd989545dcfe2c", url="https://pypi.org/packages/4a/6a/d58ec120f5e4babbf5001c144266ba623dcdae8e81dc6cdb422a98d0e0ce/etils-1.4.1-py3-none-any.whl")
    version("1.4.0", sha256="fd20131e1b134d3ed2d3297e25034b8c796761676b770b4cb5a44f26c73d3edf", url="https://pypi.org/packages/13/08/d56551b73d85a75a6c362320a4f623fe52074092a1dd47621ece9d3f1a13/etils-1.4.0-py3-none-any.whl")
    version("1.3.0", sha256="809a92ff72f12149441492cf4d9a26b56a4741dffb4dfb9c4c7b7afe055c2d28", url="https://pypi.org/packages/ca/db/47ffb866d7a1aa21132a72f67e84c4f03a4cad11ae9d069dd61c52f929de/etils-1.3.0-py3-none-any.whl")
    version("1.2.0", sha256="c6585069b387fdbeed6a2c571b8bcf312ecdb577c95065461e5fad9ed1973989", url="https://pypi.org/packages/cb/f2/8021def108dcab3592bf0d203e36d9265c4187557e812b833ec56f755f88/etils-1.2.0-py3-none-any.whl")
    version("0.9.0", sha256="635d6f7d1c519eb194304228543a4c5c7df0e6b58243302473e34c18cf720588", url="https://pypi.org/packages/76/ac/4f4b4096acd0160e0895715b47974b1f304b5e4a6b5169ce8d1355820eb4/etils-0.9.0-py3-none-any.whl")

    variant("epath", default=False)
    variant("epy", default=False)

    with default_args(type="run"):
        depends_on("python@3.11:", when="@1.8:")
        depends_on("python@3.10:", when="@1.6:1.7")
        depends_on("python@3.9:", when="@:0.1,1.4:1.5")
        depends_on("py-fsspec", when="@1.5:+epath")
        depends_on("py-importlib-resources", when="@0.2,0.6:+epath")
        depends_on("py-tf-nightly", when="@0.2:0.5+epath")
        depends_on("py-typing-extensions", when="@0.7:+epath")
        depends_on("py-typing-extensions", when="@0.5:+epy")
        depends_on("py-zipp", when="@0.2,0.6:+epath")

        # self-dependency
        # depends_on("py-etils+epy", when="@0.2,0.6:+epath")

