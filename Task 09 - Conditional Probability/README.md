# Definition

In probability theory, conditional probability is a measure of the probability of an event occurring, given that another event (by assumption, presumption, assertion or evidence) has already occurred. *[Wikipedia]*

- **Notation:** $P(\mathrm{event} \mid \mathrm{condition})$.
- It is read like this: probability of *(event)* given *(condition)*.
- We can also negate the condition or the even: $P(\mathrm{event} \mid \neg \mathrm{condition})$.
- Another possible (but less used) way is to write it like: $P_{\mathrm{condition}}(\mathrm{event})$, or for short $P_B(A)$.

## Kolmogorov definition

![Illustration of conditional probabilities with an Euler diagram.](https://upload.wikimedia.org/wikipedia/commons/thumb/9/9b/Conditional_probability.svg/640px-Conditional_probability.svg.png){ width=300px }

$$
P(A \mid B)=\frac{P(A \cap B)}{P(B)}
$$

When the unconditional probability of $B$ is greater then zero, $P(B) > 0$, we define $P(A\mid B)$ as the probability of $A$ if $B$ has or (is assumed to have) happened.

For example, in the above image we have a diagram represents our events. When the event $B_1$ happen we reduce our focus only on the area that $B_1$ occupied in the diagram. Now it is easier to get the probability of any other event happening after $B_1$ has happened. It is obvious that $A$ will certainly happen when $B_1$ happens.

Similarly, when $B_2$ we can calculate the probability of $A$ as follows:

$$
P(A \mid B_2) = \frac{0.12} { 0.12 + 0.04 } = 0.75
$$

# Total probability

$$
\begin{aligned}
P(P)= & P(P \mid C) \cdot P(C) \\
& +P(P \mid \neg C) \cdot P(\neg C)
\end{aligned}
$$

# Examples

## Randomly choose a coin

Imagine a bag that contains $n$ coins with a specific probability of heads. For example, the probability of heads of the 1st coin is $P(H \mid 1)$.

The case when we randomly choose a coin from this bag then toss it will make two dependent events. The probability of coin being head depends on the result from the previous event (random choice from the bag).

The formula of the total probability of heads is:

$$
P(H) = \frac1n\sum_{i = 1}^n P(H\mid i)
$$

Note that $\frac1n$ is the probability of choosing one coin.


