#    pyOwlBoard - The Python client for the OwlBoard API
#    Copyright (C) 2024  Frederick Boniface

#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.

#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.

#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.

import requests
import logging
from datetime import datetime
from typing import List, Dict, Tuple

from .contants import ENDPOINTS, VERSION
from .utils import format_url_datetime, url_multijoin

logger = logging.getLogger('OwlBoardClient')
logger.setLevel(logging.INFO)
ch = logging.StreamHandler()
ch.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
logger.addHandler(ch)

class OwlBoardClient:

    def __init__(self, base_url: str, api_key: str):
        self.base_url = base_url
        self.api_key = api_key
        self.headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'User-Agent': 'pyOwlBoard/' + VERSION,
            'uuid': self.api_key,
        }

        try:
            self.verify_connection()
        except Exception as e:
            logger.error(f"Error creating API Client: {e}")
            raise

    def verify_connection(self):
        url_path = url_multijoin(self.base_url, ENDPOINTS['TEST'])
        response = self._make_request('GET', url_path)
        logger.info("Connection verified: %s", response.status_code)

    def _make_request(self, method: str, url: str, **kwargs):
        try:
            response = requests.request(method, url, headers=self.headers, **kwargs)
            response.raise_for_status()
            return response
        except requests.RequestException as e:
            logger.error(f"Request failed: {e}")
            raise

    ### PIS Code Methods ###

    ## Needs fixing on API Server side
    def get_stops_by_pis(self, code: str):
        url_path = url_multijoin(self.base_url, ENDPOINTS['PIS_BY_CODE'], code)
        logger.debug(f"Generated URL: {url_path}")
        response = self._make_request('GET', url_path)
        logger.info("Response received for get_stops_by_pis")
        return response.json()

    def get_pis_by_start_end_crs(self, start_crs: str, end_crs: str):
        url_path = url_multijoin(self.base_url, ENDPOINTS['PIS_BY_START_END_CRS'], start_crs, end_crs)
        logger.debug(f"Generated URL: {url_path}")
        response = self._make_request('GET', url_path)
        logger.info("Response received for get_pis_by_start_end_crs")
        return response.json()

    def get_pis_by_tiploc_list(self, tiplocs: List[str]):
        return

    ### Train Methods ###

    def get_trains_by_headcode(self, headcode: str, date: datetime):
        if not isinstance(headcode, str):
            raise TypeError("headcode must be a string")
        if not isinstance(date, datetime):
            raise TypeError("date must be a datetime object")

        # Generate URL
        try:
            url_path = url_multijoin(
                self.base_url,
                ENDPOINTS['TIMETABLE_TRAINS'],
                format_url_datetime(date),
                'headcode',
                headcode,
            )
            logger.debug(f"Generated URL: {url_path}")
        except Exception as e:
            logger.error(f"Error generating URL: {e}")
        
        # Send request
        response = self._make_request('GET', url_path)
        logger.info("Response received for get_trains_by_headcode")
        return response.json()

    def get_trains_by_trainUid(self, train_uid: str, date: datetime):
        if not isinstance(train_uid, str):
            raise TypeError("train_uid must be a string")
        if not isinstance(date, datetime):
            raise TypeError("date must be a datetime object")
        
        # Generate URL
        try:
            url_path = url_multijoin(
                self.base_url,
                ENDPOINTS['TIMETABLE_TRAINS'],
                format_url_datetime(date),
                'byTrainUid',
                train_uid,
            )
            logger.debug(f"Generated URL: {url_path}")
        except Exception as e:
            logger.error(f"Error generating URL: {e}")
            raise
        
        # Send request
        response = self._make_request('GET', url_path)
        logger.info("Response received for get_trains_by_trainUid")
        return response.json()

        ## Location Reference Methods ##

    def get_loc_ref_codes_by_tiploc(self, tiploc: str):
        url_path = url_multijoin(self.base_url, ENDPOINTS['REF_LOCATION_BY_TIPLOC'], tiploc)
        logger.debug(f"Generated URL: {url_path}")

        # Send Request
        response = self._make_request('GET', url_path)
        logger.info("Response received for get_trains_by_trainUid")
        return response.json()

        ## Location Reference Methods ##

    def get_loc_ref_codes_by_tiploc(self, tiploc: str):
        url_path = url_multijoin(self.base_url, ENDPOINTS['REF_LOCATION_BY_TIPLOC'], tiploc)
        logger.debug(f"Generated URL: {url_path}")

        # Send Request
        response = self._make_request('GET', url_path)
        logger.info("Response received for get_trains_by_trainUid")
        return response.json()

if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)

    try:
        client = OwlBoardClient(base_url='https://owlboard.info', api_key="x")
        test = client.get_trains_by_headcode("1A99", datetime.now())
        print(test)
    except Exception as e:
        logger.error(f"Failed to create client: {e}")