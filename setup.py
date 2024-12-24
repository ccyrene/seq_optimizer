from setuptools import setup
from setuptools_rust import Binding, RustExtension

setup(
    name="seq_optimizer",
    rust_extensions=[
        RustExtension(
            "seq_optimizer._seq_optimizer",
            binding=Binding.PyO3,
            debug=False,
        )
    ],
    packages=["seq_optimizer"],
    zip_safe=False,
)