##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyUrwid(PythonPackage):
    version("2.6.9", sha256="df9f5504cc6fb07694392dd5862caf27a998bccde11513c6ea2ef2e0e1008852", url="https://pypi.org/packages/27/e5/62902d1fd709f38694280d5f11825303fddd3345bf0f956b77b935076d2c/urwid-2.6.9-py3-none-any.whl")
    version("2.6.8", sha256="c14970e1ad8e149f454a07cce1e75dbe94b2342f509dc1a626fb2e29f2632837", url="https://pypi.org/packages/9e/ae/bfe7c9950cebb6b2769471cc7095a39482685fd52fb3ceb7c9db814347d5/urwid-2.6.8-py3-none-any.whl")
    version("2.6.7", sha256="80b922d2051db6abe598b7e1b0b31d8d04fcc56d35bb1ec40b3c128fa0bd23ab", url="https://pypi.org/packages/8a/35/d6c799ab6148784932e63209dd7dd0b58fe38e23bc81c92c7210e3f2c458/urwid-2.6.7-py3-none-any.whl")
    version("2.6.6", sha256="c9c567af8a0a48aac3b7676a029d524118df7a579038d32d878d72e77cde7918", url="https://pypi.org/packages/f2/03/0604d7bf4e6c5a8fa63bac81b1d85a7a55d6a4397b9f4fe7d641ccc8f3e9/urwid-2.6.6-py3-none-any.whl")
    version("2.6.5", sha256="19203f237103e384045b882ab33298fde1c7d5de16c20d0b7fc7f17bc36f25f9", url="https://pypi.org/packages/a0/19/3585aba47e916af9306417f98529e3f95dda394b3efb5545a4fa155dc575/urwid-2.6.5-py3-none-any.whl")
    version("2.6.4", sha256="dea5b2e8f992946774fe864894d55c1045175d96c1266904755909dcd52d3cb5", url="https://pypi.org/packages/71/11/724aadfba410d4e630fd02987600769b178fc8eabefe96ee2a67b6561bc8/urwid-2.6.4-py3-none-any.whl")
    version("2.6.3", sha256="d896b9f983d1793cff3a5b942c18d3552924da88d9dfb974edf1890077e1ab43", url="https://pypi.org/packages/90/52/b235f97b36155f884b74232c7c767f529bfb3c85cfd62aa4df9c44507d0d/urwid-2.6.3-py3-none-any.whl")
    version("2.6.2", sha256="3d9f9c5012eb4b8f9a189e85d0de91be09ff5866f0b60429711e825620bfbd78", url="https://pypi.org/packages/6e/24/d65ad049251d9cf0b51fea1ca7354f57c4abac8f04eccaa5007584fe070e/urwid-2.6.2-py3-none-any.whl")
    version("2.6.1", sha256="e045cb68b84fc6ddab90e4832b756283a169c0ac4a4f6636b8d23a492e337e0f", url="https://pypi.org/packages/ab/c6/8653c2f1a1892e3fc0cd48663c260992d756b6e24b965511175b2881f6ca/urwid-2.6.1-py3-none-any.whl")
    version("2.6.0.post0", sha256="d918864cced6befe1efc04e25269563158a2feb9cf844ce468607bc6b8bc55f4", url="https://pypi.org/packages/91/59/e1f6dff9a71db231a701008e62933d70da8ee4439270efa5c38a720968f6/urwid-2.6.0.post0-py3-none-any.whl")
    version("2.1.2", sha256="588bee9c1cb208d0906a9f73c613d2bd32c3ed3702012f51efe318a3f2127eae", url="https://pypi.org/packages/94/3f/e3010f4a11c08a5690540f7ebd0b0d251cc8a456895b7e49be201f73540c/urwid-2.1.2.tar.gz")
    version("1.3.0", sha256="29f04fad3bf0a79c5491f7ebec2d50fa086e9d16359896c9204c6a92bc07aba2", url="https://pypi.org/packages/18/24/4038406a51166f2d5e3968f7e955e9f51f68402bc8b1101a227f4bb8f835/urwid-1.3.0.tar.gz")

    with default_args(type="run"):
        depends_on("py-typing-extensions", when="@2.5:")
        depends_on("py-wcwidth", when="@2.5.3:")

