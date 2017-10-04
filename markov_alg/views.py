from django.shortcuts import render
from django.views.generic.base import View

from markov_alg.forms import TextForm
from markov_alg.service import MarkovChain
from markov_alg.parser import AsyncPythonDocsParser



class WordView(View):
	form_class = TextForm
	template_name = 'form_template.html'

	def get(self, request, *args, **kwargs):
		form = self.form_class(request.POST)
		context = {
			'form': form,
		}

		return render(request, self.template_name, context)

	def post(self, request, *args, **kwargs):
		form = self.form_class(request.POST)
		context = {
			'form': form,
		}
		if form.is_valid():
			if form.cleaned_data["text_type"] == 'python':
				context['result'] = MarkovChain(AsyncPythonDocsParser().parse()).generate_text(form.cleaned_data["num"])
			else:
				context['result'] = MarkovChain(form.cleaned_data["text"]).generate_text(form.cleaned_data["num"])

		return render(request, self.template_name, context)



