#복습
def min_clicks_to_channel(N, broken_buttons):
    broken = set(broken_buttons)

    min_clicks = abs(100 - N)

    for channel in range(1000000):
        for c in str(channel):
            if int(c) in broken:
                break
        else:
            clicks = len(str(channel)) + abs(channel - N)
            min_clicks = min(min_clicks, clicks)

    return min_clicks

N = int(input())
M = int(input())
broken_buttons = list(map(int, input().split())) if M > 0 else []

min_clicks = min_clicks_to_channel(N, broken_buttons)

print(min_clicks)
