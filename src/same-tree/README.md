### 100. Same Tree

Given the roots of two binary trees `p` and `q`, write a function to
check if they are the same or not.

Two binary trees are considered the same if they are structurally
identical, and the nodes have the same value.

**Example 1:**

<img src="https://assets.leetcode.com/uploads/2020/12/20/ex1.jpg"
style="width: 622px; height: 182px;" />

    Input: p = [1,2,3], q = [1,2,3]
    Output: true

**Example 2:**

<img src="https://assets.leetcode.com/uploads/2020/12/20/ex2.jpg"
style="width: 382px; height: 182px;" />

    Input: p = [1,2], q = [1,null,2]
    Output: false

**Example 3:**

<img src="https://assets.leetcode.com/uploads/2020/12/20/ex3.jpg"
style="width: 622px; height: 182px;" />

    Input: p = [1,2,1], q = [1,1,2]
    Output: false

**Constraints:**

- The number of nodes in both trees is in the range `[0, 100]`.
- `-10`<sup>`4`</sup>`<= Node.val <= 10`<sup>`4`</sup>
