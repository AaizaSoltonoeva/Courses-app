from django.test import TestCase
from django.urls import reverse
from app.models import *


class CourseModelTest(TestCase):

    def setUp(self):
        self.category = Category.objects.create(name='Name', imgpath='pict.jpg')

    def test_course(self):
        course = Course.objects.create(name='English Zone', description='learn english', category=self.category, logo='logo.jpg',)
        branch = Branch.objects.create(latitude='12.12', longitude='14.14', address='street Manas,1', course=course,)
        contact = Contact.objects.create(type=1, value='+996777878787', course=course,)

        courses = Course.objects.all()
        self.assertEqual(len(courses), 1)
        self.assertEqual(self.category.name, 'Name')
        self.assertEqual(course.name, 'English Zone')
        self.assertEqual(course.logo, 'logo.jpg')
        self.assertEqual(branch.latitude, '12.12')
        self.assertEqual(contact.type, 1)
        self.assertEqual(contact.value, '+996777878787')

    def test_view_course(self):
        response = self.client.get('/course/')
        self.assertEqual(response.status_code, 200)
    """def test_get_course(self):
        response = self.client.post('/course/', self.course, format='json')
        self.assertEqual(response.status_code, 200)"""

    # def test_post_a_course(self):
    #     response = self.client.post('/course/')
    #     self.assertEqual(response.status_code, 200)

    def test_should_return_list_od_courses(self):
        name = 'English Zone'
        description = 'learn english'
        logo = 'logo.jpg'
        course = Course.objects.create(name=name, description=description, category=self.category,
                                       logo=logo, )
        response = self.client.get('/course/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data[0]['id'], course.id)
        self.assertEqual(response.data[0]['name'], name)
        self.assertEqual(response.data[0]['description'], description)

    def test_should_return_404_if_url_doesnt_exist(self):
        response = self.client.get('incoreect_url')
        self.assertEqual(response.status_code, 404)

    def test_should_create_course_if_data_is_valid(self):
        data = {
            "name": "English Zone",
            "description": "learn english",
            "category": self.category.id,
            "logo": "logo.jpg",
            "contacts": [
                {
                    "type": 3,
                    "value": "aaizasoltonoeva@gmail.com"
                }
            ],
            "branches": [
                {
                    "latitude": "56.66",
                    "longitude": "23",
                    "address": "street Manas,1"
                }
            ]
        }

        response = self.client.post('/course/', data=data)
        print(response.data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data['name'], data['name'])
        self.assertEqual(response.data['description'], data['description'])
        self.assertEqual(response.data['category'], self.category.id)
        self.assertEqual(response.data['logo'], data['logo'])

    def test_should_delete_by_id(self):
        name = 'English Zone'
        description = 'learn english'
        logo = 'logo.jpg'
        course = Course.objects.create(name=name, description=description, category=self.category,
                                       logo=logo, )
        response = self.client.delete('/course/'+str(course.id) +'/')
        self.assertEqual(response.status_code, 204)
        self.assertEqual(response.data, None)



# TODO http status codes



















