import multiprocessing as mp
import numpy as np
import time

# ukuran matrix
SIZE = 600

# generate matrix random
A = np.random.randint(1, 10, (SIZE, SIZE))
B = np.random.randint(1, 10, (SIZE, SIZE))

# fungsi untuk menghitung 1 baris hasil matrix
def multiply_row(i):
    return np.dot(A[i], B)

def parallel_matrix_multiply():
    pool = mp.Pool(mp.cpu_count())
    result = pool.map(multiply_row, range(SIZE))
    pool.close()
    pool.join()
    return np.array(result)

def serial_matrix_multiply():
    return np.dot(A, B)

if __name__ == "__main__":
    # SERIAL
    start = time.time()
    serial_result = serial_matrix_multiply()
    end = time.time()
    print("Serial Time:", end - start)

    # PARALLEL
    start = time.time()
    parallel_result = parallel_matrix_multiply()
    end = time.time()
    print("Parallel Time:", end - start)