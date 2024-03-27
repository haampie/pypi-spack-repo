##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyHttpcore(PythonPackage):
    version("1.0.4", sha256="ac418c1db41bade2ad53ae2f3834a3a0f5ae76b56cf5aa497d2d033384fc7d73", url="https://pypi.org/packages/2c/93/13f25f2f78646bab97aee7680821e30bd85b2ff0fc45d5fdf5393b79716d/httpcore-1.0.4-py3-none-any.whl")
    version("1.0.3", sha256="9a6a501c3099307d9fd76ac244e08503427679b1e81ceb1d922485e2f2462ad2", url="https://pypi.org/packages/11/a6/24139fa27831cf2127fcf578d6d0a852a611f10cefecd800b1c557333d7a/httpcore-1.0.3-py3-none-any.whl")
    version("1.0.2", sha256="096cc05bca73b8e459a1fc3dcf585148f63e534eae4339559c9b8a8d6399acc7", url="https://pypi.org/packages/56/ba/78b0a99c4da0ff8b0f59defa2f13ca4668189b134bd9840b6202a93d9a0f/httpcore-1.0.2-py3-none-any.whl")
    version("1.0.1", sha256="c5e97ef177dca2023d0b9aad98e49507ef5423e9f1d94ffe2cfe250aa28e63b0", url="https://pypi.org/packages/7c/bd/8f4e676af570d8990e02e3f4cefba7c0c506f2b2ce63f086e0cb939b6e1e/httpcore-1.0.1-py3-none-any.whl")
    version("1.0.0", sha256="cdbe42a0ea87dcaf9b5c751e868aff233799e947aff8b9c9eff8a2c11219ddb7", url="https://pypi.org/packages/ba/3c/a8d2514181ae7cd966f042a24aff0a2a637152fec6cb7193ff245f45f131/httpcore-1.0.0-py3-none-any.whl")
    version("0.18.0", sha256="adc5398ee0a476567bf87467063ee63584a8bce86078bf748e48754f60202ced", url="https://pypi.org/packages/ac/97/724afbb7925339f6214bf1fdb5714d1a462690466832bf8fb3fd497649f1/httpcore-0.18.0-py3-none-any.whl")
    version("0.17.3", sha256="c2789b767ddddfa2a5782e3199b2b7f6894540b17b16ec26b2c4d8e103510b87", url="https://pypi.org/packages/94/2c/2bde7ff8dd2064395555220cbf7cba79991172bf5315a07eb3ac7688d9f1/httpcore-0.17.3-py3-none-any.whl")
    version("0.17.2", sha256="5581b9c12379c4288fe70f43c710d16060c10080617001e6b22a3b6dbcbefd36", url="https://pypi.org/packages/4d/32/b908f673ccef12b6425b848a541264ee3d95f5f571f18f6ab0d8c311442e/httpcore-0.17.2-py3-none-any.whl")
    version("0.17.1", sha256="628e768aaeec1f7effdc6408ba1c3cdbd7487c1fc570f7d66844ec4f003e1ca4", url="https://pypi.org/packages/32/ce/4184bcd15c5eb9aa7d2cbd61c9123b92ce31561bd9a832c96f83dfa5da7f/httpcore-0.17.1-py3-none-any.whl")
    version("0.17.0", sha256="0fdfea45e94f0c9fd96eab9286077f9ff788dd186635ae61b312693e4d943599", url="https://pypi.org/packages/6c/39/05ebe30333ec66bba849d3c25c85d759b94c43bb03b2222de051c50d4390/httpcore-0.17.0-py3-none-any.whl")
    version("0.16.3", sha256="da1fb708784a938aa084bde4feb8317056c55037247c787bd7e19eb2c2949dc0", url="https://pypi.org/packages/04/7e/ef97af4623024e8159993b3114ce208de4f677098ae058ec5882a1bf7605/httpcore-0.16.3-py3-none-any.whl")
    version("0.16.2", sha256="52c79095197178856724541e845f2db86d5f1527640d9254b5b8f6f6cebfdee6", url="https://pypi.org/packages/91/52/93f22e5441539256c0d113faf17e45284aee16eebdd95089e3ca6f480b18/httpcore-0.16.2-py3-none-any.whl")
    version("0.16.1", sha256="8d393db683cc8e35cc6ecb02577c5e1abfedde52b38316d038932a84b4875ecb", url="https://pypi.org/packages/b1/fa/6e6ebe637cef87401ee82e7d76313d9eb014524fc6de45eb3b13cedd4c14/httpcore-0.16.1-py3-none-any.whl")
    version("0.16.0", sha256="5b9a9211757b01bea0bdfe39581e2af893c3932b5c6d66f94dff618ca43ffe43", url="https://pypi.org/packages/6f/d1/7d1cddbc4bc1e4e9f9233b79a5acf1a5e5665801157ca68a5fb4150584a1/httpcore-0.16.0-py3-none-any.whl")
    version("0.15.0", sha256="1105b8b73c025f23ff7c36468e4432226cbb959176eab66864b8e31c4ee27fa6", url="https://pypi.org/packages/ad/b9/260603ca0913072a10a4367c2dca9998706812a8c1f4558eca510f85ae16/httpcore-0.15.0-py3-none-any.whl")
    version("0.14.7", sha256="47d772f754359e56dd9d892d9593b6f9870a37aeb8ba51e9a88b09b3d68cfade", url="https://pypi.org/packages/e7/38/7b76d3d71c462dc936e333b358a3106e7af913e6c8c9dd5a45684fec08cc/httpcore-0.14.7-py3-none-any.whl")
    version("0.14.6", sha256="508401ab24060cfa1e959feda1c38eaa09ccf9074c928f9c3d2864f8921373ce", url="https://pypi.org/packages/f3/75/85083285551d68ac3f5a7ac378b406ac8569615924d9b801e49e1d2b423b/httpcore-0.14.6-py3-none-any.whl")
    version("0.14.5", sha256="2621ee769d0236574df51b305c5f4c69ca8f0c7b215221ad247b1ee42a9a9de1", url="https://pypi.org/packages/84/df/fc07a289a28238c7356c6589eada4524db34ad0dd584dda89dd816a02ac1/httpcore-0.14.5-py3-none-any.whl")
    version("0.13.7", sha256="369aa481b014cf046f7067fddd67d00560f2f00426e79569d99cb11245134af0", url="https://pypi.org/packages/73/a1/e347135b0ebb4d4c29a4258cb6d2e03c2d0c4ea207bf9ce5d255d7887a56/httpcore-0.13.7-py3-none-any.whl")
    version("0.13.6", sha256="db4c0dcb8323494d01b8c6d812d80091a31e520033e7b0120883d6f52da649ff", url="https://pypi.org/packages/b4/94/8c136dbfac58456395dab9eb71e156cd14e0449f013f6c9c007e3ef4a160/httpcore-0.13.6-py3-none-any.whl")
    version("0.13.5", sha256="52c545bc3233cb5e3ceaee96bc3d1dcda50e0ebf04da99323f6544c174b0c5a5", url="https://pypi.org/packages/f1/9a/cba5553b9c5b6745c65bc1ff30406df37b06d8170172b803641233e13a98/httpcore-0.13.5-py3-none-any.whl")
    version("0.13.4", sha256="38e09649bb3906c913a2917c4eb3e3b3e11c83d4edebad8b53b7d757abc49267", url="https://pypi.org/packages/e0/4c/90b46b4e3121a48cc0dcebb665d745937c75b0d691f54d351a3b3646e620/httpcore-0.13.4-py3-none-any.whl")
    version("0.13.3", sha256="ff614f0ef875b9e5fe0bdd459b31ea0eea282ff12dc82add83d68b3811ee94ad", url="https://pypi.org/packages/7a/89/29a26a8086268a8043b1fd0228a463bab99990d77fdfaa8a2bd07117851a/httpcore-0.13.3-py3-none-any.whl")
    version("0.11.1", sha256="72cfaa461dbdc262943ff4c9abf5b195391a03cdcc152e636adb4239b15e77e1", url="https://pypi.org/packages/d8/e7/f25e08617b4be99d38e4ef6c4d1b744bf065b9c93156ecd691d95897e0e4/httpcore-0.11.1-py3-none-any.whl")
    version("0.11.0", sha256="7a6804b18e1b8fc61ec4df868cb5c679d225fffbb81e48455ee9b57792cc3ac6", url="https://pypi.org/packages/64/fe/a9db014f98e0bb0c40d62dfee8b265f4e3a959da5daa672f68191776e523/httpcore-0.11.0-py3-none-any.whl")

    with default_args(type="run"):
        depends_on("py-anyio@3.0.0:", when="@0.16:0")
        depends_on("py-anyio@3", when="@0.13.4:0.15")
        depends_on("py-certifi", when="@0.14.1:")
        depends_on("py-h11@0.13:", when="@0.16:")
        depends_on("py-h11@0.11:0.12", when="@0.13.3:0.15")
        depends_on("py-h11@0.8:0.9", when="@0.5:0.11")
        depends_on("py-h2@3", when="@0.5:0.9")
        depends_on("py-sniffio@1:", when="@0.5:0")

