import matplotlib.pyplot as plt
def main():
    size_v1 = [64, 128, 256, 512]
    size_v2_v3 = [64, 128, 256, 512, 1024, 2048, 4096, 8192]

    times_v1 = [1138900, 8217900, 59902300, 497919600]
    times_v2 = [65000, 233400, 966900, 3898300, 16417200, 61062500, 265599700, 1000140500]
    times_v3 = [3800, 6900, 14300, 28200, 57700, 113000, 225600, 417300]

    bytes_v1 = [n * 8 for n in size_v1]
    bytes_v2_v3 = [n * 8 for n in size_v2_v3]

    plt.plot(bytes_v1, times_v1, label="1")
    plt.plot(bytes_v2_v3, times_v2, label="2")
    plt.plot(bytes_v2_v3, times_v3, label="3")

    plt.xlabel("Размер данных, байт")
    plt.ylabel("Время, нс")
    plt.title("Зависимость времени выполнения от размера")
    plt.legend()
    plt.show()


if __name__ == "__main__":
    main()