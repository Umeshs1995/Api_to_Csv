from Api_to_Csv import FlatCsv

urls = "https://collectionapi.metmuseum.org/public/collection/v1/objects"


def main():
    # Use a breakpoint in the code line below to debug your script.
    url = FlatCsv(urls)
    resp = FlatCsv.ApiCall(url)
    return FlatCsv.FlatJsonData(resp)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
