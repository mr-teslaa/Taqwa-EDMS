from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, BooleanField, IntegerField, FileField
       
#   wtf validators
from wtforms.validators import DataRequired, Length, Email


#   make a class for wtforms 
class AdmissionForm(FlaskForm):

    #   make a field for first name
    firstname = StringField(
        'First name',
        validators = [
            DataRequired(),
            Length(min=3, max=50)
        ]
    )

    #   make a field for last name
    lastname = StringField(
        'Last name',
        validators = [
            DataRequired(),
            Length(min=3, max=50)
        ]
    )

    #   make field for father's name
    father_name = StringField(
        'Father\'s Name',
        validators = [
            DataRequired(),
            Length(min=3, max=50)
        ]
    )

    #   make a field for mother's name
    mother_name = StringField(
        'Mother\'s Name',
        validators = [
            DataRequired(),
            Length(min=3, max=50)
        ]
    )

    #   make select field for select admitted class
    applicable_class = SelectField(
        'Class you want to apply',
        choices = [
            ('n/a', '--- Select Class ---'),
            ('play', 'PLAY'),
            ('nursary', 'NURSARY'),
            ('one', 'ONE'),
            ('two', 'TWO'),
            ('three', 'THREE'),
            ('four', 'FOUR'),
            ('two', 'FIVE'),
            ('three', 'SIX'),
            ('one', 'SEVEN'),
            ('two', 'EIGHT')
        ]
    )

    #   make a field for phone number
    phone_number = IntegerField(
        'Phone Number',
        validators = [
            DataRequired(),
            Length(11, 13)
        ]
    )

    #   make a datetime field for date of birth
    #   want to make this a DateTimeField. But do not know actual syntax
    birth_date = StringField(
        'Date of Birth',
        validators = [
            DataRequired()
        ]
    )

    #   make a text field for birth cirtificate id 
    birth_cirtificate_no  = IntegerField(
        'Birth Cirtificate No',
        validators = [
            DataRequired()
        ]
    )

    #   make a radio for male
    male = BooleanField('Male')
    
    #   make a radio for female
    female = BooleanField('Female')

    #   make a radio for trasportation yes
    yes = BooleanField('Yes') 
    
    #   make a radio for trasportation no
    no = BooleanField('no') 

    #   make a field for care of address
    care_of = StringField(
        'Care of',
        validators = [
            DataRequired(),
            Length(min=3, max=80)
        ]
    ) 

    #   make a field for zip code
    zip_code = IntegerField(
        'Post Code',
        validators = [
            DataRequired(),
            Length(min=4, max=4)
        ]
    )

    #   make a filed for address
    address = StringField(
        'Address',
        validators = [
            DataRequired(),
            Length(min=3, max=20)
        ]
    )

    #   make a field for email
    email = StringField(
        'E-mail',
        validators = [
            Email(),
            DataRequired()
        ]
    )

    #   make a photo upload field
    photo = FileField(
        'Photo',
        validators = [ DataRequired() ]
    )

    #   make a field for signature
    signature = FileField(
        'Signature',
        validators = [ DataRequired()]
    )

    #   make a select field for date of birth
    """ birth_date = SelectField(
        'Date of Birth',
        choices = [
            ('n/a', '--- Select Birth Date ---'),
            ('01', '01'), ('02', '02'),
            ('03', '03'), ('04', '04'),
            ('05', '05'), ('06', '06'),
            ('07', '07'), ('08', '08'),
            ('09', '09'), ('10', '10'),
            ('11', '11'), ('12', '12'),
            ('13', '13'), ('14', '14'),
            ('15', '15'), ('16', '16'),
            ('17', '17'), ('18', '18'),
            ('19', '19'), ('20', '20'),
            ('21', '21'), ('22', '22'),
            ('23', '23'), ('24', '24'),
            ('25', '25'), ('26', '26'),
            ('27', '27'), ('28', '28'),
            ('29', '29'), ('30', '30'),
            ('31', '31')
        ]
    ) """

    #   make a select field for month
    birth_month = SelectField(
        'Date of Birth',
        choices = [
            ('n/a', '--- Select Birth Month ---'), 
            ('January', '01 - January'),('February', '02 - February'), 
            ('March', '03 - March'), ('April', '04 - April'), 
            ('May', '05 - May'), ('June', '06 - June'), 
            ('July', '07 - July'), ('August', '08 - August'), 
            ('September', '09 - September'), ('October', '10 - October'), 
            ('November', '11 - November'), ('December', '12 - December')
        ]
    )

    #   make a select field for year
    birth_year = SelectField(
        'Date of Birth',
        choices = [
            ('n/a', '--- Select Birth Year ---'), ('2000', '2000'),
            ('2001', '2001'), ('2002', '2002'),
            ('2003', '2003'), ('2004', '2004'),
            ('2005', '2005'), ('2006', '2006'),
            ('2007', '2007'), ('2008', '2008'),
            ('2009', '2009'), ('2010', '2010'),
            ('2011', '2011'), ('2012', '2012'),
            ('2013', '2013'), ('2014', '2014'),
            ('2015', '2015'), ('2016', '2016'),
            ('2017', '2017'), ('2018', '2018'),
            ('2019', '2019'), ('2020', '2020'),
        ]
    )

    #   make checkbox for agree with terms and codition
    checkbox = BooleanField(
        'I cirtify that all the information is given above is true. If the authority find any false information I will accept any decission the authority take.',
        validators = [
            DataRequired(),
        ]
    )

    #   make a submit field
    submit = SubmitField('Submit')
