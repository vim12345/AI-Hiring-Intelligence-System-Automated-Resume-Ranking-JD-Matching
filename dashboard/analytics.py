
import plotly.express as px

def skill_distribution(df):

    fig = px.bar(
        df,
        x="skills",
        title="Skill Distribution"
    )

    return fig
