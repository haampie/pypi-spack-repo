##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyFlaskRestful(PythonPackage):
    version("0.3.10", sha256="1cf93c535172f112e080b0d4503a8d15f93a48c88bdd36dd87269bdaf405051b", url="https://pypi.org/packages/d7/7b/f0b45f0df7d2978e5ae51804bb5939b7897b2ace24306009da0cc34d8d1f/Flask_RESTful-0.3.10-py2.py3-none-any.whl")
    version("0.3.9", sha256="ccec650b835d48192138c85329ae03735e6ced58e9b2d9c2146d6c84c06fa53e", url="https://pypi.org/packages/5c/50/4892719b13abd401f40a69359c3d859d0ea76bf78e66db058d6c06a95b01/Flask-RESTful-0.3.9.tar.gz")
    version("0.3.8", sha256="5ea9a5991abf2cb69b4aac19793faac6c032300505b325687d7c305ffaa76915", url="https://pypi.org/packages/67/65/84f3218666fc115497a13ff727f16d02374d07d1924cd4fd72e275294e8b/Flask-RESTful-0.3.8.tar.gz")
    version("0.3.7", sha256="f8240ec12349afe8df1db168ea7c336c4e5b0271a36982bff7394f93275f2ca9", url="https://pypi.org/packages/2f/d6/4dca88aa42124fe372cf21a1fb004535615b09374c906e4e5d6ec114eccc/Flask-RESTful-0.3.7.tar.gz")
    version("0.3.6", sha256="5795519501347e108c436b693ff9a4d7b373a3ac9069627d64e4001c05dd3407", url="https://pypi.org/packages/20/f1/14a62bba209ae189e5c5fa33d5e0b7a4b5969488fa71fd3b8b323860bfc8/Flask-RESTful-0.3.6.tar.gz")
    version("0.3.5", sha256="cce4aeff959b571136b5af098bebe7d3deeca7eb1411c4e722ff2c5356ab4c42", url="https://pypi.org/packages/00/f6/250e9e11e96088a69a410adf6bcaa68651a285f40b2c41e0c27b2d579f4a/Flask-RESTful-0.3.5.tar.gz")
    version("0.3.4", sha256="89f3773363fb0dd235d16c806b7ff8fed8268152d45bf1fc618a12a36dfd1b68", url="https://pypi.org/packages/fc/18/144da33956ec818697d49847fae886b73753d4636e58852ea65546bfffc8/Flask-RESTful-0.3.4.tar.gz")
    version("0.3.3", sha256="30f70682188e6f5bd7915f6188353d35b981b62a880d86b8079c462ee7d9c6b8", url="https://pypi.org/packages/b3/98/c0f9c37c8d103de77a2e3bdd0f39befb4ca59c910f0bff1e6d16c04fb964/Flask-RESTful-0.3.3.tar.gz")
    version("0.3.2", sha256="3577a153d1728b93f7a3688316984f9369d3b68ba283cf4bb4025319285f178d", url="https://pypi.org/packages/90/be/390f352686dfb2690ce72440669699a85cb8b79befd5eb26434f083a78e8/Flask-RESTful-0.3.2.tar.gz")
    version("0.3.1", sha256="b571d6f0ee09d285877b8af981e4815a3fdf98a66cb4528c76ffbd156de2db09", url="https://pypi.org/packages/44/32/a682f42250ffbc16e1c5e30bdd269263001b167be81d978ffd255ec265ec/Flask-RESTful-0.3.1.tar.gz")

    with default_args(type="run"):
        depends_on("py-aniso8601@0.82:", when="@0.3.10:")
        depends_on("py-flask@0.8:", when="@0.3.10:")
        depends_on("py-pytz", when="@0.3.10:")
        depends_on("py-six@1.3:", when="@0.3.10:")

