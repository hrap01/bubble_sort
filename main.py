import argparse

parser = argparse.ArgumentParser(description='Process some integers with bubble sort.')
parser.add_argument('integers', metavar='N', type=int, nargs='+',
                    help='an integer for the bubble sort')

args = parser.parse_args()
print(args.integers)

def bubble_sort(l):
    i = 0
    if l is not None:
        while i < len(l) - 1:
            if l[i] <= l[i + 1]:
                i += 1
            else:
                for j in range(0, len(l) - 1):
                    if l[j] > l[j + 1]:
                        l[j], l[j + 1] = l[j + 1], l[j]
                    i = 0
    return l

print(bubble_sort(args.integers))

