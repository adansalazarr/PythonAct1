import csv


# data = [{'name': 'John Doe', 'age': 30}, {'name': 'Jane Doe', 'age': 25}]
def write_list_of_dicts_to_csv(filename, data):
    with open(filename, 'w') as f:
        writer = csv.DictWriter(f, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)


# dict = { 'SKU': 'A123', ... }
def read_csv_to_dict(filename):
    with open(filename, 'r') as f:
        reader = csv.DictReader(f)
        return list(reader)
    
def update_grocery_data(sample_data, batch_data):
    for new_item in batch_data:
        found = False
        for item in sample_data:
            if item['SKU'] == new_item['SKU']:
                item['Quantity'] = str(int(item['Quantity']) + int(new_item['Quantity']))
                found = True
                break
        if not found:
            sample_data.append(new_item)
    return sample_data


# data = [0, 1, 2, 3]
def main():
    #data = read_csv_to_dict(filename)
    #for row in data:
        # print(row)
        # Print SKU
        #sku_value = row['SKU']
        # print("SKU=" + sku_value)
        #if sku_value == "A123":
            #row['Price'] = 99999999

    sample_data = read_csv_to_dict('sample_grocery.csv')
    batch_data = read_csv_to_dict('grocery_batch_1.csv')
    updated_data = update_grocery_data(sample_data, batch_data)

    # Guardar los cambios editados
    write_list_of_dicts_to_csv("grocery_db.csv", updated_data)



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()