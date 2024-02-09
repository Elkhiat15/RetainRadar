

def app(X_train, st, option_menu, pd, pickle):
    with open("logreg_model.sav", 'rb') as file:
        model = pickle.load(file)

    st.title('Check the Risk')
    styles = {
        "icon": { "font-size": "12px"}, 
        "nav-link": {"font-size": "12px","font-family": "Monospace, Arial" ,"--hover-color": "rgba(255, 99, 71, 0.6)"},
        "nav-link-selected": {"background-color": "red","font-family": "Monospace , Arial" },
    }

    ##__________________________ Prediction Form ______________________
    with st.form('Emploee Features'):
            
        ##______________________ Section 1 ____________________________
        cc1,cc2 = st.columns([1,2])
        with cc1:
            st.markdown('Marital Status')
            Marital = option_menu(None,
                            options = ['Single', 'Married', 'Divorced'],
                             menu_icon="::",
                        icons=["::", "::", "::"],
                        styles=styles,
                       default_index=0 )
            
            st.markdown('Overtime')
            Overtime = option_menu(None,
                            options = ['No', 'Yes'],
                        menu_icon="::",
                        icons=["::" ,"::"],
                        styles=styles,
                            default_index=0 )
        
            st.markdown('Stock Option Level')    
            Stock = option_menu(None,
                            options = ['Low', 'Medium','High', 'Very High'],
                        menu_icon="::",
                        icons=["emoji-frown-fill", "emoji-neutral-fill", "emoji-smile-fill", "emoji-grin-fill"],
                        styles=styles,
                            default_index=0 )

        with cc2:
            Age =   st.slider('Age',
                    min_value=X_train["Age"].min(),
                    max_value=X_train["Age"].max(),
                    value=int(X_train["Age"].mean()))
            
            Daily = st.slider('Daily Rate',
                        min_value=X_train["DailyRate"].min(),
                        max_value=X_train["DailyRate"].max(),
                        value=int(X_train["DailyRate"].mean()))
            
            Distance = st.slider('Distance from Home',
                        min_value=X_train["DistanceFromHome"].min(),
                        max_value=X_train["DistanceFromHome"].max(),
                        value=int(X_train["DistanceFromHome"].mean()))
                        
            Training = st.slider('Training Times Last Year',
                        min_value=X_train["TrainingTimesLastYear"].min(),
                        max_value=X_train["TrainingTimesLastYear"].max(),
                        value=int(X_train["TrainingTimesLastYear"].mean()))
                        
            Income = st.slider('Monthly Income',
                            min_value=X_train["MonthlyIncome"].min(),
                            max_value=X_train["MonthlyIncome"].max(),
                            value=int(X_train["MonthlyIncome"].mean()))
                            
            TotWorking = st.slider('Total Working Years',
                            min_value=X_train["TotalWorkingYears"].min(),
                            max_value=X_train["TotalWorkingYears"].max(),
                            value=int(X_train["TotalWorkingYears"].mean()))
                            
            Current = st.slider('Years in Current Role',
                            min_value=X_train["YearsInCurrentRole"].min(),
                            max_value=X_train["YearsInCurrentRole"].max(),
                            value=int(X_train["YearsInCurrentRole"].mean()))

        ##______________________ Section 2 ____________________________
        ccc1,ccc2 = st.columns(2)
        with ccc1:               
            Travel = st.selectbox('Business Travel',
                        X_train["BusinessTravel"].unique(),
                        index= 0)
            
            Department = st.selectbox('Department',
                        X_train["Department"].unique(),
                        index= 0)
        with ccc2:    
            EducationField = st.selectbox('Education Field',
                        X_train["EducationField"].unique(),
                        index= 0)
            
            JobLevel = st.selectbox('Job Level',
                        X_train["JobLevel"].unique(),
                        index= 0)
        
        JobRole = st.selectbox('Job Role',
                    X_train["JobRole"].unique(),
                    index= 0)

        ##______________________ Section 3 ____________________________
        st.subheader('Satisfaction Rates')
        c1,c2,c3,c4 =  st.columns(4)
        with c1:
            st.markdown('Environment')
            Environment = option_menu(None,
                        options = ['Low', 'Medium','High', 'Very High'],
                        menu_icon="::",
                        icons=["emoji-frown-fill", "emoji-neutral-fill", "emoji-smile-fill", "emoji-grin-fill"],
                        styles= styles,
                        key = 0,
                        default_index=0 )
        with c2:
            st.markdown('Work-Life Balance')
            Work = option_menu(None,
                        options = ['Low', 'Medium','High', 'Very High'],
                        menu_icon="::",
                        icons=["emoji-frown-fill", "emoji-neutral-fill", "emoji-smile-fill", "emoji-grin-fill"],
                        styles = styles,
                        key = 1,
                        default_index=0 )
        with c3:
            st.markdown('Relationship')
            Relationship = option_menu(None,
                        options = ['Low', 'Medium','High', 'Very High'],
                        menu_icon="::",
                        icons=["emoji-frown-fill", "emoji-neutral-fill", "emoji-smile-fill", "emoji-grin-fill"],
                        styles=styles,
                        key = 2,
                        default_index=0 )
        
        with c4:
            st.markdown('Job')
            Job = option_menu(None,
                        options = ['Low', 'Medium','High', 'Very High'],
                        menu_icon="::",
                        icons=["emoji-frown-fill", "emoji-neutral-fill", "emoji-smile-fill", "emoji-grin-fill"],
                        styles=styles,
                        key = 3,
                        default_index=0 )

        ##______________________ Prediction and Subimition ____________________________

        data={
            'Age':Age,
            'BusinessTravel':Travel,
            'DailyRate':Daily,
            'Department':Department,
            'DistanceFromHome' :Distance,
            'EducationField':EducationField,
            'EnvironmentSatisfaction':Environment,
            'JobLevel':JobLevel,
            'JobRole':JobRole, 
            'JobSatisfaction':Job,
            'MaritalStatus':Marital,
            'MonthlyIncome':Income,
            'OverTime':Overtime,
            'RelationshipSatisfaction':Relationship,
            'StockOptionLevel':Stock,
            'TotalWorkingYears':TotWorking,
            'TrainingTimesLastYear':Training,
            'WorkLifeBalance':Work,
            'YearsInCurrentRole':Current
        }
        singleData=pd.DataFrame(data,index=[0])
        prediction = model.predict_proba(singleData)[:, 1][0]
        
        s1,s2 = st.columns(2)
        s1.subheader('')
        submited = s1.form_submit_button("Submit")
        if submited:
            if prediction > 0.4:
                st.error('Your employee is about to quit!')
                s2.metric("Probability",round(prediction, 4), "Strong", delta_color='inverse')
                Risk ="Strong"
            elif prediction > 0.3:
                st.warning('Take care of your employee')
                s2.metric("Probability",round(prediction, 4), "Medium", delta_color='off')
            else:
                st.balloons()
                s2.metric("Probability",round(prediction, 4), "-Weak", delta_color='inverse')
                 

