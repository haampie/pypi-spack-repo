# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyBokeh(PythonPackage):
    # BEGIN VERSIONS
    version("3.3.1", sha256="783fb503d80306fb1e3c06e9c775d98675bf9e07514a776d7109178798e85683", url="https://pypi.org/packages/67/a7/175a55ed75e0d64fdea3f28dfbd58010b320d33063c1b4de244736868226/bokeh-3.3.1-py3-none-any.whl")
    version("2.4.3", sha256="104d2f0a4ca7774ee4b11e545aa34ff76bf3e2ad6de0d33944361981b65da420", url="https://pypi.org/packages/15/06/706a9c43436cd0c3e2f4b94e93ae837e74965e59565c596b727974a74169/bokeh-2.4.3-py3-none-any.whl")
    version("2.4.1", sha256="b270d6ef899598fe26e64b6ae08e30f8d67a177baa1f5bfe18e1979a81bb7c4d", url="https://pypi.org/packages/26/96/3e56636664e497728b14738fea5e54297de1bc0f451b7206325a6453e73d/bokeh-2.4.1-py3-none-any.whl")
    version("2.4.0", sha256="91a7c3b8a42d9275df26f13269859a1add82dc9e5dda316f7476ad76a5a10851", url="https://pypi.org/packages/fa/d3/da92cabfdfecd47b9efaea27833aa8e9512f9ad4818236be511f3486cda1/bokeh-2.4.0-py3-none-any.whl")
    version("2.3.3", sha256="a5fdcc181835561447fcc5a371300973fce4114692d5853addec284d1cdeb677", url="https://pypi.org/packages/40/85/9c8c47dc99671590e21d0cecf5cf1208db0ddb525093b2fecdbb233e3645/bokeh-2.3.3.tar.gz")
    version("1.3.4", sha256="e2d97bed5b199a10686486001fed5c854e4c04ebe28859923f27c52b93904754", url="https://pypi.org/packages/89/25/a07183dd96ca22dafe429254985cbf8241ccd35730c5568d6502b3bc6bb7/bokeh-1.3.4.tar.gz")
    version("0.12.2", sha256="18fd6a1a4f37c8ad2f8f14d3368eefc0ae116ae0621b2bfd7d00cc9db772461c", url="https://pypi.org/packages/7b/81/6422f47023358a749cf7d5f7a748410cc933af3c9726383189b6c84254e3/bokeh-0.12.2.zip")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("python@3.9:", when="@3.2:3.4")
        depends_on("python@3.7:", when="@2.4:2,3.0.0.dev:3.0.0.dev2")
        depends_on("py-contourpy@1:", when="@3:3.3,3.4.0.dev:3.4.0.dev3")
        depends_on("py-jinja2@2.9:", when="@2.4:")
        depends_on("py-numpy@1.16.0:", when="@3.1:")
        depends_on("py-numpy@1.11.3:", when="@2.4:3.0")
        depends_on("py-packaging@16.8:", when="@2.4:")
        depends_on("py-pandas@1.2.0:", when="@3:")
        depends_on("py-pillow@7.1:", when="@2.4:")
        depends_on("py-pyyaml", when="@2.4:")
        depends_on("py-tornado@5.1:", when="@2.4:3.3,3.4.0.dev:3.4.0.dev6")
        depends_on("py-typing-extensions@3.10:", when="@2.4:3.0.0")
        depends_on("py-xyzservices@2021.9.1:", when="@3:")
    # END DEPENDENCIES

