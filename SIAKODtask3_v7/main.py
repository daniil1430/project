from heap import MinHeap


def merge_files(sizes):
    if len(sizes) <= 1:
        return [], 0

    items = [(size, i) for i, size in enumerate(sizes)]
    heap = MinHeap(items)

    plan = []
    total_cost = 0
    next_id = len(sizes)

    while heap.size() > 1:
        size1, id1 = heap.pop()
        size2, id2 = heap.pop()

        merged_size = size1 + size2
        total_cost += merged_size

        plan.append((id1, id2, merged_size))

        heap.push(merged_size, next_id)
        next_id += 1

    return plan, total_cost


if __name__ == "__main__":
    sizes = [4, 3, 2, 6]
    plan, cost = merge_files(sizes)

    print(f"Размеры файлов: {sizes}")
    print(f"План объединения:")
    for step, (f1, f2, result) in enumerate(plan, 1):
        new_id = len(sizes) + step - 1
        print(f"  Шаг {step}: объединить файлы {f1} и {f2} -> файл {new_id} (размер {result})")
    print(f"Общая стоимость: {cost}")