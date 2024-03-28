# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PySnakemakeInterfaceCommon(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("1.17.1", sha256="2fdc4f2d778cad5284e83f35d1c2328b08cd6b8b9b29e522107f1a3c5ae771da", url="https://pypi.org/packages/6b/70/b6a53b63958dfa502ed498147d1e37a127d1be55ed2617a14047e79dcaf2/snakemake_interface_common-1.17.1-py3-none-any.whl")
    version("1.17.0", sha256="86657236175eb31e387dd3d85e248c2554d381f264e00ced2490b2d5525b0187", url="https://pypi.org/packages/59/44/e1117cf00e28a60bf97b696f333c6045c6c42a25b83f65241b965d513269/snakemake_interface_common-1.17.0-py3-none-any.whl")
    version("1.16.0", sha256="3226dd499445f6aa1ea1c2b6141adc0f65b236084f9815b16be23355b249bab7", url="https://pypi.org/packages/db/b8/e2f2654d91ccc1dd12d3a46aa63d45074057a2d797ef1655438fe64ec449/snakemake_interface_common-1.16.0-py3-none-any.whl")
    version("1.15.4", sha256="19fa1c0d67c5427e3f71ee8cea1729937f214c401032c322acf08bb9cf1e2f10", url="https://pypi.org/packages/04/b2/dc563ff38810b6b02d9455f45bf28d48b5de00c7f26634145b12b703279b/snakemake_interface_common-1.15.4-py3-none-any.whl")
    version("1.15.3", sha256="78241fbbce2b8cc33a3024ddd9f0fcc697f79c6b61e84677d6478fbc6cfa0c0f", url="https://pypi.org/packages/0d/b6/6262b829cb77ed1a89b363deb11777354bbab36646e784caa65fb13cc660/snakemake_interface_common-1.15.3-py3-none-any.whl")
    version("1.15.2", sha256="3f9d3ba00017ccf5d04b5f7b878ef1a3a7fda45a928d17ab362a6854dedf8643", url="https://pypi.org/packages/9b/3a/69551bc2429a2a7e4779059c64b5f4722d4b9c405da8553455e5d0fa744b/snakemake_interface_common-1.15.2-py3-none-any.whl")
    version("1.15.1", sha256="3fdf0c2a9c37969ea099e1aedab62acf44e9c047abf5531e81acdb22f444686c", url="https://pypi.org/packages/c6/df/e635cb5089a7e5a8dcb525cb5ea807ff5af2d39ac8cf8ba3dd724325a1ed/snakemake_interface_common-1.15.1-py3-none-any.whl")
    version("1.15.0", sha256="76981f69787dc20b464363b293d2b54d5f5a2e7c32ec5ea7de9ebb94aa5a150e", url="https://pypi.org/packages/86/3f/031bd97846706f88b006776626e148231765a3a76da6ac019849b63737ad/snakemake_interface_common-1.15.0-py3-none-any.whl")
    version("1.14.5", sha256="cb13259f125ba0bfb9183f6f57ce132a7bfe26378c283ae862c499711eb17e21", url="https://pypi.org/packages/32/5f/8ce0a33e36066217c20f4b145c02cf2a72802db55d6b615860d2bceb4703/snakemake_interface_common-1.14.5-py3-none-any.whl")
    version("1.14.4", sha256="5b82010d5a6c03e0a839bfb5191d0e702d40d911f178c1484f6921351364d403", url="https://pypi.org/packages/bb/62/08723d54b0c73ba46dc78e833d3a4237264196a078e239f49f9a48e939fd/snakemake_interface_common-1.14.4-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-argparse-dataclass@2:", when="@1.4:")
        depends_on("py-configargparse@1.7:", when="@1.9.2:")
    # END DEPENDENCIES

