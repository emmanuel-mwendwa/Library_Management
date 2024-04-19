# Copyright (c) 2024, Emmanuel Mwendwa and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe.model.docstatus import DocStatus


class LibraryMembership(Document):
	
	def before_submit(self):

		exists = frappe.db.exists(
			"Library MemberShip",
			{
				"library_member": self.library_member,
				"docstatus": DocStatus.submitted(),
				# check if the membership's end date is later than membership's start date
				"to_date": (">", self.from_date),
			},
		),
		if exists:
			frappe.throw("There is an active membership for this member")
