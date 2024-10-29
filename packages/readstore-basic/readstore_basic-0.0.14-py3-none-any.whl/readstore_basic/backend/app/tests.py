# readstore-basic/backend/app/pipelines.py

import datetime

from django.test import TestCase
from django.contrib.auth.models import User
from .models import AppUser
from .models import OwnerGroup
from .models import FqFile
from .models import ProjectAttachment
from .models import Project

import unittest

# Create your tests here.
class ExampleTestCase(TestCase):
    def setUp(self):

        user = User.objects.create(username='testuser',
                                    password='testpassword')
        
        owner_group = OwnerGroup.objects.create(name = 'group1',
                                                owner = user)
        
        app_user_1 = AppUser.objects.create(user = User.objects.create(username = 'hansi', password = 'hubi'),
                                            token = 'GAGAGAG',
                                            owner_group = owner_group)
        
        app_user_2 = AppUser.objects.create(user = User.objects.create(username = 'hansi22', password = 'hubi'),
                                            token = 'TATATATA',
                                            owner_group = owner_group)
        
        fq_file = FqFile.objects.create(name = 'file1',
                                        bucket = 'bucket1',
                                        key = 'key1',
                                        source_path = 'source1',
                                        qc_passed = True,
                                        read_type = 'R1',
                                        read_length = 200,
                                        num_reads = 250000,
                                        qc_phred_mean = 32.5,
                                        qc_phred = {'1': 32.5, '2': 33.5},
                                        size_mb = 200,
                                        staging = True,
                                        md5_checksum="123456",
                                        pipeline_version = 'pipeline1',
                                        owner = app_user_1.user)
        
        project = Project.objects.create(name = 'project1',
                                        description = 'description1',
                                        metadata = {'tag1': 'tag1'},
                                        dataset_metadata_keys = {'key1': None},
                                        owner_group = owner_group,
                                        owner = app_user_1.user)
        
        project_attachment = ProjectAttachment.objects.create(project = project,
                                                              body = b'body1',
                                                              owner = app_user_1.user,
                                                              name = 'name1',
                                                              description = 'description1',
                                                              path = 'path1/1',
                                                             size_mb = 200,
                                                             filetype = 'excel')
                                                              
        user.full_clean()
        owner_group.full_clean()
        app_user_1.full_clean()
        app_user_2.full_clean()
        fq_file.full_clean()
        project.full_clean()
        project_attachment.full_clean()
                                        
        # Upload
        
    def test_get(self):
        
        app_users = AppUser.objects.all()
        owner_group = OwnerGroup.objects.all()
        fq_files = FqFile.objects.all()
        project = Project.objects.all()
        project_attachments = ProjectAttachment.objects.all()
        
        print(app_users)
        print(owner_group)
        print(fq_files[0].read_type)
        print(project)
        print(project_attachments)
        
    
    def test_delete(self):
        
        FqFile.objects.filter(name='file1').delete()
        User.objects.filter(username__contains = 'hansi').delete()
        print("Gele")   
        OwnerGroup.objects.filter(name='group1').delete()
