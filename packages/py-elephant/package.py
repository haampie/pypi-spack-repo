# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyElephant(PythonPackage):
    # BEGIN VERSIONS
    version("0.14.0", sha256="02ce3b2a8d08dc19828f95384551339ea0946bc405c1db9aace54135417c2b0f", url="https://pypi.org/packages/fe/6a/3452291852f1a5b327e99db9a96272914d6bd38b8c9d751e86bea97a0094/elephant-0.14.0.tar.gz")
    version("0.13.0", sha256="2c6463cf9ace41631f2af196c5b80b468bf1c4b264d3a6b1ea0fb587d9e7dd67", url="https://pypi.org/packages/aa/e5/a42131ffa1de8e379ba56d67c85824d2471e6fbedcf710283f589c0dd4a4/elephant-0.13.0.tar.gz")
    version("0.12.0", sha256="81f8d668f92d8688344bb7a9c5abaa8438d824560c935a411e6e36ddf7dc7c72", url="https://pypi.org/packages/73/ef/e5308696a3e7fda842f58363a9db6690d42f30a7ebf818e15cc28014bf87/elephant-0.12.0.tar.gz")
    version("0.11.2", sha256="f8759fff0bbb136ae4ffc8d1eacadeea8ba56610d705c3bf207de87ada3ba240", url="https://pypi.org/packages/dc/54/c3303b8af84ea5ee3c7b720620797d988553d8a5703e264c1c2549841380/elephant-0.11.2.tar.gz")
    version("0.11.1", sha256="d604a202583440fdf9d95d42cef50a410bd74fcaaa1a925b139435f27ab012ef", url="https://pypi.org/packages/2e/ea/2115c6230778bb1355594c60adaff23de4411134eda86358a9363626425c/elephant-0.11.1.tar.gz")
    version("0.11.0", sha256="7b547964dbd196361edc922db2c5a7c0c886ef1effcca6c6dc7adb06f966a3be", url="https://pypi.org/packages/77/a4/db60b3529e39286f90adbe04ba6f6a41549441b1a10a38cde5384bb7d0b4/elephant-0.11.0.tar.gz")
    version("0.10.0", sha256="7e69a113475e4db01b3563328953c037d37f1597d9f2edf0d51fb65e9aebf096", url="https://pypi.org/packages/0e/65/b4370f4d1a5ecfe07ba9aee921295ba22335eb6061d9db1aeda1f45c0602/elephant-0.10.0.tar.gz")
    version("0.9.0", sha256="3e3d4a8e45d708f48bdcadcc4933c66f757d1ede6a1e172af0c07331b64ca180", url="https://pypi.org/packages/cc/3d/e3ed66d0bd69328db8c69a08830da23ad7129c0339bcc725050393764ee2/elephant-0.9.0.tar.gz")
    version("0.8.0", sha256="f7c2649d5b7cfdbaa4442457c75f86af01cc8e7ce2c63f5b3d4687bb94e10af2", url="https://pypi.org/packages/b9/c9/f233456e94b88548f6b9f8974b3bd0c5e01bea62b11ac1d66300cc2ee5a5/elephant-0.8.0.tar.gz")
    version("0.7.0", sha256="76785fe10c40042504928fde2fc57182230bbe39cf0fb0dcaffaba76219b046a", url="https://pypi.org/packages/60/3b/7180eb1970ce806b8059c0ab68e42e7a784de176cc38a6adb66b1f84a132/elephant-0.7.0.tar.gz")
    version("0.6.4", sha256="b8c5f2c00ad3249e1fe428d0b8a1dbcaee4a69464481f5f8fd55d2f7f22c45a3", url="https://pypi.org/packages/a9/23/5a03b202532cf19196b6f8bab7ea58c3dc2bec9ac183da7e9e02d886e167/elephant-0.6.4.tar.gz")
    version("0.4.1", sha256="86b21a44cbacdc09a6ba6f51738dcd5b42ecd553d73acb29f71a0be7c82eac81", url="https://pypi.org/packages/ff/2b/cf614d7e039f9ffcc9fded53c47a268503e569b1ec0d838eac6edca3211a/elephant-0.4.1.tar.gz")
    version("0.3.0", sha256="747251ccfb5820bdead6391411b5faf205b4ddf3ababaefe865f50b16540cfef", url="https://pypi.org/packages/73/d0/c0695e2221f2a9ff23741f01c42e224dce4cf5e8813861e52a0e611299a4/elephant-0.3.0.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    variant("docs", default=False, description="docs")
    variant("extras", default=False, description="extras")
    # END VARIANTS

    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("python@3.8:", when="@0.12:")
        depends_on("python@3.7:", when="@0.11")
        depends_on("py-jinja2@2.11.2:", when="@0.14:+extras")
        depends_on("py-jupyter", when="@0.14:+docs")
        depends_on("py-matplotlib@3.3.2:", when="@0.14:+docs")
        depends_on("py-nbsphinx@0.8:", when="@0.14:+docs")
        depends_on("py-neo@0.10:", when="@0.14:")
        depends_on("py-numpy@1.19.5:", when="@0.14:")
        depends_on("py-numpydoc@1.1:", when="@0.14:+docs")
        depends_on("py-pandas@0.18:", when="@0.14:0+extras")
        depends_on("py-quantities@0.14.1:", when="@0.14:")
        depends_on("py-scikit-learn@0.23.2:", when="@0.14:+extras")
        depends_on("py-scipy@1.5.4:", when="@0.14:")
        depends_on("py-six@1.10:", when="@0.14:")
        depends_on("py-sphinx@3.3:", when="@0.14:+docs")
        depends_on("py-sphinx-tabs@1.3:", when="@0.14:+docs")
        depends_on("py-sphinxcontrib-bibtex@2:", when="@0.14:+docs")
        depends_on("py-statsmodels@0.12.1:", when="@0.14:+extras")
        depends_on("py-tqdm", when="@0.14:")
    # END DEPENDENCIES

