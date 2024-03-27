##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyLineProfiler(PythonPackage):
    version("4.1.2", sha256="aa56578b0ff5a756fe180b3fda7bd67c27bbd478b3d0124612d8cf00e4a21df2", url="https://pypi.org/packages/1c/e8/14bb2ee9af4ecae4c456c5faaab74436ea2b9da55b436341dd1f7c2927f2/line_profiler-4.1.2.tar.gz")
    version("3.5.1", sha256="77400208bfbd5d4341938a9a3a4fb5194f5af7fc23b2d496c913755f8310e8b8", url="https://pypi.org/packages/a7/8e/3b5d52dd5dee982bb183cd494886398ff919a9216ca6a6a50004ea28ed50/line_profiler-3.5.1.tar.gz")
    version("2.1.2", sha256="efa66e9e3045aa7cb1dd4bf0106e07dec9f80bc781a993fbaf8162a36c20af5c", url="https://pypi.org/packages/14/fc/ecf4e238bb601ff829068e5a72cd1bd67b0ee0ae379db172eb6a0779c6b6/line_profiler-2.1.2.tar.gz")
    version("2.0", sha256="739f8ad0e4bcd0cb82e99afc09e00a0351234f6b3f0b1f7f0090a8a2fbbf8381", url="https://pypi.org/packages/65/48/61da8ca03e197bb57800c8839f403f2fb7bdf1cfe87fa62e0b35b683273c/line_profiler-2.0.tar.gz")

    with default_args(type="run"):
        depends_on("py-ipython@0.13:", when="@2:2.0")

