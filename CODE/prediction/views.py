from django.shortcuts import render

def symptom_check(request):
    return render(request, 'prediction/symptom_check.html')


def body_check(request):
    return render(request, 'prediction/body_check.html')


from django.shortcuts import render
from django.http import JsonResponse
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split as tp
from sklearn import linear_model
from sklearn.linear_model import LogisticRegression
from sklearn import tree as t
from sklearn.preprocessing import LabelEncoder as le
from sklearn.model_selection import cross_val_score as cross

import joblib as jb
model = jb.load('trained_model.joblib')

def symptom_input(request):
    return render(request, 'symptom_input.html')

def save_symptoms(request):
    if request.method == 'POST':
        symptoms = request.POST.getlist('symptoms[]')
        # Here you can process and save the symptoms as needed
        print(symptoms)  # Just for demonstration
        
        final_symptoms = ['Symptom_{}_ {}'.format(index + 1, symptom) for index, symptom in enumerate(symptoms)]
        print(final_symptoms)
        diseaselist=['(vertigo) Paroymsal  Positional Vertigo',
         'AIDS',
          'Acne',
         'Alcoholic hepatitis',
        'Allergy',
        'Arthritis',
       'Bronchial Asthma',
       'Cervical spondylosis',
      'Chicken pox',
       'Chronic cholestasis',
      'Common Cold',
'Dengue',
'Diabetes',
'Dimorphic hemmorhoids(piles)',
'Drug Reaction',
'Fungal infection',
'GERD',
'Gastroenteritis',
'Heart attack',
'Hepatitis B',
'Hepatitis C',
'Hepatitis D',
'Hepatitis E',
'Hypertension',
'Hyperthyroidism',
'Hypoglycemia',
'Hypothyroidism',
'Impetigo',
'Jaundice',
'Malaria',
'Migraine',
'Osteoarthristis',
'Paralysis (brain hemorrhage)',
'Peptic ulcer diseae',
'Pneumonia',
'Psoriasis',
'Tuberculosis',
'Typhoid',
'Urinary tract infection',
'Varicose veins',
'hepatitis A']



        symptomslist=['Symptom_1_ acidity',
         'Symptom_1_ back_pain',
         'Symptom_1_ bladder_discomfort',
         'Symptom_1_ breathlessness',
          'Symptom_1_ burning_micturition',
          'Symptom_1_ chest_pain',
           'Symptom_1_ chills',
           'Symptom_1_ constipation',
             'Symptom_1_ continuous_sneezing',
              'Symptom_1_ cough',
               'Symptom_1_ cramps',
'Symptom_1_ fatigue',
'Symptom_1_ headache',
'Symptom_1_ high_fever',
'Symptom_1_ indigestion',
'Symptom_1_ joint_pain',
'Symptom_1_ mood_swings',
'Symptom_1_ muscle_wasting',
'Symptom_1_ muscle_weakness',
'Symptom_1_ neck_pain',
'Symptom_1_ pain_during_bowel_movements',
'Symptom_1_ patches_in_throat',
'Symptom_1_ pus_filled_pimples',
'Symptom_1_ shivering',
'Symptom_1_ skin_rash',
'Symptom_1_ stiff_neck',
'Symptom_1_ stomach_pain',
'Symptom_1_ sunken_eyes',
'Symptom_1_ vomiting',
'Symptom_1_ weakness_in_limbs',
'Symptom_1_ weight_gain',
'Symptom_1_ weight_loss',
'Symptom_1_ yellowish_skin',
'Symptom_1_itching',
'Symptom_2_ abdominal_pain',
'Symptom_2_ acidity',
'Symptom_2_ anxiety',
'Symptom_2_ blackheads',
'Symptom_2_ bladder_discomfort',
'Symptom_2_ blister',
'Symptom_2_ breathlessness',
'Symptom_2_ bruising',
'Symptom_2_ chest_pain',
'Symptom_2_ chills',
'Symptom_2_ cold_hands_and_feets',
'Symptom_2_ cough',
'Symptom_2_ cramps',
'Symptom_2_ dehydration',
'Symptom_2_ dizziness',
'Symptom_2_ fatigue',
'Symptom_2_ foul_smell_of urine',
'Symptom_2_ headache',
'Symptom_2_ high_fever',
'Symptom_2_ indigestion',
'Symptom_2_ joint_pain',
'Symptom_2_ knee_pain',
'Symptom_2_ lethargy',
'Symptom_2_ loss_of_appetite',
'Symptom_2_ mood_swings',
'Symptom_2_ nausea',
'Symptom_2_ neck_pain',
'Symptom_2_ nodal_skin_eruptions',
'Symptom_2_ pain_during_bowel_movements',
'Symptom_2_ pain_in_anal_region',
'Symptom_2_ patches_in_throat',
'Symptom_2_ pus_filled_pimples',
'Symptom_2_ restlessness',
'Symptom_2_ shivering',
'Symptom_2_ skin_peeling',
'Symptom_2_ skin_rash',
'Symptom_2_ stiff_neck',
'Symptom_2_ stomach_pain',
'Symptom_2_ sunken_eyes',
'Symptom_2_ sweating',
'Symptom_2_ swelling_joints',
'Symptom_2_ ulcers_on_tongue',
'Symptom_2_ vomiting',
'Symptom_2_ weakness_in_limbs',
'Symptom_2_ weakness_of_one_body_side',
'Symptom_2_ weight_gain',
'Symptom_2_ weight_loss',
'Symptom_2_ yellowish_skin',
'Symptom_3_ abdominal_pain',
'Symptom_3_ altered_sensorium',
'Symptom_3_ anxiety',
'Symptom_3_ blackheads',
'Symptom_3_ blister',
'Symptom_3_ bloody_stool',
'Symptom_3_ blurred_and_distorted_vision',
'Symptom_3_ breathlessness',
'Symptom_3_ bruising',
'Symptom_3_ burning_micturition',
'Symptom_3_ chest_pain',
'Symptom_3_ chills',
'Symptom_3_ cold_hands_and_feets',
'Symptom_3_ continuous_feel_of_urine',
'Symptom_3_ cough',
'Symptom_3_ dark_urine',
'Symptom_3_ dehydration',
'Symptom_3_ diarrhoea',
'Symptom_3_ dischromic _patches',
'Symptom_3_ dizziness',
'Symptom_3_ extra_marital_contacts',
'Symptom_3_ fatigue',
'Symptom_3_ foul_smell_of urine',
'Symptom_3_ headache',
'Symptom_3_ high_fever',
'Symptom_3_ hip_joint_pain',
'Symptom_3_ joint_pain',
'Symptom_3_ knee_pain',
'Symptom_3_ lethargy',
'Symptom_3_ loss_of_appetite',
'Symptom_3_ loss_of_balance',
'Symptom_3_ mood_swings',
'Symptom_3_ movement_stiffness',
'Symptom_3_ nausea',
'Symptom_3_ neck_pain',
'Symptom_3_ nodal_skin_eruptions',
'Symptom_3_ obesity',
'Symptom_3_ pain_in_anal_region',
'Symptom_3_ red_sore_around_nose',
'Symptom_3_ restlessness',
'Symptom_3_ scurring',
'Symptom_3_ silver_like_dusting',
'Symptom_3_ skin_peeling',
'Symptom_3_ spinning_movements',
'Symptom_3_ stomach_pain',
'Symptom_3_ sweating',
'Symptom_3_ swelling_joints',
'Symptom_3_ swelling_of_stomach',
'Symptom_3_ ulcers_on_tongue',
'Symptom_3_ vomiting',
'Symptom_3_ watering_from_eyes',
'Symptom_3_ weakness_of_one_body_side',
'Symptom_3_ weight_loss',
'Symptom_3_ yellowish_skin']

        testingsymptoms = []
    # will come from frontend
        #append zero in all coloumn fields...
        for x in range(0, len(symptomslist)):
          testingsymptoms.append(0)


        #update 1 where symptoms gets matched...
        for k in range(0, len(symptomslist)):

         for z in final_symptoms:
          if (z == symptomslist[k]):
                  testingsymptoms[k] = 1


        inputtest = [testingsymptoms]    

        predicted = model.predict(inputtest)
        predicted_disease=diseaselist[predicted[0]]

        print(predicted_disease )

        request.session['symptoms'] = symptoms
        request.session['predicted_disease'] = predicted_disease


        return JsonResponse({'message': 'Symptoms received and saved successfully.', 'diseaseName': predicted_disease})
    else:
        return JsonResponse({'error': 'Method not allowed.'}, status=405)

    