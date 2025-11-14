def func(h):
    if not h or not h.next:
        return True

    s = f = h
    l = []

    while f and f.next:
        l.append(s.value)
        s = s.next
        f = f.next.next

    if f:
        s = s.next

    while s:
        if l.pop() != s.value:
            return False
        s = s.next

    return True
