##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyRdt(PythonPackage):
    version("1.10.0", sha256="071c5525e2125f56dd2a01dce72c2adaa4f2465cbb86183b8815e540d38c83fb", url="https://pypi.org/packages/3b/c0/4c1c771a2f839b564cd6cac4d66e44655548bba22cbe73089257e5f4c2bb/rdt-1.10.0-py3-none-any.whl")
    version("1.9.2", sha256="b53418cba74f7ff879a49ffd0729313b085c846c3d52e9cc65736fa68be29273", url="https://pypi.org/packages/52/88/2dc16e2515357629bfa3b7f8744e2a4fe572ef1d1cfe6a7968f60e471f79/rdt-1.9.2-py2.py3-none-any.whl")
    version("1.9.1", sha256="afc896faae67a979e1d73ea0b16d63847731db0ea38c4a851006814bbb130748", url="https://pypi.org/packages/b8/53/68577bde368d48346dc0fd50f4764c24690897598e03f81dc6d65cc4b631/rdt-1.9.1-py2.py3-none-any.whl")
    version("1.9.0", sha256="8ded70b42bd9fa56d1e2d0e1e48c354bb31fdd4b247b2de33a9b82c32bb4ec4b", url="https://pypi.org/packages/02/bd/c3ab3d9bc9fb37277cbd490ca887a1a2ae886815159ef34836b3bde3d40e/rdt-1.9.0-py2.py3-none-any.whl")
    version("1.8.0", sha256="7886f6e1bce249bc8631a043ff8ed94269436971609833b75a2f47baebc60cdd", url="https://pypi.org/packages/ad/d2/4aecb80bba670194bc0e2077fa60d294dc3f320cf1deaea67585dc3e72b7/rdt-1.8.0-py2.py3-none-any.whl")
    version("1.7.0", sha256="b652d8457d31ed121817478ec1f733648cad2f0ee5bf18dc98c4194e1f3c747a", url="https://pypi.org/packages/24/2e/f4f711401c4f53baa57122428a253522da2327b06df378341de6329a23bb/rdt-1.7.0-py2.py3-none-any.whl")
    version("1.6.1", sha256="7ecfde12c837c7b8e54a97de1735b33fb8117547c5fe5c10b1503bf998a8266a", url="https://pypi.org/packages/b4/ff/ff3777f450f85dc6c4525c5f27c255bf4c18430ab91862572d898183f9c8/rdt-1.6.1-py2.py3-none-any.whl")
    version("1.6.0", sha256="5f3492e200f4538a71a6625f937461d346c359043e9dee457c49d0331e82abbe", url="https://pypi.org/packages/40/19/1d54f91fddf2213aa65625e24d4decd77871947d005ada4a2ff5a9a2d580/rdt-1.6.0-py2.py3-none-any.whl")
    version("1.5.0", sha256="284972e9e97cfd694a5e89a575b022ca8e8893fafd0ef532b4427caa2eab6b13", url="https://pypi.org/packages/dc/9e/b6a224937d7827d5cbbffa60543b493872d9750f69a5bc8256fd40846a02/rdt-1.5.0-py2.py3-none-any.whl")
    version("1.4.2", sha256="965ebeca90a13df1026b47aac57169942fb1ce1f18cb5705430a4441d17a1eb2", url="https://pypi.org/packages/78/5a/8f59f545c55337c87d8d50e3ea89f1e3cdd8b5549ff93e8f17e6a5bcfea3/rdt-1.4.2-py2.py3-none-any.whl")
    version("0.6.4", sha256="72d8a5567c5a50eded47ef4bd0ebdb13650852576ca5692bc4b04eb0539d8498", url="https://pypi.org/packages/6b/5c/f6184a133796ff66f65a73786972ecc19dd94a13634449892ac6dee2790c/rdt-0.6.4-py2.py3-none-any.whl")
    version("0.6.4.dev0", sha256="9464eb7355fa2ad0a69019816809bab75908f3a6b9711fc0919b64997e94ca92", url="https://pypi.org/packages/6a/31/ef55d8e4443878ee2462991274c0b8d1dc88d25494bb7e3c314e40bbbd31/rdt-0.6.4.dev0-py2.py3-none-any.whl")
    version("0.6.3", sha256="fdca21cab7a4f27284e15c09920636084add5cf8934e0fd26bfdb3af8eeabada", url="https://pypi.org/packages/3c/f6/9203c847e35dff01f2156604a6190ddf35cdb00e91318c7a84e7d80c2478/rdt-0.6.3-py2.py3-none-any.whl")
    version("0.6.3.dev3", sha256="0c0dd4ad9ed0a2fa11969b2ed1a55fdf587cf3225d3a5950c9c58e57f3386533", url="https://pypi.org/packages/b3/a0/5afb591380631e1366be800c44a9d72a492852f036be601cb30b4305a17f/rdt-0.6.3.dev3-py2.py3-none-any.whl")
    version("0.6.3.dev2", sha256="63f60c922574dac6d75b78de633277fc0d20c6eca758590ac1dd78b285d4bfcb", url="https://pypi.org/packages/56/a1/f23c436ffa89d26d8d400bdfc89aa044a4a1bdb1731cd187d6c2b07640a2/rdt-0.6.3.dev2-py2.py3-none-any.whl")
    version("0.6.3.dev1", sha256="4742de0f3c5bb058358e9d283ae14d542a1dbc30d147fc0708a58cb4c22e53f0", url="https://pypi.org/packages/7a/a1/8d25dd0ca16d3f834dc561c5111ddace4f534b975db142a17ee46c77dffe/rdt-0.6.3.dev1-py2.py3-none-any.whl")
    version("0.6.3.dev0", sha256="5f0326629dbb4bd938715088ce19656927e56fc0d198d95ebe13dc20c65864e1", url="https://pypi.org/packages/07/fd/50234c07aa4ff0873c698e6f6252f8ff77a3c8be5eb6b4d25baa4fc2a4fd/rdt-0.6.3.dev0-py2.py3-none-any.whl")
    version("0.6.2", sha256="97b8adb4a9bca87bc1be2dec4b7e7e9e0b328bd695ee1d51e767c8867562b53e", url="https://pypi.org/packages/09/c8/aeaa46aeaa01a255e50413e48c0364330972c4f39d9a0d40330a33eef465/rdt-0.6.2-py2.py3-none-any.whl")
    version("0.6.2.dev0", sha256="b774c665df6de175daebdd17d6f418294e9e1cff1ad1f26111842fcfdd8a7b0c", url="https://pypi.org/packages/f6/b1/0775d1e99b750ae233ae8407516f0237ce53e7d08e3d5fbaa5a2e90a6625/rdt-0.6.2.dev0-py2.py3-none-any.whl")
    version("0.6.1", sha256="e1c9d4c2733deb95ae1fd97848661f963ef57b79f3d1ed9fabc6bc0715029965", url="https://pypi.org/packages/0b/0e/1b3a505ada571f07a9c4ead7eb2f2130722056e968e5fb2c8bcb370c9f88/rdt-0.6.1-py2.py3-none-any.whl")

    with default_args(type="run"):
        depends_on("python@:3.11", when="@1.3:")
        depends_on("python@:3.9", when="@0.6.1:1.2,1.3.0.dev:1.3.0.dev0")
        depends_on("python@:3.8", when="@0.2.4:0.6.0")
        depends_on("py-faker@17:19", when="@1.8:")
        depends_on("py-faker@10:", when="@1.2:1.7")
        depends_on("py-numpy@1.23.3:1", when="@1.3: ^python@3.10:")
        depends_on("py-numpy@1.20.0:1", when="@1.3: ^python@:3.9")
        depends_on("py-numpy@1.20.0:1", when="@0.6.1:1.2,1.3.0.dev:1.3.0.dev0")
        depends_on("py-pandas@1.5.0:", when="@1.4.2: ^python@3.11:")
        depends_on("py-pandas@1.1.3:", when="@1.4.2: ^python@:3.9")
        depends_on("py-pandas@1.3.4:", when="@1.4.2: ^python@3.10")
        depends_on("py-pandas@1.1.3:1", when="@1.3:1.4.1 ^python@:3.9")
        depends_on("py-pandas@1.1.3:1", when="@0.6.2:1.2,1.3.0.dev:1.3.0.dev0")
        depends_on("py-pandas@1.1.3:1.1.4", when="@0.6.1")
        depends_on("py-psutil@5.7:", when="@0.5.1:1.7")
        depends_on("py-pyyaml@5.4.1:5", when="@0.6.2:1.2,1.3.0.dev:1.3.0.dev0")
        depends_on("py-scikit-learn@1.1.3:", when="@1.9.3: ^python@3.11:")
        depends_on("py-scikit-learn@1.1.0:", when="@1.9.3: ^python@3.10")
        depends_on("py-scikit-learn@0.24.0:", when="@1.3: ^python@:3.9")
        depends_on("py-scikit-learn@1.1.3:", when="@1.3:1.9.2 ^python@3.10:")
        depends_on("py-scikit-learn@0.24.0:", when="@0.6.3:1.2,1.3.0.dev:1.3.0.dev0")
        depends_on("py-scikit-learn@0.24.0:0", when="@0.6.2,0.6.3.dev:0.6.3.dev2")
        depends_on("py-scipy@1.9.2:", when="@1.3: ^python@3.10:")
        depends_on("py-scipy@1.5.4:", when="@1.3: ^python@:3.9")
        depends_on("py-scipy@1.5.4:1.7", when="@0.6.4:1.2,1.3.0.dev:1.3.0.dev0")
        depends_on("py-scipy@1.5.4:", when="@0.6.1:0.6.3")

