---
title: Numpy - Task 6
author: Muhammad Samir Assawalhy
date: March 07, 2023
---

# Notes of Task 6

## Jupyter Notebook

Jupyter Notebook is a web application that allows you to write code and notes (e.g. in markdown) in the browser which is more user friendly and easy to share and understand. It is widely by the datascientists and python developers. But it can also be used with different programming languages such as Java.

- [Official site](https://jupyter.org/)

**Instructions to run**

~~~bash {.number-lines}
# install
pip install jupyterlab
# start server
jupyter-lab
~~~

**Miscellaneous**

- [jupyterlite](https://github.com/jupyterlite/jupyterlite) is a web assembly based library to allow web users run python in a jupyter like UI.

## Numpy

The core of NumPy is well-optimized C code. Enjoy the flexibility of Python with the speed of compiled code.

- [Official site](https://numpy.org/)
- [Summary / Cheatsheet](https://drive.google.com/file/d/1NH7ttjnZTbdQEerff4rZW4XjY9uh2TNT/view)

**Fun Facts**

- Numpy was one of the technologies that were used to take the first image of a blackhole by Event Horizon Telescope.
- It was also used to detect gravitational waves by LIGO.
- Many libraries depends on Numpy such as [Dask](https://dask.org/) ans [CuPy](https://cupy.chainer.org/) to help in GPU accelerated and distributed computing.

**Boring Facts**

- All items in a numpy array:
  - must have the same datatype
  - are stored in a contiguous place in the memory
- We can apply n-D slicing, `arr[1:, :5:-1]`
- Integers in Python have dynamic sizes depending of the value, use `sys.getsizeof(x)`
- Integers in NumPy are 32-bit integers by default
- To do mathematical computations (`+`, `/`, ...) on NumPy arrays, they may have different shapes, `arr.shape`, in such a case NumPy will try to do something called broadcasting.
    > Input arrays do not need to have the same number of dimensions. The resulting array will have the same number of dimensions as the input array with the greatest number of dimensions

More boring facts:

```python {.numberLines}
>>> arr.reshape(-1)
# will flaten the arr to be 1D

>>> arr.reshape(x, y)
# x * y must equal the size

>>> arr.array([1, 2, 3], dtype="f")
# "f" will make the array of type float32

>>> arr.array([1, 2, 3], dtype="float")
# "float" will make the array of type float64
```
