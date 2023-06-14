import gdown

DATASET_LINK_ID = "1KXFzyenbE_WSgd3BXrIbUk5EDVxmuHyD"
OUTPUT_PATH = "./data/dataset.csv"


def download_dataset(link_id, output_path):
    gdown.download(f"https://drive.google.com/uc?id={link_id}", output_path, quiet=True)


if __name__ == "__main__":
    print("Dowloading dataset:", end=" ")
    download_dataset(DATASET_LINK_ID, OUTPUT_PATH)
    print("Done")
