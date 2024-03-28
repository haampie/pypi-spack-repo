# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyDeprecated(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("1.2.14", sha256="6fac8b097794a90302bdbb17b9b815e732d3c4720583ff1b198499d78470466c", url="https://pypi.org/packages/20/8d/778b7d51b981a96554f29136cd59ca7880bf58094338085bcf2a979a0e6a/Deprecated-1.2.14-py2.py3-none-any.whl")
    version("1.2.13", sha256="64756e3e14c8c5eea9795d93c524551432a0be75629f8f29e67ab8caf076c76d", url="https://pypi.org/packages/51/6a/c3a0408646408f7283b7bc550c30a32cc791181ec4618592eec13e066ce3/Deprecated-1.2.13-py2.py3-none-any.whl")
    version("1.2.12", sha256="08452d69b6b5bc66e8330adde0a4f8642e969b9e1702904d137eeb29c8ffc771", url="https://pypi.org/packages/fb/73/994edfcba74443146c84b91921fcc269374354118d4f452fb0c54c1cbb12/Deprecated-1.2.12-py2.py3-none-any.whl")
    version("1.2.11", sha256="924b6921f822b64ec54f49be6700a126bab0640cfafca78f22c9d429ed590560", url="https://pypi.org/packages/d4/56/7d4774533d2c119e1873993d34d313c9c9efc88c5e4ab7e33bdf915ad98c/Deprecated-1.2.11-py2.py3-none-any.whl")
    version("1.2.10", sha256="a766c1dccb30c5f6eb2b203f87edd1d8588847709c78589e1521d769addc8218", url="https://pypi.org/packages/76/a1/05d7f62f956d77b23a640efc650f80ce24483aa2f85a09c03fb64f49e879/Deprecated-1.2.10-py2.py3-none-any.whl")
    version("1.2.9", sha256="55b41a15bda04c6a2c0d27dd4c2b7b81ffa6348c9cad8f077ac1978c59927ab9", url="https://pypi.org/packages/2b/ae/1f02f68eaa4aa878f184b2adc20a1923becb80a4da6c76efa33450011902/Deprecated-1.2.9-py2.py3-none-any.whl")
    version("1.2.8", sha256="cd98397157a1046784c9ff155730b745f46bb4dfd0175522c5bf348ab10037a5", url="https://pypi.org/packages/46/d1/ac3a649a24542850e281cfefb9024ba4ba174157713015b6489a593806fe/Deprecated-1.2.8-py2.py3-none-any.whl")
    version("1.2.7", sha256="8b6a5aa50e482d8244a62e5582b96c372e87e3a28e8b49c316e46b95c76a611d", url="https://pypi.org/packages/f6/89/62912e01f3cede11edcc0abf81298e3439d9c06c8dce644369380ed13f6d/Deprecated-1.2.7-py2.py3-none-any.whl")
    version("1.2.6", sha256="b07b414c8aac88f60c1d837d21def7e83ba711052e03b3cbaff27972567a8f8d", url="https://pypi.org/packages/88/0e/9d5a1a8cd7130c49334cce7b8167ceda63d6a329c8ea65b626116bc9e9e6/Deprecated-1.2.6-py2.py3-none-any.whl")
    version("1.2.5", sha256="749f6cdcfbdc3f79258f8154bad43fced95adc632c337675d0385959895894bc", url="https://pypi.org/packages/9f/7a/003fa432f1e45625626549726c2fbb7a29baa764e9d1fdb2323a5d779f8a/Deprecated-1.2.5-py2.py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-wrapt@1.10:", when="@1.2.6:")
        depends_on("py-wrapt", when="@1.2:1.2.5")
    # END DEPENDENCIES

