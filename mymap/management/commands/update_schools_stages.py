from django.core.management.base import BaseCommand
from mymap.models import Schools

class Command(BaseCommand):
    help = 'Update stage_number and stage_name for primary schools'

    def handle(self, *args, **kwargs):
        nursery_schools = Schools.objects.filter(Level__in=[
                                                 'ECD/PRE-PRIMARY SCHOOL',
                                                 'PRE-PRIMARY SCHOOL',
                                                 'PRE',
                                                 'PRE-PRIMARY']
                                                 )
        nursery_counter = 0
        for school in nursery_schools:
            if school.stage_number != 1:
                nursery_counter += 1
                school.stage_number = 1
                school.stage_name = "Nursery"
                school.save()
            else:
                pass
        self.stdout.write(self.style.SUCCESS('Successfully updated {} nursery schools'.format(nursery_counter)))

        primary_schools = Schools.objects.filter(Level='PRIMARY SCHOOL')
        primary_counter = 0
        for school in primary_schools:
            if school.stage_number != 2:
                primary_counter += 1
                school.stage_number = 2
                school.stage_name = "Primary"
                school.save()
            else:
                pass
        self.stdout.write(self.style.SUCCESS('Successfully updated {} primary schools'.format(primary_counter)))

