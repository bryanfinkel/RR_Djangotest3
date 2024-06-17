import csv
from django.core.management.base import BaseCommand
from mymap.models import Schools  # Adjust the import to your app name

class Command(BaseCommand):
    help = 'Update Schools with stage_number and stage_name from CSV'

    def handle(self, *args, **kwargs):
        stages_data = {}
        csv_path = '/Users/bryanfinkel/Desktop/PROGRAM/LEARNING/PROJECTS/djangotest3/mymap/stages_table.csv'  # Adjust the path as needed

        try:
            with open(csv_path, 'r') as file:
                reader = csv.DictReader(file)
                headers = reader.fieldnames
                self.stdout.write(self.style.SUCCESS(f'CSV headers: {headers}'))

                # Print the first few rows for inspection
                for i, row in enumerate(reader):
                    if i < 5:  # Adjust the number of rows to print as needed
                        self.stdout.write(self.style.SUCCESS(f'Row {i}: {row}'))
                    stages_data[int(row['level'])] = {
                        'stage_number': int(row['stage_number']),
                        'stage_name': row['stage_name']
                    }

        except FileNotFoundError:
            self.stdout.write(self.style.ERROR(f'File not found: {csv_path}'))
            return
        except KeyError as e:
            self.stdout.write(self.style.ERROR(f'KeyError: {e}. Row data: {row}'))
            return
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error reading CSV file: {str(e)}'))
            return
        
        for school in Schools.objects.all():
            if school.level in stages_data:
                school.stage_number = stages_data[school.level]['stage_number']
                school.stage_name = stages_data[school.level]['stage_name']
                school.save()
        
        self.stdout.write(self.style.SUCCESS('Successfully updated Schools with stages data'))
