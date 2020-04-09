import argparse


if __name__ == "__main__":

    # Initialize the arguments
    prs = argparse.ArgumentParser()
    prs.add_argument('-t', '--target', help='Production target', type=str)
    prs.add_argument('-c', '--compute', help='production Computed', type=str)
    prs.add_argument('-f', '--file_name', help='File name Computed', type=str)
    # prs.add_argument('-k', '--km', help='Number of machines', type=str)
    prs = prs.parse_args()