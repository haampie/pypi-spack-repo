# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyFastavro(PythonPackage):
    # BEGIN VERSIONS
    version("1.9.4", sha256="56b8363e360a1256c94562393dc7f8611f3baf2b3159f64fb2b9c6b87b14e876", url="https://pypi.org/packages/90/92/c6b038c0a00230906810e665ed787cb5ec975ef339630cb03fbd8d667a6a/fastavro-1.9.4.tar.gz")
    version("1.9.3", sha256="a30d3d2353f6d3b4f6dcd6a97ae937b3775faddd63f5856fe11ba3b0dbb1756a", url="https://pypi.org/packages/b0/46/397429bb5dee5b765aff69cd53d0351b26df8b193c9aa8669044573baf27/fastavro-1.9.3.tar.gz")
    version("1.9.2", sha256="5c1ffad986200496bd69b5c4748ae90b5d934d3b1456f33147bee3a0bb17f89b", url="https://pypi.org/packages/84/3c/e960e7e292e3e89b939bd69b2426db076d1945b8cff26a58cf40637544c1/fastavro-1.9.2.tar.gz")
    version("1.9.1", sha256="f37011d66de8ba81b26760db0478009a14c08ebfd34269b3390abfd4616b308f", url="https://pypi.org/packages/08/29/008a1e50b064269a286aab7be465850fb56ab607c3320835c951aaac8bcb/fastavro-1.9.1.tar.gz")
    version("1.9.0", sha256="71aad82b17442dc41223f8351b9f28a60dd877a8e5a7525eaf6342f45f6d23e1", url="https://pypi.org/packages/9d/64/b23f1042d88660dd19ef99803c35bcdd5e14dcf3a509d6d57f3ed6a40342/fastavro-1.9.0.tar.gz")
    version("1.8.4", sha256="dae6118da27e81abf5957dc79a6d778888fc1bbf67645f52959cb2faba95beff", url="https://pypi.org/packages/3c/3f/16c6e903d274e052d3269d01b871c7e349db9b85aacc9df22ad820a8be90/fastavro-1.8.4.tar.gz")
    version("1.8.3", sha256="a6c2ec69516e908fce64d93a13e6e83afb880f2edb5ad3adaa1eb04c918de6d8", url="https://pypi.org/packages/6e/52/107038ee38bbd5cb2700b23dc72595c7a7d94677e2edf382f2b41e1c5aad/fastavro-1.8.3.tar.gz")
    version("1.8.2", sha256="ab9d9226d4b66b6b3d0661a57cd45259b0868fed1c0cd4fac95249b9e0973320", url="https://pypi.org/packages/cc/ea/f60f22c91e4b43e6e4feed52de575c1bef0f3bc611490b2d7c0d9d78fc59/fastavro-1.8.2.tar.gz")
    version("1.8.1", sha256="85bb4f129ea947dd18432cd63fd3d9ca30d75921dd79202c1258cbcfe7928644", url="https://pypi.org/packages/be/6d/9f0b8839b4b2916554420826214001a464fc8de04ab5564777c5d4018ef5/fastavro-1.8.1.tar.gz")
    version("1.8.0", sha256="f41c5c04157ad7e7ac6e93bbabbb61fbdef0c2542f1a610f1db461bfe6141d57", url="https://pypi.org/packages/4f/06/79fa40827fbf55143d488758fb4ca8e82a6b6c5c7932c93301f3b65a5a63/fastavro-1.8.0.tar.gz")
    version("1.0.0.post1", sha256="77e21bdcefc278df1d4c12e7bf787dcf767870478870a6e9e334a2cd486f1820", url="https://pypi.org/packages/bd/bb/be327ed421ec063418ca2e328871f6b28f4efaeeef1bed5e3215c0140110/fastavro-1.0.0.post1.tar.gz")
    version("1.0.0", sha256="c37c640f0e843880c6db5f314dd284d4c8ce79d40b9cd00194042244aa8bd626", url="https://pypi.org/packages/19/b1/3fc23eb5c5f32ec69dc072bc383c79ed013eb1fb178cae4e0b9576527ea5/fastavro-1.0.0.tar.gz")
    version("0.24.2", sha256="960b30cf364cf9bfe17219fc9fac4958290ae2814e23b4b0edd54292fd28d08d", url="https://pypi.org/packages/d3/4b/a6a51523c745cd4bd6a9814af9332fc028fbfd9191be8214667342886e92/fastavro-0.24.2.tar.gz")
    version("0.24.1", sha256="d9cdee09dc5f0dc6fc0f67a01a3eb97ebcbbc7a77bf9bdd72d566e21aeb9a9dd", url="https://pypi.org/packages/aa/ab/2d101718816bc0ef46a8e59e02c8a26e125d421dd8b2110f8be32abfb8ad/fastavro-0.24.1.tar.gz")
    version("0.24.0", sha256="28b2462c83164cf5a4a6944fc8a5425d15499dffeadb1b8a328ed78988d02022", url="https://pypi.org/packages/64/27/6cacb70babcaf9a6ec4bb2bdffdfa8c9ae5bf430055841bde58d2c665fc4/fastavro-0.24.0.tar.gz")
    version("0.23.6", sha256="47e1180022823cd03cc979a3f8a47b0721e73e98eebebc9015aa89c1019ac889", url="https://pypi.org/packages/ee/bb/8dd21f0791a6b6f1bd727d63e8814eae1fe169e388876b2dfdb5136554a0/fastavro-0.23.6.tar.gz")
    version("0.23.5", sha256="2e283274bb79e6b8101a2f97fa519b392512ac013afdc5ebd1f698c7ec087fa4", url="https://pypi.org/packages/b1/80/5e9b88e648301d1f0c4aa2eaca27dc86fc261d23624c5b90a81a8a760fe8/fastavro-0.23.5.tar.gz")
    version("0.23.4", sha256="4d102fbfe044c2f9006114484e16d478de9863ef78fad237a2e2792aae1a5901", url="https://pypi.org/packages/77/dc/3c5bf0d434c95336aa471469f8c2bdf695769f9ecf8fa743b91716361f6e/fastavro-0.23.4.tar.gz")
    version("0.23.3", sha256="ca8395bdfda867ab8a6410c36cfffce72e1560def832f7a4fc5bed7436e46051", url="https://pypi.org/packages/2d/8f/213a449898de8dc98a9d1e4405578d7433064f3337b7f155b6893a0e9d1d/fastavro-0.23.3.tar.gz")
    version("0.23.2", sha256="29fb4b2613c5be5f1f643e171efab1b167e5fe3a24fdcd6acbcc1d2aa4275a8c", url="https://pypi.org/packages/c8/f6/040ad34c5b63af88ef2faa0247865d80468946989c42a77a23d345dd155e/fastavro-0.23.2.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    # END DEPENDENCIES

