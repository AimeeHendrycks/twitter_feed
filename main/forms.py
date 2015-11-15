from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, HTML, Layout, Div, Field
from crispy_forms.bootstrap import FormActions
from main.models import Tweet


# class SearchForm(forms.ModelForm):
#     class Meta:
#         model = Tweet
#         fields = ['search_term',]

#     def __init__(self, *args, **kwargs):
#         super(SearchForm, self).__init__(*args, **kwargs)
#         self.helper = FormHelper(self)
#         self.helper.form_action = '/tweet_list/'
#         self.fields['search_term'].widget.attrs['placeholder'] = self.fields['search_term'].label or 'Search Term'
#         self.fields['search_term'].label = False
#         self.helper.layout.append(
#             FormActions(
#                 Submit('search', 'Search', css_class='btn-primary', style='background:black'),
#                 )
#             )