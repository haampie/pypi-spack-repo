# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PySphinxGallery(PythonPackage):
    # BEGIN VERSIONS
    version("0.15.0", sha256="d66d38d901f6b65b6e3ee6c2584e37476b035d9e52907b1593a3f312946ae724", url="https://pypi.org/packages/a6/0b/bcb59fd0ee7f59d2f9745594f4b3f8f5011b3e16864322d2edb469cd9872/sphinx_gallery-0.15.0-py3-none-any.whl")
    version("0.14.0", sha256="55b3ad1f378abd126232c166192270ac0a3ef615dec10b66c961ed2967be1df6", url="https://pypi.org/packages/5f/69/0deaf270322a163801fbf76416c316fac1de16e74fe4730292e3f7a98bf8/sphinx_gallery-0.14.0-py3-none-any.whl")
    version("0.13.0", sha256="5bedfa4998b4158d5affc7d1df6796e4b1e834b16680001dac992af1304d8ed9", url="https://pypi.org/packages/98/65/b71d42516e6c22901f617918acf00efe2903bf187f7378fd50d7f185fba6/sphinx_gallery-0.13.0-py3-none-any.whl")
    version("0.12.2", sha256="eb8afa1f3d0b1d53bb82829559adb2aa14455493d70b025569edb084a0d14ee5", url="https://pypi.org/packages/91/4f/cca108ea0bd61cfbfb9b57a0386c5a8cacc9246c5dbae4e33245345faf1c/sphinx_gallery-0.12.2-py3-none-any.whl")
    version("0.12.1", sha256="2146a1b097b4c11c4b275ab6be275d3bf4dc8a0fd5f3f7b31097cd2f0157c513", url="https://pypi.org/packages/eb/4d/f0546184daa50d09987552551150cc6779fb6610b5bd26d332bbe959f827/sphinx_gallery-0.12.1-py3-none-any.whl")
    version("0.12.0", sha256="07cef1ab5e1fbdd51471788cf8e2fa682e73ef3d2db2bf2e472a92508c516bd9", url="https://pypi.org/packages/19/9e/598b04051dd3e371304bb68abdab299b904190c27aa6ed4b9fa57df3920c/sphinx_gallery-0.12.0-py3-none-any.whl")
    version("0.11.1", sha256="b165cb366a5768a0f36e60e5bc6828fbf55fd1831e71645310167375223aa25c", url="https://pypi.org/packages/05/f2/5ddc3048dae2e0cc825adfd353f6f47d3cec0801e5a841322c4448167c21/sphinx_gallery-0.11.1-py3-none-any.whl")
    version("0.11.0", sha256="cb360f874d26754e2353e52661cbb5c916832f08b0b250f2605d2417f7f35a82", url="https://pypi.org/packages/0b/15/943d2612539e3fdf8847a024e47e486908e3e4ac8f0cb46e499890dd99fe/sphinx_gallery-0.11.0-py3-none-any.whl")
    version("0.10.1", sha256="953f32b0833b0a689ff33516d0866865fb8601c0626811b95d2e844286d207e4", url="https://pypi.org/packages/ca/ae/b40d475572cf93b6c27440ad15b9be05f1e8d0e65f3097ca757aa0155c63/sphinx-gallery-0.10.1.tar.gz")
    version("0.10.0", sha256="d602663beddf7c2d42771a87afec22054c65105695e955e8d6dc5b654a417921", url="https://pypi.org/packages/95/58/ea652368e46c40c28b8978d464c7ab65aa4f3bc008ac200529076c391b7e/sphinx-gallery-0.10.0.tar.gz")
    version("0.7.0", sha256="05ead72c947718ab4183c33a598e29743e771dcf75aec84c53048423bd2f4580", url="https://pypi.org/packages/9d/20/79118154e64a5280060b55c7ad025ad16f89b8192a6a9f0ffdbf71717bf0/sphinx-gallery-0.7.0.tar.gz")
    version("0.4.0", sha256="a286cf2eea47ce838a0754ecef617616afb1f40e41e52fe765723464f52e0c2f", url="https://pypi.org/packages/4f/81/5fd32065c828c928d7387bec062d15a303b5a46e1ef342e56814d63c2800/sphinx-gallery-0.4.0.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-pillow", when="@0.15:")
        depends_on("py-sphinx@4.0.0:", when="@0.13:")
        depends_on("py-sphinx@3.0.0:", when="@0.11.1:0.12")
        depends_on("py-sphinx@1.8.3:", when="@0.11:0.11.0")
    # END DEPENDENCIES

