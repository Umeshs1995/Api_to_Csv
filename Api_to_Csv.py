import flatten
import pandas as pd
import requests
from flatten_json import flatten
import logging

logging.basicConfig(filename='museum.log',
                    filemode='w',
                    format='%(asctime)s %(levelname)s-%(message)s',
                    level=logging.INFO  # if i provide level here only after that level will be printed in log file
                    )

logger = logging.getLogger()


class FlatCsv:

    def __init__(self, func):
        self.func = func

    def __str__(self):
        return str(self.func)

    def ApiCall(self):
        """Take url and converted into json data.
        :type: type of string must be string.
        """
        # logger.debug("Starting new http connection:")
        try:
            response = requests.get(self.func)
            if response.status_code == 200:
                logger.info("%s: http connection successful- %s", self.func, response.status_code)
            response.raise_for_status()  # check if error has been occurred
        except requests.exceptions.ConnectionError as ce:
            logger.error('connection error- %s', ce)
        except requests.exceptions.HTTPError as ht:
            logger.error(' http ResponseBase implementation error- %s', ht)

        resp_json = response.json()
        return resp_json

    @staticmethod
    def FlatJsonData(resp_json):
        """ converted json data into flatted data.
        :param resp_json: flatted data and convert dataframe stored list.
        """
        object_id = resp_json['objectIDs'][:20]
        lst = []
        for x in object_id:
            Urls = "https://collectionapi" \
                   ".metmuseum.org/public/collection/v1/objects" + '/' + f"{str(x)}"
            resp = requests.get(Urls)
            my_json = resp.json()

            flatten_data = flatten(my_json)
            df = pd.DataFrame.from_dict(flatten_data, orient='index')
            lst.append(df)
        # return lst
        data = pd.concat(lst, axis=1)
        data1 = data.transpose()
        data1.to_csv('museum.csv', index=False, encoding='utf-8-sig', )
        print('done')
