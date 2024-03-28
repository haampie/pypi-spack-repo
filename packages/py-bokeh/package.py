# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyBokeh(PythonPackage):
    # BEGIN VERSIONS
    version("3.4.0", sha256="d8d9ba026b734317740f90a8a58502d63c76b96c58752fc421ad4aa04df1fbcd", url="https://pypi.org/packages/f9/24/d8949753839db67197a33014b854cbed2126f8c871e03723e7abddcca12a/bokeh-3.4.0-py3-none-any.whl")
    version("3.3.4", sha256="ad7b6f89d0a7c2be01eff1db0ca24e2755ac41de14539db919a62e791809c309", url="https://pypi.org/packages/39/ba/aefd7aacc9e086e2c7f3bb42e99cb8e2a8f24dcb4bf78519ef25a9102988/bokeh-3.3.4-py3-none-any.whl")
    version("3.3.3", sha256="8f4a95f80e6e03a59eb0ae3c1bce67db3c888a7a5c4f287d4ef9f817849a8b2a", url="https://pypi.org/packages/74/42/1530abfe144a3d7db290de6c9989ecd5c01239fe26d3b27ccb0aa631cb91/bokeh-3.3.3-py3-none-any.whl")
    version("3.3.2", sha256="f70bcea96c72f85bbeae01b9dcd30a9f27aa48fbfaf8e6f45b6958dfcd08e5c5", url="https://pypi.org/packages/8f/96/3168eb2dd94fd62ef2b9d06456344754c5a09bb7fa0af917b4d6f27e1a2c/bokeh-3.3.2-py3-none-any.whl")
    version("3.3.1", sha256="783fb503d80306fb1e3c06e9c775d98675bf9e07514a776d7109178798e85683", url="https://pypi.org/packages/67/a7/175a55ed75e0d64fdea3f28dfbd58010b320d33063c1b4de244736868226/bokeh-3.3.1-py3-none-any.whl")
    version("3.3.0", sha256="65e36824c99fd46530c559263c6d14eabed6945370cd3beffc2eeedb62d6db6d", url="https://pypi.org/packages/d8/7b/74b234af7fca8c688c46f63fec30665b0c3c1f3eac2da756306691aee122/bokeh-3.3.0-py3-none-any.whl")
    version("3.2.2", sha256="e31670a013e1ff15c3d4d04f587c8162c4cc9fe1af507fd741d295e6c4e1225b", url="https://pypi.org/packages/84/60/33f23dbb15fcd785d6287bdd6fa8c9d836dacb40e21c14aad41a57a0ec0f/bokeh-3.2.2-py3-none-any.whl")
    version("3.2.1", sha256="71b882c2c9233750d80b941ebb980e03d5112f27f84c7bb2293af5c210a8e21c", url="https://pypi.org/packages/c6/5d/46cde55344ad96a0570e2f72d9df428349a6a800448f6a5b6140c337f930/bokeh-3.2.1-py3-none-any.whl")
    version("3.2.0", sha256="e6d168bd024bef7b6e11536610d4767997a910242b73e9dee31c84eea5276f64", url="https://pypi.org/packages/56/98/da78cec88a7c47b761c9b3a18677b5508ef17417184396b3d1361fc811f1/bokeh-3.2.0-py3-none-any.whl")
    version("3.1.1", sha256="a542a076ce326f81bf6d226355458572d39fe8fc9b547eab9728a2f1d71e4bdb", url="https://pypi.org/packages/96/f5/3d3d179f87908a4d4c8d2046014b2c6b38e92572ebb0ff2987212d0ee210/bokeh-3.1.1-py3-none-any.whl")
    version("2.4.3", sha256="104d2f0a4ca7774ee4b11e545aa34ff76bf3e2ad6de0d33944361981b65da420", url="https://pypi.org/packages/15/06/706a9c43436cd0c3e2f4b94e93ae837e74965e59565c596b727974a74169/bokeh-2.4.3-py3-none-any.whl")
    version("2.4.3-rc1", sha256="45b8f852ea985fbae1ad777d0c5b0575cf6f214d920ba1632bfb01478aa4dcad", url="https://pypi.org/packages/1b/9d/6543de6bc2a88b4b5096da62ef5918dbe24ef2d6cc84df9945af1d0cda33/bokeh-2.4.3rc1-py3-none-any.whl")
    version("2.4.3.dev4", sha256="fb67af3c0cbcc49a2511ca3e28159665a9adf3c0cfbc97f8030eaa2a4d83234e", url="https://pypi.org/packages/82/d8/58c033394f57970b053c606dc56f564f1b353e3704efab5c60d8fcdbd5a2/bokeh-2.4.3.dev4-py3-none-any.whl")
    version("2.4.3.dev3", sha256="7aa9fa8a0c5513f47408613a7f1f9c20540ac3a574aac1378c3363afce79a03e", url="https://pypi.org/packages/48/01/bfc9a257802fd86df739a089627acf13267ca9da2cd35982f7f6ad4f6dd9/bokeh-2.4.3.dev3-py3-none-any.whl")
    version("2.4.3.dev1", sha256="ecb5cbc5ea2bc61b6c0710a9563a6a5d98785ee84b59858da14d07eac8cd3104", url="https://pypi.org/packages/47/4c/3e97fcf3e8cd91c9bccf910b564c82d8f8f678b86534f52eeff7a39efa99/bokeh-2.4.3.dev1-py3-none-any.whl")
    version("2.4.2", sha256="2a842d717feeee802e668054277c09054b6f1561557a16dddaf5f7c452f2728c", url="https://pypi.org/packages/87/6c/c2b2911555d34c9fa24ad0f41cf42ba6887e279a521bca0cb3d091d77c17/bokeh-2.4.2-py3-none-any.whl")
    version("2.4.2-rc1", sha256="fa4101e3a7a603d9ea250d504c87ccbd3569a02e9e976cabb8a3ebadfcf18bbb", url="https://pypi.org/packages/c2/5e/b5d94704ffb6821e3dfc85bfac52326c44ce02fde09e2a4b7add36fdf515/bokeh-2.4.2rc1-py3-none-any.whl")
    version("2.4.2.dev1", sha256="9f9943af37dccbf71a86204390f959723fb245fcd261156a27dcc41ab8d412b2", url="https://pypi.org/packages/9a/2b/b8b12ea0d7c538b68e0c29d030ca279a8b0d19bc0cf655acbb4fb41de24f/bokeh-2.4.2.dev1-py3-none-any.whl")
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
        depends_on("python@3.10:", when="@3.5:")
        depends_on("python@3.9:", when="@3.2:3.4")
        depends_on("py-contourpy@1.2:", when="@3.4:")
        depends_on("py-contourpy@1:", when="@3:3.3,3.4.0.dev:3.4.0.dev3")
        depends_on("py-jinja2@2.9:", when="@2.4:")
        depends_on("py-numpy@1.16.0:", when="@3.1:")
        depends_on("py-numpy@1.11.3:", when="@2.4:3.0")
        depends_on("py-packaging@16.8:", when="@2.4:")
        depends_on("py-pandas@1.2.0:", when="@3:")
        depends_on("py-pillow@7.1:", when="@2.4:")
        depends_on("py-pyyaml", when="@2.4:")
        depends_on("py-tornado@6.2:", when="@3.4:")
        depends_on("py-tornado@5.1:", when="@2.4:3.3,3.4.0.dev:3.4.0.dev6")
        depends_on("py-typing-extensions@3.10:", when="@2.4:3.0.0")
        depends_on("py-xyzservices@2021.9.1:", when="@3:")
    # END DEPENDENCIES

