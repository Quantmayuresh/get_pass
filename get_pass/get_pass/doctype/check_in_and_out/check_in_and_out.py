# Copyright (c) 2022, Atharva and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document

class CheckInandOut(Document):
	def before_save(self):
		self.full_name = f'{self.first_name} {self.middle_name} {self.last_name}'
    
	
