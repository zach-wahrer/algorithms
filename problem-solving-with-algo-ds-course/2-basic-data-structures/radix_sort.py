def radix_sorting(nums: list) -> list:
    main_bin = nums

    sorted_list = []
    most_digits = len(str(max(nums)))

    for place in range(most_digits):

        bins = [[], [], [], [], [], [], [], [], [], []]

        for num in main_bin:
            bins[which_bin(num, place)].append(num)

        main_bin.clear()

        for digit_bin in bins:
            for value in digit_bin:
                if len(str(value)) - 1 == place:
                    sorted_list.append(value)
                else:
                    main_bin.append(value)

    return sorted_list


def which_bin(number: int, place: int) -> int:
    return int(str(number)[-(place + 1)])


# print(radix_sorting([2, 1, 9889, 672, 3, 10, 100]))
