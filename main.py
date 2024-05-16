from ftplib import FTP
from configparser import ConfigParser


def download_file(remote_file_name, local_file_path):
    try:
        ftp = FTP()
        ftp.connect(FTP_IP, FTP_PORT)
        ftp.login(user=FTP_USER, passwd=FTP_PASSWORD)

        with open(local_file_path, "wb") as file:
            ftp.retrbinary("RETR " + remote_file_name, file.write)

        ftp.quit()
        print("File downloaded successfully.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")


def upload_file(local_file_path, remote_file_name):
    try:
        ftp = FTP()
        ftp.connect(FTP_IP, FTP_PORT)
        ftp.login(user=FTP_USER, passwd=FTP_PASSWORD)

        with open(local_file_path, "rb") as file:
            ftp.storbinary("STOR " + remote_file_name, file)

        ftp.quit()
        print("File uploaded successfully.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")


def list_files():
    try:
        ftp = FTP()
        ftp.connect(FTP_IP, FTP_PORT)
        ftp.login(user=FTP_USER, passwd=FTP_PASSWORD)

        files = ftp.nlst()

        ftp.quit()

        print("List of files on the server:")
        for file in files:
            print(file)
    except Exception as e:
        print(f"An error occurred: {str(e)}")


if __name__ == "__main__":
    config = ConfigParser()
    config.read("config.ini")

    FTP_IP = config.get("SERVER", "ip")
    FTP_PORT = int(config.get("SERVER", "port"))
    FTP_USER = config.get("SERVER", "user")
    FTP_PASSWORD = config.get("SERVER", "password")

    data_file_name = config.get("SERVER", "data_file_name")
    reviews_file_name = config.get("SERVER", "reviews_file_name")

    download_file(data_file_name, data_file_name)
    download_file(reviews_file_name, reviews_file_name)
