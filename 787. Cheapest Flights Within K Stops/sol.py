def findCheapestPrice(n: int, flights: list[list[int]], src: int, dst: int, k: int):
    if src == dst:
        return 0
    
    previous = [float("inf")] * n
    current = [float("inf")] * n
    previous[src] = 0

    for i in range(1, k + 2):
        current[src] = 0

        for flight in flights:
            previous_flight, current_flight, cost = flight

            if previous[previous_flight] < float("inf"):
                current[current_flight] = min(
                    current[current_flight], 
                    previous[previous_flight] + cost
                )

        previous = current.copy()

    return -1 if current[dst] == float("inf") else current[dst]