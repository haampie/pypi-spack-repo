# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyNumcodecs(PythonPackage):
    # BEGIN VERSIONS
    version("0.12.1", sha256="05d91a433733e7eef268d7e80ec226a0232da244289614a8f3826901aec1098e", url="https://pypi.org/packages/b7/1b/1f1d880e29e719c7c6205065d1afbc91114c0d91935ac419faa43e5e08b0/numcodecs-0.12.1.tar.gz")
    version("0.12.0", sha256="6388e5f4e94d18a7165fbd1c9d3637673b74157cff8bc644005f9e2a4c717d6e", url="https://pypi.org/packages/cd/cf/790853e781102997154abb093c4afe9f380065615490a3b045e38c690ca6/numcodecs-0.12.0.tar.gz")
    version("0.11.0", sha256="6c058b321de84a1729299b0eae4d652b2e48ea1ca7f9df0da65cb13470e635eb", url="https://pypi.org/packages/19/0f/006424c07b551a13c773b59a3656beadbaadbcf9df1601e87fcae342618c/numcodecs-0.11.0.tar.gz")
    version("0.10.2", sha256="22838c6b3fd986bd9c724039b88870057f790e22b20e6e1cbbaa0de142dd59c4", url="https://pypi.org/packages/91/71/3942cb3cc8de0d702a896435c1d905a000facd55ba58afe33bd19b93f232/numcodecs-0.10.2.tar.gz")
    version("0.10.1", sha256="8ed6b01477570bc478c44b9077514e2e2f59a647a6a2b7c6fcc192f1092f804b", url="https://pypi.org/packages/81/d5/1bdc5078b420fc5923781b4008452fdd85fa91ed5f436d00652f5421228c/numcodecs-0.10.1.tar.gz")
    version("0.10.0", sha256="2dd42564e7772a9385923b02a363e3cedf053ce93094a9064485e7f69a6f1c92", url="https://pypi.org/packages/09/a9/7e6eb6c1465121b80bbb9dd3599a01ac6ece3fc446ab1290bda25730b6c5/numcodecs-0.10.0.tar.gz")
    version("0.9.1", sha256="35adbcc746b95e3ac92e949a161811f5aa2602b9eb1ef241b5ea6f09bb220997", url="https://pypi.org/packages/2c/b0/980143fa7467569fd81f0d00530c46dcf41ff790738261985dc10a26d4ec/numcodecs-0.9.1.tar.gz")
    version("0.9.0", sha256="3c23803671a3d920efa175af5828870bdff60ba2a3fcbf1d5b48bb81d68219c6", url="https://pypi.org/packages/c5/ad/d652fe094bc7edf05753b349b93c402a400ea794d305ceb8f92da7e7780c/numcodecs-0.9.0.tar.gz")
    version("0.8.1", sha256="63e75114131f704ff46ca2fe437fdae6429bfd9b4377e356253eb5dacc9e093a", url="https://pypi.org/packages/e9/a5/e70c21c9af22a4416680f6eed8947fb5e8dd01f534b167e608796816cc7e/numcodecs-0.8.1.tar.gz")
    version("0.8.0", sha256="7c7d0ea56b5e2a267ae785bdce47abed62829ef000f03be8e32e30df62d3749c", url="https://pypi.org/packages/59/99/355e23e418f003a0e99db515b95fb09e0754acfb2ab0d782c7144db4293f/numcodecs-0.8.0.tar.gz")
    version("0.7.3", sha256="022b12ad83eb623ec53f154859d49f6ec43b15c36052fa864eaf2d9ee786dd85", url="https://pypi.org/packages/fa/1d/644b26dbc7fe9666223e8744680213e5dad4db0fe67034ddf6d02ec8b1a0/numcodecs-0.7.3.tar.gz")
    version("0.6.4", sha256="ef4843d5db4d074e607e9b85156835c10d006afc10e175bda62ff5412fca6e4d", url="https://pypi.org/packages/53/2a/1dc435cbd1d082827190a3e46168fd04f74e266e91313969d5a1aab601bf/numcodecs-0.6.4.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    variant("msgpack", default=False)
    # END VARIANTS

    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-msgpack", when="@0.12:+msgpack")
        depends_on("py-numpy@1.7:", when="@0.12:")
    # END DEPENDENCIES

