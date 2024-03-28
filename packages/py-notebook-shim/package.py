# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyNotebookShim(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("0.2.4", sha256="411a5be4e9dc882a074ccbcae671eda64cceb068767e9a3419096986560e1cef", url="https://pypi.org/packages/f9/33/bd5b9137445ea4b680023eb0469b2bb969d61303dedb2aac6560ff3d14a1/notebook_shim-0.2.4-py3-none-any.whl")
    version("0.2.3", sha256="a83496a43341c1674b093bfcebf0fe8e74cbe7eda5fd2bbc56f8e39e1486c0c7", url="https://pypi.org/packages/f4/79/73250372e5bbab63018b41b02d5cc6b395655ec6c1254e477ef7c913aada/notebook_shim-0.2.3-py3-none-any.whl")
    version("0.2.2", sha256="9c6c30f74c4fbea6fce55c1be58e7fd0409b1c681b075dcedceb005db5026949", url="https://pypi.org/packages/29/34/b3d57a23287c55fe964da403bb5457baacc2c0edc1fc3bf2739d4a958d90/notebook_shim-0.2.2-py3-none-any.whl")
    version("0.2.0", sha256="481711abddfb2e5305b83cf0efe18475824eb47d1ba9f87f66a8c574b8b5c9e4", url="https://pypi.org/packages/65/1b/a898f3bf3eb98a9fdb56cba21cb6c31d553f577501cccff7f6996ce5d2e7/notebook_shim-0.2.0-py3-none-any.whl")
    version("0.1.0", sha256="02432d55a01139ac16e2100888aa2b56c614720cec73a27e71f40a5387e45324", url="https://pypi.org/packages/af/12/00c739649e40ec9dacd961c3198d87fd2dea2776f1df85e664d3e62ebe71/notebook_shim-0.1.0-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-jupyter-server@1.8:", when="@0.2:")
        depends_on("py-jupyter-server@1.8:1", when="@0.1")
    # END DEPENDENCIES

