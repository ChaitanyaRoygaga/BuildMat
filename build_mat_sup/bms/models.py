from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.
class ItemGroupMaster(models.Model):
	item_group = models.CharField("Item Group Code", primary_key=True, max_length=3)
	item_group_name = models.CharField("Item Group Name", max_length=6)
	gst_rate = models.DecimalField("GST Rate", max_digits=5, decimal_places=2)	

class ItemMaster(models.Model):
	short_name = models.CharField("Short Name", primary_key=True, max_length=6)
	item_name = models.CharField("Item Name", max_length=30)
	unit_measure = models.CharField("Unit Of Measure", max_length=8)
	item_group = models.CharField("Item Group Code", max_length=3)	

class LorryMaster(models.Model):
	lorry_code = models.CharField("Lorry Code", primary_key=True, max_length=6)
	lorry_no = models.CharField("Lorry Number", max_length=14)
	driver = models.CharField("Driver Name", max_length=30)
	contact = models.CharField("Contact", max_length=15)
	tax_date = models.DateField("Tax Date: Enter in format 'Year(xxxx)-Month(xx)-Day(xx)'")
	puc_date = models.DateField("PUC Date: Enter in format 'Year(xxxx)-Month(xx)-Day(xx)'")
	permit_date = models.DateField("Permit Date: Enter in format 'Year(xxxx)-Month(xx)-Day(xx)'")
	insur_date = models.DateField("Insurance Date: Enter in format 'Year(xxxx)-Month(xx)-Day(xx)'")
	length = models.DecimalField("Length of Lorry", max_digits=5, decimal_places=2)
	breadth = models.DecimalField("Breadth of Lorry", max_digits=5, decimal_places=2)

class StateMaster(models.Model):
	state_code = models.CharField("State Code", primary_key=True, max_length=2)
	state_no = models.IntegerField("State Number")
	state_name = models.CharField("State Name", max_length=30)

class BusinessPartnerMaster(models.Model):
	code = models.CharField("Code", max_length=8, null=True)
	name = models.CharField("Full name", primary_key=True, max_length=50)
	address_1 = models.CharField("Address line 1", max_length=50, null=True)
	address_2 = models.CharField("Address line 2", max_length=50, null=True)
	city = models.CharField("City", max_length=15, null=True)
	pin = models.CharField("ZIP / Postal code", max_length=6, null=True)
	state_code = models.CharField("State Code", max_length=2, null=True)
	gst_no = models.CharField("GST Number", max_length=15, null=True)
	pan_aadhar_no = models.CharField("PAN / Aadhar Number", max_length=16, null=True)
	bp_type = models.CharField("Business Partner Type", max_length=10)

class BusinessGroupMaster(models.Model):
	group_code = models.CharField("Business Group", primary_key=True, max_length=3)
	group_name = models.CharField("Group Name", max_length=45)
	group_head = models.CharField("Group Head", max_length=30)
	contact_no = models.CharField("Contact", max_length=15)

class SiteMaster(models.Model):
	site_code = models.CharField("Site Code", primary_key=True, max_length=7)
	site_name = models.CharField("Site Name", max_length=35)
	address_1 = models.CharField("Address line 1", max_length=45)
	address_2 = models.CharField("Address line 2", max_length=45)
	city = models.CharField("City", max_length=15)
	pin = models.CharField("ZIP / Postal code", max_length=6, null=True)
	state_code = models.CharField("State Code", max_length=2, null=True)
	gst_no = models.CharField("GST Number", max_length=15)
	contact_person = models.CharField("Contact Person", max_length=30)
	site_contact = models.CharField("Site Contact", max_length=15)

class UnitOfMeasureMaster(models.Model):
	uom_code = models.CharField("UOM Code", primary_key=True, max_length=8)
	uom_name = models.CharField("UOM Name", max_length=35)

class Quotation(models.Model):
	quot_no = models.CharField("Quotation Number", primary_key=True, max_length=9)
	quot_dt = models.DateField("Quotation Date")
	frm_dt = models.DateField("From Date")
	to_dt = models.DateField("To Date")
	buyer_code = models.CharField("Buyer Code", max_length=50, null=True)
	group_code = models.CharField("Business Group", max_length=3)
    
class QuotationDetails(models.Model):
	quot_no = models.CharField("Quotation Number", primary_key=True, max_length=9)
	site_code = models.CharField("Site Code", max_length=7)
	short_name = models.CharField("Item Short Name", max_length=6)
	rate = models.DecimalField("Rate of Item", max_digits=5, decimal_places=2)

class CompanyMaster(models.Model):
	company_code = models.CharField("Company Code", primary_key=True, max_length=8)
	comp_name = models.CharField("Company Name", max_length=50)
	address_1 = models.CharField("Address 1", max_length=50)
	address_2 = models.CharField("Address 2", max_length=50)
	city = models.CharField("City", max_length=30)
	pin = models.CharField("Pincode", max_length=6)
	state_code = models.CharField("State Code", max_length=2, null=True)
	phone = models.CharField("Phone", max_length=11)
	mobile = models.CharField("Mobile", max_length=10)
	gst_no = models.CharField("GST Number", max_length=15)
	pan_no = models.CharField("PAN Number", max_length=10)
	bank_name = models.CharField("Bank Name", max_length=50)
	ac_no = models.CharField("Account Number", max_length=20)
	ifsc_code = models.CharField("IFSC Code", max_length=11)
	jurisdiction = models.CharField("Jurisdiction", max_length=15)
	interest_rate = models.DecimalField("Interest Rate", max_digits=4, decimal_places=2)

#import datetime
#import uuid
#from uuid import uuid4

class Transaction(models.Model):
	tr_date = models.DateField("Transaction Date")
	#vr_no = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	vr_no = models.CharField(primary_key=True, max_length=16)
	lorry_code = models.CharField("Lorry Code", max_length=6, null=True)
	trip = models.IntegerField("Number of trips", null=True)
	challan_no = models.CharField("Challan Number", max_length=20, null=True)
	buyer = models.CharField("Buyer Name", max_length=50, null=True)
	supplier = models.CharField("Supplier Name", max_length=50, null=True)
	site_code = models.CharField("Site Code", max_length=7, null=True)
	short_name = models.CharField("Short Name", max_length=6, null=True)
	length = models.DecimalField("Length of Lorry", max_digits=5, decimal_places=2, null=True)
	breadth = models.DecimalField("Breadth of Lorry", max_digits=5, decimal_places=2, null=True)
	height = models.DecimalField("Height of Item", max_digits=5, decimal_places=2, null=True)
	quantity = models.DecimalField("Quantity of Item", max_digits=10, decimal_places=2, null=True)
	pur_rate = models.DecimalField("Pur Rate of Item", max_digits=5, decimal_places=2, null=True)
	sale_rate = models.DecimalField("Sale Rate of Item", max_digits=5, decimal_places=2, null=True)

	class Meta:
        	ordering = ['-tr_date', '-vr_no']