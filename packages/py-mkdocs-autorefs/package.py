##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyMkdocsAutorefs(PythonPackage):
    version("1.0.1", sha256="aacdfae1ab197780fb7a2dac92ad8a3d8f7ca8049a9cbe56a4218cd52e8da570", url="https://pypi.org/packages/f6/01/d413c98335ed75d8c211afb91320811366d55fb0ef7f4b01b9ab19630eac/mkdocs_autorefs-1.0.1-py3-none-any.whl")
    version("1.0.0", sha256="2b6d288f0582589d1be7c99ce4470c8e7c5077892014051ff0d4ff574a73dbe8", url="https://pypi.org/packages/fb/ff/129482d0deb038dd8e2749abafcbacc8d97eff6b31f532456a22e81c5d4d/mkdocs_autorefs-1.0.0-py3-none-any.whl")
    version("0.5.0", sha256="7930fcb8ac1249f10e683967aeaddc0af49d90702af111a5e390e8b20b3d97ff", url="https://pypi.org/packages/21/5f/fe501daf6f06b93d5d9dff4319c04ad6e74965348dff22465bdd53e5e2d9/mkdocs_autorefs-0.5.0-py3-none-any.whl")
    version("0.4.1", sha256="a2248a9501b29dc0cc8ba4c09f4f47ff121945f6ce33d760f145d6f89d313f5b", url="https://pypi.org/packages/fb/5c/6594400290df38f99bf8d9ef249387b56f4ad962667836266f6fe7da8597/mkdocs_autorefs-0.4.1-py3-none-any.whl")
    version("0.4.0", sha256="7959fce10003e00bee1f40adb13b2d02b274d14fb677f168a7b5491e62531561", url="https://pypi.org/packages/b2/d6/cee367c6f2ad2a45386f3f1a71a89ef25829476d4fdbf82b7c939abb8539/mkdocs_autorefs-0.4.0-py3-none-any.whl")
    version("0.3.1", sha256="f0fd7c115eaafda7fb16bf5ff5d70eda55d7c0599eac64f8b25eacf864312a85", url="https://pypi.org/packages/f1/5a/7e73c381719f4f070eda0c81be8a40a79d31845ea8f6cc399917cfcb1fa8/mkdocs_autorefs-0.3.1-py3-none-any.whl")

    with default_args(type="run"):
        depends_on("py-markdown@3.3:")
        depends_on("py-markupsafe@2.0.1:", when="@1:")
        depends_on("py-mkdocs@1.1:")

