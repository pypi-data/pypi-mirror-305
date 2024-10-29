"""
Set of function to annotate graphs with high level information
"""


def annotate_pair(x, y, pairs, offset=0.8, color="#000000", ax=None):
    """Plot brackets on top of each pair with associated text

    Args:
        x (list[float]|dict[Any, float]): x positions
        y (list[float]|dict[Any, float]): y positions (same length as x)
        pairs (list[Sequence[int,int,str]|Sequence[Any,Any,str]]): pairs of indices with associated text
        offset (float): distance above data
        color (str): color of drawn lines
        ax: matplotlib Axes

    Returns:
        None
    """
    stack_sorted = sorted(pairs, key=lambda tup: (x[tup[0]], x[tup[1]]))

    stack_ordered = [stack_sorted.pop(0)]
    for pair in stack_sorted:
        if x[pair[0]] == x[stack_ordered[-1][0]]:  # same start but larger end since sorted
            stack_ordered.append(pair)
        elif x[stack_ordered[-1][1]] <= x[pair[0]]:  # segment completely on right of last
            stack_ordered.append(pair)
        else:
            if x[pair[1]] <= x[stack_ordered[-1][1]]:  # segment completely inside last
                ind = -1
                try:
                    while x[pair[1]] <= x[stack_ordered[ind][1]]:
                        ind -= 1
                    stack_ordered.insert(ind + 1, pair)
                except IndexError:
                    stack_ordered.insert(0, pair)

            else:  # segment only halfway inside last
                stack_ordered.append(pair)

    # plot
    plt_height = y.copy()
    for i0, i1, txt in stack_ordered:
        height = max(plt_height[i0], plt_height[i1]) + offset
        plt_height[i0] = height
        plt_height[i1] = height
        ax.plot(
            [x[i0], x[i0], x[i1], x[i1]],
            [height - offset / 4, height, height, height - offset / 4],
            ls="-",
            color=color,
        )
        ax.text(x[i0] + (x[i1] - x[i0]) / 2, height, txt, ha="center", va="bottom")


def significance(pvalue):
    for th, txt in [[1e-4, "****"], [1e-3, "***"], [1e-2, "**"], [0.05, "*"], [1, "ns"]]:
        if pvalue < th:
            return txt

    return "ns"
