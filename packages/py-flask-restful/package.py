# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyFlaskRestful(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("0.3.10", sha256="1cf93c535172f112e080b0d4503a8d15f93a48c88bdd36dd87269bdaf405051b", url="https://pypi.org/packages/d7/7b/f0b45f0df7d2978e5ae51804bb5939b7897b2ace24306009da0cc34d8d1f/Flask_RESTful-0.3.10-py2.py3-none-any.whl")
    version("0.3.9", sha256="4970c49b6488e46c520b325f54833374dc2b98e211f1b272bd4b0c516232afe2", url="https://pypi.org/packages/a9/02/7e21a73564fe0d9d1a3a4ff478dfc407815c4e2fa4e5121bcfc646ba5d15/Flask_RESTful-0.3.9-py2.py3-none-any.whl")
    version("0.3.8", sha256="d891118b951921f1cec80cabb4db98ea6058a35e6404788f9e70d5b243813ec2", url="https://pypi.org/packages/e9/83/d0d33c971de2d38e54b0037136c8b8d20b9c83d308bc6c220a25162755fd/Flask_RESTful-0.3.8-py2.py3-none-any.whl")
    version("0.3.7", sha256="ecd620c5cc29f663627f99e04f17d1f16d095c83dc1d618426e2ad68b03092f8", url="https://pypi.org/packages/17/44/6e490150ee443ca81d5f88b61bb4bbb133d44d75b0b716ebe92489508da4/Flask_RESTful-0.3.7-py2.py3-none-any.whl")
    version("0.3.6", sha256="e2f1b8063de3944b94c7f8be5cee4d2161db0267c54c5b757d875295061776fa", url="https://pypi.org/packages/47/08/89cf8594735392cd71752f7cf159fa63765eac3e11b0da4324cdfeaea137/Flask_RESTful-0.3.6-py2.py3-none-any.whl")
    version("0.3.5", sha256="7799326da016045bb6e67d6ff7be334303408b9dca39a68f0a2a4e54078f0389", url="https://pypi.org/packages/15/2e/41485f3d74103412266f3ce07675adf4bd5b4da16f5f3599b2d114374631/Flask_RESTful-0.3.5-py2.py3-none-any.whl")
    version("0.3.4", sha256="6524d7cdd4d05286d7345e966fcbbf30ce4bb955c1934211be12257547978ed2", url="https://pypi.org/packages/d5/9b/e512b03799f881a345c6b3c2feb35c9d9fa44943e08dc2628baa6383c1de/Flask_RESTful-0.3.4-py2.py3-none-any.whl")
    version("0.3.3", sha256="d183efe7ee03546d88f8d0fd29191fb3ed07f56d3c624c38622d4e60bb12639e", url="https://pypi.org/packages/72/cd/00897ce79ff7fbb41115d138d8174d299e0b050eaff18eac8a7b30f06bdc/Flask_RESTful-0.3.3-py2.py3-none-any.whl")
    version("0.3.2", sha256="90e1fd25f108cd5271fbd585f1f70459a7443640b3e5b0403057a9fb83df9f47", url="https://pypi.org/packages/cf/b0/c71bdbcf8064eec2b5b7d0aab2f94c52bf1550ebdf267907c3b36553dcf6/Flask_RESTful-0.3.2-py2.py3-none-any.whl")
    version("0.3.1", sha256="794999cc9905aacff5a8ae99f69eda8a3ed11b281ca66c4f10db8f50c876ce4a", url="https://pypi.org/packages/f4/91/581f2a387700e791aa7022f638b13615562ba21c9ede2e603defd14f9e5c/Flask_RESTful-0.3.1-py2.py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-aniso8601@0.82:", when="@0.3.10:")
        depends_on("py-flask@0.8:", when="@0.3.10:")
        depends_on("py-pytz", when="@0.3.10:")
        depends_on("py-six@1.3:", when="@0.3.10:")
    # END DEPENDENCIES

