# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyReadmeRenderer(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("43.0", sha256="19db308d86ecd60e5affa3b2a98f017af384678c63c88e5d4556a380e674f3f9", url="https://pypi.org/packages/45/be/3ea20dc38b9db08387cf97997a85a7d51527ea2057d71118feb0aa8afa55/readme_renderer-43.0-py3-none-any.whl")
    version("42.0", sha256="13d039515c1f24de668e2c93f2e877b9dbe6c6c32328b90a40a49d8b2b85f36d", url="https://pypi.org/packages/b5/7e/992e0e21b37cadd668226f75fef0aa81bf21c2426c98bc06a55e514cb323/readme_renderer-42.0-py3-none-any.whl")
    version("41.0", sha256="a38243d5b6741b700a850026e62da4bd739edc7422071e95fd5c4bb60171df86", url="https://pypi.org/packages/b5/a2/99fbffc358c2d19700d3a4a038fa451e7ac6a4067a16df4588d068f841e2/readme_renderer-41.0-py3-none-any.whl")
    version("40.0", sha256="e18feb2a1e7706f2865b81ebb460056d93fb29d69daa10b223c00faa7bd9a00a", url="https://pypi.org/packages/29/a9/200b7f2397bc9f9d1653cfffa14bd57d38982317d58deac11520b7163f5c/readme_renderer-40.0-py3-none-any.whl")
    version("37.3", sha256="f67a16caedfa71eef48a31b39708637a6f4664c4394801a7b0d6432d13907343", url="https://pypi.org/packages/97/52/fd8a77d6f0a9ddeb26ed8fb334e01ac546106bf0c5b8e40dc826c5bd160f/readme_renderer-37.3-py3-none-any.whl")
    version("37.2", sha256="d3f06a69e8c40fca9ab3174eca48f96d9771eddb43517b17d96583418427b106", url="https://pypi.org/packages/20/ca/888ac82ed1ddb7cfd91a9d61d2f884ee3a5f34ef1b2a87c63d19f32ec564/readme_renderer-37.2-py3-none-any.whl")
    version("37.1", sha256="16c914ca7731fd062a316a2a8e5434a175ee34661a608af771a60c881f528a34", url="https://pypi.org/packages/2e/7e/82026464c787172b530f5194af33cc86409bebef114d6932dc452c78317d/readme_renderer-37.1-py3-none-any.whl")
    version("37.0", sha256="9fa416704703e509eeb900696751c908ddeb2011319d93700d8f18baff887a69", url="https://pypi.org/packages/02/57/84c09c2721b00eb53cebd4cc68c7c7bf666d2f9732e80dd8d4a590aeeb90/readme_renderer-37.0-py3-none-any.whl")
    version("36.0", sha256="2c37e472ca96755caba6cc58bcbf673a5574bc033385a2ac91d85dfef2799876", url="https://pypi.org/packages/0a/3e/ce07c86adbc46cfedf637dd77333184bcd0a913f9c169b0b3afc25f67b6b/readme_renderer-36.0-py3-none-any.whl")
    version("35.0", sha256="73b84905d091c31f36e50b4ae05ae2acead661f6a09a9abb4df7d2ddcdb6a698", url="https://pypi.org/packages/b0/c3/63b1bb5f406a7b223c254a5b34079f205b4f4b365143620fbc1415c98367/readme_renderer-35.0-py3-none-any.whl")
    version("24.0", sha256="c8532b79afc0375a85f10433eca157d6b50f7d6990f337fa498c96cd4bfc203d", url="https://pypi.org/packages/c3/7e/d1aae793900f36b097cbfcc5e70eef82b5b56423a6c52a36dce51fedd8f0/readme_renderer-24.0-py2.py3-none-any.whl")
    version("16.0", sha256="7f807259fc9b2ababfc1335d106fbc90254cf940f4b4e40d94aebd5a39fcab5d", url="https://pypi.org/packages/d2/c0/f16aa42d72aac3ca90aa3b4d0f80e30161b01b2873324a30772c26d43556/readme_renderer-16.0-py2.py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-bleach@2.1:", when="@17.3:41")
        depends_on("py-bleach", when="@:16")
        depends_on("py-cmarkgfm@0.2:", when="@18:22")
        depends_on("py-docutils@0.13:", when="@16:")
        depends_on("py-nh3@0.2.14:", when="@42:")
        depends_on("py-pygments@2.5:", when="@25:")
        depends_on("py-pygments", when="@:24")
        depends_on("py-six", when="@:29")
    # END DEPENDENCIES

