import matplotlib.pyplot as plt

if __name__ == "__main__":
    turb_data = []
    with open("turb.dat", "r") as turb_file:
        turb_data = turb_file.read().split()
    turb_data = map(int, turb_data)
    #print turb_data[0]
    plt.plot(turb_data)
    plt.show()
