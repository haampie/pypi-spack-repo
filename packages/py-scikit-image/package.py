# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyScikitImage(PythonPackage):
    # BEGIN VERSIONS
    version("0.20.0", sha256="2cd784fce18bd31d71ade62c6221440199ead03acf7544086261ee032264cf61", url="https://pypi.org/packages/03/55/0ff6e41c39c64d9ad18bf31c953c28f525533609c7371fa2790558ca8197/scikit_image-0.20.0.tar.gz")
    version("0.19.3", sha256="24b5367de1762da6ee126dd8f30cc4e7efda474e0d7d70685433f0e3aa2ec450", url="https://pypi.org/packages/00/d4/6682033d02917b10a2024dbe5a0636d2338b0799f7bd1885508fb114aec9/scikit-image-0.19.3.tar.gz")
    version("0.18.3", sha256="ecae99f93f4c5e9b1bf34959f4dc596c41f2f6b2fc407d9d9ddf85aebd3137ca", url="https://pypi.org/packages/c0/f2/8653713d01c46ed679f37848528adae1e988e1120f16fa589b200cca1720/scikit-image-0.18.3.tar.gz")
    version("0.18.1", sha256="fbb618ca911867bce45574c1639618cdfb5d94e207432b19bc19563d80d2f171", url="https://pypi.org/packages/6e/be/a8ccf9d949a55023cf02438310e068c263ce3dd6bbf31f9229d3db6e551a/scikit-image-0.18.1.tar.gz")
    version("0.17.2", sha256="bd954c0588f0f7e81d9763dc95e06950e68247d540476e06cb77bcbcd8c2d8b3", url="https://pypi.org/packages/54/fd/c1b0bb8f6f12ef9b4ee8d7674dac82cd482886f8b5cd165631efa533e237/scikit-image-0.17.2.tar.gz")
    version("0.14.2", sha256="1afd0b84eefd77afd1071c5c1c402553d67be2d7db8950b32d6f773f25850c1f", url="https://pypi.org/packages/7f/bd/74ed9add17c3c7529c18693c17846753649c6cf2e674e7482fbf85d636cb/scikit-image-0.14.2.tar.gz")
    version("0.12.3", sha256="82da192f0e524701e89c5379c79200bc6dc21373f48bf7778a864c583897d7c7", url="https://pypi.org/packages/86/d0/b0192dc9a544da90f2d9150bcd84b981c6873e42a1f752b6affb89180ad8/scikit-image-0.12.3.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("python@3.8:", when="@0.20:0.21")
        depends_on("python@3.7:", when="@0.18.0-rc2:0.19")
        depends_on("py-cloudpickle@0.2:", when="@0.14")
        depends_on("py-dask@1:+array", when="@0.14.2")
        depends_on("py-imageio@2.4.1:", when="@0.20.0-rc8:0.20")
        depends_on("py-imageio@2.3:", when="@0.16:0.17")
        depends_on("py-lazy-loader@0.1:", when="@0.20.0-rc8:0.20")
        depends_on("py-matplotlib@2.0.0:3.0.0-rc2,3.0.1:", when="@0.15:0.17")
        depends_on("py-matplotlib@2.0.0:", when="@0.14")
        depends_on("py-networkx@2.8:", when="@0.20.0-rc8:")
        depends_on("py-networkx@2:", when="@0.15:0.17")
        depends_on("py-networkx@1.8:", when="@0.13:0.14")
        depends_on("py-numpy@1.21.1:", when="@0.20.0-rc8:0.21")
        depends_on("py-numpy@1.15.1:", when="@0.17")
        depends_on("py-packaging@20:", when="@0.20.0-rc8:0.20")
        depends_on("py-pillow@9.0.1:", when="@0.20.0-rc8:0.22")
        depends_on("py-pillow@4.3:7.0,7.1.2:", when="@0.17")
        depends_on("py-pillow@4.3:", when="@0.14:0.16")
        depends_on("py-pywavelets@1.1.1:", when="@0.17,0.20.0-rc8:0.21")
        depends_on("py-pywavelets@0.4:", when="@0.13:0.16")
        depends_on("py-scipy@1.8.0:1.9.1", when="@0.20.0-rc8:0.20 ^python@:3.8")
        depends_on("py-scipy@1.8.0:", when="@0.20.0-rc8:0.20 ^python@3.9:")
        depends_on("py-scipy@1.0.1:", when="@0.17")
        depends_on("py-scipy@0.17:", when="@0.13:0.15")
        depends_on("py-six@1.10:", when="@0.14")
        depends_on("py-tifffile@2019.7.26:", when="@0.17,0.20.0-rc8:0.20")
    # END DEPENDENCIES

