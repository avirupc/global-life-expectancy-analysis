from pathlib import Path

import pandas as pd
from dash import Dash, dcc, html, Input, Output
import plotly.express as px

# Load data
DATA_PATH = Path(__file__).resolve().parent / "dashboard_df.csv"
df = pd.read_csv(DATA_PATH)

# Dash app
app = Dash(__name__)

# Dropdown options
country_options = sorted(df["Country Name"].dropna().unique())
income_options = sorted(df["IncomeGroup"].dropna().unique())
region_options = sorted(df["Region"].dropna().unique())

# App layout
app.layout = html.Div(
    style={"padding": "20px"},
    children=[
        # Title
        html.H1("Global Life Expectancy Dashboard", style={"textAlign": "center"}),
        html.Br(),

        # Filters
        html.Div(
            children=[
                html.Div(
                    [
                        html.Label("Country"),
                        dcc.Dropdown(
                            id="country_filter",
                            options=[{"label": c, "value": c} for c in country_options],
                            multi=True,
                        ),
                    ],
                    style={"width": "24%", "display": "inline-block"},
                ),
                html.Div(
                    [
                        html.Label("Income Group"),
                        dcc.Dropdown(
                            id="income_filter",
                            options=[{"label": x, "value": x} for x in income_options],
                            multi=True,
                        ),
                    ],
                    style={"width": "24%", "display": "inline-block", "marginLeft": "1%"},
                ),
                html.Div(
                    [
                        html.Label("Region"),
                        dcc.Dropdown(
                            id="region_filter",
                            options=[{"label": x, "value": x} for x in region_options],
                            multi=True,
                        ),
                    ],
                    style={"width": "24%", "display": "inline-block", "marginLeft": "1%"},
                ),
                html.Div(
                    [
                        html.Label("Group By"),
                        dcc.Dropdown(
                            id="groupby_filter",
                            options=[
                                {"label": "None", "value": "None"},
                                {"label": "Income Group", "value": "IncomeGroup"},
                                {"label": "Region", "value": "Region"},
                            ],
                            value="None",
                            clearable=False,
                        ),
                    ],
                    style={"width": "24%", "display": "inline-block", "marginLeft": "1%"},
                ),
            ]
        ),
        html.Br(),

        # Year slider
        html.Label("Year Range"),
        dcc.RangeSlider(
            id="year_slider",
            min=df["Year"].min(),
            max=df["Year"].max(),
            value=[df["Year"].min(), df["Year"].max()],
            marks={
                year: str(year)
                for year in range(int(df["Year"].min()), int(df["Year"].max()) + 1, 10)
            },
        ),
        html.Br(),

        # KPI Section (callback fills KPI values, info box is static)
        html.Div(
            style={"display": "flex", "justifyContent": "space-between"},
            children=[
                # KPI values injected here
                html.Div(id="kpi_cards", style={"width": "60%", "paddingRight": "20px"}),

                # Info box on far right
                html.Div(
                    dcc.Markdown(
                        """
                        **What these KPIs mean:**
                        - **Initial Year KPIs**: Averages across all selected countries for the first year in your chosen range.
                        - **Latest Year KPIs**: Averages across all selected countries for the most recent year in your chosen range.
                        - **Average Life Expectancy**: Mean number of years a newborn is expected to live.
                        - **Average Fertility Rate**: Mean number of children born per woman.
                        - **Average Death Rate**: Mean crude death rate (deaths per 1,000 people).
                        """
                    ),
                    style={
                        "width": "40%",
                        "backgroundColor": "#f9f9f9",
                        "padding": "10px",
                        "borderRadius": "5px",
                    },
                ),
            ],
        ),
        html.Hr(),

        # Charts
        dcc.Graph(id="life_expectancy_chart"),
        dcc.Graph(id="gender_gap_chart"),
        dcc.Graph(id="fertility_chart"),
        dcc.Graph(id="death_rate_chart"),
        dcc.Graph(id="aggregation_chart"),
    ],
)

# Callback
@app.callback(
    [
        Output("kpi_cards", "children"),
        Output("life_expectancy_chart", "figure"),
        Output("gender_gap_chart", "figure"),
        Output("fertility_chart", "figure"),
        Output("death_rate_chart", "figure"),
        Output("aggregation_chart", "figure"),
    ],
    [
        Input("country_filter", "value"),
        Input("income_filter", "value"),
        Input("region_filter", "value"),
        Input("year_slider", "value"),
        Input("groupby_filter", "value"),
    ],
)
def update_dashboard(countries, incomes, regions, years, groupby):
    # Apply filters
    filtered_df = df.copy()
    if countries:
        filtered_df = filtered_df[filtered_df["Country Name"].isin(countries)]
    if incomes:
        filtered_df = filtered_df[filtered_df["IncomeGroup"].isin(incomes)]
    if regions:
        filtered_df = filtered_df[filtered_df["Region"].isin(regions)]
    filtered_df = filtered_df[
        (filtered_df["Year"] >= years[0]) & (filtered_df["Year"] <= years[1])
    ]

    # Handle cases where the selected country/income group/region combination 
    # does not exist (e.g., 'Afghanistan' + 'High income' + 'Sub-Saharan Africa'). 
    # Instead of showing empty charts or "NaN" values, display a clear message 
    # to inform the user that no data is available for the chosen filters.

    if filtered_df.empty:
        empty_msg = html.Div(
            "No data matches the selected filters. Try widening your selection.",
            style={"color": "#b00020", "fontWeight": "bold"},
        )
        empty_fig = px.line(title="No data available for this selection")
        return empty_msg, empty_fig, empty_fig, empty_fig, empty_fig, empty_fig

    # KPI calculations
    initial_year = filtered_df["Year"].min()
    latest_year = filtered_df["Year"].max()

    initial_df = filtered_df[filtered_df["Year"] == initial_year]
    latest_df = filtered_df[filtered_df["Year"] == latest_year]

    init_avg_life = round(initial_df["LifeExpectancy"].mean(), 2)
    init_avg_fertility = round(initial_df["FertilityRate"].mean(), 2)
    init_avg_death = round(initial_df["DeathRate"].mean(), 2)

    latest_avg_life = round(latest_df["LifeExpectancy"].mean(), 2)
    latest_avg_fertility = round(latest_df["FertilityRate"].mean(), 2)
    latest_avg_death = round(latest_df["DeathRate"].mean(), 2)

    # KPI values side by side
    kpis = html.Div(
        style={"display": "flex", "justifyContent": "space-between"},
        children=[
            html.Div(
                [
                    html.H3(f"Initial Year: {initial_year}"),
                    html.P(f"Average Life Expectancy: {init_avg_life}"),
                    html.P(f"Average Fertility Rate: {init_avg_fertility}"),
                    html.P(f"Average Death Rate: {init_avg_death}"),
                ],
                style={"width": "45%", "paddingRight": "20px"},
            ),
            html.Div(
                [
                    html.H3(f"Latest Year: {latest_year}"),
                    html.P(f"Average Life Expectancy: {latest_avg_life}"),
                    html.P(f"Average Fertility Rate: {latest_avg_fertility}"),
                    html.P(f"Average Death Rate: {latest_avg_death}"),
                ],
                style={"width": "45%", "paddingRight": "20px"},
            ),
        ],
    )

    # Life Expectancy Chart
    fig_life = px.line(
        filtered_df,
        x="Year",
        y="LifeExpectancy",
        color="Country Name",
        hover_data=["IncomeGroup", "Region"],
        title="Life Expectancy Trends",
    )

    # Gender Gap Chart
    fig_gap = px.line(
        filtered_df,
        x="Year",
        y="GenderGap",
        color="Country Name",
        hover_data=["IncomeGroup", "Region"],
        title="Female-Male Life Expectancy Gap",
    )

    # Fertility Rate Chart
    fig_fertility = px.line(
        filtered_df,
        x="Year",
        y="FertilityRate",
        color="Country Name",
        hover_data=["IncomeGroup", "Region"],
        title="Fertility Rate Trend",
    )

    # Death Rate Chart
    fig_death = px.line(
        filtered_df,
        x="Year",
        y="DeathRate",
        color="Country Name",
        hover_data=["IncomeGroup", "Region"],
        title="Crude Death Rate Trend",
    )

    # Aggregation Chart
    if groupby != "None":
        agg_df = filtered_df.groupby([groupby, "Year"], as_index=False)[["LifeExpectancy"]].mean()
        fig_agg = px.line(
            agg_df,
            x="Year",
            y="LifeExpectancy",
            color=groupby,
            title=f"Average Life Expectancy by {groupby}",
        )
    else:
        fig_agg = px.line(title="Select Group By Option")

    return kpis, fig_life, fig_gap, fig_fertility, fig_death, fig_agg


if __name__ == "__main__":
    app.run(debug=False)
