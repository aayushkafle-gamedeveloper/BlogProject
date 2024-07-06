from django import forms
from main.models import Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["fullname"].widget.attrs.update({"placeholder":"Full Name"})
        self.fields["email"].widget.attrs.update({"placeholder": "Email"})
        self.fields["phonenumber"].widget.attrs.update({"type":"number", "placeholder":"Phone Number"})
        self.fields["subject"].widget.attrs.update({"rows":"1", "placeholder":"Subject"})
        self.fields["message"].widget.attrs.update({"cols":"30", "rows":"10", "placeholder":"Your Message"})
    
    def clean_phonenumber(self):
        phone_number = self.cleaned_data.get("phonenumber")
        if len(phone_number)!=10:
            raise forms.ValidationError("phonenumber must contain 10 digit")
        return phone_number