class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        bucket = {}

        for string in strs:
            bucketee = [0] * 26

            for s in string:
                bucketee[ord(s) - ord('a')] += 1

            key = tuple(bucketee)

            if key not in bucket:
                bucket[key] = []

            bucket[key].append(string)

        output = []

        for strings in bucket.values():
            output.append(strings)

        return output