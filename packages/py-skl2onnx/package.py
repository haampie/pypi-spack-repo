# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PySkl2onnx(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("1.16.0", sha256="7de548580c625bfa5893fe79c9dd3213c3720b12e1ff8e3fd28967da0698242d", url="https://pypi.org/packages/26/80/836824c62ff0923b4c3b8af8332170bdc3ccb469a220535b40405a93b4fb/skl2onnx-1.16.0-py2.py3-none-any.whl")
    version("1.15.0", sha256="13a9ea5d50619ce42381c67001db8c87ce574a459a8f0738b45d2f4b93f465f6", url="https://pypi.org/packages/c0/d1/ef96f715f14ab4a11a4382e3eb9fc7a57ee59e3527253a7b21d62ca20402/skl2onnx-1.15.0-py2.py3-none-any.whl")
    version("1.14.1", sha256="f4d1a72a39d156c4c0681a032e84c3c704d9c230bc5059559c4a3b3338c0f1e2", url="https://pypi.org/packages/5e/59/0a47737c195da98d33f32073174b55ba4caca8b271fe85ec887463481f67/skl2onnx-1.14.1-py2.py3-none-any.whl")
    version("1.14.0", sha256="39d5e02c3e119a1e089543d9b68f818418c92c6b45f584fece59ed76810f324a", url="https://pypi.org/packages/0a/69/ed984233454941ea572d19121da539e92ef189fbd3cd52eb215bd3b194bd/skl2onnx-1.14.0-py2.py3-none-any.whl")
    version("1.13", sha256="51011c52d445ecef71967c67522ca7d1a57fc15576556beefeef40895b960830", url="https://pypi.org/packages/09/5f/a1d80847987588aba1335bfa5818f6c4264d4effa2bed20c2d30672e6b27/skl2onnx-1.13-py2.py3-none-any.whl")
    version("1.12", sha256="2b91a1c5051f50a96634189b46fb4184729f858b6dfeda30231e6eea48be99e3", url="https://pypi.org/packages/d3/57/62e51efc91606aa447a1aaa54dc31b5028afd564ff7a750f1efc90b582cd/skl2onnx-1.12-py2.py3-none-any.whl")
    version("1.11.2", sha256="2c5a16c52a5df06a7ac431de1071de298d02c5a2706151583d5823599f0370b5", url="https://pypi.org/packages/a8/0f/39a22ea2f0fadd252357eb333e487fe229ec03af24823f4090ff714ef54d/skl2onnx-1.11.2-py2.py3-none-any.whl")
    version("1.11.1", sha256="fd02a4eb7eeaa713191bcc1296cee989ea526f0069b0d26aaeeef579bfe82394", url="https://pypi.org/packages/0a/b6/483f824032e5d35043e29244eef8783b5cc18458964e21b430c809f2f5ab/skl2onnx-1.11.1-py3-none-any.whl")
    version("1.11", sha256="3942a97f30fc0c8d2fb4d715332714a3f0571f33b8075f4aa3b2b234566165c4", url="https://pypi.org/packages/4c/bf/48210428aca59bcefa94ff52f12981f07be13809441754ed86c1abe43d1c/skl2onnx-1.11-py2.py3-none-any.whl")
    version("1.10.4", sha256="e737d21217bb2f488e8ee09993d0701f106162d3a20e69a10bba2d0d48bf84d0", url="https://pypi.org/packages/d9/b4/4a88948ec04b83791453d45412c06a64b8c80d6bcee5d5e181ca0bde7ddb/skl2onnx-1.10.4-py2.py3-none-any.whl")
    version("1.10.3", sha256="908bccb2974b6ef852878b28a2a5e65cfe59c7572ea285aee46c64a4b6d2728a", url="https://pypi.org/packages/86/2d/055c27bdbcfe8fca11ba901e9161349f608c70173632f8241914d56ed20f/skl2onnx-1.10.3-py2.py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-numpy@1.15.0:", when="@1.4.8:1.6.0,1.7:1.13")
        depends_on("py-onnx@1.2:", when="@1.4.8:1.6.0,1.7:")
        depends_on("py-onnxconverter-common@1.7:", when="@1.9.3:")
        depends_on("py-protobuf", when="@1.4.2:1.4.3,1.4.5:1.6.0,1.7:1.13")
        depends_on("py-scikit-learn@0.19.0:1.2", when="@1.14")
        depends_on("py-scikit-learn@:1.1.1", when="@1.13")
        depends_on("py-scikit-learn@0.19.0:", when="@1.4.6:1.6.0,1.7:1.13,1.15:")
        depends_on("py-scipy@1.0.0:", when="@1.7:1.13")
    # END DEPENDENCIES

