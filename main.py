from typing import List


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        map: dict[str, List[str]] = {}
        route: List[str] = []
        # 建立地圖
        for s, d in tickets:
            if s in map:
                map[s].append(d)
            else:
                map[s] = [d]
        # 機場字母排序
        for i in map:
            map[i].sort()

        def visit(airport: str):
            # 若無下一個飛行目的地
            if airport not in map:
                route.append(airport)
                return
            # 取得該地點所有目的地
            destinations = map[airport]
            # 檢查該地點所有目的地
            while destinations:
                # 由字母小的為優先目的地
                dest = destinations.pop(0)
                visit(dest)
            # 到達此地
            route.append(airport)
        visit("JFK")

        route.reverse()
        return route


sol = Solution()
tickets = [
    ["JFK", "SFO"],
    ["JFK", "ATL"],
    ["SFO", "ATL"],
    ["ATL", "JFK"],
    ["ATL", "SFO"],
    ["JFK", "ABC"],
    ["ABC", "SFO"]
]
ans = sol.findItinerary(tickets)
print(ans)

tickets = [
    ["JFK", "MUC"],
    ["MUC", "LHR"],
    ["LHR", "SFO"],
    ["SFO", "SJC"]
]
ans = sol.findItinerary(tickets)
print(ans)
