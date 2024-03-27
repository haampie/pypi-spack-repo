##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPydeck(PythonPackage):
    version("0.8.0", sha256="a8fa7757c6f24bba033af39db3147cb020eef44012ba7e60d954de187f9ed4d5", url="https://pypi.org/packages/ac/1e/676ed6c028bfd39d6c7c75abd57bc482f7eaa813f3faa715d80431732a43/pydeck-0.8.0-py2.py3-none-any.whl")
    version("0.7.1", sha256="7fc49b00840608068b930f9269169c7c9f3198b8b4635c934ba6d887c4e54503", url="https://pypi.org/packages/7d/39/f58de74a3b4055bc7772bd77eccbf6e3a6e95d84fef53bb56ae93bea2fb9/pydeck-0.7.1-py2.py3-none-any.whl")
    version("0.7.0", sha256="8db699ff8f5226e6b26d04aa01f9a32e986427219c176a216c8156fd5a37bfc6", url="https://pypi.org/packages/b9/af/6f6236dc49ecc25374f608fff7c47a7b3d0372cfff9e8c0fe2ce70086bf4/pydeck-0.7.0-py2.py3-none-any.whl")
    version("0.6.2", sha256="e0d1f36e5cf0f8181f82d25a5f33381b8296caaac671f355afe4a660964d0dea", url="https://pypi.org/packages/d6/bc/f0e44828e4290367c869591d50d3671a4d0ee94926da6cb734b7b200308c/pydeck-0.6.2-py2.py3-none-any.whl")
    version("0.6.1", sha256="9f77d28b45504010c48cc7a43bbc2108749862f6738f94dba2e9ad16a39b0be1", url="https://pypi.org/packages/1c/3f/8f04ae0c22d82ec7bec7fcc03270a142f637e362bbd285f7daeeda24fbef/pydeck-0.6.1-py2.py3-none-any.whl")
    version("0.6.0", sha256="1eb36bcf9ba93d61f2522a630ce8639c1c33fa1b7c5a5b2e562d09411d82c10a", url="https://pypi.org/packages/fd/1d/e9579cf5cbc3d85e12d04b2b2d0664d87ca132712baf9bc78bf6160bd554/pydeck-0.6.0-py2.py3-none-any.whl")
    version("0.5.0", sha256="5759842addfef5a76c6033f90f34901dfa377a740b3dbedb55e7c46d07be3c65", url="https://pypi.org/packages/9e/9d/8fbf1f56cc5891e6c3295bf94fc176e9ab0a3ffdd090cc8b354ac2640f9a/pydeck-0.5.0-py2.py3-none-any.whl")
    version("0.4.1", sha256="df781dbe6d9698264a8a9c242030e0edf889ddd0884cbb00c85d2586608a62ab", url="https://pypi.org/packages/94/0f/05708169885fa9adca54a47ce75b020bc6c16ccc3533dd4e483ea6f5e3eb/pydeck-0.4.1-py2.py3-none-any.whl")
    version("0.4.0", sha256="707d5f0143c63626d606e7d5ec704da34b0e593444eba5373860a3c675a61f9b", url="https://pypi.org/packages/38/56/9c824cad40d6dfe51310b5e5c2ba9f69007c8946e37d23d44b9824284f69/pydeck-0.4.0-py2.py3-none-any.whl")
    version("0.3.1", sha256="d88ccba2bd8f933a77cb8e68fc569156ca6bf958eb20a9f4ab0359e045f15eb3", url="https://pypi.org/packages/b6/e6/3b5b96eaabbc949b44f9f106fe50302b33aff6246336297a7106601f0993/pydeck-0.3.1-py2.py3-none-any.whl")

    with default_args(type="run"):
        depends_on("py-ipykernel@5.1.2:", when="@:0.7")
        depends_on("py-ipywidgets@7.0.0:", when="@0.2:0.7")
        depends_on("py-ipywidgets@7.0.0:7", when="@:0.1")
        depends_on("py-jinja2@2.10.1:")
        depends_on("py-numpy@1.16.4:", when="@0.3:")
        depends_on("py-traitlets@4.3.2:", when="@:0.7")

