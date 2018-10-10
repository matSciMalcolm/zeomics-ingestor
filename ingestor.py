#### table_scrape_updated_frc ####

__author__ = 'Malcolm Davidson'

__version__ = 1 # August 21, 2018  #


#### Standard Libraries ####
import os
import csv
from time import sleep
import urllib.request



#### Third Party Libraries ####
import pandas as pd
from selenium import webdriver


#### Global Variables ####
FILENAME = 'zeomics_properties.csv'
DIRECTORY = '/Users/malcolmdavidson/Documents/ODI/Collaborations/ODI_PU_XX_12_Zeomics/ingestor'


#### Classes ####


## Dataset ##
''' Stores data '''


#### Functions #### 


## open_csv ##
''' 
opens a csv file
'''
def open_csv(filename):

	csv_list = None

	try:

		with open(filename) as f:

			csv_list = list(csv.reader(f))

	except Exception:
		pass

	return csv_list

def build_url(code):

	'''Builds a URL from passed codes.

		Args:
			code (str): IZA framework code

		Returns:
			url_str (str): HTTP URL pointing to cif for code

	'''
	url_str = 'http://america.iza-structure.org/IZA-SC/cif/{}.cif'.format(code)

	return url_str

def get_cif_from_url(cif_file_path):

	'''Extracts a cif file from the IZA url using HTTP

		Args:
			url (str): an HTTP URL for the IZA website

		Returns:
			cif (??)
	'''
	driver = webdriver.Chrome('/Users/malcolmdavidson/Documents/Code/tools/chromedriver')  # Optional argument, if not specified will search path.
	driver.get('http://helios.princeton.edu/zeomics/');
	search_box = driver.find_element_by_name('cif_file')
	search_box.send_keys('/Users/malcolmdavidson/Downloads/ABW.cif') # maybe url here?
	search_box.submit()

	cif = None
	return(cif)

	def get_cif_from_url(cif_file_path):

		'''Extracts a cif file from the IZA url using HTTP

			Args:
				url (str): an HTTP URL for the IZA website

			Returns:
				cif (??)
		'''
		driver = webdriver.Chrome('/Users/malcolmdavidson/Documents/Code/tools/chromedriver')  # Optional argument, if not specified will search path.
		driver.get('http://helios.princeton.edu/zeomics/');
		search_box = driver.find_element_by_name('cif_file')
		search_box.send_keys('/Users/malcolmdavidson/Downloads/ABW.cif') # maybe url here?
		search_box.submit()

		cif = None
		return(cif)

#### Main ####
def main():

	os.chdir(DIRECTORY)


	# Open list containing the codes to look up.
	iza_fw_codes = open_csv('zeomics_id.csv')

	# Use the imporded code list to build a list of IZA URL's
	iza_urls = [build_url(code[0]) for code in iza_fw_codes]

	# How will we scrape, Tables or download CSV's?
	#  Will need the CIF for zeomics
	#  Example URL
	#  http://america.iza-structure.org/IZA-SC/cif/ABW.cif
	'''
	pwd_labels = ['Framework','< 4','4–6','> 6','< 6','6-8','> 8']
	avfm_labels = ['Framework','2','4','6','8','2','4','6','8']
	


	pwd_data = []
	avfm_data = []

	for i, row in enumerate(zeomics_urls,0):
		print('\nAcquring data for: {}'.format(zeomics_id[i][0]))
		#code = pd.DataFrame(columns=['Framework'])
		#code.loc[0] = str(zeomics_id[i][0])

		tables = pd.read_html(row)

		#raw_pwd = pd.DataFrame(data=[str(zeomics_id[i][0]),tables[1].iloc[6,0:7].dropna().transpose()],columns=labels)
		#raw_pwd = tables[1].iloc[6,0:7].dropna().to_frame().T

		new_pwd_data = tables[1].iloc[6,0:7].dropna().tolist()
		new_avfm_data = tables[3].iloc[4].dropna().tolist()

		new_pwd_data.insert(0,str(zeomics_id[i][0]))
		new_avfm_data.insert(0,str(zeomics_id[i][0]))

		#data = pd.concat([code, raw_pwd], axis=1)
		pwd_data.append(new_pwd_data)
		avfm_data.append(new_avfm_data)

		#sleep(0.001)
	
	#print(pwd_data)
	pwd_df = pd.DataFrame(data=pwd_data,columns=pwd_labels)
	pwd_df.replace(to_replace='–',value=int(0),inplace=True)
	#pwd_df.to_csv('pwd.csv', sep=',', index=False, encoding='utf-8')

	pwd_df = pd.DataFrame(data=avfm_data,columns=avfm_labels)
	pwd_df.replace(to_replace='–',value=int(0),inplace=True)
	pwd_df.to_csv('avfm.csv', sep=',', index=False, encoding='utf-8')
	'''

	

if __name__ == '__main__':
	main()

