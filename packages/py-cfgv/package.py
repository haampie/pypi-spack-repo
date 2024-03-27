##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyCfgv(PythonPackage):
    version("3.4.0", sha256="b7265b1f29fd3316bfcd2b330d63d024f2bfd8bcb8b0272f8e19a504856c48f9", url="https://pypi.org/packages/c5/55/51844dd50c4fc7a33b653bfaba4c2456f06955289ca770a5dbd5fd267374/cfgv-3.4.0-py2.py3-none-any.whl")
    version("3.3.1", sha256="c6a0883f3917a037485059700b9e75da2464e6c27051014ad85ba6aaa5884426", url="https://pypi.org/packages/6d/82/0a0ebd35bae9981dea55c06f8e6aaf44a49171ad798795c72c6f64cba4c2/cfgv-3.3.1-py2.py3-none-any.whl")
    version("3.3.0", sha256="b449c9c6118fe8cca7fa5e00b9ec60ba08145d281d52164230a69211c5d597a1", url="https://pypi.org/packages/49/54/83bf9b6ba673bf7d5ebe3846a5f6d3a53925cfd331aa29ec6b5b9c42a850/cfgv-3.3.0-py2.py3-none-any.whl")
    version("3.2.0", sha256="32e43d604bbe7896fe7c248a9c2276447dbef840feb28fe20494f62af110211d", url="https://pypi.org/packages/45/cd/3878c9248e59e5e2ebd0dc741ab984b18d86e7283ae9b127b05fc287d239/cfgv-3.2.0-py2.py3-none-any.whl")
    version("3.1.0", sha256="1ccf53320421aeeb915275a196e23b3b8ae87dea8ac6698b1638001d4a486d53", url="https://pypi.org/packages/6d/82/49913e721128ff16d6b7cf304f513de7bba698583b045dfb9c4b3bb2f467/cfgv-3.1.0-py2.py3-none-any.whl")
    version("3.0.0", sha256="f22b426ed59cd2ab2b54ff96608d846c33dfb8766a67f0b4a6ce130ce244414f", url="https://pypi.org/packages/2a/b8/1b9626e940bf80cc5a19a19e6b4c99282aa88f438cbcd2d86d7a2a666974/cfgv-3.0.0-py2.py3-none-any.whl")
    version("2.0.1", sha256="fbd93c9ab0a523bf7daec408f3be2ed99a980e20b2d19b50fc184ca6b820d289", url="https://pypi.org/packages/6e/ff/2e6bcaff26058200717c469a0910da96c89bb00e9cc31b68aa0bfc9b1b0d/cfgv-2.0.1-py2.py3-none-any.whl")
    version("2.0.0", sha256="3bd31385cd2bebddbba8012200aaf15aa208539f1b33973759b4d02fc2148da5", url="https://pypi.org/packages/2f/ec/3c0a56fbc00e6b649c1dc809dc3f12c5796fbfb7940d1167b9bddc67b818/cfgv-2.0.0-py2.py3-none-any.whl")

    with default_args(type="run"):
        depends_on("py-six", when="@0.0.2:2")

