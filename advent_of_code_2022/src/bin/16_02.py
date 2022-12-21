from collections import defaultdict
from itertools import product

INPUT = """Valve AA has flow rate=0; tunnels lead to valves DD, II, BB
Valve BB has flow rate=13; tunnels lead to valves CC, AA
Valve CC has flow rate=2; tunnels lead to valves DD, BB
Valve DD has flow rate=20; tunnels lead to valves CC, AA, EE
Valve EE has flow rate=3; tunnels lead to valves FF, DD
Valve FF has flow rate=0; tunnels lead to valves EE, GG
Valve GG has flow rate=0; tunnels lead to valves FF, HH
Valve HH has flow rate=22; tunnel leads to valve GG
Valve II has flow rate=0; tunnels lead to valves AA, JJ
Valve JJ has flow rate=21; tunnel leads to valve II"""

T_END = 26


def options(graph, cur_state):
    t, cum_flow, cur_flow, pos, opened = cur_state

    if pos[0] > pos[1]:
        pos = pos[1], pos[0]

    if t == T_END:
        return []

    options = []

    for (a, b) in product(graph[pos[0]][1] + ['open'], graph[pos[1]][1] + ['open']):
        new_cum_flow = cum_flow + cur_flow
        new_cur_flow = cur_flow
        new_opened = opened

        if a == 'open':
            a = pos[0]
            if a in new_opened or graph[a][0] == 0:
                continue

            new_opened = new_opened + [a]
            new_cur_flow += graph[a][0]

        if b == 'open':
            b = pos[1]
            if b in new_opened or graph[b][0] == 0:
                continue

            new_opened = new_opened + [b]
            new_cur_flow += graph[b][0]

        options.append((t + 1, new_cum_flow, new_cur_flow, (a, b), new_opened))

    return options

def is_worse(seen, cur_state):
    t, cum_flow, cur_flow, pos, opened = cur_state

    # First time this pos, definitely not worse
    if not seen[pos]:
        return False

    # Worse if t is larger but cum flow and cur_flow is lower
    return any(t >= s[0] and cum_flow <= s[1] and cur_flow <= s[2] for s in seen[pos])


def iterate(graph, seen, cur_state):
    for o in options(graph, cur_state):
        if is_worse(seen, o):
            continue

        t, cum_flow, cur_flow, pos, opened = o
        seen[pos].append((t, cum_flow, cur_flow))
        iterate(graph, seen, o)


if __name__ == "__main__":

    graph = {}
    for line in INPUT.split('\n'):
        frm = line[6:8]
        rate = int(line.split('flow rate=')[-1].split(';')[0])
        if 'valves' in line:
            graph[frm] = rate, line.split('valves ')[-1].split(', ')
        else:
            graph[frm] = rate, [line.split('valve ')[-1]]


    seen = defaultdict(list) # (t, cum_flow, cur_flow)

    cur_state = (0, 0, 0, ('AA', 'AA'), [])
    iterate(graph, seen, cur_state)

    flows = []
    for ss in seen.values():
        for s in ss:
            flows.append(s[1])

    print(max(flows))




