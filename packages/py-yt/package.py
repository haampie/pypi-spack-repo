# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyYt(PythonPackage):
    # BEGIN VERSIONS
    version("4.1.2", sha256="0ae03288b067721baad14c016f253dc791cd444a1f2dd5d804cf91da622a0c76", url="https://pypi.org/packages/e2/57/5c519b90ce1c0d254f21b76f04c02522277a4aeabea0a9c92ff2620e8bac/yt-4.1.2.tar.gz")
    version("3.6.1", sha256="be454f9d05dcbe0623328b4df43a1bfd1f0925e516be97399710452931a19bb0", url="https://pypi.org/packages/1e/ce/e75e41f077e330f25d912eda4a1ba124e6b5f896f457ec5ca4e8c89b97c2/yt-3.6.1.tar.gz")
    version("3.6.0", sha256="effb00536f19fd2bdc18f67dacd5550b82066a6adce5b928f27a01d7505109ec", url="https://pypi.org/packages/e6/6a/b9940c45e574a0f805f5aa049e0cbbf09c3278d85c36db69859927abfbac/yt-3.6.0.tar.gz")
    version("3.5.1", sha256="c8ef8eceb934dc189d63dc336109fad3002140a9a32b19f38d1812d5d5a30d71", url="https://pypi.org/packages/10/c6/bacc5fe84e5a58d0a2d0a373de33dec5d04e4c2cadf25c41a62d76d49fa6/yt-3.5.1.tar.gz")
    version("3.5.0", sha256="ee4bf8349f02ce21f571654c26d85c1f69d9678fc8f5c7cfe5d1686c7ed2e3ca", url="https://pypi.org/packages/a6/9f/76ad98b7ec159869ab719f990aa11e06f0d149f655901abcfd845cb833b0/yt-3.5.0.tar.gz")
    version("3.4.1", sha256="a4cfc47fe21683e7a3b680c05fe2a25fb774ffda6e3939a35755e5bf64065895", url="https://pypi.org/packages/57/b7/727fc259222233f40793d9b1de9baad24b298b0760c936d0b9db76a8dee6/yt-3.4.1.tar.gz")
    version("3.4.0", sha256="de52057d1677473a83961d8a1119a9beae3121ec69a4a5469c65348a75096d4c", url="https://pypi.org/packages/64/a9/b473642ae881c207566aa5d3cf0c5f69c1131e51d1a2c9d87a255e0951ed/yt-3.4.0.tar.gz")
    version("3.3.5", sha256="4d5c751b81b0daf6dcaff6ec0faefd97138c008019b52c043ab93403d71cedf6", url="https://pypi.org/packages/93/23/0a211d87f0344ff110e0dbe5561ec497aa651f44b3037b7618118e60b7fe/yt-3.3.5.tar.gz")
    version("3.3.4", sha256="64c109ba4baf5afc0e1bc276ed2e3de13f1c5ce85c6d8b4c60e9a47c54bf3bcb", url="https://pypi.org/packages/e2/ef/677c36f38282ad70ca0919bc0fc09ed7ff0d322fcde4cb1a20befabfa5c6/yt-3.3.4.tar.gz")
    version("3.3.3", sha256="edf6453927eee311d4b51afacb52cd5504b2b57cc6d3d92dab9c6bfaf6d883df", url="https://pypi.org/packages/31/5f/b337913e202046b365b5d1d215458a2fb6c3d15f4051789d5556dd31a829/yt-3.3.3.tar.gz")
    version("3.3.2", sha256="a18e4cf498349804c64eec6509ec4d3a6beaa34ea63366543290c35774337f0e", url="https://pypi.org/packages/98/b5/9285b3634d26841103f21fbdaec9dfd80c7a215dfbd7c9312ba710f13a2a/yt-3.3.2.tar.gz")
    version("3.3.1", sha256="01e3b3398d43b8eab698d55ba37ef3d701ea026b899c0940a1ee34b215e25a31", url="https://pypi.org/packages/56/35/fcdb0364dad9f1a45b91179b5f8ee875c9e533a0564a4d9808f452f35ff2/yt-3.3.1.tar.gz")
    version("3.3.0", sha256="537c67e85c8f5cc5530a1223a74d27eb7f11c459651903c3092c6a97b450d019", url="https://pypi.org/packages/b0/7b/ef350ef5cbf139d34008f84be52dc5f3080ca0b81c5f9a97d75b6012a5bb/yt-3.3.0.tar.gz")
    version("3.2.3", sha256="4d6ccf345d9fab965335c9faf8708c7eea79366b81d77f0f302808be3e82c0ed", url="https://pypi.org/packages/de/14/f28f19ffef74ee92647181ab28dc5d0b0c34d1b9ca4a1c79c98abd43cecf/yt-3.2.3.tar.gz")
    version("3.2.2", sha256="78866f51e4751534ad60987000f149a8295952b99b37ca249d45e4d11095a5df", url="https://pypi.org/packages/37/f9/a7ef11c4d4dae512b3766d75febe100707e45dc0e453926c1134543ee3a3/yt-3.2.2.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    variant("astropy", default=False)
    variant("h5py", default=False)
    variant("rockstar", default=False)
    variant("scipy", default=False)
    # END VARIANTS

    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("python@3.9:", when="@4.3:")
        depends_on("python@:3.11", when="@4:4.0")
        depends_on("py-cython", when="@3.3.2:3.3")
        depends_on("py-ipython@1:", when="@3.4:3.6.0")
        depends_on("py-ipython", when="@3.3.2:3.3")
        depends_on("py-matplotlib@1.5.3:", when="@3.4:3.6.0")
        depends_on("py-matplotlib", when="@3.3.2:3.3")
        depends_on("py-numpy@1.10.4:", when="@3.4:3.6.0")
        depends_on("py-numpy", when="@3.3.2:3.3")
        depends_on("py-setuptools@19.6:", when="@3.3.2:3.6.0")
        depends_on("py-sympy@1:", when="@3.4:3.6.0")
        depends_on("py-sympy", when="@3.3.2:3.3")
    # END DEPENDENCIES

