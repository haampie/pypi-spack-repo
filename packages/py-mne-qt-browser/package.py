# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyMneQtBrowser(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("0.6.2", sha256="dd143462cfa2d9088a26b4b469fd398e0d2216761bdff1387eb920920a9e4e19", url="https://pypi.org/packages/23/31/26975ad8b0433448aefd4bbdf5bbde5f59e4e3f29c869c4464c0e9903429/mne_qt_browser-0.6.2-py3-none-any.whl")
    version("0.6.1", sha256="f5ad96e29b4f777066c22bef84fff1955313ef31fe06adc07252df4f7fbd20d7", url="https://pypi.org/packages/42/9f/f3e220631dbb92f6c666a36f02db22f3d1020deb7b0a887bd09cc29cfdcd/mne_qt_browser-0.6.1-py3-none-any.whl")
    version("0.6.0", sha256="564c8eb8d2cbef6da016f1be7b80820ad0963f6c4cbccf2350a62bf72c01b564", url="https://pypi.org/packages/b1/c8/6fd7aee8f11dba86fd4ff0184fd8cd187718c4e0b3079ac125b2675a7a62/mne_qt_browser-0.6.0-py3-none-any.whl")
    version("0.5.2", sha256="d1c7cea8fa5d3c34daf98b49d235daf7bb28608ec74b11220ecd74437278432a", url="https://pypi.org/packages/ff/45/939314fbea891b306c9594b57ff78e047028a0801171c19c09eba90ed1e9/mne_qt_browser-0.5.2-py3-none-any.whl")
    version("0.5.1", sha256="bed7bf66db740dd587d5a2a0b5898e273eb22797a674bbe83b7187ebc81bee8e", url="https://pypi.org/packages/98/de/77bd2097041180d23b485e53f6339a7a103aaf9c1e8e2ee52c6f84a18d2f/mne_qt_browser-0.5.1-py3-none-any.whl")
    version("0.5.0", sha256="db2e0b9ec293266bf0d6292967c7eee857f4b07638eecaf535e939c72a5e1bd9", url="https://pypi.org/packages/bd/3a/6c1a5682989287da1ca4709bdb5b050e11607125ebe6f8f6668408f0fd0d/mne_qt_browser-0.5.0-py3-none-any.whl")
    version("0.4.0", sha256="7de1ca94207f79b6aa703dcb802c8564924ed88578f21e045ee77500af1ce7cc", url="https://pypi.org/packages/ff/07/22d60a159e2a14076f478cd1c3202f79f7f86fe88ceecfa96258818ca0c1/mne_qt_browser-0.4.0-py3-none-any.whl")
    version("0.3.2", sha256="0cf4c1a05d67eac9072cec5879f4b66c69afbb64fa14fd2e605408cee398f170", url="https://pypi.org/packages/50/20/fd8ef379c18a63ec9db7ed0b392d63d064d9f0862c3639d7f96fbbfba961/mne_qt_browser-0.3.2-py3-none-any.whl")
    version("0.3.1", sha256="833b56d6af8eef4f40235009d0363d0b96cd6c662fe01fe60ae7db72caeec53d", url="https://pypi.org/packages/c1/ef/4d645e8059a620e064e172e4b6de3c19345db9a10a5de20fd79ee101a4dd/mne_qt_browser-0.3.1-py3-none-any.whl")
    version("0.3.0", sha256="714dd7c7573abc31930a7a738bce9aa0b539f1b1610220571eaa96f08b8a9e65", url="https://pypi.org/packages/01/20/90fd5fd7d0020a9d28a30e2850af53403b03112f117fc9e56148c7fb9242/mne_qt_browser-0.3.0-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("python@3.9:", when="@0.6.2:")
        depends_on("py-colorspacious", when="@0.2.5:")
        depends_on("py-darkdetect", when="@0.3:")
        depends_on("py-matplotlib", when="@0.1.5:0.1.6,0.2:")
        depends_on("py-mne@1:", when="@0.5:")
        depends_on("py-mne@0.24:", when="@0.2:0.4")
        depends_on("py-numpy", when="@0.1.5:0.1.6,0.2:")
        depends_on("py-packaging", when="@0.5:")
        depends_on("py-pyopengl", when="@0.2.2: platform=darwin")
        depends_on("py-pyqtgraph@0.12.3:", when="@0.2:")
        depends_on("py-qdarkstyle", when="@0.3:")
        depends_on("py-qtpy", when="@0.1.5:0.1.6,0.2:")
        depends_on("py-scipy", when="@0.1.5:0.1.6,0.2:")
        depends_on("py-scooby", when="@0.2.6:")
        depends_on("py-setuptools@65:", when="@0.5:0.6.1")
    # END DEPENDENCIES

