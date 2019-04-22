# Create your views here.
from django.views.generic import DetailView
from research_areas.models import *
from directory.models import DepartmentMember
from django.shortcuts import get_object_or_404, render_to_response

class ResearchAreaDetailView(DetailView):
    
    model = ResearchArea
    context_object_name = "research_area"
    template_name = "research_areas/detail.html"

    def get_context_data(self, **kwargs):
        context = super(ResearchAreaDetailView, self).get_context_data(**kwargs)
        context['faculty_list'] = faculty_list = DepartmentMember.objects.filter(is_visible=True, user_role='Faculty').filter(researcharea__id=self.object.id).order_by('last_name')
        return context


# def research_area_detail(request, slug):
#     #Figure out which category we are in
#     research_area = get_object_or_404(ResearchArea, slug=slug)
#
#     try:
#         faculty_list = DepartmentMember.objects.filter(is_visible=True,user_role='Faculty').filter(researcharea__id=research_area.id).order_by('last_name')
#     except ResearchArea.DoesNotExist:
#         raise http404
#     return render_to_response('research_areas/detail.html', {
#         'research_area':research_area,
#         'faculty_list':faculty_list
#         })
#
#
# def research_area_geo_space(request,slug):
#     research_area = get_object_or_404(ResearchArea, slug=slug)
#
#     try:
#         faculty_list = DepartmentMember.objects.filter(is_visible=True, user_role='Faculty').filter(
#             researcharea__id=research_area.id).order_by('last_name')
#     except ResearchArea.DoesNotExist:
#         raise http404
#     return render_to_response('research_areas/detail.html', {
#         'research_area': research_area,
#         'faculty_list': faculty_list
#     })
#
#
