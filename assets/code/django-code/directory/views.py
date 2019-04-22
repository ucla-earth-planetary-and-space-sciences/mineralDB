# Create your views here.
from django.template import Context, loader
from django.views.generic import TemplateView
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse, Http404
from django.shortcuts import render_to_response, get_object_or_404
from directory.models import DepartmentMember, Alumnus, BoardMember
from research_areas.models import *


def staff_index(request):
    try:
        staff_list = DepartmentMember.objects.all().filter(is_visible=True, user_role='Staff').order_by('last_name')
    except ObjectDoesNotExist:
        raise Http404
    return render_to_response('directory/staff-index.html', {'object_list': staff_list})


def staff_detail(request, staff_id):
    try:
        staff_detail = DepartmentMember.objects.get(pk=staff_id, user_role='Staff', is_visible=True)
    except ObjectDoesNotExist:
        raise Http404
    return render_to_response('directory/staff-detail.html', {'object_detail': staff_detail})


def researcher_index(request):
    try:
        researcher_list = DepartmentMember.objects.all().filter(is_visible=True, user_role='Researcher').order_by('last_name')
    except ObjectDoesNotExist:
        raise Http404
    return render_to_response('directory/researcher-index.html', {'object_list': researcher_list})


def researcher_detail(request, researcher_id):
    try:
        researcher_detail = DepartmentMember.objects.get(pk=researcher_id,user_role='Researcher' ,is_visible=True)
    except ObjectDoesNotExist:
        raise Http404
    return render_to_response('directory/researcher-detail.html', {'object_detail': researcher_detail})


def postdoc_index(request):
    try:
        postdoc_list = DepartmentMember.objects.all().filter(is_visible=True, user_role='Postdoc').order_by('last_name')
    except ObjectDoesNotExist:
        raise Http404
    return render_to_response('directory/postdoc-index.html', {'object_list': postdoc_list})


def postdoc_detail(request, postdoc_id):
    try:
        postdoc_detail = DepartmentMember.objects.get(pk=postdoc_id,is_visible=True)
    except ObjectDoesNotExist:
        raise Http404
    return render_to_response('directory/postdoc-detail.html', {'object_detail': postdoc_detail})


def student_index(request):
    try:
        student_list = DepartmentMember.objects.all().filter(is_visible=True, user_role='Student').order_by('last_name')
    except ObjectDoesNotExist:
        raise Http404
    return render_to_response('directory/student-index.html', {'object_list': student_list})


def student_detail(request, student_id):
    try:
        student_detail = DepartmentMember.objects.get(pk=student_id, user_role='student', is_visible=True)
    except ObjectDoesNotExist:
        raise Http404
    return render_to_response('directory/student-detail.html', {'object_detail': student_detail})


def faculty_index(request):
    try:
        faculty_list = DepartmentMember.objects.filter(is_visible=True, user_role='Faculty').exclude( title__icontains='emerit').order_by('last_name')
        emeriti_list = DepartmentMember.objects.filter(is_visible=True, user_role='Faculty', title__icontains='emerit').order_by('last_name')
    except ObjectDoesNotExist:
        raise Http404
    return render_to_response('directory/faculty-index.html', {'object_list': faculty_list, 'emeriti_list':emeriti_list})


def faculty_detail(request, faculty_id):
    try:
        faculty_detail = get_object_or_404(DepartmentMember, pk=faculty_id, is_visible=True, user_role='Faculty')
    except ObjectDoesNotExist:
        raise Http404
    return render_to_response('directory/faculty-detail.html', {'object_detail': faculty_detail})

# this is the view for the alumni information page.
def alumni_index(request):
    # because we have a lot of diff titles, this list will all populate the "research or staff scientist" counter
    researcher_count_terms = [
        'Assistant Research Geologist & Rock Lab Manager',
        'Geologist',
        'Planetary Scientist',
        'Researcher',
        'Staff Scientist',
        'Senior Scientist',
        'Scientist',
        'Research Scientist',
        'Senior Project Geologist',
        'Project Geologist',
        'Associate Research Scientist',
        'Scientific Staff',
        'Research Geophysicist',
        'Scientist, Solid Earth Group',
        'Senior Research Scientist',
        'Geophysicist',
        'Assistant Researcher',
        'Research Associate',
        'Senior Staff Geologist',
        'Geologist II',
        'Physicist',
        'Research Astrophysicist',
        'Senior Geologist',
        'Consulting Geologist',
        'Geochronologist',
    ]
    try:
        alumni_list = Alumnus.objects.all().order_by('-year_graduated', 'last_name')
        alumni_total_count = alumni_list.count()
        professor_count = alumni_list.filter(title__icontains='professor').count()
        researcher_count = alumni_list.filter(title__in=researcher_count_terms).count()
        nasa_count = alumni_list.filter(institution__icontains='nasa').count()
        postdoc_count = alumni_list.filter(title__icontains='post').count()
        lecturer_count = alumni_list.filter(title__icontains='lecturer').count()
        instructor_count = alumni_list.filter(title__icontains='instructor').count()
        phd_count = alumni_list.filter(title__icontains='phd').count()
    except Alumnus.DoesNotExist:
        raise Http404
    return render_to_response('directory/alumni-index.html', {
        'alumni_list': alumni_list,
        'alumni_total_count': alumni_total_count,
        'professor_count': professor_count,
        'researcher_count': researcher_count,
        'nasa_count': nasa_count,
        'postdoc_count': postdoc_count,
        'lecturer_count': lecturer_count,
        'instructor_count': instructor_count,
        'phd_count': phd_count
    })

def board_index(request):
    try:
        board_list = BoardMember.objects.all()
    except ObjectDoesNotExist:
        raise Http404
    return render_to_response('directory/board-index.html',{'object_list':board_list})

def board_detail(request,board_id):
    try:
        board_detail = BoardMember.objects.get(pk=board_id)
    except ObjectDoesNotExist:
        raise Http404
    return render_to_response('directory/board-detail.html', {'object_detail': board_detail})
