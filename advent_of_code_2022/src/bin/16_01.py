from collections import defaultdict

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

T_END = 30


def options(graph, cur_state):
    t, cum_flow, cur_flow, pos, opened = cur_state

    options = []

    # Open valve
    if (pos not in opened) and (graph[pos][0] > 0):
        options.append((t + 1, cum_flow + cur_flow, cur_flow + graph[pos][0], pos, opened[:] + [pos]))

    for out in graph[pos][1]:
        options.append((t + 1, cum_flow + cur_flow, cur_flow, out, opened))

    # Check for end time
    options = [o for o in options if o[0] <= T_END]

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


    seen = defaultdict(list) # t, cur_flow

    cur_state = (0, 0, 0, 'AA', [])
    iterate(graph, seen, cur_state)

    flows = []
    for ss in seen.values():
        for s in ss:
            flows.append(s[1])

    # flows = [s for s in seen.values()]
    # print(flows)
    print(max(flows))




