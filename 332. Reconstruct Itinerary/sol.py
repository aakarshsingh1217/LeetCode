from collections import defaultdict

def findItinerary(tickets: list[list[str]]) -> list[str]:
    targets = defaultdict(list)

    for a, b in sorted(tickets)[::-1]:
        targets[a].append(b)

    route = []

    def visit(airport: str):
        while targets[airport]:
            visit(targets[airport].pop())

        route.append(airport)

    visit("JFK")

    return route[::-1]