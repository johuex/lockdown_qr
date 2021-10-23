from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, ValidationError, Length


class InputForm(FlaskForm):
    name = StringField('Имя', validators=[DataRequired(), Length(max=100)])
    surname = StringField('Фамилия', validators=[DataRequired(), Length(max=100)])
    patronymic = StringField('Отчество', validators=[DataRequired(), Length(max=100)])
    chip = SelectField('Модель чипа', choices=[(1, "Спутник V Core i7"),
                                                (2, "Спутник V Core i9"),
                                                (3, "Спутник V Ryzen 5"),
                                                (4, "Спутник V Ryzen 7"),
                                                (5, "Спутник V M1"),
                                                (6, "Спутник V M1 PRO"),
                                                (7, "Спутник V M1 MAX")], validate_choice=True)
    submit = SubmitField('Получить QR-код')
