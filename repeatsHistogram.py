import matplotlib.pyplot as plt
from findRepeats import findRepeats,createRepeatsBed
def repeatsHistogram(data):
    repeats = list(data.keys())
    repeatCounts = list(data.values())

    plt.bar(repeats, repeatCounts)
    plt.yscale('log')

    plt.xlabel('Repeats')
    plt.ylabel('Repeat Frequencies')
    plt.title('Histogram of Repeats')
    plt.show()

def main():
    data = findRepeats("annotatedpas.bed")
    createRepeatsBed(data, "repeatsBed.bed")
    repeatsHistogram(data)

main()

