import os
import generate_feature_vector as gf

def main():
    folder = input("Enter folder path: ")
    files_in_folder = os.listdir(folder)
    for file in files_in_folder:
        temp = folder + '/' + file
        gf.run_remote(str(temp))


if __name__ == '__main__':
    main()
