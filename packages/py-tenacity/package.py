# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyTenacity(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("8.2.3", sha256="ce510e327a630c9e1beaf17d42e6ffacc88185044ad85cf74c0a8887c6a0f88c", url="https://pypi.org/packages/f4/f1/990741d5bb2487d529d20a433210ffa136a367751e454214013b441c4575/tenacity-8.2.3-py3-none-any.whl")
    version("8.2.2", sha256="2f277afb21b851637e8f52e6a613ff08734c347dc19ade928e519d7d2d8569b0", url="https://pypi.org/packages/e7/b0/c23bd61e1b32c9b96fbca996c87784e196a812da8d621d8d04851f6c8181/tenacity-8.2.2-py3-none-any.whl")
    version("8.2.1", sha256="dd1b769ca7002fda992322939feca5bee4fa11f39146b0af14e0b8d9f27ea854", url="https://pypi.org/packages/f9/ea/c8e727fc85a098d77462dbf124650d58290ce227d141ed86285648c894e6/tenacity-8.2.1-py3-none-any.whl")
    version("8.2.0", sha256="b723061a78ed0f4524190eae321d3d84100227d51c5677035b6615d91895e0d6", url="https://pypi.org/packages/bd/5b/af94e55973625314eb8d51c50cf8570eafe91651fb4ee316169dc600139f/tenacity-8.2.0-py3-none-any.whl")
    version("8.1.0", sha256="35525cd47f82830069f0d6b73f7eb83bc5b73ee2fff0437952cedf98b27653ac", url="https://pypi.org/packages/a5/94/933ce16d18450ccf518a6da5bd51418611e8776b992070b9f40b2f9cedff/tenacity-8.1.0-py3-none-any.whl")
    version("8.0.1", sha256="f78f4ea81b0fabc06728c11dc2a8c01277bfc5181b321a4770471902e3eb844a", url="https://pypi.org/packages/f2/a5/f86bc8d67c979020438c8559cc70cfe3a1643fd160d35e09c9cca6a09189/tenacity-8.0.1-py3-none-any.whl")
    version("8.0.0", sha256="352cc77bb3dffb070111c83c548ef5afb78acf93f89a28d753c5570066411b57", url="https://pypi.org/packages/d8/f7/dcafcff418087f0f3de47431ef7504efd11a585086419ce1872af9bdf2a7/tenacity-8.0.0-py3-none-any.whl")
    version("7.0.0", sha256="a0ce48587271515db7d3a5e700df9ae69cce98c4b57c23a4886da15243603dd8", url="https://pypi.org/packages/41/ee/d6eddff86161c6a3a1753af4a66b06cbc508d3b77ca4698cd0374cd66531/tenacity-7.0.0-py2.py3-none-any.whl")
    version("6.3.1", sha256="baed357d9f35ec64264d8a4bbf004c35058fad8795c5b0d8a7dc77ecdcbb8f39", url="https://pypi.org/packages/4e/e4/bcaf6978c0811fbb480acc9bd6e024b53390a61d153fa0be4f20a6c80d94/tenacity-6.3.1-py2.py3-none-any.whl")
    version("6.3.0", sha256="a0320f92bd2509854b6a12a8ebc4bc70388e5641f70ddde941a0ea758503377e", url="https://pypi.org/packages/93/22/30f5a0cf52f92ad69effc11870337bb7f9eb0661ab0f99b3e96cb09f4b95/tenacity-6.3.0-py2.py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-six@1.9:", when="@4.5:4,5.0.3:5.0,6:7")
    # END DEPENDENCIES

