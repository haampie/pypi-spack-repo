# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyHuggingfaceHub(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("0.21.4", sha256="df37c2c37fc6c82163cdd8a67ede261687d80d1e262526d6c0ce73b6b3630a7b", url="https://pypi.org/packages/ab/28/d4b691840d73126d4c9845f8a22dad033ac872509b6d3a0d93b456eef424/huggingface_hub-0.21.4-py3-none-any.whl")
    version("0.21.3", sha256="b183144336fdf2810a8c109822e0bb6ef1fd61c65da6fb60e8c3f658b7144016", url="https://pypi.org/packages/47/8f/cf6683de320cf3873850ba48b7383db96958fe435b8e227db92119f6d867/huggingface_hub-0.21.3-py3-none-any.whl")
    version("0.21.2", sha256="16955c2b60bcff32a0778f84b9e9ae8f61d7f003da6aa1fbb7bc897a0c37b28c", url="https://pypi.org/packages/3d/c8/c3342c97848896df5d78d18abd94c558e457a4f02feec99a79989d8c30e0/huggingface_hub-0.21.2-py3-none-any.whl")
    version("0.21.1", sha256="b40dd1dc5c589b7c73178f5f17996bac516524dce83f16d5219a83e33a565712", url="https://pypi.org/packages/15/95/614f1a310e333e9bbf338bcc3c9378aa4c5ae7978b8621c934e27ce6befc/huggingface_hub-0.21.1-py3-none-any.whl")
    version("0.21.0", sha256="59c17d65c9b8f011dbf2719436802c863c041eec95d21addb60568110323b48d", url="https://pypi.org/packages/76/4d/8def98a3925c1e3a1b26eebdcf21ebc25e997b9ce85fd1c88290104b9ae5/huggingface_hub-0.21.0-py3-none-any.whl")
    version("0.20.3", sha256="d988ae4f00d3e307b0c80c6a05ca6dbb7edba8bba3079f74cda7d9c2e562a7b6", url="https://pypi.org/packages/28/03/7d3c7153113ec59cfb31e3b8ee773f5f420a0dd7d26d40442542b96675c3/huggingface_hub-0.20.3-py3-none-any.whl")
    version("0.20.2", sha256="53752eda2239d30a470c307a61cf9adcf136bc77b0a734338c7d04941af560d8", url="https://pypi.org/packages/3d/0a/aed3253a9ce63d9c90829b1d36bc44ad966499ff4f5827309099c8c9184b/huggingface_hub-0.20.2-py3-none-any.whl")
    version("0.20.1", sha256="ecfdea395a8bc68cd160106c5bd857f7e010768d95f9e1862a779010cc304831", url="https://pypi.org/packages/a0/0a/02ac0ae1047d97769003ff4fb8e6717024f3f174a5d13257415aa09e13d9/huggingface_hub-0.20.1-py3-none-any.whl")
    version("0.20.0", sha256="ff3836f3b00e09222f6c623eda9e5a24e658cb54c1fad1fa29d0e3bee9002110", url="https://pypi.org/packages/69/03/46f112e2e415926bc7bdac2f5366572de0c28cb88051537b25a586b5d881/huggingface_hub-0.20.0-py3-none-any.whl")
    version("0.19.4", sha256="dba013f779da16f14b606492828f3760600a1e1801432d09fe1c33e50b825bb5", url="https://pypi.org/packages/05/09/1945ca6ba3ad8ad6e2872ba682ce8d68c5e63c8e55458ed8ab4885709f1d/huggingface_hub-0.19.4-py3-none-any.whl")
    version("0.19.3", sha256="5f6c0d466728bc0e955ce3bfc5a54bd28a8ef9753d6d410dc23f308199f80d3f", url="https://pypi.org/packages/38/f6/06d7489a9f1b2112a640b3272abd43319d0ee625f26efafb350106893c19/huggingface_hub-0.19.3-py3-none-any.whl")
    version("0.19.2", sha256="0449f5dcf681729dabf1887ec96858c1587efaba1d2c3d9c0b205a8d5dd2ff34", url="https://pypi.org/packages/38/ea/01fab9eaff633d522d84fc76c6973873abbd54baafba03bf5992c8ef144a/huggingface_hub-0.19.2-py3-none-any.whl")
    version("0.19.1", sha256="7131d1fc3f6794e1d2c16d05b0a4784525cb7a97cc785207600a143154b6dca9", url="https://pypi.org/packages/65/cc/2891260847777eb9aaca278aaf3f846c9ff8ea1351643a4f33ff26d5d213/huggingface_hub-0.19.1-py3-none-any.whl")
    version("0.19.0", sha256="8cd7ffdb36393ba1c99b4576fbe8900b3496c98a643cde05f355348fe7d89144", url="https://pypi.org/packages/64/8c/2766ce7e136eeb8b4d502e68eb1fe65342ee1aaf9129ec1c0838e5a4f0cb/huggingface_hub-0.19.0-py3-none-any.whl")
    version("0.18.0", sha256="ee0b6b68acbf6aeb6d083ea081e981c277a1104b82ab67fdf6780ff5396830af", url="https://pypi.org/packages/ef/b5/b6107bd65fa4c96fdf00e4733e2fe5729bb9e5e09997f63074bb43d3ab28/huggingface_hub-0.18.0-py3-none-any.whl")
    version("0.17.3", sha256="545eb3665f6ac587add946e73984148f2ea5c7877eac2e845549730570c1933a", url="https://pypi.org/packages/aa/f3/3fc97336a0e90516901befd4f500f08d691034d387406fdbde85bea827cc/huggingface_hub-0.17.3-py3-none-any.whl")
    version("0.17.2", sha256="fc4a36640b2b51dced0da37a18420572145a0dd528f46715afe6c1f955cc8533", url="https://pypi.org/packages/72/21/51cddb8850ed3f4dbc21e57c3dabc49e64d5577857ddda7b2eb0ffc2ec0e/huggingface_hub-0.17.2-py3-none-any.whl")
    version("0.17.1", sha256="7a9dc262a2e0ecf8c1749c8b9a7510a7a22981849f561af4345942d421822451", url="https://pypi.org/packages/50/9d/5eac2733606df7d164b951b14cd76b056e530af96c881aaec89383bdbe45/huggingface_hub-0.17.1-py3-none-any.whl")
    version("0.17.0", sha256="8111ef89ebf5514154b4e929662f57fc43818d06c95dabdfa4c77f9087383172", url="https://pypi.org/packages/2a/b3/63f423056b99df8d23c269b2df9374ea12a526e981709be84c7491c9f1cc/huggingface_hub-0.17.0-py3-none-any.whl")
    version("0.17.0-rc0", sha256="0adb081f6b8a6644ad2b22a93f24b6f277fd9a7c6eaf021b119b863e7560ea51", url="https://pypi.org/packages/17/23/20559458a3cd569593d722fa6fa631cd626bdbca5d2d933731a6ca3e1038/huggingface_hub-0.17.0rc0-py3-none-any.whl")
    version("0.16.4", sha256="0d3df29932f334fead024afc7cb4cc5149d955238b8b5e42dcf9740d6995a349", url="https://pypi.org/packages/7f/c4/adcbe9a696c135578cabcbdd7331332daad4d49b7c43688bc2d36b3a47d2/huggingface_hub-0.16.4-py3-none-any.whl")
    version("0.14.1", sha256="9fc619170d800ff3793ad37c9757c255c8783051e1b5b00501205eb43ccc4f27", url="https://pypi.org/packages/58/34/c57b951aecd0248845932c1cfc15721237c50e463f26b0536673bcb76f4f/huggingface_hub-0.14.1-py3-none-any.whl")
    version("0.10.1", sha256="dc3b0e9a663fe6cad6a8522055c02a9d8673dbd527223288e2442bc028c253db", url="https://pypi.org/packages/b2/2b/715a1924d470691a27b2dcdf472a9ef87f04718a897de25e68bf86ac0184/huggingface_hub-0.10.1-py3-none-any.whl")
    version("0.0.19", sha256="edcea87cbd709073a63fc911efa2d8fd8304f62cfe43f0bf497dec8eaac10369", url="https://pypi.org/packages/96/9a/0686eeeea343df547cbacde15c1bd958eb7a3f5c58291b44a0e2aef1c30c/huggingface_hub-0.0.19-py3-none-any.whl")
    version("0.0.18", sha256="297ac9cb300f2622fac8fc75195cbd8947cd288da1e94e0c2f734f3c3e37d4f0", url="https://pypi.org/packages/a8/6c/6ff1108f4a3ef20c34748bd2e76d22f9d078336de960b10ae3ac508fac28/huggingface_hub-0.0.18-py3-none-any.whl")
    version("0.0.17", sha256="ff7f64cf2ed08b201e2e0e21d437c0e180192b8d42e2ed2cf2d81e361389e688", url="https://pypi.org/packages/ab/45/2d908576740ee8876438cfa2a57aefefeb9f677a3df826d6b4d3c7e6b3cc/huggingface_hub-0.0.17-py3-none-any.whl")
    version("0.0.16", sha256="c8170998f1ac43ec9253f5fd321213aeee54a9b938c9ce5e696a06274710b67c", url="https://pypi.org/packages/ca/f9/f326fa63cff226cb3610c1b680eb98d77129d7271a7f8c9741a2042b8f43/huggingface_hub-0.0.16-py3-none-any.whl")
    version("0.0.15", sha256="c6afe573b43edc91856538bbfdb8003096302bdb0944553b664941c4f5305c74", url="https://pypi.org/packages/07/77/9ee7012e683db48e2ee9be9156f9a1033d9035977499046d755e218360e0/huggingface_hub-0.0.15-py3-none-any.whl")
    version("0.0.14", sha256="3f931112abb679001d8d1310bfd2676cec9ce3417b2d9965d5a2d44dcca2e5e2", url="https://pypi.org/packages/67/d5/07894f2f047055576c3559a66d921c37d1280fda74b08fe574a8490e5999/huggingface_hub-0.0.14-py3-none-any.whl")
    version("0.0.13", sha256="c23f3231dbebae9624d653bbf040d9079cc9f593761eb2526c7507b086418091", url="https://pypi.org/packages/35/03/071adc023c0a7e540cf4652fa9cad13ab32e6ae469bf0cc0262045244812/huggingface_hub-0.0.13-py3-none-any.whl")
    version("0.0.12", sha256="5c82ff96897a72e1ed48a94c1796686f120dea05888200522f3994f130c12e6a", url="https://pypi.org/packages/2f/ee/97e253668fda9b17e968b3f97b2f8e53aa0127e8807d24a547687423fe0b/huggingface_hub-0.0.12-py3-none-any.whl")
    version("0.0.11", sha256="1e62128a5e82134f2446b56e48f8068ea5eca425cfadd9c1df5d8e77bdc4f025", url="https://pypi.org/packages/45/94/27f4f66d8d763f60204f447287cbe78d8bdf9c86d87dbc1fe26e792e727a/huggingface_hub-0.0.11-py3-none-any.whl")
    version("0.0.10", sha256="447cb5ac83da68dba8b5c42069165da81c4d9450b3d6a78ce027a9e5cce9461f", url="https://pypi.org/packages/3c/e3/fb7b6aefaf0fc7b792cebbbd590b1895c022ab0ff27f389e1019c6f2e68a/huggingface_hub-0.0.10-py3-none-any.whl")
    version("0.0.8", sha256="feec10c3cff31bab75fa90ed801a1979301d4ebcbdf681312cb0371f77f53dff", url="https://pypi.org/packages/a1/88/7b1e45720ecf59c6c6737ff332f41c955963090a18e72acbcbeac6b25e86/huggingface_hub-0.0.8-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    variant("cli", default=False)
    # END VARIANTS

    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-filelock")
        depends_on("py-fsspec@2023.5:", when="@0.18:")
        depends_on("py-fsspec", when="@0.14:0.17")
        depends_on("py-inquirerpy@0.3.4:", when="@0.10:+cli")
        depends_on("py-packaging@20.9:", when="@0.0.11:")
        depends_on("py-pyyaml@5.1:", when="@0.7:")
        depends_on("py-pyyaml", when="@0.0.19:0.6")
        depends_on("py-requests")
        depends_on("py-ruamel-yaml@0.17.16", when="@0.0.18")
        depends_on("py-tqdm@4.42.1:", when="@0.12:")
        depends_on("py-tqdm", when="@:0.11")
        depends_on("py-typing-extensions@3.7.4.3:", when="@0.1.1:")
        depends_on("py-typing-extensions", when="@0.0.9:0.1.0")
    # END DEPENDENCIES

