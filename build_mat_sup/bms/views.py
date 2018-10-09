from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy

from .models import ItemMaster, LorryMaster, BusinessPartnerMaster, StateMaster, SiteMaster, BusinessGroupMaster, Transaction, ItemGroupMaster, UnitOfMeasureMaster, Quotation, QuotationDetails, CompanyMaster
# Create your views here.
from .forms import ItemForm, ItemGroupForm, LorryForm, BusinessPartnerForm, SiteForm, BusinessGroupForm, TransactionForm, UOMForm, QuotationForm, QuotationDetailsForm, CompanyForm

from django.forms.formsets import formset_factory
from .filters import TransactionFilter

#PDF
from django.core.files.storage import FileSystemStorage
from django.template.loader import render_to_string

from weasyprint import HTML


#Index
def index(request):
	all_items = ItemMaster.objects.all()
	context = {'all_items':all_items}
	return render(request, 'bms/index.html', context)

#ItemGroupMaster
def itemgroup(request):
	all_items = ItemGroupMaster.objects.all()
	if request.method == 'POST':
		form_data = request.POST.copy()
		form = ItemGroupForm(data=form_data)
		if form.is_valid():
			item_group = form.cleaned_data.get('item_group')
			item_group_name = form.cleaned_data.get('item_group_name')
			gst_rate = form.cleaned_data.get('gst_rate')
			item_group_data = ItemGroupMaster(item_group=item_group, item_group_name=item_group_name, gst_rate=gst_rate)
			item_group_data.save() 
			form = ItemGroupForm()
	else:
		form = ItemGroupForm()
		
	return render(request, 'bms/itemgroupmaster.html', { "form": form, "view":all_items })


def itemgroupview(request):
	all_items = ItemGroupMaster.objects.all()

	return render(request, 'bms/itemgroupmasterview.html', {"view": all_items})

def itgrdelete(request, pk):
	it = ItemGroupMaster.objects.values_list('pk', flat=True)
	item = get_object_or_404(ItemGroupMaster, pk=pk)    
	if request.method=='POST':
		item.delete()
		return HttpResponse('<script type="text/javascript">window.close()</script>')
	return render(request, 'bms/item_delete.html', {'object':item, 'it':it})

#ItemMaster
def items(request):
	all_items = ItemMaster.objects.all()
	it = ItemGroupMaster.objects.values_list('pk', flat=True)
	um = UnitOfMeasureMaster.objects.all()
	if request.method == 'POST':
		form_data = request.POST.copy()
		form = ItemForm(data=form_data)
		if form.is_valid():
			short_name = form.cleaned_data.get('short_name')
			item_name = form.cleaned_data.get('item_name')
			unit_measure = form.cleaned_data.get('unit_measure')
			item_group = form.cleaned_data.get('item_group')
			item_data = ItemMaster(short_name=short_name, item_name=item_name, unit_measure=unit_measure, item_group=item_group)
			item_data.save() 
			form = ItemForm()
	else:
		form = ItemForm()
	
	return render(request, 'bms/itemmaster.html', { "it":it, "um":um, "form": form, "view":all_items })


def itemsview(request):
	all_items = ItemMaster.objects.all()
	it = ItemGroupMaster.objects.values_list('pk', flat=True)
	um = UnitOfMeasureMaster.objects.all()

	return render(request, 'bms/itemmasterview.html', {"it": it, "um": um, "view": all_items})

def itdelete(request, pk):
	it = ItemMaster.objects.values_list('pk', flat=True)
	item = get_object_or_404(ItemMaster, pk=pk)    
	if request.method=='POST':
		item.delete()
		return HttpResponse('<script type="text/javascript">window.close()</script>')
	return render(request, 'bms/item_delete.html', {'object':item, 'it':it})

#LorryMaster
def lorry(request):
	all_items = LorryMaster.objects.all()
	if request.method == 'POST':
		form_data = request.POST.copy()
		form = LorryForm(data=form_data)
		if form.is_valid():
			lorry_code = form.cleaned_data.get('lorry_code')
			lorry_no = form.cleaned_data.get('lorry_no')
			driver = form.cleaned_data.get('driver')
			contact = form.cleaned_data.get('contact')
			tax_date = form.cleaned_data.get('tax_date')
			puc_date = form.cleaned_data.get('puc_date')
			permit_date = form.cleaned_data.get('permit_date')
			insur_date = form.cleaned_data.get('insur_date')
			length = form.cleaned_data.get('length')
			breadth = form.cleaned_data.get('breadth')
			lorry_data = LorryMaster(lorry_code=lorry_code, lorry_no=lorry_no, driver=driver, contact=contact, tax_date=tax_date, puc_date=puc_date, permit_date=permit_date, insur_date=insur_date, length=length, breadth=breadth)
			lorry_data.save()
			form = LorryForm()
	else:
		form = LorryForm()
	
	return render(request, 'bms/lorrymaster.html', { "form": form, "view":all_items })


def lorryview(request):
	all_items = LorryMaster.objects.all()

	return render(request, 'bms/lorrymasterview.html', {"view": all_items})

def lorrydelete(request, pk):
	it = LorryMaster.objects.values_list('pk', flat=True)
	item = get_object_or_404(LorryMaster, pk=pk)    
	if request.method=='POST':
		item.delete()
		return HttpResponse('<script type="text/javascript">window.close()</script>')
	return render(request, 'bms/item_delete.html', {'object':item, 'it':it})

#BusinessPartnerMaster
def bp(request):
	all_items = BusinessPartnerMaster.objects.all()
	it = StateMaster.objects.all()
	if request.method == 'POST':
		form_data = request.POST.copy()
		form = BusinessPartnerForm(data=form_data)
		if form.is_valid():
			name = form.cleaned_data.get('name')
			code = form.cleaned_data.get('code')
			address_1 = form.cleaned_data.get('address_1')
			address_2 = form.cleaned_data.get('address_2')
			city = form.cleaned_data.get('city')
			pin = form.cleaned_data.get('pin')
			state_code = form.cleaned_data.get('state_code')
			gst_no = form.cleaned_data.get('gst_no')
			pan_aadhar_no = form.cleaned_data.get('pan_aadhar_no')
			bp_type = form.cleaned_data.get('bp_type')
			business_partner_data = BusinessPartnerMaster(name=name, code=code, address_1=address_1, address_2=address_2, city=city, pin=pin, state_code=state_code, gst_no=gst_no, pan_aadhar_no=pan_aadhar_no, bp_type=bp_type)
			business_partner_data.save()
			form = BusinessPartnerForm()
	else:
		form = BusinessPartnerForm()
	
	return render(request, 'bms/businesspartnermaster.html', { "form": form, "view":all_items, "it":it })


def bpview(request):
	all_items = BusinessPartnerMaster.objects.all()
	it = StateMaster.objects.all()

	return render(request, 'bms/businesspartnermasterview.html', {"view": all_items, "it": it})

def bdelete(request, pk):
	it = BusinessPartnerMaster.objects.values_list('pk', flat=True)
	item = get_object_or_404(BusinessPartnerMaster, pk=pk)    
	if request.method=='POST':
		item.delete()
		return HttpResponse('<script type="text/javascript">window.close()</script>')
	return render(request, 'bms/item_delete.html', {'object':item, 'it':it})

#BusinessGroupMaster
def businessgroup(request):
	all_items = BusinessGroupMaster.objects.all()
	if request.method == 'POST':
		form_data = request.POST.copy()
		form = BusinessGroupForm(data=form_data)
		if form.is_valid():
			group_code = form.cleaned_data.get('group_code')
			group_name = form.cleaned_data.get('group_name')
			group_head = form.cleaned_data.get('group_head')
			contact_no = form.cleaned_data.get('contact_no')
			business_group_data = BusinessGroupMaster(group_code=group_code, group_name=group_name, group_head=group_head, contact_no=contact_no)
			business_group_data.save()
			form = BusinessGroupForm()
	else:
		form = BusinessGroupForm()
	
	return render(request, 'bms/businessgroupmaster.html', { "form": form, "view":all_items })


def businessgroupview(request):
	all_items = BusinessGroupMaster.objects.all()

	return render(request, 'bms/businessgroupmasterview.html', {"view": all_items})

def bgroupdelete(request, pk):
	it = BusinessGroupMaster.objects.values_list('pk', flat=True)
	item = get_object_or_404(BusinessGroupMaster, pk=pk)    
	if request.method=='POST':
		item.delete()
		return HttpResponse('<script type="text/javascript">window.close()</script>')
	return render(request, 'bms/item_delete.html', {'object':item, 'it':it})


#StateMaster
def state(request):
	all_items = StateMaster.objects.all()
	return render(request, 'bms/statemaster.html', { 'all_items':all_items })

#SiteMaster
def sitemaster(request):
	all_items = SiteMaster.objects.all()
	it = StateMaster.objects.all()
	if request.method == 'POST':
		form_data = request.POST.copy()
		form = SiteForm(data=form_data)
		if form.is_valid():
			site_code = form.cleaned_data.get('site_code')
			site_name = form.cleaned_data.get('site_name')
			address_1 = form.cleaned_data.get('address_1')
			address_2 = form.cleaned_data.get('address_2')
			city = form.cleaned_data.get('city')
			pin = form.cleaned_data.get('pin')
			state_code = form.cleaned_data.get('state_code')
			gst_no = form.cleaned_data.get('gst_no')
			contact_person = form.cleaned_data.get('contact_person')
			site_contact = form.cleaned_data.get('site_contact')
			site_data = SiteMaster(site_code=site_code, site_name=site_name, address_1=address_1, address_2=address_2, city=city, pin=pin, state_code=state_code, gst_no=gst_no, contact_person=contact_person, site_contact=site_contact)
			site_data.save()
			form = SiteForm()
	else:
		form = SiteForm()
	
	return render(request, 'bms/sitemaster.html', { "form": form, "view":all_items, "it":it })


def sitemasterview(request):
	all_items = SiteMaster.objects.all()
	it = StateMaster.objects.all()

	return render(request, 'bms/sitemasterview.html', {"view": all_items, "it": it})

def sitedelete(request, pk):
	it = SiteMaster.objects.values_list('pk', flat=True)
	item = get_object_or_404(SiteMaster, pk=pk)    
	if request.method=='POST':
		item.delete()
		return HttpResponse('<script type="text/javascript">window.close()</script>')
	return render(request, 'bms/item_delete.html', {'object':item, 'it':it})

#Unit Of Measure
def uom(request):
	all_items = UnitOfMeasureMaster.objects.all()
	if request.method == 'POST':
		form_data = request.POST.copy()
		form = UOMForm(data=form_data)
		if form.is_valid():
			uom_code = form.cleaned_data.get('uom_code')
			uom_name = form.cleaned_data.get('uom_name')
			unit_of_measure_data = UnitOfMeasureMaster(uom_code=uom_code, uom_name=uom_name)
			unit_of_measure_data.save()
			form = UOMForm()
	else:
		form = UOMForm()
	
	return render(request, 'bms/uom.html', { "form": form, "view":all_items })


def uomview(request):
	all_items = UnitOfMeasureMaster.objects.all()

	return render(request, 'bms/uomview.html', {"view": all_items})

def uomdelete(request, pk):
	it = UnitOfMeasureMaster.objects.values_list('pk', flat=True)
	item = get_object_or_404(UnitOfMeasureMaster, pk=pk)    
	if request.method=='POST':
		item.delete()
		return HttpResponse('<script type="text/javascript">window.close()</script>')
	return render(request, 'bms/item_delete.html', {'object':item, 'it':it})

#Quotation
def quote(request):
	all_items = Quotation.objects.all()
	bp_buyer = BusinessPartnerMaster.objects.filter(bp_type='buyer')
	group = BusinessGroupMaster.objects.all()
	if request.method == 'POST':
		form_data = request.POST.copy()
		form = QuotationForm(data=form_data)
		if form.is_valid():
			quot_no = form.cleaned_data.get('quot_no')
			quot_dt = form.cleaned_data.get('quot_dt')
			frm_dt = form.cleaned_data.get('frm_dt')
			to_dt = form.cleaned_data.get('to_dt')
			buyer_code = form.cleaned_data.get('buyer_code')
			group_code = form.cleaned_data.get('group_code')
			quotation_data = Quotation(quot_no=quot_no, quot_dt=quot_dt, frm_dt=frm_dt, to_dt=to_dt, buyer_code=buyer_code, group_code=group_code)
			quotation_data.save()
			form = QuotationForm()
	else:
		form = QuotationForm()
	
	return render(request, 'bms/quotation.html', { "form": form, "view":all_items, 'bp_buyer':bp_buyer, 'group':group })


def quoteview(request):
	all_items = Quotation.objects.all()
	bp_buyer = BusinessPartnerMaster.objects.filter(bp_type='buyer')
	group = BusinessGroupMaster.objects.all()

	return render(request, 'bms/quotationview.html', {"view": all_items, 'bp_buyer': bp_buyer, 'group': group})

def quotedelete(request, pk):
	it = Quotation.objects.values_list('pk', flat=True)
	item = get_object_or_404(Quotation, pk=pk)    
	if request.method=='POST':
		item.delete()
		return HttpResponse('<script type="text/javascript">window.close()</script>')
	return render(request, 'bms/item_delete.html', {'object':item, 'it':it})

#Quotation Details
def quotedetails(request):
	QuoteDetailsFormSet = formset_factory(QuotationDetailsForm, extra=5)
	if request.method == 'POST':
		formset = QuoteDetailsFormSet(request.POST)
		if formset.is_valid():
			for form in formset:
				quot_no = form.cleaned_data.get('quot_no')
				site_code = form.cleaned_data.get('site_code')
				short_name = form.cleaned_data.get('short_name')
				rate = form.cleaned_data.get('rate')
				quotation_details_data = QuotationDetails(quot_no=quot_no, site_code=site_code, short_name=short_name, rate=rate)
				quotation_details_data.save()

			formset = QuoteDetailsFormSet()
	else:
		formset = QuoteDetailsFormSet()

	return render(request, 'bms/quotationdetails.html', {'formset': formset})

	#all_items = QuotationDetails.objects.all()
#	quote = Quotation.objects.all()
#	site = SiteMaster.objects.all()
#	item = ItemMaster.objects.all()
#	if request.method == 'POST':
#		form_data = request.POST.copy()
#		form = QuotationDetailsForm(data=form_data)
#		if form.is_valid():
#			quot_no = form.cleaned_data.get('quot_no')
#			site_code = form.cleaned_data.get('site_code')
#			short_name = form.cleaned_data.get('short_name')
#			rate = form.cleaned_data.get('rate')
#			quotation_details_data = QuotationDetails(quot_no=quot_no, site_code=site_code, short_name=short_name, rate=rate)
#			quotation_details_data.save()
#			form = QuotationDetailsForm()
#	else:
#		form = QuotationDetailsForm()
	
#	return render(request, 'bms/quotationdetails.html', { "form": form, "view":all_items, 'quote':quote, 'site':site, 'item':item })


def quotedetailsview(request):
	all_items = QuotationDetails.objects.all()
	quote = Quotation.objects.all()
	site = SiteMaster.objects.all()
	item = ItemMaster.objects.all()

	return render(request, 'bms/quotationdetailsview.html', {"view": all_items, 'quote': quote, 'site': site, 'item': item})

def quotedetailsdelete(request, pk):
	it = QuotationDetails.objects.values_list('pk', flat=True)
	item = get_object_or_404(QuotationDetails, pk=pk)    
	if request.method=='POST':
		item.delete()
		return HttpResponse('<script type="text/javascript">window.close()</script>')
	return render(request, 'bms/item_delete.html', {'object':item, 'it':it})

#CompanyMaster
def companymaster(request):
	all_items = CompanyMaster.objects.all()
	it = CompanyMaster.objects.all()
	st = StateMaster.objects.all()
	if request.method == 'POST':
		form_data = request.POST.copy()
		form = CompanyForm(data=form_data)
		if form.is_valid():
			company_code = form.cleaned_data.get('company_code')
			comp_name = form.cleaned_data.get('comp_name')
			address_1 = form.cleaned_data.get('address_1')
			address_2 = form.cleaned_data.get('address_2')
			city = form.cleaned_data.get('city')
			pin = form.cleaned_data.get('pin')
			state_code = form.cleaned_data.get('state_code')
			phone = form.cleaned_data.get('phone')
			mobile = form.cleaned_data.get('mobile')
			gst_no = form.cleaned_data.get('gst_no')
			pan_no = form.cleaned_data.get('pan_no')
			bank_name = form.cleaned_data.get('bank_name')
			ac_no = form.cleaned_data.get('ac_no')
			ifsc_code = form.cleaned_data.get('ifsc_code')
			jurisdiction = form.cleaned_data.get('jurisdiction')
			interest_rate = form.cleaned_data.get('interest_rate')
			company_data = CompanyMaster(company_code=company_code, comp_name=comp_name, address_1=address_1, address_2=address_2, city=city, pin=pin, state_code=state_code, phone=phone, mobile=mobile, gst_no=gst_no, pan_no=pan_no,bank_name=bank_name, ac_no=ac_no, ifsc_code=ifsc_code, jurisdiction=jurisdiction, interest_rate=interest_rate)
			company_data.save()
			form = CompanyForm()
	else:
		form = CompanyForm()

	return render(request, 'bms/companymaster.html', { "form":form, "view":all_items, "it":it, "st":st })

def companymasterview(request):
	all_items = CompanyMaster.objects.all()
	it = CompanyMaster.objects.all()
	st = StateMaster.objects.all()

	return render(request, 'bms/companymasterview.html', { "view":all_items, "it":it, "st":st })

def companydelete(request, pk):
	it = CompanyMaster.objects.values_list('pk', flat=True)
	item = get_object_or_404(CompanyMaster, pk=pk)   
	if request.method=='POST':
		item.delete()
		return HttpResponse('<script type="text/javascript">window.close()</script>')
	return render(request, 'bms/item_delete.html', {'object':item, 'it':it})

#Transaction
def transact(request):
	all_items = Transaction.objects.all()
	transaction_filter = TransactionFilter(request.GET, queryset=all_items)
	tl = LorryMaster.objects.values_list('pk', flat=True)
	ts = SiteMaster.objects.values_list('pk', flat=True)
	tshort = ItemMaster.objects.all()
	bp_buyer = BusinessPartnerMaster.objects.filter(bp_type='buyer')
	bp_supplier = BusinessPartnerMaster.objects.filter(bp_type='supplier')
	if request.method == 'POST':
		form_data = request.POST.copy()
		form = TransactionForm(data=form_data)
		if form.is_valid():
			tr_date = form.cleaned_data.get('tr_date')
			vr_no = form.cleaned_data.get('vr_no')
			lorry_code = form.cleaned_data.get('lorry_code')
			trip = form.cleaned_data.get('trip')
			challan_no = form.cleaned_data.get('challan_no')
			buyer = form.cleaned_data.get('buyer')
			supplier = form.cleaned_data.get('supplier')
			site_code = form.cleaned_data.get('site_code')
			short_name = form.cleaned_data.get('short_name')
			pur_rate = form.cleaned_data.get('pur_rate')
			sale_rate = form.cleaned_data.get('sale_rate')
			length = form.cleaned_data.get('length')
			breadth = form.cleaned_data.get('breadth')
			height = form.cleaned_data.get('height')
			quantity = form.cleaned_data.get('quantity')
			transaction_data = Transaction(tr_date=tr_date, vr_no=vr_no, lorry_code=lorry_code, trip=trip, challan_no=challan_no, buyer=buyer, supplier=supplier, site_code=site_code, short_name=short_name, length=length, breadth=breadth, height=height, quantity=quantity, pur_rate=pur_rate, sale_rate=sale_rate)
			transaction_data.save()
			form = TransactionForm()
	else:
		form = TransactionForm()
	
	return render(request, 'bms/transaction.html', { "lorry_code":tl, "site_code":ts, "short_name":tshort, "form": form, "view":all_items, 'filter':transaction_filter, 'bp_buyer':bp_buyer, 'bp_supplier':bp_supplier })


def transactview(request):
	all_items = Transaction.objects.all()
	transaction_filter = TransactionFilter(request.GET, queryset=all_items)
	tl = LorryMaster.objects.values_list('pk', flat=True)
	ts = SiteMaster.objects.values_list('pk', flat=True)
	tshort = ItemMaster.objects.all()
	bp_buyer = BusinessPartnerMaster.objects.filter(bp_type='buyer')
	bp_supplier = BusinessPartnerMaster.objects.filter(bp_type='supplier')

	return render(request, 'bms/transactionview.html', {"lorry_code": tl, "site_code": ts, "short_name": tshort, "view": all_items,
				   'filter': transaction_filter, 'bp_buyer': bp_buyer, 'bp_supplier': bp_supplier})

def tdelete(request, pk):
	it = Transaction.objects.values_list('pk', flat=True)
	item = get_object_or_404(Transaction, pk=pk)    
	if request.method=='POST':
		item.delete()
		return HttpResponse('<script type="text/javascript">window.close()</script>')
	return render(request, 'bms/item_delete.html', {'object':item, 'it':it})


# PDF
def html_to_pdf_view(request):
	all_items = Transaction.objects.all()
	transaction_filter = TransactionFilter(request.GET, queryset=all_items)
	html_string = render_to_string('bms/pdf_template.html', {'all_items': transaction_filter})
	HTML(string=html_string).write_pdf(target='/tmp/mypdf.pdf')
	#HTML('http://localhost:8000/bms/transactionview/#Print').write_pdf(target='/tmp/mypdf.pdf')

	fs = FileSystemStorage('/tmp')
	with fs.open('mypdf.pdf') as pdf:
		response = HttpResponse(pdf, content_type='application/pdf')
		response['Content-Disposition'] = 'attachment; filename="mypdf.pdf"'
		return response

	return response

#Export CSV
import csv

def export_transactions_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="transactions.csv"'

    writer = csv.writer(response)
    writer.writerow(['Transaction Date', 'Voucher Number', 'Lorry Code', 'Number of Trips', 'Challan Number', 'Buyer', 'Supplier', 'Site Code', 'Item Name', 'Purchase Rate', 'Sale Rate', 'Length of Lorry', 'Breadth of Lorry', 'Height of Lorry', 'Quantity'])

    transactions = Transaction.objects.all().values_list('tr_date', 'vr_no', 'lorry_code', 'trip', 'challan_no', 'buyer', 'supplier', 'site_code', 'short_name', 'length', 'breadth', 'height', 'quantity', 'pur_rate', 'sale_rate')
    for transaction in transactions:
        writer.writerow(transaction)

    return response