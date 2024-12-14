# views.py in the home app
from django.shortcuts import render
from django.http import JsonResponse

def home(request):
    return render(request, 'home/home.html')

def features(request):
    # Features page view logic
    return render(request, 'home/features.html')  # Corrected rendering of the features.html template

def contact(request):
    # Contact page view logic
    return render(request, 'home/contact.html')

def about(request):
    return render(request, 'home/about.html')

def search(request):
    return render(request, 'home/search.html')



# Define a dictionary to store information for each disease
disease_info_dict = {
    'Flu': 'Influenza, commonly known as the flu, is a contagious respiratory illness caused by influenza viruses...',
    'Common Cold': 'The common cold is a viral infection of the upper respiratory tract...',
    'Pneumonia': 'Pneumonia is an infection that inflames the air sacs in one or both lungs...',
    'COVID-19': 'COVID-19 is a contagious respiratory illness caused by the novel coronavirus SARS-CoV-2...',
    'Malaria': 'Malaria is a life-threatening disease caused by parasites that are transmitted to people through the bites of infected mosquitoes...',
    'Vertigo (Paroxysmal Positional Vertigo)': 'Vertigo is a sensation of spinning dizziness that occurs when a person is not actually moving...',
    'AIDS': 'Acquired immunodeficiency syndrome (AIDS) is a chronic, potentially life-threatening condition caused by the human immunodeficiency virus (HIV)...',
    'Acne': 'Acne is a skin condition that occurs when your hair follicles become plugged with oil and dead skin cells...',
    'Alcoholic hepatitis': 'Alcoholic hepatitis is a condition caused by excessive drinking of alcohol...',
    'Allergy': 'An allergy is an immune system response to a substance that\'s typically harmless to most people...',
    'Arthritis': 'Arthritis is the swelling and tenderness of one or more of your joints...',
    'Bronchial Asthma': 'Bronchial asthma, often simply called asthma, is a chronic lung disease characterized by inflammation and narrowing of the airways...',
    'Cervical spondylosis': 'Cervical spondylosis is a common, age-related condition that affects the joints and discs in your neck...',
    'Chicken pox': 'Chickenpox is a highly contagious viral infection that causes an itchy rash and red spots or blisters all over the body...',
    'Chronic cholestasis': 'Chronic cholestasis is a condition where the flow of bile from the liver is reduced...',
    'Dengue': 'Dengue is a mosquito-borne viral infection causing a severe flu-like illness and, sometimes causing a potentially lethal complication called severe dengue...',
    'Diabetes': 'Diabetes is a chronic disease that affects how your body turns food into energy...',
    'Dimorphic hemorrhoids (piles)': 'Hemorrhoids are swollen veins in your lower rectum or anus...',
    'Drug Reaction': 'Drug reactions are side effects or adverse effects that occur when taking medication...',
    'Fungal infection': 'Fungal infections are caused by fungi, which are microscopic organisms that can live on the skin...',
    'GERD': 'Gastroesophageal reflux disease (GERD) is a chronic digestive disorder that occurs when stomach acid flows back into the esophagus...',
    'Gastroenteritis': 'Gastroenteritis is inflammation of the stomach and intestines, typically resulting from bacterial toxins or viral infection...',
    'Heart attack': 'A heart attack occurs when the flow of blood to the heart muscle is blocked...',
    'Hepatitis B': 'Hepatitis B is a viral infection that attacks the liver and can cause both acute and chronic disease...',
    'Hepatitis C': 'Hepatitis C is a liver infection caused by the hepatitis C virus...',
    'Hepatitis D': 'Hepatitis D, also known as delta hepatitis, is a serious liver infection caused by the hepatitis D virus...',
    'Hepatitis E': 'Hepatitis E is a liver disease caused by infection with the hepatitis E virus...',
    'Hypertension': 'Hypertension, also known as high blood pressure, is a long-term medical condition in which the blood pressure in the arteries is persistently elevated...',
    'Hyperthyroidism': 'Hyperthyroidism is a condition in which the thyroid gland produces too much of the hormone thyroxine...',
    'Hypoglycemia': 'Hypoglycemia is a condition characterized by an abnormally low level of blood sugar (glucose)...',
    'Hypothyroidism': 'Hypothyroidism is a condition in which the thyroid gland doesn\'t produce enough of certain crucial hormones...',
    'Impetigo': 'Impetigo is a common and highly contagious skin infection that mainly affects infants and children...',
    'Jaundice': 'Jaundice is a condition in which the skin, whites of the eyes, and mucous membranes turn yellow...',
    'Migraine': 'A migraine is a severe headache that can cause intense throbbing or pulsing in one area of the head and is commonly accompanied by nausea, vomiting, and extreme sensitivity to light and sound...',
    'Osteoarthritis': 'Osteoarthritis is the most common form of arthritis, characterized by the breakdown of cartilage in the joints...',
    'Paralysis (brain hemorrhage)': 'Paralysis is a loss of muscle function in part of your body...',
    'Peptic ulcer disease': 'Peptic ulcer disease is a painful condition in which open sores develop on the lining of the stomach, small intestine, or esophagus...',
    'Psoriasis': 'Psoriasis is a common skin condition that speeds up the life cycle of skin cells, causing them to build up rapidly on the surface of the skin...',
    'Tuberculosis': 'Tuberculosis (TB) is an infectious disease usually caused by Mycobacterium tuberculosis (MTB) bacteria...',
    'Typhoid': 'Typhoid fever is a bacterial infection that can lead to a high fever, diarrhea, and vomiting...',
    'Urinary tract infection': 'A urinary tract infection (UTI) is an infection in any part of your urinary system, including your kidneys, ureters, bladder, and urethra...',
    'Varicose veins': 'Varicose veins are gnarled, enlarged veins, most commonly appearing in the legs and feet...',
    'Hepatitis A': 'Hepatitis A is a highly contagious liver infection caused by the hepatitis A virus...'
    # Add information for other diseases similarly
}

# Define a dictionary to store information for each medicine
medicine_info_dict = {
    'Paracetamol': 'Paracetamol, also known as acetaminophen, is a medication used to treat pain and fever...',
    'Ibuprofen': 'Ibuprofen is a medication in the nonsteroidal anti-inflammatory drug class that is used for treating pain, fever, and inflammation...',
     'Aspirin': 'Aspirin, also known as acetylsalicylic acid (ASA), is a medication used to reduce pain, fever, or inflammation...',
    'Omeprazole': 'Omeprazole, sold under the brand names Prilosec and Losec, is a medication used in the treatment of gastroesophageal reflux disease...',
    'Metformin': 'Metformin, sold under the brand name Glucophage among others, is a medication used to treat type 2 diabetes...',
    'Atorvastatin': 'Atorvastatin, sold under the brand name Lipitor, is a medication used to prevent cardiovascular disease in those at high risk and to treat abnormal lipid levels...',
    'Simvastatin': 'Simvastatin, sold under the brand name Zocor among others, is a medication used to decrease high cholesterol and triglycerides levels in the blood...',
    'Levothyroxine': 'Levothyroxine, also known as L-thyroxine, is a manufactured form of the thyroid hormone thyroxine (T4)...',
    'Metoprolol': 'Metoprolol, sold under the brand name Lopressor among others, is a medication used to treat high blood pressure, chest pain due to poor blood flow to the heart, and a number of conditions involving an abnormally fast heart rate...',
    'Losartan': 'Losartan, sold under the brand name Cozaar among others, is a medication used to treat high blood pressure, heart failure, and diabetic kidney disease...',
    'Amlodipine': 'Amlodipine, sold under the brand name Norvasc among others, is a medication used to treat high blood pressure and coronary artery disease...',
    'Lisinopril': 'Lisinopril, sold under the brand name Prinivil among others, is a medication used to treat high blood pressure, heart failure, and to improve survival after heart attack...',
    'Clopidogrel': 'Clopidogrel, sold under the brand name Plavix among others, is a medication used to reduce the risk of heart disease and stroke in those at high risk...',
    'Alprazolam': 'Alprazolam, sold under the brand name Xanax among others, is a medication primarily used for the short-term relief of symptoms of anxiety disorders...',
    'Metronidazole': 'Metronidazole, sold under the brand name Flagyl among others, is an antibiotic and antiprotozoal medication...',
    'Amoxicillin': 'Amoxicillin, also spelled amoxycillin, is an antibiotic used to treat bacterial infections, including bronchitis, pneumonia, and infections of the ear, nose, throat, skin, and urinary tract...',
    'Ciprofloxacin': 'Ciprofloxacin is an antibiotic used to treat a number of bacterial infections, including urinary tract infections, sinus infections, pneumonia, gonorrhea, and others...',
    'Doxycycline': 'Doxycycline is an antibiotic used to treat a wide range of infections, including respiratory tract infections, urinary tract infections, and sexually transmitted infections...',
    'Prednisone': 'Prednisone is a corticosteroid medication used to treat a variety of conditions, including allergic disorders, skin conditions, ulcerative colitis, arthritis, lupus, psoriasis, and breathing disorders...',
    'Tramadol': 'Tramadol, sold under the brand name Ultram among others, is an opioid pain medication used to treat moderate to moderately severe pain...',
    'Omeprazole': 'Omeprazole, sold under the brand names Prilosec and Losec, is a medication used in the treatment of gastroesophageal reflux disease...',
    'Citalopram': 'Citalopram, sold under the brand name Celexa among others, is an antidepressant medication used to treat major depressive disorder, panic disorder, and obsessive-compulsive disorder...',
    'Venlafaxine': 'Venlafaxine, sold under the brand name Effexor among others, is an antidepressant medication used to treat major depressive disorder, generalized anxiety disorder, panic disorder, and social phobia...',
    'Warfarin': 'Warfarin, sold under the brand name Coumadin among others, is a medication that is used as an anticoagulant (blood thinner)...',
    'Fluoxetine': 'Fluoxetine, sold under the brand names Prozac and Sarafem among others, is an antidepressant of the selective serotonin reuptake inhibitor (SSRI) class...',
    'Amitriptyline': 'Amitriptyline, sold under the brand name Elavil among others, is a medication used to treat a number of mental illnesses...',
    # Add information for other medicines similarly
}

def searching(request):
    query = request.GET.get('query', '')
    option = request.GET.get('option', 'disease')
    suggestions = []

    if option == 'disease':
        # Filter disease suggestions based on the query
        for disease, info in disease_info_dict.items():
            if query.lower() in disease.lower():
                suggestions.append({'disease': disease, 'info': info})
    elif option == 'medicine':
        # Filter medicine suggestions based on the query
        for medicine, info in medicine_info_dict.items():
            if query.lower() in medicine.lower():
                suggestions.append({'medicine': medicine, 'info': info})

    return JsonResponse({'suggestions': suggestions})

def get_info(request):
    query = request.GET.get('query', '')
    option = request.GET.get('option', 'disease')
    info = ''

    if option == 'disease':
        info = disease_info_dict.get(query, 'No information available')
    elif option == 'medicine':
        info = medicine_info_dict.get(query, 'No information available')

    return JsonResponse({'info': info})
