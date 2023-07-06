from django.views.generic  import  TemplateView


class AutosView(TemplateView):
    template_name = "index.html"
    
    