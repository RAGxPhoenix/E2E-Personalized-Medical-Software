Commands to run:

pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py runserver

follow link to go to website

By default only can sign in as a healthworker and not admin
if want to sign in as an admin then:
    go to symptom_checker/symptom_checker/settings.py
    comment line 126 " AUTH_USER_MODEL = 'authentication.Patient' "
    now you can sign in as an admin

now if you want to sign in back as a healthworker then:
    uncomment line 126