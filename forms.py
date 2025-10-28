from sixth_app.models import BOOK
class BookForm(forms.ModelForm):
    class Meta:
        model = BOOK
        fields = '__all__'
