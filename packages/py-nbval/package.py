# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyNbval(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("0.11.0", sha256="307aecc866c9a1e8a13bb5bbb008a702bacfda2394dff6fe504a3108a58042a0", url="https://pypi.org/packages/2c/5c/eb1e3ce54c4e94c7734b3831756c63f21badb3de91a98d77b9e23c0ca76a/nbval-0.11.0-py2.py3-none-any.whl")
    version("0.10.0", sha256="427e42caabeae39f493d8baca629b03816269fc11f1b7e2046e10929a3149a73", url="https://pypi.org/packages/16/9c/1da45f3bf4065cb6bace83cca6c66ff82cc11a641b423e6ac3fcd9b6aa67/nbval-0.10.0-py2.py3-none-any.whl")
    version("0.9.6", sha256="4f9b780997d8942408853513f2c5ee6c1863de193559fc3f95e1c1cde8110439", url="https://pypi.org/packages/b0/92/23d60d4593b6e69f2114caf6fec238ce461233a8633dcbef6f619ad339c9/nbval-0.9.6-py2.py3-none-any.whl")
    version("0.9.5", sha256="10aced0f9a28893e608c2704b2e8bdcbc57635db9640d454f85fe0545fda5002", url="https://pypi.org/packages/8a/a0/03ca3ca5cc92e60fedf743e045b1d0a66240a69219e3828234bebfb4d08b/nbval-0.9.5-py2.py3-none-any.whl")
    version("0.9.4", sha256="66cc65fdc143e8e13ae3801702da5b699f3d5056434d71b335434e1a2be291e5", url="https://pypi.org/packages/1f/80/70b39c934c407c038aab67f7047cabb2c05894bbf9d465f9765461f0cf30/nbval-0.9.4-py2.py3-none-any.whl")
    version("0.9.3", sha256="ae529024ae63d8a09eac36358d61b17f631c4a481e5721bca9d4a40edb07a666", url="https://pypi.org/packages/80/08/6b1e7d87a90edb02c272e30f4f6f325da5a5c8dfc3eaeaa4a8138fb97e43/nbval-0.9.3-py2.py3-none-any.whl")
    version("0.9.2", sha256="178ea3e9d0ffb4b1eb175728b0655f3da208e57bc47c11072a48ddedc4314c40", url="https://pypi.org/packages/2f/2a/e34cbb6c5932a2aa4a874c21d7be16775500b96ce6677412bb329fe6ad48/nbval-0.9.2-py2.py3-none-any.whl")
    version("0.9.1", sha256="74ff5e2c90a50b1ddf7edd02978c4e43221b1ee252dc14fcaa4230aae4492eda", url="https://pypi.org/packages/0b/c7/f12cf36398ba2a821dccd591b91d5a5d38afccd36fd9b37cc5507cd5d5f4/nbval-0.9.1-py2.py3-none-any.whl")
    version("0.9.0", sha256="cb359442fc2a605bd1a57513cc7a6c6485a02dc965e182f0de235eceb7a0a84b", url="https://pypi.org/packages/21/94/a5173b196698c37de25fdf080cafb5aef68e09b7431b6d0c578b268c9f6b/nbval-0.9.0-py2.py3-none-any.whl")
    version("0.8.0", sha256="b2d79da13b904b634ad2c78adef135059786f74ababc7c4b386fe148c54ba27e", url="https://pypi.org/packages/b9/dd/eba22ba91e6b9445cf7bafd8febbcbf03744ef846eeea44a4649a7e7486b/nbval-0.8.0-py2.py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-coverage@:4", when="@0.9.4")
        depends_on("py-coverage", when="@0.9:0.9.3,0.9.5:")
        depends_on("py-ipykernel", when="@:0.3.2,0.4.1:")
        depends_on("py-jupyter-client", when="@:0.3.2,0.3.6:")
        depends_on("py-nbformat", when="@:0.3.2,0.3.6:")
        depends_on("py-pytest@7.0.0:", when="@0.11:")
        depends_on("py-pytest@2.8:", when="@0.5:0.10")
        depends_on("py-six", when="@:0.3.2,0.3.6:0.9")
    # END DEPENDENCIES

