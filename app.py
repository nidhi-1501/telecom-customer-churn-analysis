import pandas as pd

# Load the CSV file into a DataFrame
df = pd.read_csv('WA_Fn-UseC_-Telco-Customer-Churn.csv')

# display the first five rows of the DataFrame
df.head()

# structure of the DataFrame
df.info() 

#statistical summary of the dataset
df.describe()

#number of rows and columns
df.shape

#converting the datatype
df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors="coerce")

print(df["TotalCharges"].dtype)

#finding if there are missing values in the data
df.isnull().sum()

#filling the null values with 0
df.fillna(0, inplace=True)

#mapping another column for churn data and using 0 and 1 instead of yes or no
df['Churn_label'] = df['Churn'].map({'No' : 0, 'Yes' : 1})

print(df[['Churn','Churn_label']].head())

#bins is the parameter that divides the data into ranges
bins = [0,50,85, df['MonthlyCharges'].max()]

#labels for each data range
labels = ['Low spending', 'Moderate spending', 'High spending']

#creating a new column for monthly charges category
df['MonthlyCharges_Category'] = pd.cut(
    df['MonthlyCharges'],
    bins = bins,
    labels = labels,
    include_lowest = True
)

print(df[['MonthlyCharges', 'MonthlyCharges_Category']].head())

#counting the number of customers in each category of monthly charges
print(df['MonthlyCharges_Category'].value_counts())

#dividing data into ranges
bins = [-1,12,36, df['tenure'].max()]

#labels for each data range
labels = ['New Customer', 'Regular Customer', 'Loyal Customer']

df['CustomerType'] = pd.cut(
    df['tenure'],
    bins = bins,
    labels = labels
)

print(df[['tenure', 'CustomerType']].head())

#counting the number of customers in each category
print(df["CustomerType"].value_counts())

#displays the name of all the columns
df.columns

# TELECOM CUSTOMER CHURN DASHBOARD

from dash import Dash, dcc, html, Input, Output
import plotly.express as px
import plotly.graph_objects as go

# APP

app = Dash(
    __name__,
    external_scripts=[
        "https://cdnjs.cloudflare.com/ajax/libs/html2canvas/1.4.1/html2canvas.min.js"
    ]
)

# COLORS

BG = "#f1f5f9"
WHITE = "#ffffff"
TEXT = "#0f172a"
SECONDARY = "#64748b"
GRID = "#e2e8f0"

BLUE = "#3b82f6"
RED = "#f43f5e"

# KPI CARD

def create_kpi(title, value):

    return html.Div(

        [

            html.Div(
                title,
                style={
                    "fontSize": "15px",
                    "fontWeight": "600",
                    "color": SECONDARY,
                    "marginBottom": "10px"
                }
            ),

            html.Div(
                value,
                style={
                    "fontSize": "32px",
                    "fontWeight": "700",
                    "color": TEXT
                }
            )

        ],

        style={

            "width": "calc((100% - 60px) / 4)",
            "minWidth": "0",
            "boxSizing": "border-box",

            "backgroundColor": WHITE,

            "padding": "22px 20px",

            "borderRadius": "12px",

            "boxShadow":
                "0 2px 10px rgba(0,0,0,0.08)",

            "textAlign": "center",

            "height": "122px",

            "display": "flex",

            "flexDirection": "column",

            "justifyContent": "center",

            "alignItems": "center"

        }
    )

# CREATE CHARTS

def create_charts(filtered_df):

    # CONTRACT

    fig_contract = px.histogram(

        filtered_df,

        x="Contract",

        color="Churn",

        barmode="group",

        category_orders={
            "Contract": [
                "Month-to-month",
                "One year",
                "Two year"
            ]
        },

        color_discrete_map={
            "No": BLUE,
            "Yes": RED
        }

    )

    fig_contract.update_layout(

        height=330,

        margin=dict(
            l=55,
            r=25,
            t=55,
            b=65
        ),

        title=dict(
            text="<b>Churn by Contract Type</b>",
            x=0.02,
            xanchor="left",
            y=0.96,
            font=dict(
                size=17,
                color=TEXT
            )
        ),

        plot_bgcolor=WHITE,
        paper_bgcolor=WHITE,

         legend=dict(
            orientation="h",
            yanchor="top",
            y=0.99,
            xanchor="right",
            x=0.98,
            font=dict(size=12)
        ),

        bargap=0.18,

        hovermode="x unified"

    )

    fig_contract.update_xaxes(

        title_text=None,

        tickfont=dict(
            size=11,
            color="#334155"
        ),

        showgrid=False,

        zeroline=False,

        automargin=True

    )

    fig_contract.update_yaxes(

        title_text="Count",

        title_font=dict(size=12),

        tickfont=dict(
            size=11,
            color="#334155"
        ),

        showgrid=True,

        gridcolor=GRID,

        zeroline=False,

        automargin=True

    )

    # INTERNET SERVICE

    fig_internet = px.histogram(

        filtered_df,

        x="InternetService",

        color="Churn",

        barmode="group",

        color_discrete_map={
            "No": BLUE,
            "Yes": RED
        }

    )

    fig_internet.update_layout(

        height=330,

        margin=dict(
            l=55,
            r=25,
            t=55,
            b=65
        ),

        title=dict(
            text="<b>Churn by Internet Service</b>",
            x=0.02,
            xanchor="left",
            y=0.96,
            font=dict(
                size=17,
                color=TEXT
            )
        ),

        plot_bgcolor=WHITE,
        paper_bgcolor=WHITE,

        legend=dict(
            orientation="h",
            yanchor="top",
            y=0.99,
            xanchor="right",
            x=0.98,
            font=dict(size=12)
        ),

        bargap=0.18,

        hovermode="x unified"

    )

    fig_internet.update_xaxes(
        title_text=None,

        tickfont=dict(
            size=11,
            color="#334155"
        ),

        showgrid=False,

        zeroline=False,

        automargin=True

    )

    fig_internet.update_yaxes(

        title_text="Count",

        title_font=dict(size=12),

        tickfont=dict(
            size=11,
            color="#334155"
        ),

        showgrid=True,

        gridcolor=GRID,

        zeroline=False,

        automargin=True

    )

    # MONTHLY CHARGES
    fig_monthly = px.histogram(

        filtered_df,

        x="MonthlyCharges",

        color="Churn",

        nbins=25,

        barmode="overlay",

        opacity=0.72,

        color_discrete_map={
            "No": BLUE,
            "Yes": RED
        }

    )

    fig_monthly.update_layout(

        height=330,

        margin=dict(
            l=55,
            r=25,
            t=55,
            b=65
        ),

        title=dict(
            text="<b>Monthly Charges Distribution</b>",
            x=0.02,
            xanchor="left",
            y=0.96,
            font=dict(
                size=17,
                color=TEXT
            )
        ),

        plot_bgcolor=WHITE,
        paper_bgcolor=WHITE,

        legend=dict(
            orientation="h",
            yanchor="top",
            y=0.99,
            xanchor="right",
            x=0.98,
            font=dict(size=12)
        ),

        hovermode="x unified"

    )

    fig_monthly.update_xaxes(

        title_text="Monthly Charges",

        title_font=dict(size=12),

        tickfont=dict(
            size=11,
            color="#334155"
        ),

        showgrid=False,

        zeroline=False,

        automargin=True

    )

    fig_monthly.update_yaxes(

        title_text="Count",

        title_font=dict(size=12),

        tickfont=dict(
            size=11,
            color="#334155"
        ),

        showgrid=True,

        gridcolor=GRID,

        zeroline=False,

        automargin=True

    )
    
    # TENURE

    fig_tenure = px.histogram(

        filtered_df,

        x="tenure",

        color="Churn",

        nbins=25,

        barmode="overlay",

        opacity=0.72,

        color_discrete_map={
            "No": BLUE,
            "Yes": RED
        }

    )

    fig_tenure.update_layout(

        height=330,

        margin=dict(
            l=55,
            r=25,
            t=55,
            b=65
        ),

        title=dict(
            text="<b>Customer Tenure Analysis</b>",
            x=0.02,
            xanchor="left",
            y=0.96,
            font=dict(
                size=17,
                color=TEXT
                )
        ),

        plot_bgcolor=WHITE,
        paper_bgcolor=WHITE,

        legend=dict(
            orientation="h",
            yanchor="top",
            y=0.99,
            xanchor="right",
            x=0.98,
            font=dict(size=12)
        ),

        hovermode="x unified"

    )

    fig_tenure.update_xaxes(

        title_text="Tenure (Months)",

        title_font=dict(size=12),

        tickfont=dict(
            size=11,
            color="#334155"
        ),

        showgrid=False,

        zeroline=False,

        automargin=True

    )

    fig_tenure.update_yaxes(

        title_text="Count",

        title_font=dict(size=12),

        tickfont=dict(
            size=11,
            color="#334155"
        ),

        showgrid=True,

        gridcolor=GRID,

        zeroline=False,

        automargin=True

    )

    # CORRELATION HEATMAP

    numeric_df = filtered_df[

        [
            "SeniorCitizen",
            "tenure",
            "MonthlyCharges",
            "TotalCharges",
            "Churn_label"
        ]

    ]

    corr = numeric_df.corr()

    fig_heatmap = go.Figure(

        data=go.Heatmap(

            z=corr.values,

            x=corr.columns,

            y=corr.columns,

            text=corr.round(2).values,

            texttemplate="%{text}",

            textfont=dict(
                size=13
            ),

            colorscale="RdBu",

            zmid=0,

            colorbar=dict(

                title=dict(
                    text="Correlation",
                    font=dict(size=12)
                ),

                thickness=14,

                len=0.82

            ),

            hovertemplate=

                "<b>%{y}</b> vs <b>%{x}</b>" +

                "<br>Correlation: %{z:.2f}" +

                "<extra></extra>"

        )

    )


    fig_heatmap.update_layout(

        height=370,

        margin=dict(
            l=100,
            r=75,
            t=60,
            b=65
        ),

        title=dict(

            text="<b>Correlation Heatmap</b>",

            x=0.02,

            xanchor="left",

            y=0.96,

            font=dict(
                size=17,
                color=TEXT
            )

        ),

        plot_bgcolor=WHITE,

        paper_bgcolor=WHITE

    )


    fig_heatmap.update_xaxes(

        tickfont=dict(
            size=11,
            color="#334155"
        ),

        side="bottom",

        automargin=True

    )


    fig_heatmap.update_yaxes(

        tickfont=dict(
            size=11,
            color="#334155"
        ),

        automargin=True

    )

    return (

        fig_contract,
        fig_internet,
        fig_monthly,
        fig_tenure,
        fig_heatmap

    )

# DASHBOARD

app.layout = html.Div(

    [

        html.Div(

            [

                # HEADER + CAMERA BUTTON

                html.Div(

                    [

                        html.Div(

                            [

                                html.H1(

                                    "Telecom Customer Churn",

                                    style={

                                        "fontSize": "34px",

                                        "fontWeight": "700",

                                        "color": TEXT,

                                        "margin":
                                            "0 0 6px 0"

                                    }

                                ),

                                html.P(

                                    "Customer retention and service performance overview",

                                    style={

                                        "fontSize": "16px",

                                        "color": SECONDARY,

                                        "margin": "0"

                                    }

                                )

                            ]

                        ),

                        # DASHBOARD CAMERA

                        html.Button(

                            "📷",

                            id="dashboard-camera",

                            title="Download dashboard as PNG",

                            n_clicks=0,

                            style={

                                "border": "none",

                                "background": "transparent",

                                "fontSize": "21px",

                                "color": "#64748b",

                                "cursor": "pointer",

                                "padding": "6px 8px",

                                "borderRadius": "6px",

                                "marginTop": "2px"

                            }

                        )

                    ],

                    style={

                        "display": "flex",

                        "justifyContent":
                            "space-between",

                        "alignItems": "flex-start",

                        "marginBottom": "28px"

                    }

                ),

                # KPI CARDS

                html.Div(

                    [

                        create_kpi(
                            "Total Customers",
                            f"{len(df):,}"
                        ),

                        create_kpi(
                            "Active Customers",
                            f"{(df['Churn'] == 'No').sum():,}"
                        ),

                        create_kpi(
                            "Churned Customers",
                            f"{(df['Churn'] == 'Yes').sum():,}"
                        ),

                        create_kpi(
                            "Churn Rate",
                            f"{(df['Churn'] == 'Yes').mean() * 100:.2f}%"
                        )

                    ],

                    style={

                        "display": "flex",

                        "gap": "20px",

                        "width": "100%",

                        "marginBottom": "22px",

                        "boxSizing": "border-box"

                    }

                ),

                # FILTERS

                html.Div(

                    [

                        # Gender
                        html.Div(

                            [

                                html.Label(

                                    "Gender",

                                    style={
                                        "fontWeight": "600",
                                        "fontSize": "15px",
                                        "color": TEXT,
                                        "marginBottom": "8px",
                                        "display": "block"
                                    }
                                    ),

                                dcc.Dropdown(

                                    id="gender-filter",

                                    options=[

                                        {
                                            "label": "All",
                                            "value": "All"
                                        }

                                    ]
                                    +

                                    [

                                        {
                                            "label": x,
                                            "value": x
                                        }

                                        for x in sorted(
                                            df["gender"]
                                            .dropna()
                                            .unique()
                                        )

                                    ],

                                    value="All",

                                    clearable=False

                                )

                            ],

                            style={
                                "flex": "1",
                                "minWidth": "0"
                            }

                        ),


                        # Contract
                        html.Div(

                            [

                                html.Label(

                                    "Contract Type",

                                    style={
                                        "fontWeight": "600",
                                        "fontSize": "15px",
                                        "color": TEXT,
                                        "marginBottom": "8px",
                                        "display": "block"
                                    }

                                ),

                                dcc.Dropdown(

                                    id="contract-filter",

                                    options=[

                                        {
                                            "label": "All",
                                            "value": "All"
                                        }

                                        ]
                                    +

                                    [

                                        {
                                            "label": x,
                                            "value": x
                                        }

                                        for x in sorted(
                                            df["Contract"]
                                            .dropna()
                                            .unique()
                                        )

                                    ],

                                    value="All",

                                    clearable=False

                                )

                            ],

                            style={
                                "flex": "1",
                                "minWidth": "0"
                            }

                        ),


                        # Internet
                        html.Div(
                            [

                                html.Label(

                                    "Internet Service",

                                    style={
                                        "fontWeight": "600",
                                        "fontSize": "15px",
                                        "color": TEXT,
                                        "marginBottom": "8px",
                                        "display": "block"
                                    }

                                ),

                                dcc.Dropdown(

                                    id="internet-filter",

                                    options=[

                                        {
                                            "label": "All",
                                            "value": "All"
                                        }

                                    ]
                                    +

                                    [

                                        {
                                            "label": x,
                                            "value": x
                                        }

                                        for x in sorted(
                                            df["InternetService"]
                                            .dropna()
                                            .unique()
                                        )

                                    ],

                                    value="All",

                                    clearable=False

                                )

                            ],

                            style={
                                "flex": "1",
                                "minWidth": "0"
                            }

                        )

                    ],

                    style={

                        "display": "flex",

                        "gap": "28px",

                        "backgroundColor": WHITE,

                        "padding":
                            "20px 24px",

                        "borderRadius": "12px",

                        "boxShadow":
                            "0 2px 10px rgba(0,0,0,0.06)",

                        "marginBottom": "22px",

                        "boxSizing": "border-box"

                    }

                ),

                # GRAPH ROW 1

                html.Div(

                    [

                        html.Div(

                            dcc.Graph(

                                id="contract-chart",

                                config={

                                    # HIDE INDIVIDUAL TOOLBAR
                                    # because we have one at top
                                    "displayModeBar": False,

                                    "displaylogo": False,

                                    "responsive": True

                                },

                                style={
                                    "height": "350px"
                                }

                                ),

                            style={

                                "backgroundColor": WHITE,

                                "borderRadius": "12px",

                                "padding":
                                    "8px 10px 5px 10px",

                                "boxShadow":
                                    "0 2px 10px rgba(0,0,0,0.06)",

                                "overflow": "hidden"

                            }

                        ),


                        html.Div(

                            dcc.Graph(

                                id="internet-chart",

                                config={

                                    "displayModeBar": False,

                                    "displaylogo": False,

                                    "responsive": True

                                },

                                style={
                                    "height": "350px"
                                }

                            ),

                            style={

                                "backgroundColor": WHITE,

                                "borderRadius": "12px",

                                "padding":
                                    "8px 10px 5px 10px",

                                "boxShadow":
                                    "0 2px 10px rgba(0,0,0,0.06)",

                                "overflow": "hidden"

                            }

                        )

                    ],

                    style={

                        "display": "grid",

                        "gridTemplateColumns":
                            "1fr 1fr",

                        "gap": "22px",

                        "marginBottom": "22px"

                    }

                    ),

                # GRAPH ROW 2

                html.Div(

                    [

                        html.Div(

                            dcc.Graph(

                                id="monthly-chart",

                                config={

                                    "displayModeBar": False,

                                    "displaylogo": False,

                                    "responsive": True

                                },

                                style={
                                    "height": "350px"
                                }

                            ),

                            style={

                                "backgroundColor": WHITE,

                                "borderRadius": "12px",

                                "padding":
                                    "8px 10px 5px 10px",

                                "boxShadow":
                                    "0 2px 10px rgba(0,0,0,0.06)",

                                "overflow": "hidden"

                            }

                        ),


                        html.Div(

                            dcc.Graph(

                                id="tenure-chart",

                                config={

                                    "displayModeBar": False,

                                    "displaylogo": False,

                                    "responsive": True

                                },

                                style={
                                    "height": "350px"
                                }

                            ),

                            style={

                                "backgroundColor": WHITE,

                                "borderRadius": "12px",

                                "padding":
                                    "8px 10px 5px 10px",

                                "boxShadow":
                                    "0 2px 10px rgba(0,0,0,0.06)",

                                "overflow": "hidden"

                            }

                        )

                    ],

                    style={

                        "display": "grid",

                        "gridTemplateColumns":
                            "1fr 1fr",

                        "gap": "22px",

                        "marginBottom": "22px"

                    }

                ),

                # HEATMAP

                html.Div(

                    dcc.Graph(

                        id="heatmap-chart",

                        config={
                            "displayModeBar": False,

                            "displaylogo": False,

                            "responsive": True

                        },

                        style={
                            "height": "390px"
                        }

                    ),

                    style={

                        "backgroundColor": WHITE,

                        "borderRadius": "12px",

                        "padding":
                            "8px 10px 5px 10px",

                        "boxShadow":
                            "0 2px 10px rgba(0,0,0,0.06)",

                        "marginBottom": "25px",

                        "overflow": "hidden"

                    }

                )

            ],

            id="dashboard-container",
            style={

                "width": "100%",

                "boxSizing": "border-box"

            }

        )

    ],

    style={

        "backgroundColor": BG,

        "minHeight": "100vh",

        "padding":
            "30px 4% 50px 4%",

        "fontFamily":
            "Arial, sans-serif",

        "boxSizing":
            "border-box"

    }

)

# DASHBOARD FILTER CALLBACK

@app.callback(

    [

        Output(
            "contract-chart",
            "figure"
        ),

        Output(
            "internet-chart",
            "figure"
        ),

        Output(
            "monthly-chart",
            "figure"
        ),

        Output(
            "tenure-chart",
            "figure"
        ),

        Output(
            "heatmap-chart",
            "figure"
        )

    ],

    [

        Input(
            "gender-filter",
            "value"
        ),

        Input(
            "contract-filter",
            "value"
        ),

        Input(
            "internet-filter",
            "value"
        )

    ]

)


def update_dashboard(

    gender,
    contract,
    internet

):

    filtered_df = df.copy()


    if gender != "All":

        filtered_df = filtered_df[
            filtered_df["gender"] == gender
        ]


    if contract != "All":

        filtered_df = filtered_df[
            filtered_df["Contract"] == contract
        ]


    if internet != "All":

        filtered_df = filtered_df[
            filtered_df["InternetService"] == internet
        ]


    return create_charts(
        filtered_df
    )

# CAMERA BUTTON

app.clientside_callback(

    """
    function(n_clicks) {

        if (!n_clicks) {
            return window.dash_clientside.no_update;
        }

        var dashboard =
            document.getElementById("dashboard-container");

        if (!dashboard) {
            return window.dash_clientside.no_update;
        }

        html2canvas(

            dashboard,

            {
                scale: 2,
                backgroundColor: "#f1f5f9",
                useCORS: true
            }

        ).then(function(canvas) {
        var link =
                document.createElement("a");

            link.download =
                "Telecom_Customer_Churn_Dashboard.png";

            link.href =
                canvas.toDataURL("image/png");

            link.click();

        });

        return window.dash_clientside.no_update;
    }
    """,

    Output(
        "dashboard-camera",
        "n_clicks"
    ),

    Input(
        "dashboard-camera",
        "n_clicks"
    )

)

# RUN

server = app.server

if __name__ == "__main__":

    app.run(
        debug=True,
        port=8050
    )