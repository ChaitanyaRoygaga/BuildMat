from django import forms
from .models import UnitOfMeasureMaster, ItemGroupMaster, StateMaster, BusinessGroupMaster, BusinessPartnerMaster, Quotation, ItemMaster, SiteMaster
#from bootstrap_datepicker.widgets import DatePicker
#from django.forms.fields import DateField

import datetime

#ItemGroupMaster
class ItemGroupForm(forms.Form):
	error_css_class = 'error'
	required_css_class = 'required'
	item_group = forms.CharField(label='ITEM GROUP', max_length=3)
	item_group_name = forms.CharField(label='ITEM GROUP NAME', max_length=6)
	gst_rate = forms.DecimalField(label='GST RATE', max_digits=5, decimal_places=2)

#ItemMaster
class ItemForm(forms.Form):
	short_name = forms.CharField(label='SHORT NAME', max_length=6)
	item_name = forms.CharField(label='ITEM NAME', max_length=30)
	unit_measure = forms.ModelChoiceField(label='UNIT OF MEASURE', queryset=UnitOfMeasureMaster.objects.values_list('pk', flat=True), empty_label="- - - - - - SELECT - - - - - -")
	item_group = forms.ModelChoiceField(label='ITEM GROUP', queryset=ItemGroupMaster.objects.values_list('pk', flat=True), empty_label="- - - - - - SELECT - - - - - -")

#LorryMaster
class LorryForm(forms.Form):
	lorry_code = forms.CharField(label='LORRY CODE', max_length=6)
	lorry_no = forms.CharField(label='LORRY NUMBER', max_length=14)
	driver = forms.CharField(label='DRIVER NAME', max_length=30)
	contact = forms.CharField(label='CONTACT NUMBER', max_length=15)
	tax_date = forms.DateField(label='TAX DATE', )
	puc_date = forms.DateField(label='PUC DATE', )
	permit_date = forms.DateField(label='PERMIT DATE', )
	insur_date = forms.DateField(label='INSURANCE DATE', )
	length = forms.DecimalField(label='LENGTH', max_digits=5, decimal_places=2)
	breadth = forms.DecimalField(label='BREADTH', max_digits=5, decimal_places=2)

#BusinessPartnerMaster
class BusinessPartnerForm(forms.Form):
	BP_TYPE_CHOICES = (
		('Buyer', 'Buyer'),
		('Supplier', 'Supplier'),
	)

	code = forms.CharField(label='CODE', max_length=8)
	name = forms.CharField(label='NAME', max_length=50)
	address_1 = forms.CharField(label='ADDRESS LINE 1', max_length=50)
	address_2 = forms.CharField(label='ADDRESS LINE 2', max_length=50)
	city = forms.CharField(label='CITY', max_length=15)
	pin = forms.CharField(label='PIN CODE', max_length=6)
	state_code = forms.ModelChoiceField(label='STATE CODE', queryset=StateMaster.objects.values_list('pk', flat=True), empty_label="- - - - - - SELECT - - - - - -")
	gst_no = forms.CharField(label='GST NUMBER', max_length=15)
	pan_aadhar_no = forms.CharField(label='PAN/AADHAR NUMBER', max_length=16)
	bp_type = forms.CharField(label='BUSINESS PARTNER TYPE', widget=forms.Select(choices=BP_TYPE_CHOICES))

#BusinessGroupMaster
class BusinessGroupForm(forms.Form):
	group_code = forms.CharField(label='CODE', max_length=3)
	group_name = forms.CharField(label='NAME', max_length=45)
	group_head = forms.CharField(label='GROUP HEAD', max_length=30)
	contact_no = forms.CharField(label='CONTACT NUMBER', max_length=15)

#SiteMaster
class SiteForm(forms.Form):
	site_code = forms.CharField(label='CODE', max_length=7)
	site_name = forms.CharField(label='NAME', max_length=35)
	address_1 = forms.CharField(label='ADDRESS LINE 1', max_length=45)
	address_2 = forms.CharField(label='ADDRESS LINE 2', max_length=45)
	city = forms.CharField(label='CITY', max_length=15)
	pin = forms.CharField(label='PIN CODE', max_length=6)
	state_code = forms.ModelChoiceField(label='STATE CODE', queryset=StateMaster.objects.values_list('pk', flat=True), empty_label="- - - - - - SELECT - - - - - -")
	gst_no = forms.CharField(label='GST NUMBER', max_length=15)
	contact_person = forms.CharField(label='CONTACT PERSON', max_length=30)
	site_contact = forms.CharField(label='SITE CONTACT', max_length=15)

#UnitOfMeasureMaster
class UOMForm(forms.Form):
	uom_code = forms.CharField(label='CODE', max_length=8)
	uom_name = forms.CharField(label='NAME', max_length=35)

#Quotation
class QuotationForm(forms.Form):
	quot_no = forms.CharField(label='QUOTE NUMBER', max_length=9)
	quot_dt = forms.DateField(label='QUOTE DATE', )
	frm_dt = forms.DateField(label='VALID FROM', )
	to_dt = forms.DateField(label='VALID TO', )
	buyer_code = forms.ModelChoiceField(label='BUYER', queryset=BusinessPartnerMaster.objects.values_list('pk', flat=True).filter(bp_type='buyer'), empty_label="- - - - - - SELECT - - - - - -")
	group_code = forms.ModelChoiceField(label='GROUP CODE', queryset=BusinessGroupMaster.objects.values_list('pk', flat=True), empty_label="- - - - - - SELECT - - - - - -")

#QuotationDetails
class QuotationDetailsForm(forms.Form):
	quot_no = forms.ModelChoiceField(label='QUOTE NUMBER', queryset=Quotation.objects.values_list('pk', flat=True), empty_label="- - - - - - SELECT - - - - - -")
	site_code = forms.ModelChoiceField(label='SITE CODE', queryset=SiteMaster.objects.values_list('pk', flat=True), empty_label="- - - - - - SELECT - - - - - -")
	short_name = forms.ModelChoiceField(label='ITEM', queryset=ItemMaster.objects.values_list('pk', flat=True), empty_label="- - - - - - SELECT - - - - - -")
	rate = forms.DecimalField(label='RATE', max_digits=5, decimal_places=2)

#CompanyMaster
class CompanyForm(forms.Form):
	company_code = forms.CharField(label='COMPANY CODE', max_length=8)
	comp_name = forms.CharField(label='COMPANY NAME', max_length=50)
	address_1 = forms.CharField(label='ADDRESS LINE 1', max_length=50)
	address_2 = forms.CharField(label='ADDRESS LINE 2', max_length=50)
	city = forms.CharField(label='CITY', max_length=30)
	pin = forms.DecimalField(label='PIN CODE', max_digits=6)
	state_code = forms.ModelChoiceField(label='STATE CODE', queryset=StateMaster.objects.values_list('pk', flat=True), empty_label="- - - - - - SELECT - - - - - -")
	phone = forms.DecimalField(label='LANDLINE', max_digits=11)
	mobile = forms.DecimalField(label='MOBILE NUMBER', max_digits=10)
	gst_no = forms.CharField(label='GST NUMBER', max_length=15)
	pan_no = forms.CharField(label='PAN NUMBER', max_length=10)
	bank_name = forms.CharField(label='BANK NAME', max_length=50)
	ac_no = forms.DecimalField(label='ACCOUNT NUMBER', max_digits=20)
	ifsc_code = forms.DecimalField(label='IFSC CODE', max_digits=11)
	jurisdiction = forms.CharField(label='JURISDICTION', max_length=15)
	interest_rate = forms.DecimalField(label='INTEREST RATE', max_digits=4, decimal_places=2)

#Transaction
class TransactionForm(forms.Form):
	tr_date = forms.DateField(label='TRANSACTION DATE', initial=datetime.date.today)
	vr_no = forms.IntegerField(label='VOUCHER NUMBER', )
	lorry_code = forms.CharField(label='LORRY CODE', max_length=6)
	trip = forms.IntegerField(label='NUMBER OF TRIPS', )
	challan_no = forms.CharField(label='CHALLAN NUMBER', max_length=20)
	buyer = forms.CharField(label='BUYER', max_length=50)
	supplier = forms.CharField(label='SUPPLIER', max_length=50)
	site_code = forms.CharField(label='SITE CODE', max_length=7)
	short_name = forms.CharField(label='ITEM', max_length=6)
	length = forms.DecimalField(label='LENGTH OF LORRY', max_digits=5, decimal_places=2)
	breadth = forms.DecimalField(label='BREADTH OF LORRY', max_digits=5, decimal_places=2)
	height = forms.DecimalField(label='HEIGHT OF LORRY', max_digits=5, decimal_places=2)
	quantity = forms.DecimalField(label='QUANTITY', max_digits=10, decimal_places=2)
	pur_rate = forms.DecimalField(label='PURCHASE RATE', max_digits=5, decimal_places=2)
	sale_rate = forms.DecimalField(label='SALE RATE', max_digits=5, decimal_places=2)