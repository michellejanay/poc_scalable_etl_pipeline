import csv

def extract_csv(filename):
    extracted_data = []
#open the csv file
    with open(filename,mode='r', newline= '', encoding= 'utf-8') as file:
        headers = ['Timestamp','location','customer_name','item_purchased','total_amount','payment_method','card_num']
        csv_reader = csv.DictReader(file, fieldnames=headers)
        for row in csv_reader:
            extracted_data.append(row)
        return extracted_data










    
