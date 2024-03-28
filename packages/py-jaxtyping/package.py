# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyJaxtyping(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("0.2.28", sha256="4a54eb964087cd46463d9a86c805b4e4f5c20cce5f22049d6f35a26d9f105bd3", url="https://pypi.org/packages/9a/0c/8055b6e60e6b2795c1cee6058287c39f168466e5937d6437b58b6c7e77f7/jaxtyping-0.2.28-py3-none-any.whl")
    version("0.2.27", sha256="a8eafc92106887e5d8e1ce148d5b236afaf2ee63f2b5bca3adb78aa08ae674ab", url="https://pypi.org/packages/0e/b8/11687d03bfeb824bdb20a80e1dae82b9b7f0d183e1bb77563316ef25dd18/jaxtyping-0.2.27-py3-none-any.whl")
    version("0.2.26", sha256="211d17bde8421323d9a19e10ddf49ab9e68cec5edd3c5cfc23bc95ce5a3090b1", url="https://pypi.org/packages/c1/cd/b2b1e40671cef742ea15ffeb9b5520cf5bd7e68c414c9cebc53a54e7f24f/jaxtyping-0.2.26-py3-none-any.whl")
    version("0.2.25", sha256="503772cf985ff50bd160d0661266e1628da47cc8b9a302de16f230e07f5ac119", url="https://pypi.org/packages/72/26/2dc56d7d12ed0b927fe582ece4db87d59cc916b4f3a79ac9abdc2d7daac5/jaxtyping-0.2.25-py3-none-any.whl")
    version("0.2.24", sha256="b0e90891bbee882d5d3487023d132227d45bdaca3e72937d491b74334f148826", url="https://pypi.org/packages/be/5b/474e8f71c20a3fe6059f7287c5bf194ecdee80b894633292b9da24b0c7df/jaxtyping-0.2.24-py3-none-any.whl")
    version("0.2.23", sha256="c8df034f8403dc6289117723cb43386a2f27e73dff63c8169cc4bbf3e81261bf", url="https://pypi.org/packages/1f/8f/90f81553044a40c56e546b24de94cafd0a7549ee0361ec39882c5e2abb15/jaxtyping-0.2.23-py3-none-any.whl")
    version("0.2.22", sha256="7b68a8d34bfb823ff5537b94552850a2e7f2687d61afeaee0689c0615bfcea98", url="https://pypi.org/packages/9a/ed/472785389fbbcf190671fc32f56c7323515bd931bd11e18426948cb3e509/jaxtyping-0.2.22-py3-none-any.whl")
    version("0.2.21", sha256="d94afe0def7df435090f1f699d97c06b8b8cfa04667be8fe9215a33bb0f17980", url="https://pypi.org/packages/ee/a3/fea2d62ed8b055102d52a8c2df435eb9ca924ef3d65d7114308be0ded0a7/jaxtyping-0.2.21-py3-none-any.whl")
    version("0.2.20", sha256="7038e71cc9352b67a8673d1fc39b6c7e95a326623a1fd43ee7c56faf20866ab9", url="https://pypi.org/packages/93/18/d7aa49c569dec7a84ea44fb0b2d7aff5a1579709c5576a0f1386013eace6/jaxtyping-0.2.20-py3-none-any.whl")
    version("0.2.19", sha256="651352032799d422987e783fd1b77699b53c3bb28ffa644bbca5f75ec4fbb843", url="https://pypi.org/packages/7f/8f/b39d40fef81d7def4898ad11bbe686185e09cb9e39db905e2afc77f1d350/jaxtyping-0.2.19-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("python@3.9:", when="@0.2.20:")
        depends_on("py-numpy@1.20.0:", when="@0.1:")
        depends_on("py-typeguard@2.13.3:2", when="@0.2.23:")
        depends_on("py-typeguard@2.13.3:", when="@:0.2.22")
        depends_on("py-typing-extensions@3.7.4.1:", when="@0.2.8:0.2.25")
    # END DEPENDENCIES

