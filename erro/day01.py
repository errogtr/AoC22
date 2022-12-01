from itertools import groupby

from erro import get_data_path


if __name__ == "__main__":
    with open(get_data_path(__file__)) as f:
        data = f.readlines()

    # PART 1
    print(max(sum(map(int, g)) for k, g in groupby(data, key=lambda x: x != "\n") if k))
