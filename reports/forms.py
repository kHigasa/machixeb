from django import forms


class ReportForm(forms.Form):
    is_draft = forms.BooleanField(
        label='下書き',
    )

    date = forms.DateField(
        label='日付',
    )
    
    opening_time = forms.TimeField(
        label='開始時間',
    )

    closing_time = forms.TimeField(
        label='終了時間',
    )

    recess = forms.TimeField(
        label='休憩時間',
    )

    feeling = forms.CharField(
        label='気分',
        max_length=255,
    )

    core_value = forms.CharField(
        label='意識したcore value',
        max_length=255,
    )

    done = forms.CharField(
        label='やったこと',
    )

    todo = forms.CharField(
        label='次やること',
    )

    review = forms.CharField(
        label='フリー記述欄（振り返りや感想）',
    )
