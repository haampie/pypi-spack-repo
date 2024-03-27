##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyJupyterEvents(PythonPackage):
    version("0.10.0", sha256="4b72130875e59d57716d327ea70d3ebc3af1944d3717e5a498b8a06c6c159960", url="https://pypi.org/packages/a5/94/059180ea70a9a326e1815176b2370da56376da347a796f8c4f0b830208ef/jupyter_events-0.10.0-py3-none-any.whl")
    version("0.9.1", sha256="e51f43d2c25c2ddf02d7f7a5045f71fc1d5cb5ad04ef6db20da961c077654b9b", url="https://pypi.org/packages/f2/db/65f23494d5b379cf34ae94a3c2a7ede4829a489bb0a81744609056b36d21/jupyter_events-0.9.1-py3-none-any.whl")
    version("0.9.0", sha256="d853b3c10273ff9bc8bb8b30076d65e2c9685579db736873de6c2232dde148bf", url="https://pypi.org/packages/e3/55/0c1aa72f4317e826a471dc4adc3036acd11d496ded68c4bbac2a88551519/jupyter_events-0.9.0-py3-none-any.whl")
    version("0.8.0", sha256="81f07375c7673ff298bfb9302b4a981864ec64edaed75ca0fe6f850b9b045525", url="https://pypi.org/packages/47/47/cd46c2d3e409bed27338aec1610dfa13da67f64c671f739b7eff0954c14d/jupyter_events-0.8.0-py3-none-any.whl")
    version("0.7.0", sha256="4753da434c13a37c3f3c89b500afa0c0a6241633441421f6adafe2fb2e2b924e", url="https://pypi.org/packages/15/0d/3c67f6c432d8085a3cee250e1e235f27b764be90cc2d16fdcc0b1cee9572/jupyter_events-0.7.0-py3-none-any.whl")
    version("0.6.3", sha256="57a2749f87ba387cd1bfd9b22a0875b889237dbf2edc2121ebb22bde47036c17", url="https://pypi.org/packages/ee/14/e11a93c1b47a69432ee7898f1b55f1da27f2f93b009a34dbdafb9b903f81/jupyter_events-0.6.3-py3-none-any.whl")
    version("0.6.2", sha256="6030f7e997160f5cb6c27f9a1f14df7b520f4a1a6dcd17b894a8f3e69c2b2ffd", url="https://pypi.org/packages/8b/4b/0ce249a805aa99b98429626644fa86875a95bbd08c2c57632c3486faf7fd/jupyter_events-0.6.2-py3-none-any.whl")
    version("0.6.1", sha256="353b165928cd411eecba6b194fd4a80219981e7d8ed2842b19b3c7beb4116258", url="https://pypi.org/packages/48/95/856e48cdfb9bc806bf989f8a2d535aff2ba7bb442a5c3dee677f10e53fb5/jupyter_events-0.6.1-py3-none-any.whl")
    version("0.6.0", sha256="587f3055fe965f023b23b9929b22d2070e8b5c79ef0a42e37bdb12199862f63c", url="https://pypi.org/packages/da/0c/3dcfc130ec1f66f2dec960f3c96e2fbb54ef84e4845e1a821c928a8a6aa7/jupyter_events-0.6.0-py3-none-any.whl")

    with default_args(type="run"):
        depends_on("py-jsonschema@4.18.0:+format-nongpl", when="@0.7:")
        depends_on("py-jsonschema@3.2:+format-nongpl", when="@0.6.1:0.6")
        depends_on("py-jsonschema@4.3:+format-nongpl", when="@0.5:0.6.0")
        depends_on("py-python-json-logger@2.0.4:", when="@0.6:")
        depends_on("py-pyyaml@5.3:", when="@0.6.2:")
        depends_on("py-pyyaml@6.0:", when="@0.6:0.6.1")
        depends_on("py-referencing", when="@0.7:")
        depends_on("py-rfc3339-validator", when="@0.6.1:")
        depends_on("py-rfc3986-validator@0.1.1:", when="@0.6.1:")
        depends_on("py-traitlets@5.3:5.3.0.0,5.4:", when="@0.6:")

