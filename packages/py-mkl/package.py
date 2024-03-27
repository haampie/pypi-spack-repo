##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyMkl(PythonPackage):
    version("2024.0.0", sha256="6c92752440a8ccb9a1e7c0df4abe0db232f879b34fc31238175acfb5bc892d22", url="https://pypi.org/packages/83/a2/e1e489f2bf4fae3c4e95faf93a7bbb4ba24bfd921481f1200355032075a1/mkl-2024.0.0-py2.py3-none-win_amd64.whl")
    version("2023.2.1", sha256="953a55a778d87cea9fd44f777c3b0a7a5804e9e810dc5f22852b2c4a42a79bcb", url="https://pypi.org/packages/f3/77/5cfa3161c078bfc47cf60b97a8903eecbd610b022694a34136e2081b5f7d/mkl-2023.2.1-py2.py3-none-macosx_10_15_x86_64.macosx_11_0_x86_64.whl")
    version("2023.2.0", sha256="7b93b9a20c51e8c60f891097924f3f2be786797d4b587dc848725efacd559a0b", url="https://pypi.org/packages/e2/2a/0b72eb7ad44fe21a95850163f4f7f77c86519a39483fb6cbc9eac97b3584/mkl-2023.2.0-py2.py3-none-win_amd64.whl")
    version("2023.1.0", sha256="2c0468f39395721d52e929c894983576adb51fa8df983b69c63dbfb38e3e1e57", url="https://pypi.org/packages/69/77/58128796938d4cac8c8fad173fe0e4180ccf12a65967f414203e9018e6d0/mkl-2023.1.0-py2.py3-none-win32.whl")
    version("2023.0.0", sha256="e75ce244cd8ba36c497404fa166896f9042531a2f838ae83c75591c9af15589e", url="https://pypi.org/packages/8c/db/818ac8ff6f2a7e75680ef1da377270ac333a0306ebc0392afe12d7fe0394/mkl-2023.0.0-py2.py3-none-macosx_10_15_x86_64.macosx_11_0_x86_64.whl")
    version("2022.2.1", sha256="98ca4b8de23d361d7a5c314d23ec9490d5377bec68421c57d564d99adc60bab8", url="https://pypi.org/packages/58/5b/e6844227edff4851346aae539141af37cd150e719d38f55a871f5a9b11be/mkl-2022.2.1-py2.py3-none-win32.whl")
    version("2022.2.0", sha256="50632b1edc474551ca9d6af0224bcc2f7de607c2689314b80c344837b1b5b09e", url="https://pypi.org/packages/9c/d5/a15154b0a809cd19565deda282cc8cfe7d67e8acf978fbf29237bd72fba0/mkl-2022.2.0-py2.py3-none-win_amd64.whl")
    version("2022.1.0", sha256="13e90792800a114f213a405220444a85bbe7eb59a7a273487562da980c668470", url="https://pypi.org/packages/aa/cc/c9680ae21c896a24a6917e75a29f5ff01f49aa1050930d0fc70f62e21d90/mkl-2022.1.0-py2.py3-none-win_amd64.whl")
    version("2022.0.3", sha256="706f74f142f7f7f7ed184eadb1472b95bce6f61bfd1a35e41daa362d089cec93", url="https://pypi.org/packages/4c/8a/19501f27f057996e2c88601c9a49e1319e65d806264933ff16a13510bdc0/mkl-2022.0.3-py2.py3-none-win_amd64.whl")
    version("2022.0.2", sha256="07fa7c2dfab146d1411ccd6e3e2fa6e3ab9efa8186706e0421c7d49d7986efe0", url="https://pypi.org/packages/3f/ba/fd77f2e0f7adb54bdfc6eeace49ddb3af3b7779e786e60e9ef339a24598e/mkl-2022.0.2-py2.py3-none-win_amd64.whl")

    with default_args(type="run"):
        depends_on("py-intel-openmp@2024:", when="@2024:")
        depends_on("py-intel-openmp@2023", when="@2023")
        depends_on("py-intel-openmp@2022", when="@2022")
        depends_on("py-tbb@2021:", when="@2021:")

