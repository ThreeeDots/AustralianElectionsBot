import pywikibot as pwb
import time
import datetime

class PageNotSavedError(Exception):
	'''Page saving has failed.'''
	pass

class NotLoggedInError(Exception):
	'''Bot is not correctly logged in.'''
	pass

class AustralianElectionsBot(pwb.SingleSiteBot, pwb.CurrentPageBot):
	