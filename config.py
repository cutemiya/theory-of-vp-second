alphabet = ['1', '2', '3']

states = ['S', 'A', 'B', 'C', 'Z']
transitions = [
    # 1 2 3
    [3, 2, 1],    # S
    [-1, 4, 1],   # A
    [4, 2, -1],   # B
    [3, -1, 4],  # C
    [1, 3, 2],    # Z
]  # p.s. -1 = no transition
