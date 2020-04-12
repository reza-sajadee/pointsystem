from django import forms
from django.db import models
from phone_field import PhoneField
from profile_app.models import Profile
from django_countries.fields import CountryField
from django.contrib.auth import authenticate, get_user_model
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.contrib import messages
cityList = (
    ('Abadan','Abadan'),
    ('Abadeh','Abadeh'),
    ('Abarkuh','Abarkuh'),
    ('Abhar','Abhar'),
    ('Abyek','Abyek'),
    ('Ahar','Ahar'),
    ('Ahvaz [Ahvaz]','Ahvaz [Ahvaz]'),
    ('Ajab Shir','Ajab Shir'),
    ('Aleshtar','Aleshtar'),
    ('Ali Abad','Ali Abad'),
    ('Aligudarz','Aligudarz'),
    ('Alvand','Alvand'),
    ('Amirkola','Amirkola'),
    ('Amol','Amol'),
    ('Andimeshk','Andimeshk'),
    ('Andisheh','Andisheh'),
    ('Aq Qala','Aq Qala'),
    ('Arak','Arak'),
    ('Aran Va Bidgol','Aran Va Bidgol'),
    ('Ardabil','Ardabil'),
    ('Ardakan','Ardakan'),
    ('Asad-Abad','Asad-Abad'),
    ('Ashkhaneh','Ashkhaneh'),
    ('Astaneh-E Ashrafiyeh','Astaneh-E Ashrafiyeh'),
    ('Astara','Astara'),
    ('Azadshahr','Azadshahr'),
    ('Azarshahr','Azarshahr'),
    ('Azna','Azna'),
    ('Babol','Babol'),
    ('Babolsar','Babolsar'),
    ('Bafq','Bafq'),
    ('Baft','Baft'),
    ('Bagh-E Malek','Bagh-E Malek'),
    ('Baghestan','Baghestan'),
    ('Bahar','Bahar'),
    ('Baharestan','Baharestan'),
    ('Bam','Bam'),
    ('Bandar-E -Abas [Bandar Abbas]','Bandar-E -Abas [Bandar Abbas]'),
    ('Bandar-E Anzali','Bandar-E Anzali'),
    ('Bandar-E Deylam','Bandar-E Deylam'),
    ('Bandar-E Emam Khomeyni','Bandar-E Emam Khomeyni'),
    ('Bandar-E Ganaveh','Bandar-E Ganaveh'),
    ('Bandar-E Kangan','Bandar-E Kangan'),
    ('Bandar-E Lengeh [Bandar Lengeh]','Bandar-E Lengeh [Bandar Lengeh]'),
    ('Bandar-E Mahshahr','Bandar-E Mahshahr'),
    ('Bandar-E Torkaman','Bandar-E Torkaman'),
    ('Baneh','Baneh'),
    ('Baqershahr','Baqershahr'),
    ('Bardaskan','Bardaskan'),
    ('Bardsir','Bardsir'),
    ('Behbahan','Behbahan'),
    ('Behshahr','Behshahr'),
    ('Bijar','Bijar'),
    ('Birjand','Birjand'),
    ('Bojnurd','Bojnurd'),
    ('Bonab','Bonab'),
    ('Borazjan','Borazjan'),
    ('Borujen','Borujen'),
    ('Borujerd','Borujerd'),
    ('Bukan','Bukan'),
    ('Bumahen','Bumahen'),
    ('Bushehr','Bushehr'),
    ('Chabahar','Chabahar'),
    ('Chaharbagh','Chaharbagh'),
    ('Chahardangeh','Chahardangeh'),
    ('Chalus','Chalus'),
    ('Chamran','Chamran'),
    ('Chenaran','Chenaran'),
    ('Damavand','Damavand'),
    ('Damghan','Damghan'),
    ('Darab','Darab'),
    ('Dargaz','Dargaz'),
    ('Dehbarez (Rudan)','Dehbarez (Rudan)'),
    ('Dehdasht','Dehdasht'),
    ('Dehgolan','Dehgolan'),
    ('Dehloran','Dehloran'),
    ('Delijan','Delijan'),
    ('Dezful','Dezful'),
    ('Divandareh','Divandareh'),
    ('Dorcheh Piaz','Dorcheh Piaz'),
    ('Dowlat Abad','Dowlat Abad'),
    ('Dugonbadan [Dogonbadan]','Dugonbadan [Dogonbadan]'),
    ('Durud [Dorud]','Durud [Dorud]'),
    ('Eqbaliyeh','Eqbaliyeh'),
    ('Eqlid','Eqlid'),
    ('Esfahan [Isfahan]','Esfahan [Isfahan]'),
    ('Esfarayen','Esfarayen'),
    ('Eshtehard','Eshtehard'),
    ('Eslamabad-E Gharb','Eslamabad-E Gharb'),
    ('Eslamshahr','Eslamshahr'),
    ('Estahban','Estahban'),
    ('Falavarjan','Falavarjan'),
    ('Fardis','Fardis'),
    ('Fariman','Fariman'),
    ('Farokh Shahr','Farokh Shahr'),
    ('Farsan','Farsan'),
    ('Fasa','Fasa'),
    ('Ferdows','Ferdows'),
    ('Ferdowsieh','Ferdowsieh'),
    ('Fereydunkenar','Fereydunkenar'),
    ('Firuz-Abad','Firuz-Abad'),
    ('Fuladshahr','Fuladshahr'),
    ('Fuman','Fuman'),
    ('Garmsar','Garmsar'),
    ('Gerash','Gerash'),
    ('Germi','Germi'),
    ('Golbahar','Golbahar'),
    ('Goldasht','Goldasht'),
    ('Golestan (Soltanabad)','Golestan (Soltanabad)'),
    ('Golpayegan','Golpayegan'),
    ('Gonabad','Gonabad'),
    ('Gonbad-E Kavus [Gonbad-E Qabus]','Gonbad-E Kavus [Gonbad-E Qabus]'),
    ('Gorgan','Gorgan'),
    ('Hadishahr','Hadishahr'),
    ('Ḥaji Abad [Hajjiabad]','Ḥaji Abad [Hajjiabad]'),
    ('Hamadan','Hamadan'),
    ('Ḥamidiya','Ḥamidiya'),
    ('Harsin','Harsin'),
    ('Ḥasan Abad','Ḥasan Abad'),
    ('Hashtgerd','Hashtgerd'),
    ('Hashtpar','Hashtpar'),
    ('Hendijan','Hendijan'),
    ('Ilam','Ilam'),
    ('Iranshahr','Iranshahr'),
    ('Ivan','Ivan'),
    ('Izeh','Izeh'),
    ('Jahrom','Jahrom'),
    ('Jam','Jam'),
    ('Javanrud','Javanrud'),
    ('Jiroft','Jiroft'),
    ('Juybar','Juybar'),
    ('Kahnuj','Kahnuj'),
    ('Kahrizak','Kahrizak'),
    ('Kalaleh','Kalaleh'),
    ('Kamal Shahr','Kamal Shahr'),
    ('Kamyaran','Kamyaran'),
    ('Kangavar','Kangavar'),
    ('Karaj','Karaj'),
    ('Kashan','Kashan'),
    ('Kashmar','Kashmar'),
    ('Kavar','Kavar'),
    ('Kazerun','Kazerun'),
    ('Kelishad Va Sudarjan','Kelishad Va Sudarjan'),
    ('Kerman','Kerman'),
    ('Kermanshah (Bakhtaran)','Kermanshah (Bakhtaran)'),
    ('Khalkhal','Khalkhal'),
    ('Khash','Khash'),
    ('Khomeyn','Khomeyn'),
    ('Khomeyni Shahr (Homayunshahr)','Khomeyni Shahr (Homayunshahr)'),
    ('Khoram Abad','Khoram Abad'),
    ('Khoramdareh [Khorramdarreh]','Khoramdareh [Khorramdarreh]'),
    ('Khoramshahr (Khuninshahr)','Khoramshahr (Khuninshahr)'),
    ('Khurmuj','Khurmuj'),
    ('Khuy [Khoy]','Khuy [Khoy]'),
    ('Khvaf','Khvaf'),
    ('Khvorzuq','Khvorzuq'),
    ('Kish','Kish'),
    ('Konarak','Konarak'),
    ('Kordkuy','Kordkuy'),
    ('Kuhdasht','Kuhdasht'),
    ('Kut-E Abdallah','Kut-E Abdallah'),
    ('Lahijan','Lahijan'),
    ('Lamerd','Lamerd'),
    ('Langarud','Langarud'),
    ('Lar','Lar'),
    ('Lordegan','Lordegan'),
    ('Mahabad','Mahabad'),
    ('Maḥalat [Mahallat]','Maḥalat [Mahallat]'),
    ('Mahdasht','Mahdasht'),
    ('Maḥmud-Abad','Maḥmud-Abad'),
    ('Maku','Maku'),
    ('Malard','Malard'),
    ('Malayer','Malayer'),
    ('Malekan','Malekan'),
    ('Maragheh','Maragheh'),
    ('Marand','Marand'),
    ('Marivan','Marivan'),
    ('Marvdasht','Marvdasht'),
    ('Mashhad [Meshed]','Mashhad [Meshed]'),
    ('Masjed-E Soleyman','Masjed-E Soleyman'),
    ('Mehriz','Mehriz'),
    ('Meshgin Shahr','Meshgin Shahr'),
    ('Meshkin Dasht','Meshkin Dasht'),
    ('Meybod','Meybod'),
    ('Mianduab [Miandoab]','Mianduab [Miandoab]'),
    ('Mianeh','Mianeh'),
    ('Minab','Minab'),
    ('Minudasht','Minudasht'),
    ('Mobarakeh','Mobarakeh'),
    ('Moḥamadiyeh','Moḥamadiyeh'),
    ('Moḥamadshahr','Moḥamadshahr'),
    ('Nahavand','Nahavand'),
    ('Na-In [Naeen]','Na-In [Naeen]'),
    ('Najaf Abad','Najaf Abad'),
    ('Naqadeh','Naqadeh'),
    ('Nasim Shahr (Akbarabad)','Nasim Shahr (Akbarabad)'),
    ('Nasirshahr','Nasirshahr'),
    ('Naẓar-Abad','Naẓar-Abad'),
    ('Neka','Neka'),
    ('Neyriz','Neyriz'),
    ('Nishabur [Nishapur]','Nishabur [Nishapur]'),
    ('Nowshahr','Nowshahr'),
    ('Nur','Nur'),
    ('Nur-Abad','Nur-Abad'),
    ('Nur-Abad','Nur-Abad'),
    ('Omidiyeh','Omidiyeh'),
    ('Orumiyeh (Reza-Iyeh) [Urmia]','Orumiyeh (Reza-Iyeh) [Urmia]'),
    ('Oshnavieh','Oshnavieh'),
    ('Pakdasht','Pakdasht'),
    ('Parand','Parand'),
    ('Pardis','Pardis'),
    ('Pars Abad','Pars Abad'),
    ('Paveh','Paveh'),
    ('Piranshahr','Piranshahr'),
    ('Pishva','Pishva'),
    ('Pol-E Dokhtar','Pol-E Dokhtar'),
    ('Qa-Emiyeh','Qa-Emiyeh'),
    ('Qa-Em Shahr','Qa-Em Shahr'),
    ('Qa-En','Qa-En'),
    ('Qahderijan','Qahderijan'),
    ('Qarah Ziya-Aldin','Qarah Ziya-Aldin'),
    ('Qarchak','Qarchak'),
    ('Qazvin','Qazvin'),
    ('Qeshm','Qeshm'),
    ('Qeydar','Qeydar'),
    ('Qods','Qods'),
    ('Qom','Qom'),
    ('Qorveh','Qorveh'),
    ('Quchan','Quchan'),
    ('Rafsanjan','Rafsanjan'),
    ('Ramhormoz','Ramhormoz'),
    ('Ramsar','Ramsar'),
    ('Ramshir','Ramshir'),
    ('Rasht','Rasht'),
    ('Robat Karim','Robat Karim'),
    ('Rudehen','Rudehen'),
    ('Rudsar','Rudsar'),
    ('Sabashahr (Qasemabad)','Sabashahr (Qasemabad)'),
    ('Sabzevar','Sabzevar'),
    ('Safadasht','Safadasht'),
    ('Safashahr','Safashahr'),
    ('Sahand','Sahand'),
    ('Saḥneh','Saḥneh'),
    ('Saleḥieh [Saleḥabad]','Saleḥieh [Saleḥabad]'),
    ('Salmas','Salmas'),
    ('Sanandaj','Sanandaj'),
    ('Saqqez','Saqqez'),
    ('Sarab','Sarab'),
    ('Sarakhs','Sarakhs'),
    ('Saravan','Saravan'),
    ('Sardasht','Sardasht'),
    ('Sardrud','Sardrud'),
    ('Sari','Sari'),
    ('Sarpol-E Dhahab [Sarpol-E Zahab]','Sarpol-E Dhahab [Sarpol-E Zahab]'),
    ('Saveh','Saveh'),
    ('Semirom','Semirom'),
    ('Semnan','Semnan'),
    ('Shadegan','Shadegan'),
    ('Shahedshahr','Shahedshahr'),
    ('Shahin Dezh','Shahin Dezh'),
    ('Shahin Shahr','Shahin Shahr'),
    ('Shahr-E Babak','Shahr-E Babak'),
    ('Shahr-E Jadid-E Hashtgerd','Shahr-E Jadid-E Hashtgerd'),
    ('Shahr-E Kord','Shahr-E Kord'),
    ('Shahr-E Sadra','Shahr-E Sadra'),
    ('Shahreza (Qomsheh) [Shahreza]','Shahreza (Qomsheh) [Shahreza]'),
    ('Shahriar','Shahriar'),
    ('Shahrud (Emamshahr)','Shahrud (Emamshahr)'),
    ('Sheybani','Sheybani'),
    ('Shiraz [Shiraz]','Shiraz [Shiraz]'),
    ('Shirvan','Shirvan'),
    ('Showt','Showt'),
    ('Shush','Shush'),
    ('Shushtar','Shushtar'),
    ('Sirjan','Sirjan'),
    ('Sonqor','Sonqor'),
    ('Sowme-Eh Sara','Sowme-Eh Sara'),
    ('Susangerd','Susangerd'),
    ('Tabas','Tabas'),
    ('Tabriz [Tabriz]','Tabriz [Tabriz]'),
    ('Takab','Takab'),
    ('Takestan','Takestan'),
    ('Taybad','Taybad'),
    ('Tehran','Tehran'),
    ('Tonekabon','Tonekabon'),
    ('Torbat-E Ḥeydarieh','Torbat-E Ḥeydarieh'),
    ('Torbat-E Jam','Torbat-E Jam'),
    ('Tuyserkan','Tuyserkan'),
    ('Vaḥidieh','Vaḥidieh'),
    ('Varamin','Varamin'),
    ('Yasuj','Yasuj'),
    ('Yazd','Yazd'),
    ('Zabol','Zabol'),
    ('Zahedan','Zahedan'),
    ('Zanjan','Zanjan'),
    ('Zarand','Zarand'),
    ('Zarin Shahr','Zarin Shahr'),
    ('Zarqan','Zarqan'),
)


#Player Form


class UserPlayerCreationForm(forms.ModelForm):

    """
    A form for creating new users. Includes all the required
    fields, plus a repeated password.
    """
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = Profile
        fields = (
                'isf_id','password1','password2','email',
                'first_name','last_name','country_names',
                'city_name','club','phone_number','profile_image',
                'id_number','year','mounth','day'
                )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        
        self.fields['isf_id'].widget.attrs.update({'class': 'form-control'})
        self.fields['email'].widget.attrs.update({'class': 'form-control'})      
        self.fields['first_name'].widget.attrs.update({'class': 'form-control'})        
        self.fields['last_name'].widget.attrs.update({'class': 'form-control'})
        self.fields['phone_number'].widget.attrs.update({'class': 'form-control'})
        self.fields['country_names'].widget.attrs.update({'class': 'form-control'})
        self.fields['city_name'].widget.attrs.update({'class': 'form-control'})
        self.fields['club'].widget.attrs.update({'class': 'form-control'})
        self.fields['id_number'].widget.attrs.update({'class': 'form-control'})
        self.fields['year'].widget.attrs.update({'class': 'form-control'})
        self.fields['mounth'].widget.attrs.update({'class': 'form-control'})
        self.fields['day'].widget.attrs.update({'class': 'form-control'})
       
        self.fields['password1'].widget.attrs.update({'class': 'form-control'})
        self.fields['password2'].widget.attrs.update({'class': 'form-control'})
       

        self.fields['isf_id'].Label          ='Insert yor Isf Id'
        self.fields['email'].Label           ='Insert yor Email'
        self.fields['first_name'].Label      ='Insert your first name'
        self.fields['last_name'].Label       ='Insert your last name'
        self.fields['phone_number'].Label    ='Insert your phone number'
        self.fields['country_names'].Label   ='select your country'
        self.fields['city_name'].Label       ='Insert your select your city'
        self.fields['club'].Label            ='Insert your club name'
        self.fields['profile_image'].Label   ='upload your profile picture'
        self.fields['id_number'].Label       ='select your country'
        self.fields['year'].Label            ='Insert your select your city'
        self.fields['mounth'].Label          ='Insert your club name'
        self.fields['day'].Label             ='upload your profile picture'



    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2
    
   

    def clean_isf_id(self):
        isf_id = self.cleaned_data.get("isf_id")
        qs = Profile.objects.get_player_by_isf_id(isf_id=isf_id)
        if qs.exists():
            raise forms.ValidationError("Isf Id is taken")
        return isf_id

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(UserPlayerCreationForm, self).save(commit=False)
        user.player=True
        user.set_password(self.cleaned_data["password1"])
        
        if commit:
            user.save()
        return user


class UserPlayerChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = Profile
        fields = (
             'isf_id','password','email',
             'first_name','last_name','country_names',
             'city_name','club','phone_number','profile_image',
             'id_number','year','mounth','day'
             )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        
        self.fields['isf_id'].widget.attrs.update({'class': 'form-control'})
        self.fields['email'].widget.attrs.update({'class': 'form-control'})      
        self.fields['first_name'].widget.attrs.update({'class': 'form-control'})        
        self.fields['last_name'].widget.attrs.update({'class': 'form-control'})
        self.fields['phone_number'].widget.attrs.update({'class': 'form-control'})
        self.fields['country_names'].widget.attrs.update({'class': 'form-control'})
        self.fields['city_name'].widget.attrs.update({'class': 'form-control '})
        self.fields['club'].widget.attrs.update({'class': 'form-control'})
        self.fields['profile_image'].widget.attrs.update({'class': 'form-control'})
        self.fields['password'].widget.attrs.update({'class': 'form-control'})
        self.fields['id_number'].widget.attrs.update({'class': 'form-control'})
        self.fields['year'].widget.attrs.update({'class': 'form-control'})
        self.fields['mounth'].widget.attrs.update({'class': 'form-control'})
        self.fields['day'].widget.attrs.update({'class': 'form-control'})
       
      

        self.fields['isf_id'].Label          ='Insert yor Isf Id'
        self.fields['email'].Label           ='Insert yor Email'
        self.fields['first_name'].Label      ='Insert your first name'
        self.fields['last_name'].Label       ='Insert your last name'
        self.fields['phone_number'].Label    ='Insert your phone number'
        self.fields['country_names'].Label   ='select your country'
        self.fields['city_name'].Label       ='Insert your select your city'
        self.fields['club'].Label            ='Insert your club name'
        self.fields['profile_image'].Label   ='upload your profile picture'
        self.fields['id_number'].Label       ='select your country'
        self.fields['year'].Label            ='Insert your select your city'
        self.fields['mounth'].Label          ='Insert your club name'
        self.fields['day'].Label             ='upload your profile picture'


    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]

#Judge Form




class UserJudgeCreationForm(forms.ModelForm):

    """
    A form for creating new users. Includes all the required
    fields, plus a repeated password.
    """
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)
    
    class Meta:
        model = Profile
        fields = (
                'isf_id','password1','password2','email',
                'first_name','last_name','country_names',
                'city_name','cridit_card','phone_number','profile_image'
                )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        
        self.fields['isf_id'].widget.attrs.update({'class': 'form-control'})
        self.fields['email'].widget.attrs.update({'class': 'form-control'})      
        self.fields['first_name'].widget.attrs.update({'class': 'form-control'})        
        self.fields['last_name'].widget.attrs.update({'class': 'form-control'})
        self.fields['phone_number'].widget.attrs.update({'class': 'form-control'})
        self.fields['country_names'].widget.attrs.update({'class': 'form-control'})
        self.fields['city_name'].widget.attrs.update({'class': 'form-control'})
        self.fields['cridit_card'].widget.attrs.update({'class': 'form-control'})
       
        self.fields['password1'].widget.attrs.update({'class': 'form-control'})
        self.fields['password2'].widget.attrs.update({'class': 'form-control'})
       

        self.fields['isf_id'].Label          ='Insert yor Isf Id'
        self.fields['email'].Label           ='Insert yor Email'
        self.fields['first_name'].Label      ='Insert your first name'
        self.fields['last_name'].Label       ='Insert your last name'
        self.fields['phone_number'].Label    ='Insert your phone number'
        self.fields['country_names'].Label   ='select your country'
        self.fields['city_name'].Label       ='Insert your select your city'
        self.fields['cridit_card'].Label     ='Insert your cridit_card name'
        self.fields['profile_image'].Label   ='upload your profile picture'



    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def clean_isf_id(self):
        isf_id = self.cleaned_data.get("isf_id")
        qs = Profile.objects.get_judge_by_isf_id(isf_id=isf_id)
        if qs.exists():
            raise forms.ValidationError("Isf Id is taken")
        return isf_id

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(UserJudgeCreationForm, self).save(commit=False)
        user.judge=True
        print(user)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserJudgeChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = Profile
        fields = (
            'isf_id','password','email',
             'first_name','last_name','country_names',
             'city_name','cridit_card','phone_number','profile_image'
             )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        
        self.fields['isf_id'].widget.attrs.update({'class': 'form-control'})
        self.fields['email'].widget.attrs.update({'class': 'form-control'})      
        self.fields['first_name'].widget.attrs.update({'class': 'form-control'})        
        self.fields['last_name'].widget.attrs.update({'class': 'form-control'})
        self.fields['phone_number'].widget.attrs.update({'class': 'form-control'})
        self.fields['country_names'].widget.attrs.update({'class': 'form-control'})
        self.fields['city_name'].widget.attrs.update({'class': 'form-control'})
        self.fields['cridit_card'].widget.attrs.update({'class': 'form-control'})
        self.fields['profile_image'].widget.attrs.update({'class': 'form-control'})
        self.fields['password'].widget.attrs.update({'class': 'form-control'})

       

        self.fields['isf_id'].Label          ='Insert yor Isf Id'
        self.fields['email'].Label           ='Insert yor Email'
        self.fields['first_name'].Label      ='Insert your first name'
        self.fields['last_name'].Label       ='Insert your last name'
        self.fields['phone_number'].Label    ='Insert your phone number'
        self.fields['country_names'].Label   ='select your country'
        self.fields['city_name'].Label       ='Insert your select your city'
        self.fields['cridit_card'].Label     ='Insert your cridit_card name'
        self.fields['profile_image'].Label   ='upload your profile picture'



    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]











#Global Form Class
User = get_user_model()
class UserLoginForm(forms.Form):
    username        = forms.CharField()
    password        = forms.CharField(widget=forms.PasswordInput)



    username.widget.attrs = {'class':'form-control'}
    password.widget.attrs = {'class':'form-control'}


    def clean(self,*args, **kwargs):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        
        if username and password:
            user = authenticate(username = username , password = password)
            if not user:
                raise forms.ValidationError('this user is not exist ')
            if not user.check_password:
                raise forms.ValidationError('Password is wrong')
            if not user.is_active:
                raise forms.ValidationError('this user is not activate')
            return super(UserLoginForm,self).clean(*args, **kwargs)


class ProfileRegisterForm(forms.ModelForm):
    
    country_names                = CountryField()
    city_name                    = forms.ChoiceField(choices = cityList,initial='Tehran',widget=forms.Select(),required=True)
    phone_number                 = PhoneField()
    profile_image                = forms.ImageField(required=False)



    
    city_name.widget.attrs       = {'class':'form-control'}
    profile_image.widget.attrs   = {'class':'form-control'}


    class Meta:
        model = Profile
        fields = 'country_names','city_name','phone_number','profile_image'
        exclid = 'isf_id'


class UserRegisterForm(forms.ModelForm):
    email           = forms.EmailField(label='Email Adress', required=False)
    password        = forms.CharField(widget=forms.PasswordInput)
    password2       = forms.CharField(widget=forms.PasswordInput,label='Password Confirmation')
    first_name      = forms.CharField(label='First Name')
    last_name       = forms.CharField(label='Last Name')
    username        = forms.CharField(label='User Name')
    

    email.widget.attrs           = {'class':'form-control'}
    password.widget.attrs        = {'class':'form-control'}
    password2.widget.attrs       = {'class':'form-control'}
    first_name.widget.attrs      = {'class':'form-control'}
    last_name.widget.attrs       = {'class':'form-control'}
    username.widget.attrs        = {'class':'form-control'}


    class Meta:
        model = User
        fields = 'email', 'password', 'password2', 'first_name', 'last_name', 'username',  




    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)   
    

    def clean_email(self):
        email = self.cleaned_data.get("email")
        email_qs = User.objects.filter(email=email)
        if email_qs.exists():
            raise forms.ValidationError("this Email is Exist")
        return email



class UserAdminCreationForm(forms.ModelForm):
    """
    A form for creating new users. Includes all the required
    fields, plus a repeated password.
    """
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = Profile
        fields = ('isf_id','email', 'first_name','last_name','phone_number','country_names','city_name','phone_number','profile_image')

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(UserAdminCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserAdminChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = Profile
        fields = ('email', 'password', 'active', 'admin')

    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]