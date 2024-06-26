# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyKeras(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("3.1.1", sha256="b5d45f0b5116b11db502da00bd501592364325d01724e6cb2032711e3e32677e", url="https://pypi.org/packages/59/a8/d94e8acb59d678d908fe1db0c7ad89dfa2c2e2e529eeb3c2b3cc218a758d/keras-3.1.1-py3-none-any.whl")
    version("3.1.0", sha256="7a7c35cc3a3292a4a0e2170bc36b6439240bd9e2ae21d8f0c3eb7068e8160908", url="https://pypi.org/packages/38/28/63b0e7851c36dcb1a10757d598c68cc1e48a669bdb63bfdd9a1b9b1c643f/keras-3.1.0-py3-none-any.whl")
    version("3.0.5", sha256="4a022f2e97ea5a3db12ed809ffcb7ce1ef8d34feaeac52315ec8553ded2dcf97", url="https://pypi.org/packages/b0/b2/104733bb67fde86f3d10010f0b5c93cfa1d5bf552f904584cf9e5b3ba719/keras-3.0.5-py3-none-any.whl")
    version("3.0.4", sha256="579138e667d9c65d5e30df470175f2c6d39f95dc308c9d825957a875459939f9", url="https://pypi.org/packages/a3/31/982a0c8da5e06b8e915e09e7cae7f7815eecfef7e9e16fd733b105aa09ab/keras-3.0.4-py3-none-any.whl")
    version("3.0.3", sha256="d87f1d0a42beca7f32b1fb0cf4e75f6ea57a2b166da6d33abc164019507a77f3", url="https://pypi.org/packages/2f/4c/6cf3038612d54bc5bee37b7350b6173511234d61c3fce70d11fa1686cd20/keras-3.0.3-py3-none-any.whl")
    version("3.0.2", sha256="db632678126ae6fb8d7398cb3c3cf0b0842850c7ad803e743b86a5d55cb32fa4", url="https://pypi.org/packages/ca/48/643d21747d52fa380f572f76c493779fc5b4bd03605247209d2dd0a6d9a9/keras-3.0.2-py3-none-any.whl")
    version("3.0.1", sha256="69f1a5174ccd98fc5db80ab8a195442f88b3a18bc5df72482df417f142aabad0", url="https://pypi.org/packages/b2/e4/30b53d839608d2212b97972a8516ba0c7e776ee1102eaa82624807b944cf/keras-3.0.1-py3-none-any.whl")
    version("3.0.0", sha256="ff3f3efa2aa5cc134b1d8b85693aab32558b1d9c860630a13f58934e6d1c908d", url="https://pypi.org/packages/24/63/bbc83d949e1940d079dcd1cd87e31498bfb71d641c8e33d917ca3f2e51a9/keras-3.0.0-py3-none-any.whl")
    version("2.15.0", sha256="2dcc6d2e30cf9c951064b63c1f4c404b966c59caf09e01f3549138ec8ee0dd1f", url="https://pypi.org/packages/fc/a7/0d4490de967a67f68a538cc9cdb259bff971c4b5787f7765dc7c8f118f71/keras-2.15.0-py3-none-any.whl")
    version("2.14.0", sha256="d7429d1d2131cc7eb1f2ea2ec330227c7d9d38dab3dfdf2e78defee4ecc43fcd", url="https://pypi.org/packages/fe/58/34d4d8f1aa11120c2d36d7ad27d0526164b1a8ae45990a2fede31d0e59bf/keras-2.14.0-py3-none-any.whl")
    version("2.13.1", sha256="5ce5f706f779fa7330e63632f327b75ce38144a120376b2ae1917c00fa6136af", url="https://pypi.org/packages/2e/f3/19da7511b45e80216cbbd9467137b2d28919c58ba1ccb971435cb631e470/keras-2.13.1-py3-none-any.whl")
    version("2.12.0", sha256="35c39534011e909645fb93515452e98e1a0ce23727b55d4918b9c58b2308c15e", url="https://pypi.org/packages/d5/80/34e55d7e3ed9cf18020929460f969de1bf82cf2f509c639b358ae2b25618/keras-2.12.0-py2.py3-none-any.whl")
    version("2.11.0", sha256="38c6fff0ea9a8b06a2717736565c92a73c8cd9b1c239e7125ccb188b7848f65e", url="https://pypi.org/packages/de/44/bf1b0eef5b13e6201aef076ff34b91bc40aace8591cd273c1c2a94a9cc00/keras-2.11.0-py2.py3-none-any.whl")
    version("2.10.0", sha256="26a6e2c2522e7468ddea22710a99b3290493768fc08a39e75d1173a0e3452fdf", url="https://pypi.org/packages/f9/4d/dc255a437c9616b155e5bd55e325e092b7cdcb4652361d733ae051d40853/keras-2.10.0-py2.py3-none-any.whl")
    version("2.9.0", sha256="55911256f89cfc9343c9fbe4b61ec45a2d33d89729cbe1ab9dcacf8b07b8b6ab", url="https://pypi.org/packages/ff/ff/f25909606aed26981a8bd6d263f89d64a20ca5e5316e6aafb4c75d9ec8ae/keras-2.9.0-py2.py3-none-any.whl")
    version("2.8.0", sha256="744d39dc6577dcd80ff4a4d41549e92b77d6a17e0edd58a431d30656e29bc94e", url="https://pypi.org/packages/4f/2f/eb9391bdcba2693cc8396f244bd3b4512bcd1123c2ea06f4dfcf50dc5ce9/keras-2.8.0-py2.py3-none-any.whl")
    version("2.7.0", sha256="0c33ae1f728064ca0d35dfba999e9c316f03623bf5688c82fb83cc74a80ea248", url="https://pypi.org/packages/6b/8b/065f94ba03282fa41b2d76942b87a180a9913312c4611ea7d6508fbbc114/keras-2.7.0-py2.py3-none-any.whl")
    version("2.6.0", sha256="504af5656a9829fe803ce48a8580ef16916e89906aceddad9e098614269437e7", url="https://pypi.org/packages/5a/38/04d9b7fb53acdf861df2c4505fa96b06c779817a511e94b8882d284ba360/keras-2.6.0-py2.py3-none-any.whl")
    version("2.4.3", sha256="05e2faf6885f7899482a7d18fc00ba9655fe2c9296a35ad96949a07a9c27d1bb", url="https://pypi.org/packages/44/e1/dc0757b20b56c980b5553c1b5c4c32d378c7055ab7bfa92006801ad359ab/Keras-2.4.3-py2.py3-none-any.whl")
    version("2.4.2", sha256="8cf38465ed5a7679c5b4ec7b7ac1c34895e4e9943254cd46be6151a2faef0b1f", url="https://pypi.org/packages/17/c7/9eb83942f2dfc84503125c93a40fce94a100ea911f033dcb63805cb63fb0/Keras-2.4.2-py2.py3-none-any.whl")
    version("2.4.1", sha256="3bf6fb704bbb6d75ed7d10ea4ba4e9bfa12d1ce24bcd942e70edde44e2d0e1b5", url="https://pypi.org/packages/a2/35/321f9d354ac1e8c21bb8b650ca183474397c2b485eff741efcbf06e75f5a/Keras-2.4.1-py2.py3-none-any.whl")
    version("2.4.0", sha256="d23f98be074a9fea1f99c9822f775b1d244de065a6f7480ca9dfa1e8d0296e87", url="https://pypi.org/packages/b6/19/9d8f1c86c09d05369da39b03d011cd689edef86c0e6b2777dbcedc49dfc6/Keras-2.4.0-py2.py3-none-any.whl")
    version("2.3.1", sha256="d08a57bd63546175f8f19232ba05906514d419da3e0af8ef7437fa1c11442e20", url="https://pypi.org/packages/ad/fd/6bfe87920d7f4fd475acd28500a42482b6b84479832bdc0fe9e589a60ceb/Keras-2.3.1-py2.py3-none-any.whl")
    version("2.3.0", sha256="ff7db814756d9106c273afc4bd798f48924fa66f9328157a4b722d535baef363", url="https://pypi.org/packages/1b/18/2e1ef121e5560ac24c7ac9e363aa5fa7006c40563c989e7211aba95b793a/Keras-2.3.0-py2.py3-none-any.whl")
    version("2.2.5", sha256="5a75cfdf69c6cb9de81a82aa19542ac69a5c2e78a48a58c1649fc5cdb55c917c", url="https://pypi.org/packages/f8/ba/2d058dcf1b85b9c212cc58264c98a4a7dd92c989b798823cc5690d062bb2/Keras-2.2.5-py2.py3-none-any.whl")
    version("2.2.4", sha256="794d0c92c6c4122f1f0fcf3a7bc2f49054c6a54ddbef8d8ffafca62795d760b6", url="https://pypi.org/packages/5e/10/aa32dad071ce52b5502266b5c659451cfd6ffcbf14e6c8c4f16c0ff5aaab/Keras-2.2.4-py2.py3-none-any.whl")
    version("2.2.3", sha256="fd5a2b129d3eba8cdb2b0454b7abfae4b9d8c9e17d0300cd66bba43de8d256f2", url="https://pypi.org/packages/06/ea/ad52366ce566f7b54d36834f98868f743ea81a416b3665459a9728287728/Keras-2.2.3-py2.py3-none-any.whl")
    version("2.2.2", sha256="253cce021d73fa6d6e69e740bd985d6e2419dcb9fca96b2c8dbdd1736e3ec68d", url="https://pypi.org/packages/34/7d/b1dedde8af99bd82f20ed7e9697aac0597de3049b1f786aa2aac3b9bd4da/Keras-2.2.2-py2.py3-none-any.whl")
    version("2.2.1", sha256="64633419cb4ca46402b1da1ae76b19e23913131a0e43b2fa0afa276f187c14be", url="https://pypi.org/packages/62/51/0192489a2614e8c6a22de860e43221e566f4bbd44a047ff48c2fdbc59373/Keras-2.2.1-py2.py3-none-any.whl")
    version("2.2.0", sha256="fa71a1f576dbd643532b872b8952afb65cc3ff7ed20d172e6b49657b710b43d0", url="https://pypi.org/packages/68/12/4cabc5c01451eb3b413d19ea151f36e33026fc0efb932bf51bcaf54acbf5/Keras-2.2.0-py2.py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    variant("backend", default=False, description="backend")
    # END VARIANTS

    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("python@3.9:", when="@2.14,3:")
        depends_on("python@3.8:", when="@2.12:2.13,2.15:2")
        depends_on("python@3.7:", when="@2.11")
        depends_on("py-absl-py", when="@3:")
        depends_on("py-dm-tree", when="@3:3.0")
        depends_on("py-h5py", when="@2.1.6:2.4,3:")
        depends_on("py-keras-applications@1.0.8:", when="@2.2.5:2.2")
        depends_on("py-keras-applications@1.0.6:", when="@2.2.3:2.2.4,2.3")
        depends_on("py-keras-applications@1.0.4", when="@2.2.1:2.2.2")
        depends_on("py-keras-applications@1.0.2", when="@2.2:2.2.0")
        depends_on("py-keras-preprocessing@1.1:", when="@2.2.5:2.2")
        depends_on("py-keras-preprocessing@1.0.5:", when="@2.2.3:2.2.4,2.3")
        depends_on("py-keras-preprocessing@1.0.2", when="@2.2.1:2.2.2")
        depends_on("py-keras-preprocessing@1.0.1", when="@2.2:2.2.0")
        depends_on("py-ml-dtypes", when="@3.0.5:")
        depends_on("py-namex", when="@3:")
        depends_on("py-numpy", when="@3:")
        depends_on("py-numpy@1.9.1:", when="@2.0.8:2.4")
        depends_on("py-optree", when="@3.1:")
        depends_on("py-pyyaml", when="@:2.4")
        depends_on("py-rich", when="@3:")
        depends_on("py-scipy@0.14:", when="@2.0.8:2.4")
        depends_on("py-six@1.9:", when="@2.0.8:2.3")
        depends_on("py-tensorflow", when="@2.4.1")
        depends_on("py-tensorflow@2.2.0:", when="@2.4:2.4.0")
    # END DEPENDENCIES

