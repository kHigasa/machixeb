from django import forms


class ShiftForm(forms.Form):
    date = forms.DateField(
        label='日付',
    )

    opening_time = forms.TimeField(
        label='開始時間',
    )

    closing_time = forms.TimeField(
        label='終了時間',
    )
