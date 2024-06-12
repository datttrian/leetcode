class Solution:
    def kthSmallestPrimeFraction(self, arr: list[int], k: int) -> list[int]:
        n = len(arr)
        low, high = 0.0, 1.0

        while low < high:
            mid = (low + high) / 2
            count = 0
            max_fraction = (0, 1)
            i = 0

            for j in range(1, n):
                while i < j and arr[i] / arr[j] <= mid:
                    i += 1
                count += i

                if i > 0:
                    i -= 1

                    if arr[i] / arr[j] <= mid and (
                        arr[i] * max_fraction[1] > arr[j] * max_fraction[0]
                    ):
                        max_fraction = (arr[i], arr[j])

            if count == k:
                return list(max_fraction)

            if count < k:
                low = mid + 1e-9
            else:
                high = mid

        return []
