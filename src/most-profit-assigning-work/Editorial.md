## Solution

### Overview

We are given some jobs that each have a difficulty level and an amount
of profit that can be made from performing the job. We also have some
workers.

You can think of these jobs as roles within a company. Each worker can
have only one role, and the role must not be too difficult for them.
However, just like in the real world, the assigned role can be easier
than what the worker is capable of handling. Our goal is to assign roles
to workers in a way that maximizes the company's profit.

Constraints on `n` and `m` are `1 <= n` & `m <= 10000`, respectively.
Therefore, we need to consider an approach with linear or log-linear
time complexity.

### Approach 1: Binary Search and Greedy (Sort by Job Difficulty)

#### Intuition

When assigning a job to any worker, we disregard any jobs that are too
difficult and then select the job with the highest profit. An example is
shown below:

![figA](https://assets.leetcode.com/static_assets/media/original_images/826/Slide1.PNG)

If we need to choose the most optimal job for the worker
algorithmically, we could use a linear search to find the maximum profit
among all jobs. However, this approach would result in a Time Limit
Exceeded (TLE) verdict since each job assignment would take
<span class="math math-inline"><span class="katex"><span class="katex-mathml">O(n)O(n)</span><span class="katex-html"
aria-hidden="true"><span class="base"><span class="strut"
style="height: 1em; vertical-align: -0.25em;"></span><span class="mord mathnormal"
style="margin-right: 0.02778em;">O</span><span class="mopen">(</span><span class="mord mathnormal">n</span><span class="mclose">)</span></span></span></span></span>
time, where `n` is the size of the job list.

Another approach is to use a binary search for every worker. We can sort
the `difficulty` array in increasing order to apply binary search and
rearrange the `profits` array in the same order.

For each worker, we will find the index where the difficulty value is
just less than or equal to the worker's ability. The worker can perform
all jobs up to this index. Consequently, the worker will choose the job
with the highest profit up to this index. To do this, we can preprocess
the array to store the maximum profit values up to each index.

During the binary search process, we will add the value of the
preprocessed maximum profit of the calculated job for each worker. This
sum will give us the total profit. Since the profit for each worker is
maximized, the total profit will also be maximized.

#### Algorithm

1. Initialize an array of pairs `jobProfile` with `{0, 0}`.
2. For `i` from `0` to `n` (where `n` is the size of the `difficulty`
    and `profit` arrays):
    - Append `{difficulty[i], profit[i]}` to `jobProfile`.
3. Sort `jobProfile` by `difficulty` in ascending order.
4. For `i` from `0` to `n-1`:
    - Update `jobProfile[i].profit` to be the maximum of its current
        value and the previous profit value.
5. Initialize `netProfit` to `0`.
6. For each `ability` in the `worker` array:
    - Set binary search parameters: `l = 0`, `r = n-1`,
        `jobProfit = 0`.
    - While `l` &lt;= `r`:
        - Calculate `mid = (l + r) / 2`.
        - If `jobProfile[mid].difficulty` &lt;= `ability`:
            - Update `jobProfit` to the maximum of `jobProfit` and
                `jobProfile[mid].profit`.
            - Set `l = mid + 1`.
        - Else:
            - Set `r = mid - 1`.
    - Add `jobProfit` to `netProfit`.
7. Return `netProfit`.  

#### Implementation

#### Complexity Analysis

Let
<span class="math math-inline"><span class="katex"><span class="katex-mathml">nn</span><span class="katex-html"
aria-hidden="true"><span class="base"><span class="strut"
style="height: 0.4306em;"></span><span class="mord mathnormal">n</span></span></span></span></span>
be the size of the `difficulty` and `profit` arrays, and `m` be the size
of the `worker` array.

- Time complexity:
    <span class="math math-inline"><span class="katex"><span class="katex-mathml">O(n⋅log⁡n+m⋅log⁡n)O(n
    \cdot \log n + m \cdot \log n)</span><span class="katex-html"
    aria-hidden="true"><span class="base"><span class="strut"
    style="height: 1em; vertical-align: -0.25em;"></span><span class="mord mathnormal"
    style="margin-right: 0.02778em;">O</span><span class="mopen">(</span><span class="mord mathnormal">n</span><span class="mspace"
    style="margin-right: 0.2222em;"></span><span class="mbin">⋅</span><span class="mspace"
    style="margin-right: 0.2222em;"></span></span><span class="base"><span class="strut"
    style="height: 0.8889em; vertical-align: -0.1944em;"></span><span class="mop">lo<span style="margin-right: 0.01389em;">g</span></span><span class="mspace"
    style="margin-right: 0.1667em;"></span><span class="mord mathnormal">n</span><span class="mspace"
    style="margin-right: 0.2222em;"></span><span class="mbin">+</span><span class="mspace"
    style="margin-right: 0.2222em;"></span></span><span class="base"><span class="strut"
    style="height: 0.4445em;"></span><span class="mord mathnormal">m</span><span class="mspace"
    style="margin-right: 0.2222em;"></span><span class="mbin">⋅</span><span class="mspace"
    style="margin-right: 0.2222em;"></span></span><span class="base"><span class="strut"
    style="height: 1em; vertical-align: -0.25em;"></span><span class="mop">lo<span style="margin-right: 0.01389em;">g</span></span><span class="mspace"
    style="margin-right: 0.1667em;"></span><span class="mord mathnormal">n</span><span class="mclose">)</span></span></span></span></span>

    The time complexity for sorting the `jobProfile` array is
    <span class="math math-inline"><span class="katex"><span class="katex-mathml">O(n⋅log⁡n)O(n
    \cdot \log n)</span><span class="katex-html"
    aria-hidden="true"><span class="base"><span class="strut"
    style="height: 1em; vertical-align: -0.25em;"></span><span class="mord mathnormal"
    style="margin-right: 0.02778em;">O</span><span class="mopen">(</span><span class="mord mathnormal">n</span><span class="mspace"
    style="margin-right: 0.2222em;"></span><span class="mbin">⋅</span><span class="mspace"
    style="margin-right: 0.2222em;"></span></span><span class="base"><span class="strut"
    style="height: 1em; vertical-align: -0.25em;"></span><span class="mop">lo<span style="margin-right: 0.01389em;">g</span></span><span class="mspace"
    style="margin-right: 0.1667em;"></span><span class="mord mathnormal">n</span><span class="mclose">)</span></span></span></span></span>.

    While iterating the `worker` array of size `m`, we perform a binary
    search with search space size `n`. The time complexity is given by
    <span class="math math-inline"><span class="katex"><span class="katex-mathml">O(m⋅log⁡n)O(m
    \cdot \log n)</span><span class="katex-html"
    aria-hidden="true"><span class="base"><span class="strut"
    style="height: 1em; vertical-align: -0.25em;"></span><span class="mord mathnormal"
    style="margin-right: 0.02778em;">O</span><span class="mopen">(</span><span class="mord mathnormal">m</span><span class="mspace"
    style="margin-right: 0.2222em;"></span><span class="mbin">⋅</span><span class="mspace"
    style="margin-right: 0.2222em;"></span></span><span class="base"><span class="strut"
    style="height: 1em; vertical-align: -0.25em;"></span><span class="mop">lo<span style="margin-right: 0.01389em;">g</span></span><span class="mspace"
    style="margin-right: 0.1667em;"></span><span class="mord mathnormal">n</span><span class="mclose">)</span></span></span></span></span>.

    Therefore, the total time complexity is given by
    <span class="math math-inline"><span class="katex"><span class="katex-mathml">O(n⋅log⁡n+m⋅log⁡n)O(n
    \cdot \log n + m \cdot \log n)</span><span class="katex-html"
    aria-hidden="true"><span class="base"><span class="strut"
    style="height: 1em; vertical-align: -0.25em;"></span><span class="mord mathnormal"
    style="margin-right: 0.02778em;">O</span><span class="mopen">(</span><span class="mord mathnormal">n</span><span class="mspace"
    style="margin-right: 0.2222em;"></span><span class="mbin">⋅</span><span class="mspace"
    style="margin-right: 0.2222em;"></span></span><span class="base"><span class="strut"
    style="height: 0.8889em; vertical-align: -0.1944em;"></span><span class="mop">lo<span style="margin-right: 0.01389em;">g</span></span><span class="mspace"
    style="margin-right: 0.1667em;"></span><span class="mord mathnormal">n</span><span class="mspace"
    style="margin-right: 0.2222em;"></span><span class="mbin">+</span><span class="mspace"
    style="margin-right: 0.2222em;"></span></span><span class="base"><span class="strut"
    style="height: 0.4445em;"></span><span class="mord mathnormal">m</span><span class="mspace"
    style="margin-right: 0.2222em;"></span><span class="mbin">⋅</span><span class="mspace"
    style="margin-right: 0.2222em;"></span></span><span class="base"><span class="strut"
    style="height: 1em; vertical-align: -0.25em;"></span><span class="mop">lo<span style="margin-right: 0.01389em;">g</span></span><span class="mspace"
    style="margin-right: 0.1667em;"></span><span class="mord mathnormal">n</span><span class="mclose">)</span></span></span></span></span>.

- Space complexity:
    <span class="math math-inline"><span class="katex"><span class="katex-mathml">O(n)O(n)</span><span class="katex-html"
    aria-hidden="true"><span class="base"><span class="strut"
    style="height: 1em; vertical-align: -0.25em;"></span><span class="mord mathnormal"
    style="margin-right: 0.02778em;">O</span><span class="mopen">(</span><span class="mord mathnormal">n</span><span class="mclose">)</span></span></span></span></span>

    We create an additional `jobProfile` array of size
    <span class="math math-inline"><span class="katex"><span class="katex-mathml">2⋅n2
    \cdot n</span><span class="katex-html"
    aria-hidden="true"><span class="base"><span class="strut"
    style="height: 0.6444em;"></span><span class="mord">2</span><span class="mspace"
    style="margin-right: 0.2222em;"></span><span class="mbin">⋅</span><span class="mspace"
    style="margin-right: 0.2222em;"></span></span><span class="base"><span class="strut"
    style="height: 0.4306em;"></span><span class="mord mathnormal">n</span></span></span></span></span>.
    Apart from this, some extra space is used when we sort an array in
    place. The space complexity of the sorting algorithm depends on the
    programming language.

  - In Python, the `sort` method sorts a list using the Tim Sort
        algorithm which is a combination of Merge Sort and Insertion
        Sort and has
        <span class="math math-inline"><span class="katex"><span class="katex-mathml">O(n)O(n)</span><span class="katex-html"
        aria-hidden="true"><span class="base"><span class="strut"
        style="height: 1em; vertical-align: -0.25em;"></span><span class="mord mathnormal"
        style="margin-right: 0.02778em;">O</span><span class="mopen">(</span><span class="mord mathnormal">n</span><span class="mclose">)</span></span></span></span></span>
        additional space. Additionally, Tim Sort is designed to be a
        stable algorithm.
  - In Java, `Arrays.sort()` is implemented using a variant of the
        Quick Sort algorithm which has a space complexity of
        <span class="math math-inline"><span class="katex"><span class="katex-mathml">O(log⁡n)O(
        \log n)</span><span class="katex-html"
        aria-hidden="true"><span class="base"><span class="strut"
        style="height: 1em; vertical-align: -0.25em;"></span><span class="mord mathnormal"
        style="margin-right: 0.02778em;">O</span><span class="mopen">(</span><span class="mop">lo<span style="margin-right: 0.01389em;">g</span></span><span class="mspace"
        style="margin-right: 0.1667em;"></span><span class="mord mathnormal">n</span><span class="mclose">)</span></span></span></span></span>
        for sorting an array.
  - In C++, the `sort()` function is implemented as a hybrid of
        Quick Sort, Heap Sort, and Insertion Sort, with a worse-case
        space complexity of
        <span class="math math-inline"><span class="katex"><span class="katex-mathml">O(log⁡n)O(
        \log n)</span><span class="katex-html"
        aria-hidden="true"><span class="base"><span class="strut"
        style="height: 1em; vertical-align: -0.25em;"></span><span class="mord mathnormal"
        style="margin-right: 0.02778em;">O</span><span class="mopen">(</span><span class="mop">lo<span style="margin-right: 0.01389em;">g</span></span><span class="mspace"
        style="margin-right: 0.1667em;"></span><span class="mord mathnormal">n</span><span class="mclose">)</span></span></span></span></span>.

    Therefore, space complexity is given by
    <span class="math math-inline"><span class="katex"><span class="katex-mathml">O(n)O(n)</span><span class="katex-html"
    aria-hidden="true"><span class="base"><span class="strut"
    style="height: 1em; vertical-align: -0.25em;"></span><span class="mord mathnormal"
    style="margin-right: 0.02778em;">O</span><span class="mopen">(</span><span class="mord mathnormal">n</span><span class="mclose">)</span></span></span></span></span>.
