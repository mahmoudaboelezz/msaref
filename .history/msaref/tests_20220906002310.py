from django.test import TestCase
from .models import Section, Total, Paid, Band

# Create tests for Paid , Total and Band, and Section
class PaidTestCase(TestCase):
    def setUp(self):
        self.section = Section.objects.create(name='Section 1')
        self.paid = Paid.objects.create(section=self.section, name='Paid 1', price=1000)
        self.band = Band.objects.create(name='Band 1', section=self.section)
        self.total = Total.objects.create(section=self.section, Total=1000)
        
    def test_paid(self):
        self.assertEqual(self.paid.name, 'Paid 1')
        self.assertEqual(self.paid.price, 1000)
        self.assertEqual(self.paid.residual, 1000)
        self.assertEqual(self.paid.paid_up, 0)
        self.assertEqual(self.paid.done, False)
        self.assertEqual(self.paid.section, self.section)
        self.assertEqual(self.paid.band_elm, None)
        
    def test_band(self):
        self.assertEqual(self.band.name, 'Band 1')
        self.assertEqual(self.band.section, self.section)
        self.assertEqual(self.band.paid_elm, None)
        
    def test_total(self):
        self.assertEqual(self.total.Total, 1000)
        self.assertEqual(self.total.section, self.section)
        self.assertEqual(self.total.residual_total, 1000)
        self.assertEqual(self.total.overall_total, 1000)
        
    def test_section(self):
        self.assertEqual(self.section.name, 'Section 1')
        
    def test_paid_save(self):
        self.paid.save()
        self.assertEqual(self.paid.residual, 1000)
        self.assertEqual(self.paid.done, False)
        self.assertEqual(self.paid.band_elm, None)
        
    def test_band_save(self):
        self.band.save()
        self.assertEqual(self.band.paid_elm, None)
        
    def test_total_save(self):
        self.total.save()
        self.assertEqual(self.total.residual_total, 1000)
        self.assertEqual(self.total.overall_total, 1000)
        
    def test_section_save(self):
        self.section.save()
        self.assertEqual(self.section.name, 'Section 1')
        
    def test_paid_update(self):
        self.paid.save()
        self.paid.paid_up = 1000
        self.paid.save()
        self.assertEqual(self.paid.residual, 0)
        self.assertEqual(self.paid.done, True)
        self.assertEqual(self.paid.band_elm, None)
        
    def test_band_update(self):
        self.band.save()
        
class BandTestCase(TestCase):
    def setUp(self):
        self.section = Section.objects.create(name='Section 1')
        receive_section = Section.objects.get(id=self.section.id)
        self.paid = Paid.objects.create(section=self.section, name='Paid 1', price=1000)
        receive_paid = Paid.objects.get(id=self.paid.id)
        self.band = Band.objects.create(name='Band 1', section=self.section, paid_elm=receive_paid)
        receive_band = Band.objects.get(id=self.band.id)
        self.total = Total.objects.create(section=self.section, Total=1000)
        
    def test_paid(self):
        self.assertEqual(self.paid.name, 'Paid 1')
        self.assertEqual(self.paid.price, 1000)
        self.assertEqual(self.paid.residual, 1000)
        self.assertEqual(self.paid.paid_up, 0)
        self.assertEqual(self.paid.done, False)
        self.assertEqual(self.paid.section, self.section)
        self.assertEqual(self.paid.band_elm, None)
        
    def test_band(self):
        self.assertEqual(self.band.name, 'Band 1')
        self.assertEqual(self.band.section, self.section)
        self.assertEqual(self.band.paid_elm, None)
        
    def test_total(self):
        self.assertEqual(self.total.Total, 1000)
        self.assertEqual(self.total.section, self.section)
        self.assertEqual(self.total.residual_total, 1000)
        self.assertEqual(self.total.overall_total, 1000)
        
    def test_section(self):
        self.assertEqual(self.section.name, 'Section 1')
        
    def test_paid_save(self):
        self.paid.save()
        self.assertEqual(self.paid.residual, 1000)
        self.assertEqual(self.paid.done, False)
        self.assertEqual(self.paid.band_elm, None)
        
    def test_band_save(self):
        self.band.save()
        self.assertEqual(self.band.paid_elm, None)
        
    def test_total_save(self):
        self.total.save()
        self.assertEqual(self.total.residual_total, 1000)
        self.assertEqual(self.total.overall_total, 1000)
        
    def test_section_save(self):
        self.section.save()
        self.assertEqual(self.section.name, 'Section 1')
        
    def test_paid_update(self):
        self.paid.save()
        self.paid.paid_up = 1000
        self.paid.save()
        self.assertEqual(self.paid.residual, 0)
        self.assertEqual(self.paid.done, True)
        self.assertEqual(self.paid.band_elm, None)
        
    def test_band_update(self):
        self.band.save()
        
class TotalTestCase(TestCase):
    def setUp(self):
        self.section = Section.objects.create(name='Section 1')
        self.paid = Paid.objects.create(section=self.section, name='Paid 1', price=1000)
        self.band = Band.objects.create(name='Band 1', section=self.section)
        self.total = Total.objects.create(section=self.section, Total=1000)
        
    def test_paid(self):
        self.assertEqual(self.paid.name, 'Paid 1')
        self.assertEqual(self.paid.price, 1000)
        self.assertEqual(self.paid.residual, 1000)
        self.assertEqual(self.paid.paid_up, 0)
        self.assertEqual(self.paid.done, False)
        self.assertEqual(self.paid.section, self.section)
        self.assertEqual(self.paid.band_elm, None)
        
    def test_band(self):
        self.assertEqual(self.band.name, 'Band 1')
        self.assertEqual(self.band.section, self.section)
        self.assertEqual(self.band.paid_elm, None)
        
    def test_total(self):
        self.assertEqual(self.total.Total, 1000)
        self.assertEqual(self.total.section, self.section)
        self.assertEqual(self.total.residual_total, 1000)
        self.assertEqual(self.total.overall_total, 1000)
        
    def test_section(self):
        self.assertEqual(self.section.name, 'Section 1')
        
    def test_paid_save(self):
        self.paid.save()
        self.assertEqual(self.paid.residual, 1000)
        self.assertEqual(self.paid.done, False)
        self.assertEqual(self.paid.band_elm, None)
        
    def test_band_save(self):
        self.band.save()
        self.assertEqual(self.band.paid_elm, None)
        
    def test_total_save(self):
        self.total.save()
        self.assertEqual(self.total.residual_total, 1000)
        self.assertEqual(self.total.overall_total, 1000)
        
    def test_section_save(self):
        self.section.save()
        self.assertEqual(self.section.name, 'Section 1')
        
    def test_paid_update(self):
        self.paid.save()
        self.paid.paid_up = 1000
        self.paid.save()
        self.assertEqual(self.paid.residual, 0)
        self.assertEqual(self.paid.done, True)
        self.assertEqual(self.paid.band_elm, None)
        
    def test_band_update(self):
        self.band.save()
