#Window utility scripts for NVDA
#Developer guide example 3

import globalPluginHandler
from scriptHandler import script
import ui
import api

class GlobalPlugin(globalPluginHandler.GlobalPlugin):

	@script(
		description=_("Announces the window class name of the current focus object"),
		gesture="kb:NVDA+leftArrow"
	)
	def script_announceWindowClassName(self, gesture):
		focusObj = api.getFocusObject()
		name = focusObj.name
		windowClassName = focusObj.windowClassName
		ui.message("class for %s window: %s" % (name, windowClassName))

	@script(
		description=_("Announces the window control ID of the current focus object"),
		gesture="kb:NVDA+rightArrow"
	)
	def script_announceWindowControlID(self, gesture):
		focusObj = api.getFocusObject()
		name = focusObj.name
		windowControlID = focusObj.windowControlID
		ui.message("Control ID for %s window: %d" % (name, windowControlID))