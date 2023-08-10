class Solution:     
	def findMedianSortedArrays(self, a, b):

		l = len(a) + len(b)

		if l == 0:
			return None
		if l % 2:
			return self.get_median(a, b, l // 2)
		else:
			return (self.get_median(a, b, l // 2) + self.get_median(a, b, l // 2 - 1))  / 2

		

	def get_median(self, a, b, idx):

		if not a:
			return b[idx]
		if not b:
			return a[idx]

		ai = len(a) // 2
		bi = len(b) // 2
		ma = a[ai]
		mb = b[bi]

		if ma > mb:
			ma, mb = mb, ma
			ai, bi = bi, ai
			a, b = b, a

		max_idx_ma = len(a) // 2 + len(b) // 2

		if max_idx_ma < idx:
			med = self.get_median(a[ai+1:], b, idx - (len(a)//2+1))
		else:
			# max_idx_ma < min_idx_mb (because they are different numbers) 
			# => idx <= max_idx_ma <  min_idx_mb => idx < min_idx_mb
			med = self.get_median(a, b[:bi], idx)

		return med
