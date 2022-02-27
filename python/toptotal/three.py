def solution(factories):
    current = total = sum(factories)
    filters = 0

    while current > total / 2:
        factories = sorted(factories)
        to_filter = factories.pop()
        reduction = to_filter / 2
        factories.append(reduction)
        current -= reduction
        filters += 1
    
    return filters