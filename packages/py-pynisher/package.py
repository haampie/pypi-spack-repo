##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPynisher(PythonPackage):
    version("1.0.10", sha256="2722b795d22129ddd5247038bba727ae06ecdb3a5942070817be7c8d4a680e31", url="https://pypi.org/packages/eb/56/1d5ed36041e11c943833a93137ff2562db97da48851d68431f1feaa8f82f/pynisher-1.0.10.tar.gz")
    version("1.0.9", sha256="865379b9496099c8a942a9abdb6ac1db8e681173947b9581f635a8ecc5d75621", url="https://pypi.org/packages/e2/b4/f3bedf863f036956cb7e8a0e209fe8a7dfa644256c2c03b9709d2c62d79f/pynisher-1.0.9.tar.gz")
    version("1.0.8", sha256="0531f7e33bfb38069529cdb454049fbf741ac40b7f635e0391dfcf068fd5eafa", url="https://pypi.org/packages/6b/7e/d0858a7b8d2c2fdc9a886f1259e08052635a323a42673a804392022efcc2/pynisher-1.0.8.tar.gz")
    version("1.0.7", sha256="72a811a15dc0267f7acc024319b449e5edf1393bae8e606ef07c198b6450e866", url="https://pypi.org/packages/6f/05/bcb70c171ee9a85b245034e428e4f88f34a34637cfa620233eef90b0fb33/pynisher-1.0.7.tar.gz")
    version("1.0.6", sha256="2b259b5c10d230b6bf9b575e8da520001d119bbbadb0c7c0faacf7a167c87ad3", url="https://pypi.org/packages/b7/33/8e9a0cbf2bd7aeb6a2b2a003d8ebe6c19fda10150d4efdae1dacd78d4fac/pynisher-1.0.6.tar.gz")
    version("1.0.5", sha256="bac4a8c200b0193013897d5d6cfa5270ef7f148f84e7aeddbc6671002fb34b5e", url="https://pypi.org/packages/06/c9/ae65927f382f80e99841d05b3ef19fc5dd6fa0684f00812ed055c0909821/pynisher-1.0.5.tar.gz")
    version("1.0.4", sha256="e6ebcd4dfd62fd01a86f65229a1ed7c73962617af477f06e53628e4e60abf96b", url="https://pypi.org/packages/0a/16/d053c45db6297062129988531c617d1ce4ebd47896940b6200c8d3d8292e/pynisher-1.0.4.tar.gz")
    version("1.0.3", sha256="2156f60967045b5ef12feb237201e17c1f8d3054879114c87aea7debd2279003", url="https://pypi.org/packages/65/dc/b1a3858d80c9c6cc8c04e834b223557e63f9e0551d3b197121e355ef7b74/pynisher-1.0.3.tar.gz")
    version("1.0.2", sha256="0642911415809ec90836b06908ef7412a85c20cc9e0818919fb59b6254ec407e", url="https://pypi.org/packages/ac/01/b7b6899686c440cc3ec2d08672fe6989d7ae465c74eadcd61379a0bda2e1/pynisher-1.0.2.tar.gz")
    version("1.0.1", sha256="cef15ca67bd082e655ef099006a38bbc6bf19fe9ba4a7994b4c23c441c53b51b", url="https://pypi.org/packages/03/f9/f6779c9e5c72d0dbd51e633e22a1f2158a625de4c63115f8a83d340d7f74/pynisher-1.0.1.tar.gz")
    version("0.6.4", sha256="111d91aad471375c0509a912415ff90053ef909100facf412511383af107c124", url="https://pypi.org/packages/8d/39/edac9acf3bd245ecf475151014cce3652c25ca3c2352eac725502cfce6ea/pynisher-0.6.4.tar.gz")

    with default_args(type="run"):
        depends_on("py-psutil", when="@1.0.10:")
        depends_on("py-pywin32", when="@1.0.10: platform=windows")
        depends_on("py-typing-extensions", when="@1.0.10:")

