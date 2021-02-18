import csv

with open('names.csv', 'r') as f:
    csv_reader = csv.DictReader(f)
    fieldnames = ['first_name', 'last_name',]

    with open('new_names.csv', 'w') as g:
        writer = csv.DictWriter(g, fieldnames=fieldnames, delimiter='|')
        writer.writeheader()
        # writer.writerow({'last_name': 'Sabanli', 'first_name': 'Idris', 'email': 'idris@gmail.com' })
        # writer.writerow({'last_name': 'Sabanli', 'first_name': 'Idris', 'email': 'idris@gmail.com' })
        # writer.writerow({'last_name': 'Sabanli', 'first_name': 'Idris', 'email': 'idris@gmail.com' })

        for row in csv_reader:
            # del row['email']
            writer.writerow(row)







# with open('names.csv', 'r') as f:
#     csv_reader = csv.reader(f)

#     with open('new_names.csv', 'w') as g:
#         csv_writer = csv.writer(g, delimiter=',')

#         for line in csv_reader:
#             csv_writer.writerow(line)