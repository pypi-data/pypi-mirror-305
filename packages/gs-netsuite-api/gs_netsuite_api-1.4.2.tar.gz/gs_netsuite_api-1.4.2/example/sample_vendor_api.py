import logging
from pprint import pprint

from gs_netsuite_api.api import VendorAPI
from gs_netsuite_api.ns_utils import NetSuiteCredential, SearchParams

logging.root.setLevel(logging.DEBUG)
logging.root.addHandler(logging.StreamHandler())


if __name__ == "__main__":
    # Existe d'autre methode pour avoir un NetSuiteCredential
    cred = NetSuiteCredential.from_env_file("./auth_netsuite.env")
    api = VendorAPI(credential=cred, search_params=SearchParams(page_size=5, nb_pages=2))

    data_one = api.get_one(54839)
    pprint(data_one)
