from rest_framework import generics, viewsets
from django.shortcuts import get_object_or_404
from django.core.mail import send_mail
from django.utils.crypto import get_random_string
from django.contrib.auth.models import User, Group
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from rest_framework.decorators import action
from rest_framework import status
from django.contrib.auth import login, authenticate, logout
import secrets
import re
import json
from django.db.models import Q
from .encrypt_utils import encrypt, decrypt
from datetime import datetime, timedelta
from django.utils import timezone
import random
import decimal
import math
import string

def slugify(s):
    s = s.lower().strip()
    s = re.sub(r'[^\w\s-]', '', s)
    s = re.sub(r'[\s_-]+', '-', s)
    s = re.sub(r'^-+|-+$', '', s)
    return s
