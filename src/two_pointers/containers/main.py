#Given an array heights where each element represents the height of a vertical line, pick two lines to act as the walls of a container. Return the maximum area (amount of water) the container can hold.
#What is area? Width × height, where width is the distance between walls, and height is the shorter wall (water overflows at the shorter wall).


class Solution:
    def max_area(self, heights: List[int]) -> int:
        left, right = 0, len(heights)-1
        min_height = min(heights[left], heights[right])
        current_area = min_height * (right - left)
        print(current_area)
        while True:
            if heights[left] > heights[right]:
                right = right - 1
            else:
                left = left + 1
            if left == right:
                break
            min_height = min(heights[left], heights[right])
            tmp_area = min_height * (right - left)
            if tmp_area > current_area:
                current_area = tmp_area
        return current_area

if __name__ == "__main__":
    heights = [1,8,6,2,5,4,8,3,7]
    sol = Solution()
    print(sol.max_area(heights))  # Output: 49