import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from scipy import stats
def app(df, st):
    #_________________________ Helper Functions __________________________    
    def PlotPies(st=""):
        '''Plot four beside pie charts.'''
        bus=df.groupby([st,'Attrition'],as_index=False)['Age'].count()
        bus.rename(columns={'Age':'Count'},inplace=True)
        fig=go.Figure()
        fig = make_subplots(rows=1, cols=4,
                            specs=[[{"type": "pie"}, {"type": "pie"},{"type": "pie"}, {"type": "pie"}]],
                            subplot_titles=('Very High', 'High','Medium','Low'))

        fig.add_trace(
            go.Pie(values=bus[bus[st]=='Very High']['Count'], labels=bus[bus[st]=='Very High']['Attrition'],
                   pull=[0,0.1],showlegend=False)
                   ,row=1,col=1)
        fig.add_trace(
            go.Pie(values=bus[bus[st]=='High']['Count'], labels=bus[bus[st]=='High']['Attrition'],
                   pull=[0,0.1],showlegend=False)
                   ,row=1,col=2)
        fig.add_trace(
            go.Pie(values=bus[bus[st]=='Medium']['Count'], labels=bus[bus[st]=='Medium']['Attrition'],
                   pull=[0,0.1],showlegend=False)
                   ,row=1,col=3)
        fig.add_trace(
            go.Pie(values=bus[bus[st]=='Low']['Count'], labels=bus[bus[st]=='Low']['Attrition'],
                   pull=[0,0.1],showlegend=True)
                   ,row=1,col=4)

        fig.update_layout(template='plotly',showlegend=True,
                        legend_title_text="Attrition",title_text=f"Employee Attrition based on {st}",
                        font_family="Times New Roman",title_font_family="Times New Roman")
        return fig

    #____________________________________ Some Metrics _________________________
    st.title("Employees Analytics")

    col1, col2, col3, col4 = st.columns(4)
    col1.metric(":red[Total Employees]", len(df))
    col2.metric(":red[Males]", len(df[df['Gender'] == 'Male']))
    col3.metric(":red[Females]", len(df[df['Gender'] == 'Female']))
    col4.metric(":red[Attrition Rate]", "16.12%")

    #____________________________________ Sample of data  _______________________
    btn = st.button("Show Sample")
    if btn:
        st.dataframe(df.iloc[:, : - 2].sample(5))

    #____________________________________ Bar Plots _________________________
    st.header("Counts and Percentages")
    c1, c2 = st.columns(2)
    selected = c1.selectbox('Select', ['JobRole' , 'JobLevel', 'Department',
                                       'EducationField','MaritalStatus','Education'])
    colored = c2.selectbox('Filter By', ['Attrition' , 'JobSatisfaction', 'EnvironmentSatisfaction',
                                         'WorkLifeBalance','RelationshipSatisfaction'])

    subData = df.groupby([selected, colored])["Age"].count().reset_index(name='Counts')
    fig =px.bar(subData, y ="Counts", x =selected,color=colored, template='plotly',
                title=f"{selected} with {colored}")
    st.plotly_chart(fig, use_container_width=True)
   
    #____________________________________ Box Plots _________________________
    st.header("Distributions by defferent aspects")
    cc1, cc2, cc3 = st.columns(3)

    Numerical = cc1.selectbox('Select', ['Age','DistanceFromHome', 'MonthlyIncome', 'YearsAtCompany'])
    Category = cc2.selectbox('Filter By', ['Attrition' , 'OverTime', 'JobSatisfaction',
                                          'JobRole' , 'JobLevel', 'Department',
                                       'EducationField','MaritalStatus','Education',
                                         'WorkLifeBalance'])
    By = cc3.selectbox('Select', [None, 'Attrition','OverTime'])
    if Category == By :
        By = None

    fig =px.box(df, x=Category, y=Numerical, color=By, template='plotly',
                title=f"{Numerical} distribution by different {Category}s")
    st.plotly_chart(fig, use_container_width=True)

    #____________________________________ Pie Plots _________________________
    st.header("Satisfaction and work life balance rates")
    sel = st.selectbox('Choose', ['JobSatisfaction','EnvironmentSatisfaction',
                            'RelationshipSatisfaction', 'WorkLifeBalance'
                              ])

    fig =PlotPies(sel)
    st.plotly_chart(fig, use_container_width=True)


    #____________________________________ Scatter with Correlation  __________
    st.header("Correlation Between numerical features")
    ccc1, ccc2, ccc3, ccc4 = st.columns(4)

    Numerical1 = ccc1.selectbox('Between', options=[ 'Age' ,'YearsAtCompany','MonthlyIncome'])
    Numerical2 = ccc2.selectbox('And', options=['MonthlyIncome' ,'Age','YearsAtCompany'])
    By2 = ccc3.selectbox('Filtered By', options=[None, 'Attrition','OverTime', 'Department'])

    Corr = round(stats.pearsonr(df[Numerical1], df[Numerical2]).statistic , 4)
    ccc4.metric("Correlation", Corr)

    fig = px.scatter( df, x= Numerical1, y=Numerical2, color=By2, trendline='ols'
                    , opacity=0.5,template='plotly',
                    title=f'Correlation between {Numerical} and {Numerical2}')
    st.plotly_chart(fig, use_container_width=True)
