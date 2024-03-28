# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPreCommit(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("3.7.0", sha256="5eae9e10c2b5ac51577c3452ec0a490455c45a0533f7960f993a0d01e59decab", url="https://pypi.org/packages/53/1a/1870d52d0d86d534d4d5f7a58e65d40a4610b57e13309917faa9e62818fe/pre_commit-3.7.0-py2.py3-none-any.whl")
    version("3.6.2", sha256="ba637c2d7a670c10daedc059f5c49b5bd0aadbccfcd7ec15592cf9665117532c", url="https://pypi.org/packages/f8/7c/f7a50d07ae9fa86d2149d4acb2daf61e7c0257b56bc1a24a7fb09c1b70df/pre_commit-3.6.2-py2.py3-none-any.whl")
    version("3.6.1", sha256="9fe989afcf095d2c4796ce7c553cf28d4d4a9b9346de3cda079bcf40748454a4", url="https://pypi.org/packages/a9/24/857113af29eb47ff108642f8029ebfd7691d677c13d8cbf6ac3654488df7/pre_commit-3.6.1-py2.py3-none-any.whl")
    version("3.6.0", sha256="c255039ef399049a5544b6ce13d135caba8f2c28c3b4033277a788f434308376", url="https://pypi.org/packages/e2/e3/54cd906d377e1766299df14710ded125e195d5c685c8f1bafecec073e9c6/pre_commit-3.6.0-py2.py3-none-any.whl")
    version("3.5.0", sha256="841dc9aef25daba9a0238cd27984041fa0467b4199fc4852e27950664919f660", url="https://pypi.org/packages/6c/75/526915fedf462e05eeb1c75ceaf7e3f9cde7b5ce6f62740fe5f7f19a0050/pre_commit-3.5.0-py2.py3-none-any.whl")
    version("3.4.0", sha256="96d529a951f8b677f730a7212442027e8ba53f9b04d217c4c67dc56c393ad945", url="https://pypi.org/packages/58/56/3b24f8641c39021218ca16115a9cd88512ae16eab790513e832a36269e90/pre_commit-3.4.0-py2.py3-none-any.whl")
    version("3.3.3", sha256="10badb65d6a38caff29703362271d7dca483d01da88f9d7e05d0b97171c136cb", url="https://pypi.org/packages/e3/b7/1d145c985d8be9729672a45b8b8113030ad60dff45dec592efc4e5f5897a/pre_commit-3.3.3-py2.py3-none-any.whl")
    version("3.3.2", sha256="8056bc52181efadf4aac792b1f4f255dfd2fb5a350ded7335d251a68561e8cb6", url="https://pypi.org/packages/45/30/c3d5d192b97de482b9adfa356724dfbb07e293b54d94c3b98dd2e5f24759/pre_commit-3.3.2-py2.py3-none-any.whl")
    version("3.3.1", sha256="218e9e3f7f7f3271ebc355a15598a4d3893ad9fc7b57fe446db75644543323b9", url="https://pypi.org/packages/77/39/86e07f4e9671ee9311fa4bafc41c66d6a907192707160e3f45272e78be38/pre_commit-3.3.1-py2.py3-none-any.whl")
    version("3.3.0", sha256="7577a012399334d9f001873b5553f9fabc1ccc5b3e2b29e0793f84ce18e9d042", url="https://pypi.org/packages/d8/46/eec6ed304fc3e7ef16ed49b0dd2d70c305e748fdadfefd8624bf8630b019/pre_commit-3.3.0-py2.py3-none-any.whl")
    version("2.20.0", sha256="51a5ba7c480ae8072ecdb6933df22d2f812dc897d5fe848778116129a681aac7", url="https://pypi.org/packages/b2/6c/9ccb5213a3d9fd3f8c0fd69d207951901eaef86b7a1a69bcc478364d3072/pre_commit-2.20.0-py2.py3-none-any.whl")
    version("2.17.0", sha256="725fa7459782d7bec5ead072810e47351de01709be838c2ce1726b9591dad616", url="https://pypi.org/packages/d6/a0/9c06353771c8dae6db437dd513a885eccdb1566cb332569130484eddf4e7/pre_commit-2.17.0-py2.py3-none-any.whl")
    version("2.10.1", sha256="16212d1fde2bed88159287da88ff03796863854b04dc9f838a55979325a3d20e", url="https://pypi.org/packages/7d/ce/382156bfb1919168354dd6b441b9dd553e264fa7190073a0af3ee52b001e/pre_commit-2.10.1-py2.py3-none-any.whl")
    version("1.20.0", sha256="c2e4810d2d3102d354947907514a78c5d30424d299dc0fe48f5aa049826e9b50", url="https://pypi.org/packages/89/97/fe584f47dc43332ac254ed3940d2a3401877be73e3150a557641c9f812a6/pre_commit-1.20.0-py2.py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("python@3.9:", when="@3.6:")
        depends_on("py-aspy-yaml", when="@0.8:2.0")
        depends_on("py-cfgv@2:", when="@1.17:")
        depends_on("py-identify@1:", when="@0.15:")
        depends_on("py-nodeenv@0.11.1:", when="@0.8:")
        depends_on("py-pyyaml@5.1:", when="@2.1:")
        depends_on("py-pyyaml", when="@0.8:2.0")
        depends_on("py-six", when="@0.13.4:1")
        depends_on("py-toml", when="@1.10:2.20")
        depends_on("py-virtualenv@20.10:", when="@2.21:")
        depends_on("py-virtualenv@20.0.8:", when="@2.4:2.20")
        depends_on("py-virtualenv@15.2:", when="@1.14.3:2.3")
    # END DEPENDENCIES

