import requests
from exceptions import AppError, NotFoundError, AccessDeniedError
from etl import ETL

def DownloadFile(url, fileName = "latest.txt"):
    resp = requests.get(url)

    if resp.status_code == 404:
        raise NotFoundError
    if resp.status_code == 403:
        raise AccessDeniedError
    if resp.status_code != 200:
        raise AppError

    with open(fileName, 'w', newline="") as file:
        print(f"Writing data from: {url} to file: {fileName}")
        file.write(resp.text)

def main():
    print("Program start")
    fileName = "data.txt"
    try:
        DownloadFile("https://oleksandr-fedoruk.com/wp-content/uploads/2025/10/sample.csv", fileName)
        ETL(fileName).run()

    except NotFoundError:
        print("The server cannot find the requested resource.")
    except AccessDeniedError:
        print("The client does not have access rights to the content")
    except AppError:
        print("Application error")
    else:
        print("Success !")


if __name__ == "__main__":
    main()