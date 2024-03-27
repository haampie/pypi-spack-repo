##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PySklearn(PythonPackage):
    version("0.0.post12", sha256="54cff9e20839b7b202321178228af4d9388bedf78425d9299fd9ee170d68802e", url="https://pypi.org/packages/46/1c/395a83ee7b2d2ad7a05b453872053d41449564477c81dc356f720b16eac4/sklearn-0.0.post12.tar.gz")
    version("0.0.post11", sha256="af035c4f0b970b7fc2d3856079aa1aa1032df3d7f65048a9d87114abf13c4629", url="https://pypi.org/packages/a4/0b/d1c703256cf293be77b7db44dbef62251fe02a97d0bef981f7120b0b0c0f/sklearn-0.0.post11.tar.gz")
    version("0.0.post10", sha256="d4cd5a2e64b3caaf82cd5e33c46884dfeec5ebf991710d9faeb4fe81cadb3ba6", url="https://pypi.org/packages/b9/0e/b2a4cfaa9e12b9ca4c71507bc26d2c99d75de172c0088c9835a98cf146ff/sklearn-0.0.post10.tar.gz")
    version("0.0.post9", sha256="1ff5864cf30489ee48a014fe8f4320d7bb59592392a4ef52ae9d7a37942615ac", url="https://pypi.org/packages/28/86/207a003339023247fef1bb5bc9f5093140d17294b2f6d15bfcd4885e469e/sklearn-0.0.post9.tar.gz")
    version("0.0.post7", sha256="1c89020b364fdc3aa2839e0ae34e8f0b406669e4b5c2359dda3ac398f9c76874", url="https://pypi.org/packages/70/ce/81aa643f3c43488c4a1e417e45f696a61e7ac82b57190fad3c310df2c07b/sklearn-0.0.post7.tar.gz")
    version("0.0.post5", sha256="7377c714a03a79bbe9196f435db931fd2a6fa8c68514da7ed3a251fd08c52e2c", url="https://pypi.org/packages/7a/93/e0e1b1e98f39dfca7ec9795cb46f6e09e88a2fd5d4a28e4b3d1f618a2aec/sklearn-0.0.post5.tar.gz")
    version("0.0.post4", sha256="0e81ec9c32d4bb418e7be8f1ec1027d174975502dc84cbc4f4564b4cba31e674", url="https://pypi.org/packages/99/b2/165110013aa66fae6fc13918ad0e9de4801e5f1691d371bf8b63328037e6/sklearn-0.0.post4.tar.gz")
    version("0.0.post2", sha256="9e834e4dbda273814efb21a105d66179326362c5b7a0516e257d868995b023a0", url="https://pypi.org/packages/c7/42/6496b55f00df3202030e56f43737bc8b3b8dbc79dc6db7e5944e1583a31e/sklearn-0.0.post2.tar.gz")
    version("0.0.post1", sha256="76b9ed1623775168657b86b5fe966d45752e5c87f528de6240c38923b94147c5", url="https://pypi.org/packages/db/1e/af4e9cded5093a92e60d4ae7149a02c7427661b2db66c8ea4d34b17864a2/sklearn-0.0.post1.tar.gz")
    version("0.0", sha256="e23001573aa194b834122d2b9562459bf5ae494a2d59ca6b8aa22c85a44c0e31", url="https://pypi.org/packages/1e/7a/dbb3be0ce9bd5c8b7e3d87328e79063f8b263b2b1bfa4774cb1147bfcd3f/sklearn-0.0.tar.gz")


