import streamlit as st
import pandas as pd
import altair as alt
from PIL import Image
import numpy as np


st.title("Dean's Recovery Contest App:eggplant:")

image = Image.open('Dean.PNG')

st.image(image, caption='Dean Before His Life-Altering Surgery')

#st.write(
#    "The Contest Began Monday at 12:00 AM ✨ "

#)
st.write(
    "Current Standings :eggplant:"

)

#st.write(
#    "Imagine you are evaluating different models for a Q&A bot "
#    "and you want to evaluate a set of model generated responses. "
#    "You have collected some user data. "
#    "Here is a sample question and response set."
#)

data = {
    "Participant": [
        "Nathan Van Wieren",
        "Josh Dean",
        "Rob Van Dam",
        "David Van Dam",
        "Adam Brouwer",
        "Jesse Powers",
        "Keith the Lover of Pugs",
    ],
    "Current Score": [
        "11",
        "11",
        "7",
        "6",
        "8",
        "11",
        "8",
    ],
}

df = pd.DataFrame(data)

st.dataframe(df, hide_index=True)


# st.bar_chart(df)

# modified = pd.DataFrame(data)

# modified=modified.set_index("Participant")

# st.bar_chart(modified)




Participant = np.array(['Nathan Van Wieren', 'Josh Dean', 'Rob Van Dam', 'David Van Dam', 'Adam Brouwer', 'Jesse Powers', 'Keith Lover of Pugs' ])
Score = np.array([11, 11, 7, 6, 8, 11, 8])

chart_data = pd.DataFrame()
chart_data['Participant'] = Participant
chart_data['Score'] = Score

chart_v1 = alt.Chart(chart_data).mark_bar().encode(
x='Participant',
y='Score')
st.write("", "", chart_v1)

# Bar_Chart = alt.Chart(df).mark_bar().encode(
#      alt.X('Participant'),
#      alt.Y('Current Score'),
#      ).properties(
#          title="Standings"
#      ).configure_title(
#          anchor='middle'
#      )

# chart_data = df

# st.bar_chart(chart_data, x="Participant", y="Current Score", Title="Standings")


# Bar_Chart2 = alt.Chart(df).mark_bar().encode(
#     x='Participant',
#     y='Current Score'
# )


# st.altair_chart(Bar_Chart2)

# data2 = {
#     "Participant": [
#         "Nathan Van Wieren",
#         "Josh Dean",
#         "Rob Van Dam",
#         "David Van Dam",
#         "Adam Brouwer",
#         "Jesse Powers",
#         "Keith the Lover of Pugs",
#     ],
#     "July 8": [
#         "3",
#         "6",
#         "1",
#         "2",
#         "4",
#         "7",
#         "2",
#     ],

#         "July 9": [
#         "2",
#         "4",
#         "7",
#         "1",
#         "3",
#         "5",
#         "4",
#     ],
# }

# df2 = pd.DataFrame(data2)

# Bar_Chart2 = alt.Chart(df).mark_bar().encode(
#     x='Participant',
#     y='July 9'
# )


# st.write(
#     "Now I want to evaluate the responses from my model. "
#     "One way to achieve this is to use the very powerful `st.data_editor` feature. "
#     "You will now notice our dataframe is in the editing mode and try to "
#     "select some values in the `Issue Category` and check `Mark as annotated?` once finished 👇"
# )

# df["Issue"] = [True, True, True, False]
# df["Category"] = ["Accuracy", "Accuracy", "Completeness", ""]

# new_df = st.data_editor(
#     df,
#     column_config={
#         "Questions": st.column_config.TextColumn(width="medium", disabled=True),
#         "Answers": st.column_config.TextColumn(width="medium", disabled=True),
#         "Issue": st.column_config.CheckboxColumn("Mark as annotated?", default=False),
#         "Category": st.column_config.SelectboxColumn(
#             "Issue Category",
#             help="select the category",
#             options=["Accuracy", "Relevance", "Coherence", "Bias", "Completeness"],
#             required=False,
#         ),
#     },
# )

# st.write(
#     "You will notice that we changed our dataframe and added new data. "
#     "Now it is time to visualize what we have annotated!"
# )

# st.divider()

# st.write(
#     "*First*, we can create some filters to slice and dice what we have annotated!"
# )

# col1, col2 = st.columns([1, 1])
# with col1:
#     issue_filter = st.selectbox("Issues or Non-issues", options=new_df.Issue.unique())
# with col2:
#     category_filter = st.selectbox(
#         "Choose a category",
#         options=new_df[new_df["Issue"] == issue_filter].Category.unique(),
#     )

# st.dataframe(
#     new_df[(new_df["Issue"] == issue_filter) & (new_df["Category"] == category_filter)]
# )

# st.markdown("")
# st.write(
#     "*Next*, we can visualize our data quickly using `st.metrics` and `st.bar_plot`"
# )

# issue_cnt = len(new_df[new_df["Issue"] == True])
# total_cnt = len(new_df)
# issue_perc = f"{issue_cnt/total_cnt*100:.0f}%"

# col1, col2 = st.columns([1, 1])
# with col1:
#     st.metric("Number of responses", issue_cnt)
# with col2:
#     st.metric("Annotation Progress", issue_perc)

# df_plot = new_df[new_df["Category"] != ""].Category.value_counts().reset_index()

# st.bar_chart(df_plot, x="Category", y="count")

# st.write(
#     "Here we are at the end of getting started with streamlit! Happy Streamlit-ing! :balloon:"
# )

