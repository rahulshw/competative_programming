"""
https://leetcode.com/explore/challenge/card/july-leetcoding-challenge/546/week-3-july-15th-july-21st/3394/

There are a total of n courses you have to take, labeled from 0 to n-1.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, return the ordering of courses you should take to finish all courses.

There may be multiple correct orders, you just need to return one of them. If it is impossible to finish all courses, return an empty array.

Example 1:

Input: 2, [[1,0]]
Output: [0,1]
Explanation: There are a total of 2 courses to take. To take course 1 you should have finished
             course 0. So the correct course order is [0,1] .

Example 2:

Input: 4, [[1,0],[2,0],[3,1],[3,2]]
Output: [0,1,2,3] or [0,2,1,3]
Explanation: There are a total of 4 courses to take. To take course 3 you should have finished both
             courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0.
             So one correct course order is [0,1,2,3]. Another correct ordering is [0,2,1,3] .

Note:

    The input prerequisites is a graph represented by a list of edges, not adjacency matrices. Read more about how a graph is represented.
    You may assume that there are no duplicate edges in the input prerequisites.

"""
from typing import List


class Solution:

    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        courses_prerequisites = []
        for i in range(numCourses):
            courses_prerequisites.append([])

        for i in prerequisites:
            courses_prerequisites[i[0]].append(i[1])

        # courses_prerequisites = [[],[0],[0],[1,2]]

        course_visited = [False] * numCourses
        ordered_courses = []
        courses_in_queue = [False] * numCourses
        for i in range(numCourses):
            if not course_visited[i]:
                no_loop = self.solve_dependency(i, courses_prerequisites, course_visited, ordered_courses,
                                                courses_in_queue)
                if not no_loop:
                    print("loop")
                    return []
                ordered_courses.append(i)

        return ordered_courses

    def solve_dependency(self, course, courses_prerequisites, course_visited, ordered_courses, courses_in_queue):
        print(course,courses_in_queue)
        if courses_in_queue[course]:
            return []
        courses_in_queue[course] = True
        for i in courses_prerequisites[course]:
            if not course_visited[i]:
                no_loop = self.solve_dependency(i, courses_prerequisites, course_visited, ordered_courses,
                                                courses_in_queue)
                if not no_loop:
                    return []
                ordered_courses.append(i)
        courses_in_queue[course] = False
        course_visited[course] = True
        return True


if __name__ == "__main__":
    s = Solution()
    print(s.findOrder(4, [[1,0],[2,0],[3,1],[3,2]]))
    print(s.findOrder(2, [[0,1],[1,0]]))
    print(s.findOrder(2, [[0,1]]))

