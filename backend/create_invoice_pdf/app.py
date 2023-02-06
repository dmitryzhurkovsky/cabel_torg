import jinja2
import pdfkit
from  num2words import num2words
from datetime import datetime
import locale
import sys

##########################

     # VARIABLES

##########################
invoice_number = '100-C'
today_date = datetime.today().strftime("%d %b, %Y")
day = datetime.today().strftime("%d")
month = datetime.today().strftime("%B")
year = datetime.today().strftime("%Y")
# customer_credential = ОАО "ГОТТЦ "Гарант", УНП 500044457, 230002. г. Гродно. ул. Врублевского, 86А., р/с BY25BELB30121400750250226000 в банке ОАО "Банк БелВЭБ"
# БИК BELBBY2X
print(datetime.today().strftime("%m"))
customer_name = 'ОАО "ГОТТЦ "Гарант"'
customer_unp = "УНП 500044457"
customer_address = "230002. г. Гродно. ул. Врублевского, 86А."
customer_IBAN = "BY25BELB30121400750250226000"
customer_bank ='ОАО "Банк БелВЭБ"'
customer_BIK = "BELBBY2X"

customer_credential  = customer_name + ', ' + customer_unp + ', ' + customer_address + ', ' + customer_IBAN + 'в банке ' +  customer_bank + ', ' + customer_BIK

dogovor_number = str(day)+'/'+datetime.today().strftime("%m")+' от '+str(today_date)
final_price_text = num2words(325.5, lang='ru')

context = {'invoice_number':invoice_number, 'today_date': today_date, 'month':month, 'year':year,
           'customer_name':customer_name, 'customer_credential':customer_credential, 'dogovor_number':dogovor_number, 'final_price_text':final_price_text

           }

template_loader = jinja2.FileSystemLoader('./')
template_env = jinja2.Environment(loader=template_loader)

html_template = 'invoice.html'
template = template_env.get_template(html_template)
output_text = template.render(context)

config = pdfkit.configuration(wkhtmltopdf='/usr/bin/wkhtmltopdf')
output_pdf = 'invoice.pdf'

options = {
    'page-size': 'Letter',
    'margin-top': '0.75in',
    'margin-right': '0.75in',
    'margin-bottom': '0.75in',
    'margin-left': '0.75in',
    'encoding': "UTF-8",
    'no-outline': None
}

pdfkit.from_string(output_text, output_pdf, configuration=config, css='style.css', options=options)