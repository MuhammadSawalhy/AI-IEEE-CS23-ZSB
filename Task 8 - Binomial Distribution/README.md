# Binomial distribution

Binomial coeficients is a very useful way to count. It is an essential part of combinatorics (the math of counting). It is basically a way to answer the following question: How many way I can choose k item from n set of items?

$$
^nC_r =  {n \choose k} = \frac{n!} {k! (n - k)!} = \frac{^nP_r} {k!}
$$

- Permutations cares about the order of element, if we swaps two elements we get another different permutation.
- Combinations doesn't care out order, so we need to know how many ways to get a subset of size $k$ of a set of items of size $n$.
- We can think about combinations as permutations but also dividing it by $k!$ which is the number of ways to order these $k$ items.
- So at the end we get the above formula simply proven.

**Binomial distribution:**

Binomial distribution can be use with any events with two outputs, i.e heads or tails, buy or not but, fraud or not fraud.

Let think about the coin flip example. This is an event with two outputs, head or tail. If we need to calculate the probability to get $k$ heads after fliping a coin $n$ times with probability of head equal $p$.

This is the formula to calculate this probability:

$$
\frac{n !}{(n-k) ! k !} \cdot p^k(1-p)^{(n-k)}
$$

- Notice that the sequence of heads and tails doesn't matter
- What matter is how many heads we got $k$
- Hence the probability of any sequence of $n$ flips which contains $k$ heads is $p^k(1-p)^{(n-k)}$.
- To count how many events with $k$ flips we simply use combinations (binomial coeficients).
