from main import main
# Benchmark the RSA encryption and decryption process using pytest-benchmark
def test_rsa_benchmark(benchmark):
    result = benchmark(main)
    assert result == None