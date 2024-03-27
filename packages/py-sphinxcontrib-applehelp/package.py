##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PySphinxcontribApplehelp(PythonPackage):
    version("1.0.8", sha256="cb61eb0ec1b61f349e5cc36b2028e9e7ca765be05e49641c97241274753067b4", url="https://pypi.org/packages/56/89/fea3fbf6785b388e6cb8a1beaf62f96e80b37311bdeed6e133388a732426/sphinxcontrib_applehelp-1.0.8-py3-none-any.whl")
    version("1.0.7", sha256="094c4d56209d1734e7d252f6e0b3ccc090bd52ee56807a5d9315b19c122ab15d", url="https://pypi.org/packages/c0/0c/261c0949083c0ac635853528bb0070c89e927841d4e533ba0b5563365c06/sphinxcontrib_applehelp-1.0.7-py3-none-any.whl")
    version("1.0.6", sha256="c0578efa23cab5a2f3aaa8af5691b952433f4fdfaac255befd3452448e7ea4a4", url="https://pypi.org/packages/b1/db/2c9a62f9d7c8abf45fa79d28a9d0c80e16cb42deac58a699cbd952efda1a/sphinxcontrib_applehelp-1.0.6-py3-none-any.whl")
    version("1.0.5", sha256="2bf6dc21596142496e3a7623adc6918014e6a9bbfeeeb37d27543727bebabd0f", url="https://pypi.org/packages/57/57/1cdaff9321329139ffb0616b9907f2ddf46fa9a6a9488a93f049b2325472/sphinxcontrib_applehelp-1.0.5-py3-none-any.whl")
    version("1.0.4", sha256="29d341f67fb0f6f586b23ad80e072c8e6ad0b48417db2bde114a4c9746feb228", url="https://pypi.org/packages/06/c1/5e2cafbd03105ce50d8500f9b4e8a6e8d02e22d0475b574c3b3e9451a15f/sphinxcontrib_applehelp-1.0.4-py3-none-any.whl")
    version("1.0.3", sha256="ba0f2a22e6eeada8da6428d0d520215ee8864253f32facf958cca81e426f661d", url="https://pypi.org/packages/f1/c0/14cb04bc35d1aa062ae89497d5d1a6aa47d0a1c9bba140a21a1bb386adef/sphinxcontrib.applehelp-1.0.3-py3-none-any.whl")
    version("1.0.2", sha256="806111e5e962be97c29ec4c1e7fe277bfd19e9652fb1a4392105b43e01af885a", url="https://pypi.org/packages/dc/47/86022665a9433d89a66f5911b558ddff69861766807ba685de2e324bd6ed/sphinxcontrib_applehelp-1.0.2-py2.py3-none-any.whl")
    version("1.0.1", sha256="fb8dee85af95e5c30c91f10e7eb3c8967308518e0f7488a2828ef7bc191d0d5d", url="https://pypi.org/packages/13/9a/4428b3114d654cb1cd34d90d5e6fab938d5436f94a571155187ea1dd78b4/sphinxcontrib_applehelp-1.0.1-py2.py3-none-any.whl")
    version("1.0.0", sha256="0d7c946681539cc4999d5d16de91689221a79a5032a448267b11492d1d407dcf", url="https://pypi.org/packages/68/a4/6a6704005f3828106bd513bdf9d8f671e650efbc6e9f686a07c26a8a0c97/sphinxcontrib_applehelp-1.0.0-py2.py3-none-any.whl")

    with default_args(type="run"):
        depends_on("python@3.9:", when="@1.0.5:")
        depends_on("py-sphinx@5.0.0:", when="@1.0.5:1.0.7")

