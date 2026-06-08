import time
import numpy as np

if __name__ == "__main__":
    a = np.array([1, 2, 3, 4, 5])
    b = np.array([6, 7, 8, 9, 10])

    print(a + b)
    print(a * 2)

    c = np.random.randn(1_000_000)

    result = []
    t1_start = time.perf_counter()
    print(f'Start t1 --> {t1_start}')
    for x in c:
        result.append(max(0,x))
    t1_end = time.perf_counter()
    print(f'End t1 --> {t1_end}')
    loop_time = t1_end - t1_start
    print(result[:5])

    t2_start = time.perf_counter()
    print(f'Start t2 --> {t2_start}')

    res = np.maximum(0,c)
    t2_end = time.perf_counter()
    numpy_time = t2_end - t2_start
    print(f'End t2 --> {t2_end}')


    # Loop time : ~0.32s
    # Numpy time : ~0.0019s
    print(f'{loop_time / numpy_time} numpy is faster')
    print(res[:5])
