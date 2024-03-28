# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyCachecontrol(PythonPackage):
    # BEGIN VERSIONS
    version("0.14.0", sha256="f5bf3f0620c38db2e5122c0726bdebb0d16869de966ea6a2befe92470b740ea0", url="https://pypi.org/packages/a3/a9/7d331fec593a4b2953338df33e954aac6ff79eb5a073bca2783766bc7722/cachecontrol-0.14.0-py3-none-any.whl")
    version("0.13.1", sha256="95dedbec849f46dda3137866dc28b9d133fc9af55f5b805ab1291833e4457aa4", url="https://pypi.org/packages/1d/e3/a22348e6226dcd585d5a4b5f0175b3a16dabfd3912cbeb02f321d00e56c7/cachecontrol-0.13.1-py3-none-any.whl")
    version("0.13.1-rc0", sha256="2ae4d63c02199286b41ec36b1acf16c69331aaaafbeb122b91db9808219b6837", url="https://pypi.org/packages/61/39/164a7c1ebf7e08e662d7b6ba448c61715f7cdf1256e84a0cdf7facc8597d/cachecontrol-0.13.1rc0-py3-none-any.whl")
    version("0.13.0", sha256="4544a012a25cf0a73c53cd986f68b4f9c9f6b1df01d741c2923c3d56c66c7bda", url="https://pypi.org/packages/65/03/9ed07561cc4b428204fc59fa090ae6652b6fe0a6506c2b05adfcb09085b9/CacheControl-0.13.0-py3-none-any.whl")
    version("0.12.14", sha256="1c2939be362a70c4e5f02c6249462b3b7a24441e4f1ced5e9ef028172edf356a", url="https://pypi.org/packages/72/a2/28e0ef082f7d78253aded97933e1d7b94bab3c5be366e8afd6513de4028e/CacheControl-0.12.14-py2.py3-none-any.whl")
    version("0.12.13", sha256="431fc10c5ab1a1589ce08c05b948abac31c0f76962d5fc9efab9da280c9790aa", url="https://pypi.org/packages/a2/ab/fc647c0069493a904be5519dd03a535a2d49a51e98d5e3cb5d93d332293d/CacheControl-0.12.13-py2.py3-none-any.whl")
    version("0.12.12", sha256="5986a16897cd296bdb7b86b42e0403c4ca30b9875f0e0c7c8e509b50cff115b7", url="https://pypi.org/packages/1e/49/9db6d5be74f606d1b6f2bd4469827b0eed557c4bbafb30134519510f7f0d/CacheControl-0.12.12-py2.py3-none-any.whl")
    version("0.12.11", sha256="2c75d6a8938cb1933c75c50184549ad42728a27e9f6b92fd677c3151aa72555b", url="https://pypi.org/packages/83/63/15ce47ede5b03657e920f3f006e56ca9a16f7873978146f2f77e297bdd22/CacheControl-0.12.11-py2.py3-none-any.whl")
    version("0.12.10", sha256="b0d43d8f71948ef5ebdee5fe236b86c6ffc7799370453dccb0e894c20dfa487c", url="https://pypi.org/packages/d3/39/b7cd9ef1be03ac33e71f76837a23d59842b016e5159cf5aff30c0b340907/CacheControl-0.12.10-py2.py3-none-any.whl")
    version("0.12.9", sha256="1675f6b0ed902b419f60af4f1d33486e2379743e3723c594eca2f95b10e4370a", url="https://pypi.org/packages/21/66/20f741c1f2e0df071eca4ed13499622d5771897f22e2eb412c19a9880e0d/CacheControl-0.12.9-py2.py3-none-any.whl")
    version("0.12.8", sha256="a02648eef39d764f0ac566c7a50f8549e7011649b9d17024b94233cafa235bd1", url="https://pypi.org/packages/0f/7d/da6cd412304352be1f12cc99ac9f541d6ad748b40d1a0a57439d13fd09f6/CacheControl-0.12.8-py2.py3-none-any.whl")
    version("0.12.6", sha256="10d056fa27f8563a271b345207402a6dcce8efab7e5b377e270329c62471b10d", url="https://pypi.org/packages/18/71/0a9df4206a5dc5ae7609c41efddab2270a2c1ff61d39de7591dc7302ef89/CacheControl-0.12.6-py2.py3-none-any.whl")
    version("0.12.5", sha256="cef77effdf51b43178f6a2d3b787e3734f98ade253fa3187f3bb7315aaa42ff7", url="https://pypi.org/packages/5e/f0/2c193ed1f17c97ae539da7e1c2d48b80d8cccb1917163b26a91ca4355aa6/CacheControl-0.12.5.tar.gz")
    version("0.12.4", sha256="a7d21ba4e3633d95ac9fed5be205ee6d1da36bdc4b8914eb7a57ff50b7e5628c", url="https://pypi.org/packages/98/f5/76619a63f0e4a1d2f5a1792ebc233a395c648c63d3461dc0331479ef120a/CacheControl-0.12.4.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    variant("filecache", default=False)
    variant("redis", default=False)
    # END VARIANTS

    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-filelock@3.8:", when="@0.12.12:0.12.13,0.13:+filecache")
        depends_on("py-lockfile@0.9:", when="@0.12.6:0.12.11,0.12.14:0.12+filecache")
        depends_on("py-msgpack@0.5.2:", when="@0.12.6:")
        depends_on("py-redis@2.10.5:", when="@0.12.6:+redis")
        depends_on("py-requests@2.16:", when="@0.13:")
        depends_on("py-requests", when="@0.12.6:0.12")
    # END DEPENDENCIES

