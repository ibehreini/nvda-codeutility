import appModuleHandler
from scriptHandler import script
from NVDAObjects.IAccessible import IAccessible
import controlTypes
import ui

class AppModule(appModuleHandler.AppModule):

	def chooseNVDAObjectOverlayClasses(self, obj, clsList):
		if obj.windowClassName == "SWT_Window0" and obj.role == controlTypes.ROLE_EDITABLETEXT:
			clsList.insert(0, EnhancedEditField)

class EnhancedEditField(IAccessible):

	@script(gesture="kb:NVDA+l")
	def script_reportLength(self, gesture):
		ui.message("hiya ida")