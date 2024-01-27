import heapq


def heap_sort(iterable):
    h = []
    for value in iterable:
        heapq.heappush(h, value)

    return [heapq.heappop(h) for _ in range(len(h))]


def minimal_cost(iterable):
    total_cost = sum(iterable[:2])

    for cabel in iterable[2:]:
        total_cost += total_cost + cabel

    return total_cost


# Example
arr = [2, 1, 9, 5]
sorted_arr = heap_sort(arr)
print("Відсортований масив:", sorted_arr)
print("Мінімальна вартість:", minimal_cost(sorted_arr))
