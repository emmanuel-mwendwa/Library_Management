# Copyright (c) 2024, Emmanuel Mwendwa and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class LibraryMember(Document):
	
	def run_before_save_methods(self):
		self.full_name = f'{self.first_name} {self.last_name or ""}'
