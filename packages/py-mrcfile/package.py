# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyMrcfile(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("1.5.0", sha256="9c3af796b35d84dd2ddc357b8427d2034212ad58de0a8f0201c2a724b9e59ad1", url="https://pypi.org/packages/a4/b4/2bceabec5a7349831ee5dac446ca0cea5f7808374588e6eded625a6d1dc1/mrcfile-1.5.0-py2.py3-none-any.whl")
    version("1.4.3", sha256="798fa12f2861e74d627546bd1989836857b10090fa2a148913ea468bbbb27e80", url="https://pypi.org/packages/09/b5/c1a218305dfb1165a5d058373d57c64b9dac0def8bcca3f31f1376b72ada/mrcfile-1.4.3-py2.py3-none-any.whl")
    version("1.4.2", sha256="c5eab9c623b063b9e0a01ec26866613b81723fb97abfffcf9efd28562f16c979", url="https://pypi.org/packages/0d/8e/323819dc30dcb64346c1e66b0f9e569bb0c738a60f4607283bf3fac69101/mrcfile-1.4.2-py2.py3-none-any.whl")
    version("1.4.1", sha256="b15600d43c5844794602a5abfcae75a9c7b7e788791293d379dcf99a66bc26ec", url="https://pypi.org/packages/ed/54/990e000e3478d5788c02c56486fced5a7f198f7ba692f2e359581fe77584/mrcfile-1.4.1-py2.py3-none-any.whl")
    version("1.4.0", sha256="2df610f4495c4b8faa65964c27286590e4c2c391ff9f1515492b8ce250052e34", url="https://pypi.org/packages/25/a7/83aa22b5444bac819b0c6f6ef23f7bceb91045c4b718faa7597ab503b496/mrcfile-1.4.0-py2.py3-none-any.whl")
    version("1.3.0", sha256="4eeaed257eee22dbe142481c35498244d190e4ca10a2daf2ba3749db6822fd41", url="https://pypi.org/packages/7d/b3/6d35d37e5f51ebb1a6ed4c5178206705bcaf8848c853db790254a15039be/mrcfile-1.3.0-py2.py3-none-any.whl")
    version("1.2.0", sha256="bb9accb62529f3f9a64abbf3961cf410a3d3e4c8d625f3d28175da20dab74257", url="https://pypi.org/packages/c3/ab/b5f3c70f241a95cd7ea38ce474c42298ab28046340b5a1d6a58af5762cb0/mrcfile-1.2.0-py2.py3-none-any.whl")
    version("1.1.2", sha256="52ee39d54bc163f8b6a20538f52b12b6a5b06871b2bae33217e9ea68a7166651", url="https://pypi.org/packages/79/aa/52aa135830f66259783207021849a8234551fc5e3db15f685201cb3d1bfa/mrcfile-1.1.2-py2.py3-none-any.whl")
    version("1.1.1", sha256="a9ff7d7331261787078060f5a2b680de7f8b39ce2c5d425748669c26f1f44ae0", url="https://pypi.org/packages/61/eb/1585371bd67d51d6f662eb72d462a4c885d6c71975e84e9cc2a5bae292b8/mrcfile-1.1.1-py2.py3-none-any.whl")
    version("1.1.0", sha256="30bf9cae6c2e5ead392e3f9eab9c7476583d66dcfd1dedca349626ff2462655e", url="https://pypi.org/packages/77/c5/02f02af855df5e79cb325dfb5f29a05b2ee98153ba5a65788b9402e44172/mrcfile-1.1.0-py2.py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-numpy@1.16.0:", when="@1.4:")
        depends_on("py-numpy@1.11.0:1.15", when="@1.1.1")
        depends_on("py-numpy@1.12.0:", when="@0.2:0.2.3,1.2:1.3")
        depends_on("py-numpy@1.11.0:", when="@:0.1,0.2.4:1.0.1,1.0.4:1.1.0,1.1.2:1.1")
    # END DEPENDENCIES

