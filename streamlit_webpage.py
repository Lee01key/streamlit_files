import matplotlib.pyplot as plt
import pandas as pd
import pickle
import streamlit as st


page_config = st.set_page_config(
    page_icon='💊',
    page_title="Pops! Diabetes CARE",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.image('./data/image/main_page/logo.jpg')


page = st.sidebar.selectbox(
    'Select Page',
    ['MAIN', 'SVI', 'NLP', 'YODA', 'SENTIMENT', 'DRUG'],
)
if page == 'MAIN':
    meet_our_team = '<b><p style="font-size: 30px; line-height: 1"> 💊 MEET OUR AWESOME TEAM</b>'
    st.markdown(meet_our_team, unsafe_allow_html=True)
    st.image('./data/image/main_page/meet_our_team.png')
    
    space = '<br><br><br><br><br><br><br><br>'
    st.markdown(space, unsafe_allow_html=True)
    overview = '<b><p style="font-size: 30px; line-height: 1"> 💊 PROJECT OVERVIEW/ PROBLEM STATEMENT</b>'
    st.markdown(overview, unsafe_allow_html=True)
    st.image('./data/image/main_page/overview.png')
    
    space = '<br><br><br><br><br><br><br><br>'
    st.markdown(space, unsafe_allow_html=True)
    
    workflow = '<b><p style="font-size: 30px; line-height: 1"> 💊 PROJECT WORKFLOW</b>'
    st.markdown(workflow, unsafe_allow_html=True)
    st.image('./data/image/main_page/workflow.png')

elif page == 'SVI':
    
    space = '<br><br><br>'
    st.markdown(space, unsafe_allow_html=True)
    svi_definition = '<b><p style="font-size: 30px; line-height: 1"> 💊 Socially Vulnerable Index (SVI) </b>'
    st.markdown(svi_definition, unsafe_allow_html=True)  
    svi_content = '<li style="font-size: 25px; line-height: 1.5"> CDC/ATSDR used US Census Data to calculate a county’s socially vulnerable index </li> <li style="font-size: 25px; line-height: 1.5"> SVI “refers to the potential negative effects on communities caused by external stresses on human health.” </li> <li style="font-size: 25px; line-height: 1.5"> These features include the number of a county’s population, determined to be more vulnerable by the CDC. This includes features such as non-white ethnicities, non-primarily English speaking, unemployed, disabilities, no high school education, and more. </li></b>'
    st.markdown(svi_content, unsafe_allow_html=True)  

    space = '<br><br><br><br><br><br><br><br><br><br><br>'
    st.markdown(space, unsafe_allow_html=True)
    
    overlap_svi_diabetes = '<b><p style="font-size: 30px; line-height: 1"> 💊 Overlap between Overall percentile ranking for SVI and Average Diabetes Rate</b>'
    st.markdown(overlap_svi_diabetes, unsafe_allow_html=True)  


    diabetes_map = './data/image/svi_image/diabetes_rate_geomap.png'
    svi_map = './data/image/svi_image/svi_rates_geomap.png'
    maps_image = [diabetes_map, svi_map]
    st.image(maps_image, width = 500)
    
    st.image('./data/image/svi_image/diabetes_rate_geomap.png')
    st.image('./data/image/svi_image/svi_rates_geomap.png')


    space = '<br><br><br><br><br><br><br><br>'
    st.markdown(space, unsafe_allow_html=True)
    
    model_performance = '<b><p style="font-size: 30px; line-height: 1"> 💊 Modeling, and Modeling Performance</b>'
    st.markdown(model_performance, unsafe_allow_html=True)  
    
    model_performance_bp = '<li style="font-size: 25px; line-height: 1.5">  Regression: 65% </li> <li style="font-size: 25px; line-height: 1.5">  Classification for above median diabetes rates among counties - 65% </li> <li style="font-size: 25px; line-height: 1.5">  SVI data alone not likely to predict population’s diabetes rate </li></b>'
    st.markdown(model_performance_bp, unsafe_allow_html=True)  
    space = '<br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br>'
    st.markdown(space, unsafe_allow_html=True)
    
    check_correlations = '<b><p style="font-size: 30px; line-height: 1"> 💊 Checking Correlations for Counties with Diabetes Rates Above 20% of Population</b>'
    st.markdown(check_correlations, unsafe_allow_html=True)  
    st.image('./data/image/svi_image/outliers.png')    
    st.markdown(space, unsafe_allow_html=True)

    st.image('./data/image/svi_image/correlations.png', width = 800)
    
    
elif page == 'NLP':
    nlp_wordcloud = '<b><p style="font-size: 30px; line-height: 1"> 💊 Wordcloud: Most frequent words</b>'
    st.markdown(nlp_wordcloud, unsafe_allow_html=True)  
    st.image('./data/image/nlp_image/wordcloud_white.png', width = 600)
    
    nlp_top25 = '<b><p style="font-size: 30px; line-height: 1"> 💊 Top 25 most frequent words: Reddit r/diabetes user </b>'
    st.markdown(nlp_top25, unsafe_allow_html=True)  
    st.image('./data/image/nlp_image/50freqwords.png')
    
    nlp_bigram = '<b><p style="font-size: 30px; line-height: 1"> 💊 Top 25 Bigrams: Reddit r/diabetes user </b>'
    st.markdown(nlp_bigram, unsafe_allow_html=True)  
    st.image('./data/image/nlp_image/bigram25.png')

    nlp_trigram = '<b><p style="font-size: 30px; line-height: 1"> 💊 Top 25 Trigrams: Reddit r/diabetes user </b>'
    st.markdown(nlp_trigram, unsafe_allow_html=True)  
    st.image('./data/image/nlp_image/trigram25.png')


    



elif page == 'YODA':
    
    import chatterbot
    import streamlit as st
    from chatterbot import ChatBot
    from chatterbot.logic import LogicAdapter, BestMatch
    from chatterbot.trainers import ListTrainer, ChatterBotCorpusTrainer

    import os
    
    yoda = ChatBot('yoda')

    yoda = ChatBot(
        'yoda',
    
        storage_adapter='chatterbot.storage.SQLStorageAdapter',
    
        database_uri='sqlite:///database.sqlite3',
    
        preprocessors=[
            'chatterbot.preprocessors.clean_whitespace',
            'chatterbot.preprocessors.unescape_html',
            'chatterbot.preprocessors.convert_to_ascii'
            ],
    
        logic_adapters=[
                {

                'import_path': 'chatterbot.logic.BestMatch',
                'default_response': 'I am sorry, but I do not understand.',
                'maximum_similarity_threshold': 0.90,
            '   statement_comparison_function': 'chatterbot.comparisons.LevenshteinDistance',
            
            }
        ]
     
    )

    trainer_corpus = ChatterBotCorpusTrainer(yoda)
    trainer_corpus.train("chatterbot.corpus.english.greetings", 
                         "chatterbot.corpus.english.conversations")
    
    trainer = ListTrainer(yoda)

    trainer.train([

        'Online diabetes support',
        
        'Eat Smart, Move More, Prevent Diabetes (Online) https://esmmpreventdiabetes.com/ SinfoniaRx https://www.sinfoniarx.com/preventdiabetes, (844) 326-3043, preventdiabetes@trhc.com Online with flexible class times, Harris Teeter https://www.mywelsana.com/ (888) 246-4520, 4) BeMeta Health (301) 648-4202.'
     
        
    ])
    
    trainer.train([

        'May the force be with you',
        'May the Force be with you'
        
        
    ])
    
    
    trainer.train([
        'Any diabetes center in Jones, NC?',
        'There is Free/Low-Cost Class: 418 NC Hwy. 58 N. Unit C / Trenton, North Carolina  28585 | http://www.jonescountyhealth.com | (252) 448-9111',
        
        'How can I see diabetes doctor in Jones, NC?',
        '1) Carteret Health Care: 500 Arendell St, Morehead City, NC 28557, 2) Onslow Memorial Hospital: 317 Western Blvd, Jacksonville, NC 28546, 3) Naval Hospital Camp Lejeune: 100 Brewster Blvd, Camp Lejeune, NC 28547, 4) UNC Lenoir Health Care: 100 Airport Rd, Kinston, NC 28501, 5) Vidant Medical Center: 2100 Stantonsburg Rd, Greenville, NC 27834, 6) Pitt County Memorial Hospital, 2100 Stantonsburg Rd, Greenville, NC 27834, 7) Wayne UNC Health Care: 2700 Wayne Memorial Dr, Goldsboro, NC 27534'
    ])
    
    trainer.train([
        'Any diabetes center in Bullock, AL?',
        'The Health Care Authority for Baptist Health, An Affiliate of UAB Health System. Address: 4371 Narrow Lane Road, Suite 200, Montgomery, AL 36116 | Phone Number 334-747-7700 | Baptist Health Center for Diabetes.',


    ])

    trainer.train([
        'Any diabetes center in Tippah, MS?',
        '1) Magnolia Regional Health Center | 3704 hwy 72 west, corinth, MS 38834 | Phone Number 662-665-8041 2) Duncan\'s Pharmacy | 28271 Highway 15, Walnut, MS 38683 | Phone Number (662) 223-4727.'
    ])



    trainer.train([
        'Do or not.',
        'There is no try.',
        
        'Size matters not.',
        'Look at me. Judge me by my size, do you?'
    ])

    trainer.train([
        
        'Who are you?',
        'I am YODA, your own diabetes assistant.',


        'What can you do?',
        'I will help you with diabetes',
    
    
        'What is diabetes?',
        'Diabetes is a disease in which blood glucose (sugar) levels are above normal. Plant foods which are mostly sugars and starches (carbohydrates) are turned into glucose, or sugar, for our bodies to use for energy. The pancreas, an organ that lies near the stomach, makes a hormone called insulin to help glucose get into the cells of our bodies. When you have diabetes, your body either does not make enough insulin or cannot use its own insulin as well as it should. This causes sugar to build up in your blood. Diabetes can cause serious health complications including heart disease, blindness, kidney failure, and lower-extremity amputations. Diabetes is the 6th leading cause of death in the United States.',
    
        'What are the types of diabetes?',
        'There are three. Type 1 diabetes, Type 2 diabetes, and Gestational diabetes.',
    
        'What is prediabetes?',
        'A person with prediabetes has a blood sugar level higher than normal, but not high enough for a diagnosis of diabetes. He or she is at higher risk for developing type 2 diabetes and other serious health problems, including heart disease, and stroke. Without lifestyle changes to improve their health, 15% to 30% of people with prediabetes will develop type 2 diabetes within five years.'])
    
    
       
   
    trainer.train([
        'Any diabetes center in Jones, NC?',
        'There is Free/Low-Cost Class: 418 NC Hwy. 58 N. Unit C / Trenton, North Carolina  28585 | http://www.jonescountyhealth.com | (252) 448-9111',
        
        'How can I see diabetes doctor in Jones, NC?',
        '1) Carteret Health Care: 500 Arendell St, Morehead City, NC 28557, 2) Onslow Memorial Hospital: 317 Western Blvd, Jacksonville, NC 28546, 3) Naval Hospital Camp Lejeune: 100 Brewster Blvd, Camp Lejeune, NC 28547, 4) UNC Lenoir Health Care: 100 Airport Rd, Kinston, NC 28501, 5) Vidant Medical Center: 2100 Stantonsburg Rd, Greenville, NC 27834, 6) Pitt County Memorial Hospital, 2100 Stantonsburg Rd, Greenville, NC 27834, 7) Wayne UNC Health Care: 2700 Wayne Memorial Dr, Goldsboro, NC 27534'
    ])
    
    trainer.train([
        'Any diabetes center in Bullock, AL?',
        'The Health Care Authority for Baptist Health, An Affiliate of UAB Health System. Address: 4371 Narrow Lane Road, Suite 200, Montgomery, AL 36116 | Phone Number 334-747-7700 | Baptist Health Center for Diabetes.',


    ])
    
    trainer.train([
        'What are most affordable drugs for diabetes?',
        'Here are the most affordable drugs: they are all Less than 10: Glucotrol XL oral,Glucotrol oral, glipizide oral',


    ])
    
    trainer.train([
        'What are other affordable drugs for diabetes?',
        'Here are the other affordable drugs: they are between 10 - 20:  pioglitazone oral, metformin oral, glyburide-metformin oral, glyburide oral, glimepiride oral, acarbose oral, Precose oral, Prandin oral,Micronase oral,Glucophage oral, Glucovance oral, Amaryl oral, Actos oral',


    ])
    
    trainer.train([
        'Are there other drugs for diabetes?',
        'Here are the most affordable drugs: Between 20-30: nateglinide oral, Pioglitazone / Metformin, Starlix oral,Between 30-40: glipizide-metformin oral, Between 40-50: Humalog KwikPen subcutaneous, Humalog subcutaneous',


    ])
    
    trainer.train([
        'Are there more drug options for diabetes?',
        'Here are more drug optons: Between 50- 100: Fortamet oral, Glumetza oral, Humalog Mix 75-25 KwikPen subcutaneous, Humalog Mix 75-25 subcutaneous, Humulin 70-30 subcutaneous, Novolog Flexpen subcutaneous, Novolog Mix 70-30 FlexPen subcutaneous, Novolog subcutaneous',


    ])
    
    trainer.train([
        'What are more expensive drug options for diabetes?',
        'Between 100- 200: Admelog U-100 Insulin lispro subcutaneous, UETACT oral, Lantus subcutaneous, Novolin R injection, Oseni oral, Riomet oral, Between 200- 500: Jentadueto oral, Kombiglyze XR oral, Levemir FlexTouch subcutaneous,Levemir Flexpen subcutaneous, Levemir subcutaneous, Onglyza ora, Toujeo SoloStar subcutaneous, Tradjenta oral',


    ])
    
    trainer.train([
        'What are most expensive drug options for diabetes?',
        'Over 500: sitagliptin oral, Xigduo XR oral, Victoza 3-Pak subcutaneous, Victoza 2-Pak subcutaneous, Trulicity, Synjardy oral, Ozempic subcutaneous, Jardiance oral, Januvia oral, Janumet oral, Janumet XR oral, Invokana oral, Invokamet oral, Glyxambi oral, Glucophage XR oral, Farxiga oral, Byetta subcutaneous, Apidra subcutaneous, Afrezza inhalation, Actoplus MET oral',


    ])
    
    trainer.train([
        'What are Diabetes Symptoms ?',
        'Urinate (pee) a lot, often at night; Are very thirsty; Lose weight without trying; Are very hungry; Have blurry vision; Have numb or tingling hands or feet; Feel very tired; Have very dry skin; Have sores that heal slowly; Have more infections than usual. If you have any of the  diabetes symptoms, see your doctor about getting your blood tests',


    ])
    
    trainer.train([
        'What is prediabetes?',
        'Prediabetes means a person\'s blood glucose (sugar) level is higher than normal. People with prediabetes can get type 2 diabetes. They can also get other health problems, such as stroke and heart attack',


    ])
    
    trainer.train([
        'What are the symptoms and signs of prediabetes??',
        'There are usually no signs when you have prediabetes. You can have prediabetes for years and not know. Many people don\'t know they have prediabetes until more serious health problems show up. All the more reason to take the online risk test and talk to your doctor.',


    ])
    
    trainer.train([
        'Who is most at risk for prediabetes and type 2 diabetes?',
        'If any of these apply to you, you’re at risk for prediabetes and type 2 diabetes: I have a family history of type 2 diabetes; I am over age 40; I am overweight; I had gestational diabetes (diabetes when pregnant) or high blood sugar when pregnant; I have high blood pressure; I am Hispanic, African American, Asian, or Native American.'


    ])
    
    trainer.train([
        'What is DSMES?',
        'Diabetes Self-Management Education and Support (DSMES) services help people with diabetes learn how to take the best care of themselves. DSMES services will help you: Make better decisions about your diabetes. Work with your health care team to get the support you need. Understand how to take care of yourself and learn the skills to: Eat healthy. Be active. Check your blood sugar (glucose). Take your medicine. Solve problems. Cope with the emotional side of diabetes. Reduce your risk of other health problems.'


    ])
    
    trainer.train([
        'What is Insulin therapy?',
        'If you have type 1 diabetes, insulin therapy is vital for replacing the insulin your body doesn\'t produce. Sometimes, people with type 2 diabetes or gestational diabetes need insulin therapy if other treatments haven\'t been able to keep blood glucose levels within the desired range. Insulin therapy helps prevent diabetes complications by keeping your blood sugar within your target range.',


    ])
    
    
    trainer.train([
        'What is Metformin?',
        'Metformin is one of the best drugs to treat diabetes, it is very affordable, it used with a proper diet and exercise program and possibly with other medications to control high blood sugar. It is used in patients with type 2 diabetes. Controlling high blood sugar helps prevent kidney damage, blindness, nerve problems, loss of limbs, and sexual function problems. Proper control of diabetes may also lessen your risk of a heart attack or stroke. Metformin works by helping to restore your body\'s proper response to the insulin you naturally produce. It also decreases the amount of sugar that your liver makes and that your stomach/intestines absorb.',


    ])
    
    
    
    trainer.train([
        'What is Glipizide?',
        'Glipizide is one of the best drugs to treat diabetes, it is very affordable, it is used with a proper diet and exercise program to control high blood sugar in people with type 2 diabetes. It may also be used with other diabetes medications. Controlling high blood sugar helps prevent kidney damage, blindness, nerve problems, loss of limbs, and sexual function problems. Proper control of diabetes may also lessen your risk of a heart attack or stroke. Glipizide belongs to the class of drugs known as sulfonylureas. It lowers blood sugar by causing the release of your body\'s natural insulin.',


    ])
    
    trainer.train([
        'What is Glimepiride?',
        'Glimepiride is used with a proper diet and exercise program to control high blood sugar in people with type 2 diabetes. It may also be used with other diabetes medications. Controlling high blood sugar helps prevent kidney damage, blindness, nerve problems, loss of limbs, and sexual function problems. Proper control of diabetes may also lessen your risk of a heart attack or stroke. Glimepiride belongs to the class of drugs known as sulfonylureas. It lowers blood sugar by causing the release of your body\'s natural insulin.',


    ])
    
    trainer.train([
        'What is Invokana?',
        'Genetic name is Canagliflozin, it is used with a proper diet and exercise program to control high blood sugar in people with type 2 diabetes. Controlling high blood sugar helps prevent kidney damage, blindness, nerve problems, loss of limbs, and sexual function problems. Canagliflozin is also used by people with type 2 diabetes and heart disease to lower the risk of death from heart attack or stroke. Canagliflozin is also used by people with type 2 diabetes and kidney disease to lower the risk of dialysis, death from heart disease, and the need to go to the hospital for heart failure. Canagliflozin works by increasing the removal of sugar by your kidneys.',


    ])
    
    trainer.train([
        'What is Jardiance?',
        'Genetic name is Empagliflozin, it is used with a proper diet and exercise program to control high blood sugar in people with type 2 diabetes. Controlling high blood sugar helps prevent kidney damage, blindness, nerve problems, loss of limbs, and sexual function problems. Empagliflozin is also used in patients with type 2 diabetes and heart disease to lower the risk of death from heart attack or stroke. Empagliflozin works by increasing the removal of sugar by your kidneys. Empagliflozin is also used to treat heart failure. It may help you live longer and lower your risk of going to the hospital for heart failure. Empagliflozin works by increasing the removal of sodium by your kidneys.',


    ])
    
    
    trainer.train([
        'What is Januvia?',
        'Genetic name is Sitagliptin, it is used with a proper diet and exercise program and possibly with other medications to control high blood sugar. It is used in people with type 2 diabetes. Controlling high blood sugar helps prevent kidney damage, blindness, nerve problems, loss of limbs, and sexual function problems. Proper control of diabetes may also lessen your risk of a heart attack or stroke.Sitagliptin is a diabetes drug that works by increasing levels of natural substances called incretins. Incretins help to control blood sugar by increasing insulin release, especially after a meal. They also decrease the amount of sugar your liver makes.',


    ])
    
    trainer.train([
        'What is Pioglitazone?',
        'Pioglitazone is a diabetes drug (thiazolidinedione-type, also called "glitazones") used along with a proper diet and exercise program to control high blood sugar in patients with type 2 diabetes. It works by helping to restore your body\'s proper response to insulin, thereby lowering your blood sugar.Controlling high blood sugar helps prevent kidney damage, blindness, nerve problems, loss of limbs, and sexual function problems. Proper control of diabetes may also lessen your risk of a heart attack or stroke. Pioglitazone is used either alone or in combination with other diabetes medications (such as metformin or a sulfonylurea such as glyburide).Talk to your doctor about the risks and benefits of pioglitazone.',


    ])
    
    
    trainer.train([
        'What is Victoza?',
        'VictozaLiraglutide is used either alone or with other medications, and with a proper diet and exercise program, to control high blood sugar. It is used in people with type 2 diabetes. Controlling high blood sugar helps prevent kidney damage, blindness, nerve problems, loss of limbs, and sexual function problems. Liraglutide is also used in people with type 2 diabetes and heart disease to lower the risk of a heart attack, stroke, or death caused by heart disease. Liraglutide is similar to a natural hormone in your body (incretin). It works by causing insulin release in response to high sugar levels (such as after a meal) and decreasing the amount of sugar your liver makes. Liraglutide is not a substitute for insulin if you require insulin treatment.',


    ])
    
    trainer.train([
        'What is Trulicity?',
        'GENERIC NAME: DULAGLUTIDE. Dulaglutide is used with a proper diet and exercise program to control high blood sugar in people with type 2 diabetes. Controlling high blood sugar helps prevent kidney damage, blindness, nerve problems, loss of limbs, and sexual function problems. This medication is also used to lessen the risk of a major cardiovascular event (such as heart attack or stroke) in people who already have, or are at high risk for heart/blood vessel disease.  Dulaglutide is similar to a natural hormone in your body (incretin). It works by causing insulin release in response to high blood sugar (such as after a meal) and by decreasing the amount of sugar your liver makes. Dulaglutide is not a substitute for insulin if you need insulin treatment.',


    ])
    
    
    trainer.train([
        'What Are Normal Blood Sugar Levels?',
        'They are less than 100 mg/dL after not eating (fasting) for at least 8 hours. And they\'re less than 140 mg/dL 2 hours after eating. During the day, levels tend to be at their lowest just before meals. For most people without diabetes, blood sugar levels before meals hover around 70 to 80 mg/dL. For some people, 60 is normal; for others, 90.',


    ])
    
    trainer.train([
        'What\'s a low blood sugar level?',
        'It varies widely. Many people\'s glucose won\'t ever fall below 60, even with prolonged fasting. When you diet or fast, the liver keeps your levels normal by turning fat and muscle into sugar. A few people\'s levels may fall somewhat lower.',


    ])
    
    trainer.train([
        'What\'s a high sugar level?',
        'Blood sugar levels are considered high if they\'re over 130 mg/dL before a meal or 180 mg/dL within one to two hours after a meal. Many people won\'t start to experience symptoms from high blood sugar until their levels are at 250 mg/dL or higher.',

    ])
    

    
    
        
    space = '<br><br><br>'
    st.markdown(space, unsafe_allow_html=True)
    
    st.image('./data/image/main_page/yoda_intro.png')    

    space = '<br><br><br><br><br><br><br><br>'
    st.markdown(space, unsafe_allow_html=True)
    
    st.image('./data/image/main_page/yoda_sql.png')   
    st.image('./data/image/main_page/sql_storage.png')   
    st.markdown(space, unsafe_allow_html=True)
    st.markdown(space, unsafe_allow_html=True)


    st.image('./data/image/main_page/meet_yoda.png')  
    ##st.image('./data/image/streamlit_chatbot/yoda.png', width = 700)
    request=st.text_input('I sense fear in you: ', max_chars = 500)
    




    st.text_area('YODA:', value = yoda.get_response(request), height = 300, max_chars = None,
                     key = None)
        
elif page == 'SENTIMENT':
    import plotly.graph_objects as go
    df_drug = pd.read_pickle('./sentiment_analysis/sentiment.pkl')
    
    type2 = '<b><p style="font-size: 25px; line-height: 1"> 💊 Type 2 Diabetes Data: Ease of Use, Effectiveness, Satisfaction by Drug Type</b>'
    st.markdown(type2, unsafe_allow_html=True)
    
    st.dataframe(df_drug)
    
    
    hover_text = []
    bubble_size = []

    for index, row in df_drug.iterrows():
        hover_text.append(('Drug: {drug} <br>'+
                            'Effectiveness: {effectiveness} <br>'+
                            'Satisfaction: {satisfaction} <br>'+
                            'Review: {review}').format(drug=row['drug'],
                                            effectiveness=row['effectiveness'],
                                            easeofuse = row['easeofuse'],
                                            satisfaction=row['satisfaction'],
                                            review = row['count']))
        bubble_size.append(row['count'])

    df_drug['text'] = hover_text
    df_drug['count'] = bubble_size
    sizeref = 2.*max(df_drug['count'])/(100**2)

    drug_types = ['pill', 'injection', 'inhaler']
    drug_data = {drug:df_drug.query("type == '%s'" %drug)
                              for drug in drug_types}

    # Graph1
    
    graph1_effectivness = '<b><p style="font-size: 25px; line-height: 1"> 📈 Type 2 Diabetes data: Effectivness and satisfaction</b>'
    st.markdown(graph1_effectivness, unsafe_allow_html=True)


    fig = go.Figure()

    for drug_types, drug in drug_data.items():
        fig.add_trace(go.Scatter(
            x=drug['effectiveness'], y=drug['satisfaction'],
            name=drug_types, text=drug['text'],
            marker_size=df_drug['count'],
            ))

    # Tune marker appearance and layout
    fig.update_traces(mode='markers', marker=dict(sizemode='area',
                                              sizeref=sizeref, line_width=2))

    fig.update_layout(
        title='Effectiveness v. Satisfaction: with Reviews',
        xaxis=dict(
            title='Diabetes: Type 2 Drug Effectiveness',
            gridcolor='white',
            gridwidth=2,
        ),
        yaxis=dict(
            title='Drug Satisfacttion',
            gridcolor='white',
            gridwidth=2,
        ),
        paper_bgcolor='rgb(243, 243, 243)',
        plot_bgcolor='rgb(243, 243, 243)',
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    graph2_easeofuse = '<b><p style="font-size: 25px; line-height: 1"> 📈 Type 2 Diabetes data: Ease of Use and satisfaction</b>'
    st.markdown(graph2_easeofuse, unsafe_allow_html=True)

    fig2 = go.Figure()

    for drug_types, drug in drug_data.items():
        fig2.add_trace(go.Scatter(
            x=drug['easeofuse'], y=drug['satisfaction'],
            name=drug_types, text=drug['text'],
            marker_size=df_drug['count'],
            ))

    # Tune marker appearance and layout
    fig2.update_traces(mode='markers', marker=dict(sizemode='area',
                                              sizeref=sizeref, line_width=2))

    fig2.update_layout(
        title='Ease of Use v. Satisfaction: with Reviews',
        xaxis=dict(
            title='Dibetes: Type 2 Drug Ease of Use',
            gridcolor='white',
            gridwidth=2,
        ),
        yaxis=dict(
            title='Drug Satisfacttion',
            gridcolor='white',
            gridwidth=2,
        ),
        paper_bgcolor='rgb(243, 243, 243)',
        plot_bgcolor='rgb(243, 243, 243)',
    )
    
    st.plotly_chart(fig2, use_container_width=True)
    
    classification_model = '<b><p style="font-size: 25px; line-height: 1"> 📈 Drug satisfaction predition</b>'
    st.markdown(classification_model, unsafe_allow_html=True)
    classification_model_sub = '<b><h2><p style="margin-left: 50px; font-size: 20px; line-height: 1"> ✅ Variables</b>'
    st.markdown(classification_model_sub, unsafe_allow_html=True)
    
    variables = '<li style="margin-left: 100px; font-size: 20px; line-height: 1.5"> Ease of use (1-5 pt) </li> <li style="margin-left: 100px; font-size: 20px; line-height: 1.5">  Effectiveness </li> <li style="margin-left: 100px; font-size: 20px; line-height: 1.5"> (Whether the review was) Helpful </li></b> <li style="margin-left: 100px; font-size: 20px; line-height: 1.5"> Patient status (patient, caregiver) </li> <li style="margin-left: 100px; font-size: 20px; line-height: 1.5"> Gender </li></b><li style="margin-left: 100px; font-size: 20px; line-height: 1.5"> Treatment period </li></b> <li style="margin-left: 100px; font-size: 20px; line-height: 1.5"> Age </li></b> <li style="margin-left: 100px; font-size: 20px; line-height: 1.5"> Vader compound score </li></b>'
    st.markdown(variables, unsafe_allow_html=True)
   
    modeling_methods = '<b><h2><p style="margin-left: 50px; font-size: 20px; line-height: 1"> ✅ Methods</b>'
    st.markdown(modeling_methods, unsafe_allow_html=True)
    
    metrics_result = '<li style="margin-left: 100px; font-size: 20px; line-height: 1.5"> Randomforest: r2 (0.674, 0.648)</li> <li style="margin-left: 100px; font-size: 20px; line-height: 1.5">  Multinomial NB: r2(0.472, 0.464) </li> <li style="margin-left: 100px; font-size: 20px; line-height: 1.5"> GradientBoostingi Classifier: r2 (0.676, 0.663) </li></b>'
    st.markdown(metrics_result, unsafe_allow_html=True)
    
elif page == 'DRUG':
    space = '<br><br><br>'
    st.markdown(space, unsafe_allow_html=True)
    st.image('./data/image/main_page/druginfo.png')

    space = '<br><br><br><br><br><br><br><br><br><br>'
    st.markdown(space, unsafe_allow_html=True)   
    
    import pandas as pd
    import numpy as np
    from scipy import sparse
    from sklearn.metrics.pairwise import pairwise_distances, cosine_distances, cosine_similarity
    import streamlit as st


    
    
    df = pd.read_csv('./data/cleaned/cleaned_df.csv')

    df.dropna(inplace = True)

    sat_df = df[['drug', 'satisfaction', 'reviewer']]

    pivot = pd.pivot_table(sat_df, index='drug', columns='reviewer', values='satisfaction')

    sparse_pivot = sparse.csr_matrix(pivot.fillna(0))

    dists = pairwise_distances(sparse_pivot, metric='cosine')

    similarities = cosine_similarity(sparse_pivot)

    recommender_df = pd.DataFrame(dists, 
                              columns=pivot.index, 
                              index=pivot.index)

    #get drug name
    def name_of_drug(drug):
        return drug

    #get drug satisfiaction
    def satisfaction_drug(drug):
        satisfaction = pivot.loc[drug, :].mean()
        return satisfaction

    def number_of_drug_review(drug):
        number_of_drug_review = pivot.T[drug].count()
        return number_of_drug_review

    def recommended_drug(drug):
        recommended = pd.DataFrame(recommender_df[drug].sort_values()[1:6]).reset_index()
        drug_name_recommended = recommended['drug']
        return drug_name_recommended

    st.image('./data/image/main_page/search_your_drug_info.png')


    drug_inq = st.text_input(f'Hi, what drugs are you currently taking?:', 'Afrezza inhalation')

    st.image('./data/image/drug_image/'+drug_inq+'.jpeg')


    
    st.write(f'💊 You are currently taking {name_of_drug(drug_inq)}.')
    st.write(f'📝 In our system, {number_of_drug_review(drug_inq)} users also treid this medication and left reviews.')

    space = '<br><br><br><br><br><br><br><br>'
    st.markdown(space, unsafe_allow_html=True)   
    
    st.image('./data/image/main_page/check_others_review.png')   
    satisfaction_info = '<b><p style="font-size: 25px; line-height: 1"> 💬 Emotions Associated with this Drug</b>'

    st.markdown(satisfaction_info, unsafe_allow_html=True)

    st.write(f'❤️ Average satisfaction of users taking this drug was {round(satisfaction_drug(drug_inq),2)}/5.')
    st.write(f'Emotions associate with chosen {name_of_drug(drug_inq)}:')
    st.image('./data/image/drug_sentiment_piegraph/'+drug_inq+'.png')
    st.markdown(space, unsafe_allow_html=True)   
    
    st.image('./data/image/main_page/alternative_drug.png')       
    alt_drug = '<b><p style="font-size: 25px; line-height: 1"> 💬 Alternative Drugs you may Consider </b>'
    st.markdown(alt_drug, unsafe_allow_html=True)
    st.write(' ✅ Considering alternative drugs due to side effects? People with same gender, age, treatment period also considered medication below.')
    st.write(recommended_drug(drug_inq))

    st.markdown(space, unsafe_allow_html=True)   

    

elif page == 'Make a prediction':
    st.subheader('Which author do you write like?')

    st.write('''
Enter some text to make a prediction!''')
