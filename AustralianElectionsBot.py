import pywikibot as pwb
import time
import datetime
import logging
import requests
import re

logging.basicConfig(level=logging.INFO)

class PageNotSavedError(Exception):
	'''Page saving has failed.'''
	pass

class NotLoggedInError(Exception):
	'''Bot is not correctly logged in.'''
	pass

class AustralianElectionsBot(pwb.SingleSiteBot, pwb.CurrentPageBot):
	"""
	A pywikibot bot to standardise and update Australian election results pages.
	The following tasks are to be performed:

	1. Rename all Australian election pages to follow standardised conventions.
	2. Update results tables of recent elections to the official results.
	3. Include in the results table the svg displaying the composition of the chamber due to that election, if the svg exists.
	4. Fix any double-redirects caused by pagemoves.
	5. Embed the results contained in sub-pages into main pages, using {{excerpt}}, which is best practice.
	"""

	def __init__(self, **kwargs):
		# Initialise SingleSiteBot and CurrentPageBot with configs.
		super().__init__(site=True, **kwargs)

	def run(self):
		self.rename_pages()
		self.update_results_tables()
		self.include_composition_file()
		self.fix_double_redirects()
		self.embedding()

	def rename_pages(self):
		# This function's contents.
		return

	def update_results_tables(self):
		# This function's contents.
		return
	
	def include_composition_file(self):
		# This function's contents.
		return
	
	def fix_double_redirects(self):
		# This function's contents.
		return
	
	def embedding(self):
		# This function's contents.
		return
	
if __name__ == '__main__':
	bot = AustralianElectionsBot()
	bot.run()