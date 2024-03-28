# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPep8Naming(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("0.13.3", sha256="1a86b8c71a03337c97181917e2b472f0f5e4ccb06844a0d6f0a33522549e7a80", url="https://pypi.org/packages/4f/48/9533518e0394fb858ac2b4b55fe18f24aa33c87c943f691336ec842d9728/pep8_naming-0.13.3-py3-none-any.whl")
    version("0.13.2", sha256="59e29e55c478db69cffbe14ab24b5bd2cd615c0413edf790d47d3fb7ba9a4e23", url="https://pypi.org/packages/7d/e3/9d7afb48ad9366c8ae9821ba8049f9b2b856e84c3fcbc44338387b0f9497/pep8_naming-0.13.2-py3-none-any.whl")
    version("0.13.1", sha256="f7867c1a464fe769be4f972ef7b79d6df1d9aff1b1f04ecf738d471963d3ab9c", url="https://pypi.org/packages/66/8f/ec60626cd61ffa3862705e4c7a0096060ea9bc481cee4a7f73dc892a5c2c/pep8_naming-0.13.1-py3-none-any.whl")
    version("0.13.0", sha256="069ea20e97f073b3e6d4f789af2a57816f281ca64b86210c7d471117a4b6bfd0", url="https://pypi.org/packages/19/df/c0167cb07d9a621b8ce0444c718b103417500b37771bfd39cb7282859736/pep8_naming-0.13.0-py3-none-any.whl")
    version("0.12.1", sha256="4a8daeaeb33cfcde779309fc0c9c0a68a3bbe2ad8a8308b763c5068f86eb9f37", url="https://pypi.org/packages/5d/5d/2b8fc7b8776e0285d9a1f88593ee2bd84ba35736c5a3b80b0d8adf45b799/pep8_naming-0.12.1-py2.py3-none-any.whl")
    version("0.12.0", sha256="2321ac2b7bf55383dd19a6a9c8ae2ebf05679699927a3af33e60dd7d337099d3", url="https://pypi.org/packages/39/cb/fbdd4fa715a89343e92847525e4b869eabc180b8de59eb399f5a63711859/pep8_naming-0.12.0-py2.py3-none-any.whl")
    version("0.11.1", sha256="f43bfe3eea7e0d73e8b5d07d6407ab47f2476ccaeff6937c84275cd30b016738", url="https://pypi.org/packages/44/57/d6544d56909f5fc77e24dd6c6727c33cd8d06c67828ecb05c650f3ec95ec/pep8_naming-0.11.1-py2.py3-none-any.whl")
    version("0.11.0", sha256="a078f3a32fb85142fd5e36ea15929c023e2143e66cbf7d42bf262079c7baddf9", url="https://pypi.org/packages/89/1b/828bc9a2f46e6baa6d8e49bf30eeb13b90c55e7a7e60fdc3f8b4d81f0ae6/pep8_naming-0.11.0-py2.py3-none-any.whl")
    version("0.10.0", sha256="5d9f1056cb9427ce344e98d1a7f5665710e2f20f748438e308995852cfa24164", url="https://pypi.org/packages/5b/69/6018efb8ae18bd5a05f5f447666060a44aa8fe017f439c50fe8c8bd990cf/pep8_naming-0.10.0-py2.py3-none-any.whl")
    version("0.9.1", sha256="45f330db8fcfb0fba57458c77385e288e7a3be1d01e8ea4268263ef677ceea5f", url="https://pypi.org/packages/70/dc/213f334d78fd71ca5f79f1d5273689f92288d3e7e0d17fa523300d7d517d/pep8_naming-0.9.1-py2.py3-none-any.whl")
    version("0.7.0", sha256="360308d2c5d2fff8031c1b284820fbdb27a63274c0c1a8ce884d631836da4bdd", url="https://pypi.org/packages/39/bb/a34544c789e7e5458ed2db6cbd1c8e227bb01e4ce03a0b15ec4ec93e486d/pep8_naming-0.7.0-py2.py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-flake8@5:", when="@0.13.3:")
        depends_on("py-flake8@3.9.1:", when="@0.12:0.13.2")
        depends_on("py-flake8-polyfill@1.0.2:", when="@0.5:0.12")
    # END DEPENDENCIES

