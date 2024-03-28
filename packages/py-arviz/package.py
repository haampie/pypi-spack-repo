# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyArviz(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("0.17.1", sha256="c6d24bea85a801d781d95cd21b583079ae882aa4a25ff385321a83eb47ee1e4a", url="https://pypi.org/packages/d7/4d/cb2a58af7c747c30af357972151233f5d24d1699276e2d38621e57a22aa8/arviz-0.17.1-py3-none-any.whl")
    version("0.17.0", sha256="3f00f83af5b8db129b01fa9c52a8138a25da32e1154a905b6dddf5e88d1f7089", url="https://pypi.org/packages/9b/c5/6fb0c9b9941cd1e59bbd3d2cd20ccaecbb156ec2030a027cfbb0b6837657/arviz-0.17.0-py3-none-any.whl")
    version("0.16.1", sha256="872d1d685719f81a31f94c25278cbaef314df7f6cad0671935f26a006182b8d4", url="https://pypi.org/packages/8c/43/b5be65de19e4ca0cfeb522addc3ac4abdafa9d29f3512dec05b8a672c615/arviz-0.16.1-py3-none-any.whl")
    version("0.16.0", sha256="c6fab85030f0400ffdc28cb6c8cd09c0f741fd668b88e412dec02bc8a5d1bd4d", url="https://pypi.org/packages/e8/fb/ead5d542ce3ba5383d6d5a169ba0318f39ba231738908651043e03c39047/arviz-0.16.0-py3-none-any.whl")
    version("0.15.1", sha256="120695738fb81cc39e8da98b8b751f8f08c618267efda2a6dcb3f1511b599311", url="https://pypi.org/packages/95/97/af3c62d325ce05cf8aa8dea095de5dde683afa41fd064a4d4679c2a85c09/arviz-0.15.1-py3-none-any.whl")
    version("0.15.0", sha256="24f46d864c050d3ad422e7a0ebb93735dd9a0a38cc5b2cf5bfa8254a35ea63b4", url="https://pypi.org/packages/7b/b6/4841405002cb56951bd819365664105b9c29f0a9bc581b0dce3537c009c8/arviz-0.15.0-py3-none-any.whl")
    version("0.14.0", sha256="40cc4aa478173b0ac5e30dfdfd381c284a38672f3f4d35ed851d3987349dcca1", url="https://pypi.org/packages/b4/6c/251a8bb1f20e961547d3822648931c321b638be522c75b0f66d983896d7e/arviz-0.14.0-py3-none-any.whl")
    version("0.13.0", sha256="c96c23726bd458f0266d2713ff728b4f7fcd306f0cbfa6399b6ede5139325b48", url="https://pypi.org/packages/ae/58/5082e73697435476be518608f1d038f5ea64b26165c0b0b7337c4cbf040b/arviz-0.13.0-py3-none-any.whl")
    version("0.12.1", sha256="95a2b94995e30683b52c30f82326eed1544d057244bea468d421d5c42ed1f245", url="https://pypi.org/packages/95/c0/dd9b4bf085d974de1c6d5fffea8e25153e8208ece6b363fa3a9263ed7e51/arviz-0.12.1-py3-none-any.whl")
    version("0.12.0", sha256="08ef308a90ddbe52332ef90aeffa367ea080960ada4104a88716cc234dbcee1f", url="https://pypi.org/packages/90/ba/97a37d1208434357bbc8b249063b2afb6fce34eeb1aab101d740adf7c4f6/arviz-0.12.0-py3-none-any.whl")
    version("0.6.1", sha256="fa613e6f796501f352462c747638d7e1d7ae3e3ed36e665e547def1b2524602c", url="https://pypi.org/packages/ec/8b/83472d660e004a69b8e7b3c1dd12a607167774097138445d0dda1a3590dc/arviz-0.6.1-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("python@3.9:", when="@0.16:")
        depends_on("py-h5netcdf@1.0.2:", when="@0.15:")
        depends_on("py-matplotlib@3.2.0:", when="@0.15:0.16")
        depends_on("py-matplotlib@3.5.0:", when="@0.13:0.14,0.17:")
        depends_on("py-matplotlib@3.0.0:", when="@0.2:0.12")
        depends_on("py-netcdf4", when="@0.1:0.14")
        depends_on("py-numpy@1.22.0:1", when="@0.17:")
        depends_on("py-numpy@1.21.0:1", when="@0.16.1:0.16")
        depends_on("py-numpy@1.21.0:", when="@0.16:0.16.0")
        depends_on("py-numpy@1.20.0:", when="@0.13.0:0.15")
        depends_on("py-numpy@1.12.0:", when="@0.5:0.12")
        depends_on("py-packaging", when="@0.6:")
        depends_on("py-pandas@1.3.0:", when="@0.15.1:0.16")
        depends_on("py-pandas@1.4.0:", when="@0.13:0.15.0,0.17:")
        depends_on("py-pandas@0.23.0:", when="@0.5:0.12")
        depends_on("py-scipy@1.8.0:", when="@0.13:")
        depends_on("py-scipy@0.19:", when="@0.5:0.12")
        depends_on("py-setuptools@60:", when="@0.13:")
        depends_on("py-setuptools@38.4:", when="@0.10:0.12")
        depends_on("py-typing-extensions@4.1:", when="@0.13:")
        depends_on("py-typing-extensions@3.7.4.3:", when="@0.12")
        depends_on("py-xarray@0.21:", when="@0.13:")
        depends_on("py-xarray@0.16.1:", when="@0.10:0.12")
        depends_on("py-xarray@0.11:", when="@0.5:0.9")
        depends_on("py-xarray-einstats@0.3:", when="@0.13:")
        depends_on("py-xarray-einstats@0.2:", when="@0.12.1:0.12")
    # END DEPENDENCIES

