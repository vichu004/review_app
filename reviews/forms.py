from django import forms

class ReviewForm(forms.Form):
    user_name=forms.CharField(label="Your Name",max_length=5,error_messages={"required:Name should not be empty "})
    review_text=forms.CharField(label="Feedback",widget=forms.Textarea)
    rating=forms.IntegerField(label="Your Rating",min_value=0,max_value=5)