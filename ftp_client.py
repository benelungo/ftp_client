from ftplib import FTP
from configparser import ConfigParser
import schedule


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


def main():
    download_file(data_file_name, data_local_file_path)
    download_file(reviews_file_name, reviews_local_file_path)


if __name__ == "__main__":
    config = ConfigParser()
    config.read("config.ini")

    FTP_IP = config.get("SERVER", "ip")
    FTP_PORT = int(config.get("SERVER", "port"))
    FTP_USER = config.get("SERVER", "user")
    FTP_PASSWORD = config.get("SERVER", "password")

    data_file_name = config.get("PATH", "data_file_name")
    reviews_file_name = config.get("PATH", "reviews_file_name")
    data_local_file_path = config.get("PATH", "data_local_file_path")
    reviews_local_file_path = config.get("PATH", "reviews_local_file_path")

    run_time = config.get("RUN OPTIONS", "run_time")

    if config.getboolean("RUN OPTIONS", "run_on_start"):
        main()

    if config.getboolean("RUN OPTIONS", "run_schedule"):
        schedule.every(1).day.at(run_time).do(main)
        while True:
            schedule.run_pending()
