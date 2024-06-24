def oxford_comma(items):
    if len(items) == 1:
        return items[0]
    elif len(items) == 2:
        return ' and '.join(items)
    else:
        items_without_end = items[0:len(items) - 1]
        joined_items_without_end = ', '.join(items_without_end)
        joined_plus_end = [joined_items_without_end, items[len(items) - 1]]
        return ', and '.join(joined_plus_end)