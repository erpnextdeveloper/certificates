from __future__ import unicode_literals
import frappe
from frappe.utils import cint, get_gravatar, format_datetime, now_datetime,add_days,today,formatdate,date_diff,getdate,get_last_day
from frappe import throw, msgprint, _
from frappe.utils.password import update_password as _update_password
from frappe.desk.notifications import clear_notifications
from frappe.utils.user import get_system_managers
import frappe.permissions
import frappe.share
import re
import string
import random
import json
import time
from datetime import datetime
from datetime import date
from datetime import timedelta
import collections
import math
import logging

@frappe.whitelist()
def test(doc,method):
	frappe.db.sql("""update `tabCertificate` set parent=%s,parentfield='crewmember_certificates',parenttype='Employee' where name=%s""",(doc.employee_link,doc.name))


@frappe.whitelist()
def addCertificateOwnerInformer(doc,method):
	data=frappe.db.sql("""select name from `tabCertificate Informer` where certificate_id=%s""",doc.name)
	if data:
		doc1=frappe.get_doc("Certificate Informer",data[0][0])
		doc1.owner_certicate=str(doc.employee_link)
		doc1.owner_id=str(getUserId(doc.employee_link))
		doc1.informer_certificate=str(doc.cert_who_informed)
		doc1.informer_id=str(getUserId(doc.cert_who_informed))
		doc1.certificate_expiration=str(doc.certificate_expiration)
		doc1.save()
	else:
		doc1=frappe.get_doc({
				"docstatus": 0,
				"doctype": "Certificate Informer",
				"name": "New Certificate Informer 1",
				"owner_certicate":str(doc.employee_link),
				"parent":str(doc.cert_who_informed),
				"parentfield": "certificate_informer",
				"parenttype": "Employee",
				"certificate_id":str(doc.name),
				"owner_id":str(getUserId(doc.employee_link)),
				"informer_certicate":str(doc.cert_who_informed),
				"informer_id":str(getUserId(doc.cert_who_informed)),
				"certificate_expiration":str(doc.certificate_expiration)
			})
		doc1.insert()
	


@frappe.whitelist()
def getUserId(emp_code):
	doc=frappe.get_doc("Employee",emp_code)
	if doc.user_id:
		return doc.user_id
	elif doc.personal_email:
		return doc.personal_emal
	else:
		return str()
		 
	
