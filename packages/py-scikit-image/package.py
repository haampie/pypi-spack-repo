# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyScikitImage(PythonPackage):
    # BEGIN VERSIONS
    version("0.23.0-rc0", sha256="8d78737020e9c173af6fcdd14ac7eca88a9169d072f3c8b24e602ba3acf65cf7", url="https://pypi.org/packages/2a/e3/ec27b0d8a63fd8a2effe78bfcea3a56480ed8b0be46e5232ada3f911512a/scikit_image-0.23.0rc0.tar.gz")
    version("0.22.0", sha256="018d734df1d2da2719087d15f679d19285fce97cd37695103deadfaef2873236", url="https://pypi.org/packages/65/c1/a49da20845f0f0e1afbb1c2586d406dc0acb84c26ae293bad6d7e7f718bc/scikit_image-0.22.0.tar.gz")
    version("0.22.0-rc1", sha256="55ce8fc3f304f6eb574110ff5c10287924990bb5d2a5f79eb01aea84236d0857", url="https://pypi.org/packages/2e/ee/22754555a2991c9c1b909c7ae92b0d2fe765be1a7fbb0473baaf1d9d3061/scikit_image-0.22.0rc1.tar.gz")
    version("0.21.0", sha256="b33e823c54e6f11873ea390ee49ef832b82b9f70752c8759efd09d5a4e3d87f0", url="https://pypi.org/packages/1d/c2/a54d5e6e2d6708e0722a1aaccef4b7cc1e6df6f76c8b4ce98cd6d0c332c3/scikit_image-0.21.0.tar.gz")
    version("0.21.0-rc1", sha256="98b7eb01ad1645475440e2f5fed82bc06b657fe31f648bc2a4c163dd3b794e79", url="https://pypi.org/packages/9a/31/ecc1b9d98cd3dcc50fd6e3fe2839fd111c1e43ee356452e2fad189da6d38/scikit_image-0.21.0rc1.tar.gz")
    version("0.20.0", sha256="2cd784fce18bd31d71ade62c6221440199ead03acf7544086261ee032264cf61", url="https://pypi.org/packages/03/55/0ff6e41c39c64d9ad18bf31c953c28f525533609c7371fa2790558ca8197/scikit_image-0.20.0.tar.gz")
    version("0.20.0-rc8", sha256="492499eb052b27c47ccea8fc96a277e79a5e498dfc3720100c88a13559c7c99d", url="https://pypi.org/packages/03/d6/a1495c30d82bd7a0f7e76bcc31273485ddbee92347d5b99ccf8e309f47ae/scikit_image-0.20.0rc8.tar.gz")
    version("0.19.3", sha256="24b5367de1762da6ee126dd8f30cc4e7efda474e0d7d70685433f0e3aa2ec450", url="https://pypi.org/packages/00/d4/6682033d02917b10a2024dbe5a0636d2338b0799f7bd1885508fb114aec9/scikit-image-0.19.3.tar.gz")
    version("0.19.2", sha256="d433b4642a6f8219e749dfbbe4b5e742d560996540c9749ede510274d061866d", url="https://pypi.org/packages/83/7d/756dcbf1f2fcbfd60e14842aeadefa2354eff714ed4ec3ae7a107a5787d1/scikit-image-0.19.2.tar.gz")
    version("0.19.1", sha256="48f00ee1e8ec2818ae6a152c72df15f4db7f566e839f5c34e1a0c3c9e5210138", url="https://pypi.org/packages/e7/54/4b57761f25be6e2536130ca3bc8742dee45bb9047c5df798197203220e37/scikit-image-0.19.1.tar.gz")
    version("0.19.0", sha256="bcc79d06ca88ec081d1b0eacc0ae2ca3abbd993a5d89dc54fabe25f2480f0626", url="https://pypi.org/packages/25/8d/c5f060de238a6ed08e24b607f0a9a57d73e3fa654eed2a544571f73dc78a/scikit-image-0.19.0.tar.gz")
    version("0.19.0-rc0", sha256="95b0791610d359aac30d9f5073baabb531f9c902308a8507fe728f6d1f9a1fb1", url="https://pypi.org/packages/66/a0/5ff92987539f54405c1b8a0424f8378e9a816db6377a88d4edda5f2650ba/scikit-image-0.19.0rc0.tar.gz")
    version("0.18.3", sha256="ecae99f93f4c5e9b1bf34959f4dc596c41f2f6b2fc407d9d9ddf85aebd3137ca", url="https://pypi.org/packages/c0/f2/8653713d01c46ed679f37848528adae1e988e1120f16fa589b200cca1720/scikit-image-0.18.3.tar.gz")
    version("0.18.2", sha256="32ff472355fbf8ab40a8e9ed685906c6c51a863f1ea8737882d26be9221631f3", url="https://pypi.org/packages/e1/e9/98185042c1c3cc6b20e2a5dd8cc74215b9fee7268c82781a7c4f7cc854f4/scikit-image-0.18.2.tar.gz")
    version("0.18.2-rc2", sha256="c0993e920558fa2e503da97f12414ffd5babf3ddfc9c888d3289dcb0d9f58d1d", url="https://pypi.org/packages/d2/da/9463122ed45833dd54dde7683514c690744db000a4e7c964f2b58a4b9ff6/scikit-image-0.18.2rc2.tar.gz")
    version("0.18.1", sha256="fbb618ca911867bce45574c1639618cdfb5d94e207432b19bc19563d80d2f171", url="https://pypi.org/packages/6e/be/a8ccf9d949a55023cf02438310e068c263ce3dd6bbf31f9229d3db6e551a/scikit-image-0.18.1.tar.gz")
    version("0.18.0", sha256="a0c78a117080101dbeeaa430804fe9512575cf2696ddbf822a7ee30d0776f5da", url="https://pypi.org/packages/f5/0d/bcdf6e43c3b40b3edc0a1e2f8bfa3cfad46c18869aeff31ec2b209f61e79/scikit-image-0.18.0.tar.gz")
    version("0.17.2", sha256="bd954c0588f0f7e81d9763dc95e06950e68247d540476e06cb77bcbcd8c2d8b3", url="https://pypi.org/packages/54/fd/c1b0bb8f6f12ef9b4ee8d7674dac82cd482886f8b5cd165631efa533e237/scikit-image-0.17.2.tar.gz")
    version("0.14.2", sha256="1afd0b84eefd77afd1071c5c1c402553d67be2d7db8950b32d6f773f25850c1f", url="https://pypi.org/packages/7f/bd/74ed9add17c3c7529c18693c17846753649c6cf2e674e7482fbf85d636cb/scikit-image-0.14.2.tar.gz")
    version("0.12.3", sha256="82da192f0e524701e89c5379c79200bc6dc21373f48bf7778a864c583897d7c7", url="https://pypi.org/packages/86/d0/b0192dc9a544da90f2d9150bcd84b981c6873e42a1f752b6affb89180ad8/scikit-image-0.12.3.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("python@3.10:", when="@0.23:")
        depends_on("python@3.9:", when="@0.22")
        depends_on("py-cloudpickle@0.2:", when="@0.14")
        depends_on("py-dask@1:+array", when="@0.14.2")
        depends_on("py-imageio@2.33:", when="@0.23:")
        depends_on("py-imageio@2.27:", when="@0.21.0:0.22")
        depends_on("py-imageio@2.27", when="@0.21.0-rc1")
        depends_on("py-imageio@2.4.1:", when="@0.20.0-rc8:0.20")
        depends_on("py-imageio@2.3:", when="@0.16:0.17")
        depends_on("py-lazy-loader@0.3:", when="@0.22:")
        depends_on("py-lazy-loader@0.2:", when="@0.21")
        depends_on("py-lazy-loader@0.1:", when="@0.20.0-rc8:0.20")
        depends_on("py-matplotlib@2.0.0:3.0.0-rc2,3.0.1:", when="@0.15:0.17")
        depends_on("py-matplotlib@2.0.0:", when="@0.14")
        depends_on("py-networkx@2.8:", when="@0.20.0-rc8:")
        depends_on("py-networkx@2:", when="@0.15:0.17")
        depends_on("py-networkx@1.8:", when="@0.13:0.14")
        depends_on("py-numpy@1.23.0:", when="@0.23:")
        depends_on("py-numpy@1.22.0:", when="@0.22")
        depends_on("py-numpy@1.21.1:", when="@0.20.0-rc8:0.21")
        depends_on("py-numpy@1.15.1:", when="@0.17")
        depends_on("py-packaging@21:", when="@0.21:")
        depends_on("py-packaging@20:", when="@0.20.0-rc8:0.20")
        depends_on("py-pillow@9.1:", when="@0.23:")
        depends_on("py-pillow@9.0.1:", when="@0.20.0-rc8:0.22")
        depends_on("py-pillow@4.3:7.0,7.1.2:", when="@0.17")
        depends_on("py-pillow@4.3:", when="@0.14:0.16")
        depends_on("py-pooch@0.5.2:", when="@0.17:0.17.1")
        depends_on("py-pywavelets@1.1.1:", when="@0.17,0.20.0-rc8:0.21")
        depends_on("py-pywavelets@0.4:", when="@0.13:0.16")
        depends_on("py-scipy@1.9.0:", when="@0.23:")
        depends_on("py-scipy@1.8.0:", when="@0.21:0.22")
        depends_on("py-scipy@1.8.0:", when="@0.20.0-rc8:0.20 ^python@3.9.1:")
        depends_on("py-scipy@1.8.0:1.9.1", when="@0.20.0-rc8:0.20 ^python@:3.9.0")
        depends_on("py-scipy@1.0.1:", when="@0.17")
        depends_on("py-scipy@0.17:", when="@0.13:0.15")
        depends_on("py-six@1.10:", when="@0.14")
        depends_on("py-tifffile@2022.8.12:", when="@0.21:")
        depends_on("py-tifffile@2019.7.26:", when="@0.17,0.20.0-rc8:0.20")
    # END DEPENDENCIES

