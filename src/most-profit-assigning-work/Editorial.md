## Solution

------------------------------------------------------------------------

### <a href="#overview"
class="!text-sd-muted-foreground absolute right-full top-1/2 -translate-y-1/2 cursor-pointer pr-0.5 text-xs opacity-0 group-hover/heading:opacity-100"
aria-hidden="true" tabindex="-1"></a>


Overview

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

------------------------------------------------------------------------

### <a href="#approach-1-binary-search-and-greedy-sort-by-job-difficulty"
class="!text-sd-muted-foreground absolute right-full top-1/2 -translate-y-1/2 cursor-pointer pr-0.5 text-xs opacity-0 group-hover/heading:opacity-100"
aria-hidden="true" tabindex="-1"></a>


Approach 1: Binary Search and Greedy (Sort by Job Difficulty)

#### Intuition

When assigning a job to any worker, we disregard any jobs that are too
difficult and then select the job with the highest profit. An example is
shown below:

![figA](../Figures/826/Slide1.PNG)

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

1.  Initialize an array of pairs `jobProfile` with `{0, 0}`.
2.  For `i` from `0` to `n` (where `n` is the size of the `difficulty`
    and `profit` arrays):
    -   Append `{difficulty[i], profit[i]}` to `jobProfile`.
3.  Sort `jobProfile` by `difficulty` in ascending order.
4.  For `i` from `0` to `n-1`:
    -   Update `jobProfile[i].profit` to be the maximum of its current
        value and the previous profit value.
5.  Initialize `netProfit` to `0`.
6.  For each `ability` in the `worker` array:
    -   Set binary search parameters: `l = 0`, `r = n-1`,
        `jobProfit = 0`.
    -   While `l` &lt;= `r`:
        -   Calculate `mid = (l + r) / 2`.
        -   If `jobProfile[mid].difficulty` &lt;= `ability`:
            -   Update `jobProfit` to the maximum of `jobProfit` and
                `jobProfile[mid].profit`.
            -   Set `l = mid + 1`.
        -   Else:
            -   Set `r = mid - 1`.
    -   Add `jobProfit` to `netProfit`.
7.  Return `netProfit`.  

#### Implementation

#### Complexity Analysis

Let
<span class="math math-inline"><span class="katex"><span class="katex-mathml">nn</span><span class="katex-html"
aria-hidden="true"><span class="base"><span class="strut"
style="height: 0.4306em;"></span><span class="mord mathnormal">n</span></span></span></span></span>
be the size of the `difficulty` and `profit` arrays, and `m` be the size
of the `worker` array.

-   Time complexity:
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

-   Space complexity:
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

    -   In Python, the `sort` method sorts a list using the Tim Sort
        algorithm which is a combination of Merge Sort and Insertion
        Sort and has
        <span class="math math-inline"><span class="katex"><span class="katex-mathml">O(n)O(n)</span><span class="katex-html"
        aria-hidden="true"><span class="base"><span class="strut"
        style="height: 1em; vertical-align: -0.25em;"></span><span class="mord mathnormal"
        style="margin-right: 0.02778em;">O</span><span class="mopen">(</span><span class="mord mathnormal">n</span><span class="mclose">)</span></span></span></span></span>
        additional space. Additionally, Tim Sort is designed to be a
        stable algorithm.
    -   In Java, `Arrays.sort()` is implemented using a variant of the
        Quick Sort algorithm which has a space complexity of
        <span class="math math-inline"><span class="katex"><span class="katex-mathml">O(log⁡n)O(
        \log n)</span><span class="katex-html"
        aria-hidden="true"><span class="base"><span class="strut"
        style="height: 1em; vertical-align: -0.25em;"></span><span class="mord mathnormal"
        style="margin-right: 0.02778em;">O</span><span class="mopen">(</span><span class="mop">lo<span style="margin-right: 0.01389em;">g</span></span><span class="mspace"
        style="margin-right: 0.1667em;"></span><span class="mord mathnormal">n</span><span class="mclose">)</span></span></span></span></span>
        for sorting an array.
    -   In C++, the `sort()` function is implemented as a hybrid of
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

------------------------------------------------------------------------

### <a href="#approach-2-binary-search-and-greedy-sort-by-profit"
class="!text-sd-muted-foreground absolute right-full top-1/2 -translate-y-1/2 cursor-pointer pr-0.5 text-xs opacity-0 group-hover/heading:opacity-100"
aria-hidden="true" tabindex="-1"></a>


Approach 2: Binary Search and Greedy (Sort by profit)

#### Intuition

Is it possible to use binary search on the `profit` array to maximize
the profit for a worker?

Suppose we sort the `profit` array in decreasing order while rearranging
the `difficulty` array to preserve the original ordering of indices. For
each worker, we will find the first index where the value of difficulty
is less than or equal to the worker's ability. This index will store the
maximum profit possible for that worker's ability. To efficiently apply
binary search, we can preprocess the array to store the minimum
difficulty up to the current index.

Similar to the previous approach, we will return the sum of all
individual job profits as the maximum total profit.

#### Algorithm

1.  Initialize an array of pairs `jobProfile` with `{0, 0}`.
2.  For `i` from `0` to `n` (where `n` is the size of the `difficulty`
    and `profit` arrays):
    -   Append `{difficulty[i], profit[i]}` to `jobProfile`.
3.  Sort `jobProfile` by `profit` in descending order.
4.  For `i` from `0` to `n-1`:
    -   Update `jobProfile[i].difficulty` to be the minimum of its
        current value and the previous difficulty value.
5.  Initialize `netProfit` to `0`.
6.  For each `ability` in the `worker` array:
    -   Set binary search parameters: `l = 0`, `r = n-1`,
        `jobProfit = 0`.
    -   While `l` &lt;= `r`:
        -   Calculate `mid = (l + r) / 2`.
        -   If `jobProfile[mid].difficulty` &lt;= `ability`:
            -   Update `jobProfit` to the maximum of `jobProfit` and
                `jobProfile[mid].profit`.
            -   Set `r = mid - 1`.
        -   Else:
            -   Set `l = mid + 1`.
    -   Add `jobProfit` to `netProfit`.
7.  Return `netProfit`.  

#### Implementation

#### Complexity Analysis

Let
<span class="math math-inline"><span class="katex"><span class="katex-mathml">nn</span><span class="katex-html"
aria-hidden="true"><span class="base"><span class="strut"
style="height: 0.4306em;"></span><span class="mord mathnormal">n</span></span></span></span></span>
be the size of the `difficulty` and `profit` arrays and `m` be the size
of the `worker` array.

-   Time complexity:
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

    The time complexity for sorting the difficulty array is
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
    search with search space size `n`. The time complexity for is given
    by
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

-   Space complexity:
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

    -   In Python, the `sort` method sorts a list using the Tim Sort
        algorithm which is a combination of Merge Sort and Insertion
        Sort and has
        <span class="math math-inline"><span class="katex"><span class="katex-mathml">O(n)O(n)</span><span class="katex-html"
        aria-hidden="true"><span class="base"><span class="strut"
        style="height: 1em; vertical-align: -0.25em;"></span><span class="mord mathnormal"
        style="margin-right: 0.02778em;">O</span><span class="mopen">(</span><span class="mord mathnormal">n</span><span class="mclose">)</span></span></span></span></span>
        additional space. Additionally, Tim Sort is designed to be a
        stable algorithm.
    -   In Java, `Arrays.sort()` is implemented using a variant of the
        Quick Sort algorithm which has a space complexity of
        <span class="math math-inline"><span class="katex"><span class="katex-mathml">O(log⁡n)O(
        \log n)</span><span class="katex-html"
        aria-hidden="true"><span class="base"><span class="strut"
        style="height: 1em; vertical-align: -0.25em;"></span><span class="mord mathnormal"
        style="margin-right: 0.02778em;">O</span><span class="mopen">(</span><span class="mop">lo<span style="margin-right: 0.01389em;">g</span></span><span class="mspace"
        style="margin-right: 0.1667em;"></span><span class="mord mathnormal">n</span><span class="mclose">)</span></span></span></span></span>
        for sorting an array.
    -   In C++, the `sort()` function is implemented as a hybrid of
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

------------------------------------------------------------------------

### <a href="#approach-3-greedy-and-two-pointers"
class="!text-sd-muted-foreground absolute right-full top-1/2 -translate-y-1/2 cursor-pointer pr-0.5 text-xs opacity-0 group-hover/heading:opacity-100"
aria-hidden="true" tabindex="-1"></a>


Approach 3: Greedy and Two-Pointers

#### Intuition

In the first approach, we sorted the `jobProfile` array by difficulty
values. Now, let's also sort the `worker` array in increasing order.

Once we've assigned the optimal job to a worker, then all the workers
ahead of that worker (in ability) will receive a job with difficulty
greater than or equal to the assigned job. Therefore, after assigning a
job, we don't need the jobs present before it.

So, we can use two pointers to find the most optimal job while iterating
through the sorted job profile and sorted worker arrays.

Start with the first worker and iterate through the list maintaining a
maxima of profits until you find the last assignable job with maximum
difficulty. The maximum profit up to this index will give us the profit
of the first worker.

Since the worker array is sorted, the ability of the next worker will be
greater than all previous workers. So, continue iterating the job
profile until you find the last assignable job. Repeat the process for
all workers and store the total profit as the sum of the maximum profit.

#### Algorithm

1.  Initialize an array of pairs `jobProfile`.
2.  For `i` from `0` to `n` (where `n` is the size of the `difficulty`
    and `profit` arrays):
    -   Append `{difficulty[i], profit[i]}` to `jobProfile`.
3.  Sort `jobProfile` by `difficulty` in ascending order.
4.  Sort `worker` in ascending order by their abilities.
5.  Initialize `netProfit`, `maxProfit`, and `index` to `0`.
6.  For each `ability` in the `worker` array:
    -   While `index` is within bounds and the worker's ability is
        greater than or equal to `jobProfile[index].difficulty`:
        -   Update `maxProfit` to the maximum of `maxProfit` and
            `jobProfile[index].profit`.
        -   Increment `index` by `1`.
    -   Add `maxProfit` to `netProfit`.
7.  Return `netProfit`.

<img
src="blob:https://leetcode.com/9f79a76b-b538-4645-81f8-8c5dc80968ac"
class="object-fit-contain !mb-0 max-h-full max-w-full" alt="Current" />



1 / 14

#### Implementation

#### Complexity Analysis

Let
<span class="math math-inline"><span class="katex"><span class="katex-mathml">nn</span><span class="katex-html"
aria-hidden="true"><span class="base"><span class="strut"
style="height: 0.4306em;"></span><span class="mord mathnormal">n</span></span></span></span></span>
be the size of the `difficulty` and `profit` arrays and `m` be the size
of the `worker` array.

-   Time complexity:
    <span class="math math-inline"><span class="katex"><span class="katex-mathml">O(n⋅log⁡n+m⋅log⁡(m))O(n
    \cdot \log n + m \cdot \log(m))</span><span class="katex-html"
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
    style="height: 1em; vertical-align: -0.25em;"></span><span class="mop">lo<span style="margin-right: 0.01389em;">g</span></span><span class="mopen">(</span><span class="mord mathnormal">m</span><span class="mclose">))</span></span></span></span></span>

    The time taken for sorting the `difficulty` array is
    <span class="math math-inline"><span class="katex"><span class="katex-mathml">O(n⋅log⁡n)O(n
    \cdot \log n)</span><span class="katex-html"
    aria-hidden="true"><span class="base"><span class="strut"
    style="height: 1em; vertical-align: -0.25em;"></span><span class="mord mathnormal"
    style="margin-right: 0.02778em;">O</span><span class="mopen">(</span><span class="mord mathnormal">n</span><span class="mspace"
    style="margin-right: 0.2222em;"></span><span class="mbin">⋅</span><span class="mspace"
    style="margin-right: 0.2222em;"></span></span><span class="base"><span class="strut"
    style="height: 1em; vertical-align: -0.25em;"></span><span class="mop">lo<span style="margin-right: 0.01389em;">g</span></span><span class="mspace"
    style="margin-right: 0.1667em;"></span><span class="mord mathnormal">n</span><span class="mclose">)</span></span></span></span></span>
    and sorting the `worker` array is
    <span class="math math-inline"><span class="katex"><span class="katex-mathml">O(m⋅log⁡(m))O(m
    \cdot \log(m))</span><span class="katex-html"
    aria-hidden="true"><span class="base"><span class="strut"
    style="height: 1em; vertical-align: -0.25em;"></span><span class="mord mathnormal"
    style="margin-right: 0.02778em;">O</span><span class="mopen">(</span><span class="mord mathnormal">m</span><span class="mspace"
    style="margin-right: 0.2222em;"></span><span class="mbin">⋅</span><span class="mspace"
    style="margin-right: 0.2222em;"></span></span><span class="base"><span class="strut"
    style="height: 1em; vertical-align: -0.25em;"></span><span class="mop">lo<span style="margin-right: 0.01389em;">g</span></span><span class="mopen">(</span><span class="mord mathnormal">m</span><span class="mclose">))</span></span></span></span></span>.

    In the two pointers, while iterating through the `worker` array we
    iterate the `jobProfile` array exactly once. Time complexity is
    given by
    <span class="math math-inline"><span class="katex"><span class="katex-mathml">O(n+m)O(n +
    m)</span><span class="katex-html"
    aria-hidden="true"><span class="base"><span class="strut"
    style="height: 1em; vertical-align: -0.25em;"></span><span class="mord mathnormal"
    style="margin-right: 0.02778em;">O</span><span class="mopen">(</span><span class="mord mathnormal">n</span><span class="mspace"
    style="margin-right: 0.2222em;"></span><span class="mbin">+</span><span class="mspace"
    style="margin-right: 0.2222em;"></span></span><span class="base"><span class="strut"
    style="height: 1em; vertical-align: -0.25em;"></span><span class="mord mathnormal">m</span><span class="mclose">)</span></span></span></span></span>

    Therefore, the total time complexity is given by
    <span class="math math-inline"><span class="katex"><span class="katex-mathml">O(n⋅log⁡n+m⋅log⁡(m))O(n
    \cdot \log n + m \cdot \log(m))</span><span class="katex-html"
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
    style="height: 1em; vertical-align: -0.25em;"></span><span class="mop">lo<span style="margin-right: 0.01389em;">g</span></span><span class="mopen">(</span><span class="mord mathnormal">m</span><span class="mclose">))</span></span></span></span></span>.

-   Space complexity:
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

    -   In Python, the `sort` method sorts a list using the Tim Sort
        algorithm which is a combination of Merge Sort and Insertion
        Sort and has
        <span class="math math-inline"><span class="katex"><span class="katex-mathml">O(n)O(n)</span><span class="katex-html"
        aria-hidden="true"><span class="base"><span class="strut"
        style="height: 1em; vertical-align: -0.25em;"></span><span class="mord mathnormal"
        style="margin-right: 0.02778em;">O</span><span class="mopen">(</span><span class="mord mathnormal">n</span><span class="mclose">)</span></span></span></span></span>
        additional space. Additionally, Tim Sort is designed to be a
        stable algorithm.
    -   In Java, `Arrays.sort()` is implemented using a variant of the
        Quick Sort algorithm which has a space complexity of
        <span class="math math-inline"><span class="katex"><span class="katex-mathml">O(log⁡n)O(
        \log n)</span><span class="katex-html"
        aria-hidden="true"><span class="base"><span class="strut"
        style="height: 1em; vertical-align: -0.25em;"></span><span class="mord mathnormal"
        style="margin-right: 0.02778em;">O</span><span class="mopen">(</span><span class="mop">lo<span style="margin-right: 0.01389em;">g</span></span><span class="mspace"
        style="margin-right: 0.1667em;"></span><span class="mord mathnormal">n</span><span class="mclose">)</span></span></span></span></span>
        for sorting an array.
    -   In C++, the `sort()` function is implemented as a hybrid of
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

------------------------------------------------------------------------

### <a href="#approach-4-memoization"
class="!text-sd-muted-foreground absolute right-full top-1/2 -translate-y-1/2 cursor-pointer pr-0.5 text-xs opacity-0 group-hover/heading:opacity-100"
aria-hidden="true" tabindex="-1"></a>


Approach 4: Memoization

#### Intuition

Given the constraints on the maximum values of the `difficulty` and
`ability` arrays, we can create an array of this size to store the
maximum profit for every possible ability.

We don't need the profit of jobs with a difficulty level higher than
what the worker can handle. Therefore, we can create an array sized to
the maximum ability to store the results.

Store the profit in this array with the difficulty of each job as the
index. If multiple jobs share the same difficulty (same index), store
the maximum profit among them.

Now, what if there exists a job with difficulty lower than another job
but provides a higher profit? To find the maximum profit at each index,
we must determine the highest value occurrence in all indices up to the
current index. To do this, we need to store the maxima of all previous
profit values in this array while iterating through the abilities.

Therefore, the maximum total profit is given by the sum of values in
this array with worker abilities as the indices.

#### Algorithm

1.  Initialize `maxAbility` as the maximum ability in the `worker`
    array.
2.  Initialize an array `jobs` of size `maxAbility`.
3.  Iterate a variable `i` from 0 to `difficulty.size - 1`:
    -   If the `difficulty` at the current index `i` is less than or
        equal to the worker's ability:
        -   Store the `profit` at index `i` at the `difficulty[i]` index
            of `jobs` array. If a value already exists, take the maximum
            of both values.
4.  Iterate through all values in `jobs`:
    -   Store the maximum of current and previous `jobs` values in the
        current `jobs` index.
5.  Iterate through all abilities in the `worker` array:
    -   Store `maxProfit` as `jobs[ability]` where `ability` denotes the
        ability of the current worker.
    -   Increment `maxProfit` to `netProfit`.
6.  Return `netProfit`.

<img
src="blob:https://leetcode.com/9ab99931-e29a-4d63-92e6-720a06d57a4f"
class="object-fit-contain !mb-0 max-h-full max-w-full" alt="Current" />



1 / 10

#### Implementation

#### Complexity Analysis

Let
<span class="math math-inline"><span class="katex"><span class="katex-mathml">nn</span><span class="katex-html"
aria-hidden="true"><span class="base"><span class="strut"
style="height: 0.4306em;"></span><span class="mord mathnormal">n</span></span></span></span></span>
be the size of the `difficulty` and `profit` arrays and `m` be the size
of the `worker` array. Also, let `maxAbility` be the maximum value in
the `worker` array.

-   Time complexity:
    <span class="math math-inline"><span class="katex"><span class="katex-mathml">O(n+m+maxAbility)O(n +
    m + maxAbility)</span><span class="katex-html"
    aria-hidden="true"><span class="base"><span class="strut"
    style="height: 1em; vertical-align: -0.25em;"></span><span class="mord mathnormal"
    style="margin-right: 0.02778em;">O</span><span class="mopen">(</span><span class="mord mathnormal">n</span><span class="mspace"
    style="margin-right: 0.2222em;"></span><span class="mbin">+</span><span class="mspace"
    style="margin-right: 0.2222em;"></span></span><span class="base"><span class="strut"
    style="height: 0.6667em; vertical-align: -0.0833em;"></span><span class="mord mathnormal">m</span><span class="mspace"
    style="margin-right: 0.2222em;"></span><span class="mbin">+</span><span class="mspace"
    style="margin-right: 0.2222em;"></span></span><span class="base"><span class="strut"
    style="height: 1em; vertical-align: -0.25em;"></span><span class="mord mathnormal">ma</span><span class="mord mathnormal">x</span><span class="mord mathnormal">A</span><span class="mord mathnormal">bi</span><span class="mord mathnormal"
    style="margin-right: 0.01968em;">l</span><span class="mord mathnormal">i</span><span class="mord mathnormal">t</span><span class="mord mathnormal"
    style="margin-right: 0.03588em;">y</span><span class="mclose">)</span></span></span></span></span>

    In this approach, we iterate through the `difficulty`, `worker` and
    `jobs` arrays exactly once.

    Therefore, the total time complexity is given by
    <span class="math math-inline"><span class="katex"><span class="katex-mathml">O(n+m+maxAbility)O(n +
    m + maxAbility)</span><span class="katex-html"
    aria-hidden="true"><span class="base"><span class="strut"
    style="height: 1em; vertical-align: -0.25em;"></span><span class="mord mathnormal"
    style="margin-right: 0.02778em;">O</span><span class="mopen">(</span><span class="mord mathnormal">n</span><span class="mspace"
    style="margin-right: 0.2222em;"></span><span class="mbin">+</span><span class="mspace"
    style="margin-right: 0.2222em;"></span></span><span class="base"><span class="strut"
    style="height: 0.6667em; vertical-align: -0.0833em;"></span><span class="mord mathnormal">m</span><span class="mspace"
    style="margin-right: 0.2222em;"></span><span class="mbin">+</span><span class="mspace"
    style="margin-right: 0.2222em;"></span></span><span class="base"><span class="strut"
    style="height: 1em; vertical-align: -0.25em;"></span><span class="mord mathnormal">ma</span><span class="mord mathnormal">x</span><span class="mord mathnormal">A</span><span class="mord mathnormal">bi</span><span class="mord mathnormal"
    style="margin-right: 0.01968em;">l</span><span class="mord mathnormal">i</span><span class="mord mathnormal">t</span><span class="mord mathnormal"
    style="margin-right: 0.03588em;">y</span><span class="mclose">)</span></span></span></span></span>.

-   Space complexity:
    <span class="math math-inline"><span class="katex"><span class="katex-mathml">O(maxAbility)O(maxAbility)</span><span class="katex-html"
    aria-hidden="true"><span class="base"><span class="strut"
    style="height: 1em; vertical-align: -0.25em;"></span><span class="mord mathnormal"
    style="margin-right: 0.02778em;">O</span><span class="mopen">(</span><span class="mord mathnormal">ma</span><span class="mord mathnormal">x</span><span class="mord mathnormal">A</span><span class="mord mathnormal">bi</span><span class="mord mathnormal"
    style="margin-right: 0.01968em;">l</span><span class="mord mathnormal">i</span><span class="mord mathnormal">t</span><span class="mord mathnormal"
    style="margin-right: 0.03588em;">y</span><span class="mclose">)</span></span></span></span></span>

    We create an additional `jobs` array of size
    <span class="math math-inline"><span class="katex"><span class="katex-mathml">maxAbilitymaxAbility</span><span class="katex-html"
    aria-hidden="true"><span class="base"><span class="strut"
    style="height: 0.8889em; vertical-align: -0.1944em;"></span><span class="mord mathnormal">ma</span><span class="mord mathnormal">x</span><span class="mord mathnormal">A</span><span class="mord mathnormal">bi</span><span class="mord mathnormal"
    style="margin-right: 0.01968em;">l</span><span class="mord mathnormal">i</span><span class="mord mathnormal">t</span><span class="mord mathnormal"
    style="margin-right: 0.03588em;">y</span></span></span></span></span>.
    Apart from this, no additional space is used.

    Therefore, space complexity is given by
    <span class="math math-inline"><span class="katex"><span class="katex-mathml">O(maxAbility)O(maxAbility)</span><span class="katex-html"
    aria-hidden="true"><span class="base"><span class="strut"
    style="height: 1em; vertical-align: -0.25em;"></span><span class="mord mathnormal"
    style="margin-right: 0.02778em;">O</span><span class="mopen">(</span><span class="mord mathnormal">ma</span><span class="mord mathnormal">x</span><span class="mord mathnormal">A</span><span class="mord mathnormal">bi</span><span class="mord mathnormal"
    style="margin-right: 0.01968em;">l</span><span class="mord mathnormal">i</span><span class="mord mathnormal">t</span><span class="mord mathnormal"
    style="margin-right: 0.03588em;">y</span><span class="mclose">)</span></span></span></span></span>.

------------------------------------------------------------------------
