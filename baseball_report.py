import dash
import dash_table
import dash_core_components as dcc
import dash_html_components as html
import dash.dependencies as dd
import plotly.graph_objs as go
import pandas as pd
from tnorma import tnorma


# List of all CSV files
csv_files = [
    "C:/Users/82104/Desktop/baseball/new_data/1nd lotte/kMin_001.csv",
    "C:/Users/82104/Desktop/baseball/new_data/1nd lotte/kMin_002.csv",
    "C:/Users/82104/Desktop/baseball/new_data/1nd lotte/kMin_003.csv",
    "C:/Users/82104/Desktop/baseball/new_data/1nd lotte/kMin_004.csv",
    "C:/Users/82104/Desktop/baseball/new_data/1nd lotte/kMin_005.csv",
    "C:/Users/82104/Desktop/baseball/new_data/1nd lotte/kMin_006.csv",
    "C:/Users/82104/Desktop/baseball/new_data/1nd lotte/kMin_007.csv",
    "C:/Users/82104/Desktop/baseball/new_data/1nd lotte/kMin_008.csv",
    "C:/Users/82104/Desktop/baseball/new_data/1nd lotte/kMin_009.csv"
]

# Load and consolidate data from all CSV files into one DataFrame
all_data = []
for idx, file in enumerate(csv_files, 1):
    df = pd.read_csv(file)

    nor_t, b, c = tnorma(df)
    new_data = pd.DataFrame(nor_t)
    new_data.columns = df.columns
    
    new_data['TRIAL'] = idx
    new_data['TIME'] = range(101)
    all_data.append(new_data)

# Concatenate all dataframes
df_all = pd.concat(all_data, ignore_index=True)


custom_palette = ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#9467bd",
                  "#8c564b", "#e377c2", "#7f7f7f", "#bcbd22", "#17becf",
                  "#1a55FF", "#FF551a", "#00FF55", "#55FF00", "#FFFF00",
                  "#FF00FF", "#00FFFF", "#FF0000", "#00FF00", "#0000FF",
                  "#555555", "#5555FF", "#55FF55", "#FF5555", "#959595",
                  "#9595FF", "#95FF95", "#FF9595", "#595959", "#5959FF",
                  "#59FF59", "#FF5959", "#252525", "#2525FF", "#25FF25",
                  "#FF2525", "#9B9B9B", "#9B9BFF", "#9BFF9B", "#FF9B9B"]

kinematic_columns = ['PELVIC_ANGULAR_VELOCITY',
                     'TORSO_ANGULAR_VELOCITY',
                     'RT_ELBOW_ANGULAR_VELOCITY',
                     'RT_SHOULDER_ANGULAR_VELOCITY']

kinematic_colors = {'PELVIC_ANGULAR_VELOCITY': 'red',
                    'TORSO_ANGULAR_VELOCITY': 'orange',
                    'RT_ELBOW_ANGULAR_VELOCITY': 'green',
                    'RT_SHOULDER_ANGULAR_VELOCITY': 'blue'}

col_name = {'TORSO_PELVIC_ANGLE_Z' : "Hip/Shoulder Separation",
            'RT_ELBOW_ANGLE_X' : "Elbow Flexion",
            'RT_SHOULDER_ANGLE_Z' : "Shoulder External Rotaion",
            'RT_SHOULDER_ANGLE_X' : "Shoulder Horizontal Abduction",
            'RT_SHOULDER_ANGLE_Y' : "Shoulder Abduction",
            'LT_KNEE_ANGLE_X' : "Lead Leg Knee Flexion",
            'LT_KNEE_ANGULAR_VELOCITY' : "Lead Leg Knee Extension Angular Velocity",
            'TORSO_ANGLE_X' : "Trunk Forward Tilt",
            'TORSO_ANGLE_Y' : "Trunk Lateral Tilt",
            'PELVIC_ANGULAR_VELOCITY' : "Pelvis Angular Velocity",
            'TORSO_ANGULAR_VELOCITY' : "Torso Angular Velocity",
            'RT_ELBOW_ANGULAR_VELOCITY' : "Elbow Angular Velocity",
            'RT_SHOULDER_ANGULAR_VELOCITY' : "Shoulder Angular Velocity",
            'Kinematic Sequence' : "Kinematic Sequence"}

src_name = {'TORSO_PELVIC_ANGLE_Z' : "https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FF1hNM%2FbtsyXZNSsG0%2FqHcaFPr3U5IqKBP8enGdlk%2Fimg.png",
            'RT_ELBOW_ANGLE_X' : "https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FYPj8D%2Fbtsy4b0PjGT%2FacxybeGX01XUgjOW3KzTuk%2Fimg.png",
            'RT_SHOULDER_ANGLE_Z' : "https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FcA5uIp%2FbtsyTXXzk3H%2F3gvShC3j2W5dpkP6oSn6qK%2Fimg.png",
            'RT_SHOULDER_ANGLE_X' : "https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FbMNU1k%2FbtsyTxEQCGe%2FazjHlTudjOQJdjkMd45RBK%2Fimg.png",
            'RT_SHOULDER_ANGLE_Y' : "https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FZ68RV%2FbtsyU4h6MxZ%2FLMfDEMRO2rtfncrGKPkiE1%2Fimg.png",
            'LT_KNEE_ANGLE_X' : "https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FAISc3%2FbtsyViAqe0j%2FqkKnVXFoxKbWz5maT1McHK%2Fimg.png",
            'LT_KNEE_ANGULAR_VELOCITY' : "https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2Fc8xB5Z%2Fbtsy4i6t7rz%2F6PbsxYYtYkrS1Y1lzxKMnk%2Fimg.png",
            'TORSO_ANGLE_X' : "https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FbbxkIS%2FbtsyYpFwfBU%2FNGGK8ebdS8iVWTmUxwNKr0%2Fimg.png",
            'TORSO_ANGLE_Y' : "https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2Fb4GH1Z%2Fbtsy3OSltlF%2FqGNLUkvxLZfIeupKkjoox1%2Fimg.png",
            'Kinematic Sequence' : "https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2Fbyb824%2FbtsyV1Stif0%2FiEXEHXjrkcKNNoPltvHAIK%2Fimg.png"}


# Initialization
app = dash.Dash(__name__)

# 2. Layout
app.layout = html.Div([
    # Buttons for "Consistency" and "Mean" at the top
    html.Div([
        dcc.RadioItems(
            id='graph-type-radioitems',
            options=[
                {'label': 'Consistency', 'value': 'consistency'},
                {'label': 'Mean', 'value': 'mean'}
            ],
            value='consistency',  # Default value
            inline=True,
            style={'fontFamily': 'Verdana', 'color': 'white'},
            labelStyle={'display': 'inline-block', 'margin-right': '20px'}
        ),
    ], style={'marginLeft': '30px', 'padding': '10px', 'marginBottom': '30px', 'backgroundColor': '#2B303D', 'marginTop': '30px'}),


    html.Div([
        html.Label("Select Trials", style={'marginBottom': '15px', 'fontSize': '20px', 'color': 'white', 'fontFamily': 'Verdana'}),
        html.Div([
            html.Button("Select All", id="select-all-trials-button", style={'marginRight': '5px'}),
            html.Button("Clear All", id="clear-all-trials-button"),
        ], style={'marginTop': '20px', 'marginBottom': '10px'}),
        dcc.Checklist(
            id='trial-checklist',
            options=[{'label': f'Trial {i}', 'value': i} for i in df_all['TRIAL'].unique()],
            value=[1],
            inline=True,
            style={'color': 'white', 'fontFamily': 'Verdana'},
            labelStyle={'marginRight': '20px'}
        ),
    ], style={'marginLeft': '30px', 'padding': '10px', 'marginBottom': '30px', 'backgroundColor': '#2B303D'}),

    
    html.Div(
        [html.Label("Select Variables", style={'marginBottom': '15px', 'fontSize': '20px', 'color': 'white', 'fontFamily': 'Verdana'}),

        html.Div([html.Button("Select All", id="select-all-columns-button", style={'marginRight': '5px'}),
                  html.Button("Clear All", id="clear-all-columns-button")], style={'marginTop': '20px', 'marginBottom': '10px'}),

        dcc.Checklist(
            id='column-checklist',
            options=[{'label': col_name[col], 'value': col} for col in df_all.columns if col not in ['TIME', 'TRIAL', 'PELVIC_ANGULAR_VELOCITY', 'TORSO_ANGULAR_VELOCITY', 'RT_ELBOW_ANGULAR_VELOCITY', 'RT_SHOULDER_ANGULAR_VELOCITY']] + [{'label': col_name['Kinematic Sequence'], 'value': 'Kinematic Sequence'}],
            value=[col_name['TORSO_PELVIC_ANGLE_Z']],
            inline=True,
             style={'color': 'white', 'fontFamily': 'Verdana'},
             labelStyle={'marginRight': '20px'}
        )
    ], style={'marginLeft': '30px', 'padding': '10px', 'marginBottom': '30px', 'backgroundColor': '#2B303D'}),

    html.Div(id='graphs-container', style={'marginLeft': '30px', 'padding': '10px', 'marginBottom': '30px', 'backgroundColor': '#252934'})
], style={'backgroundColor': '#252934'})



# 3. Callbacks
def generate_image(src, *args, **kwargs):
    img_url = src[0] if isinstance(src, list) and src else src if isinstance(src, str) else ""
    return html.Img(src=img_url, height=300, width=300, style={'marginRight': '20px'})

@app.callback(
    [dd.Output('trial-checklist', 'value'),
     dd.Output('column-checklist', 'value')],
    [dd.Input('select-all-trials-button', 'n_clicks'),
     dd.Input('clear-all-trials-button', 'n_clicks'),
     dd.Input('select-all-columns-button', 'n_clicks'),
     dd.Input('clear-all-columns-button', 'n_clicks')]
)
def handle_selection(select_all_trials, clear_all_trials, select_all_columns, clear_all_columns):
    ctx = dash.callback_context
    if not ctx.triggered:
        return [], ['TORSO_PELVIC_ANGLE_Z']
    
    button_id = ctx.triggered[0]['prop_id'].split('.')[0]
    
    trial_values = dash.no_update
    column_values = dash.no_update
    
    if button_id == 'select-all-trials-button':
        trial_values = [i for i in df_all['TRIAL'].unique()]
    elif button_id == 'clear-all-trials-button':
        trial_values = []
    elif button_id == 'select-all-columns-button':
        column_values = [col for col in df_all.columns if col not in ['TIME', 'TRIAL']] + ['Kinematic Sequence']
    elif button_id == 'clear-all-columns-button':
        column_values = []
    
    return trial_values, column_values

@app.callback(
    dd.Output('graphs-container', 'children'),
    [
        dd.Input('trial-checklist', 'value'),
        dd.Input('column-checklist', 'value'),
        dd.Input('graph-type-radioitems', 'value')
    ]
)

def update_graphs(trials, columns, graph_type):
    graphs = []

    # Helper function to generate the image and graph side by side
    def generate_graph_and_image(col, traces):
        return html.Div([
            html.Img(src=src_name.get(col, ""), height=350, width=300, style={'backgroundColor': '#2B303D'}),
            dcc.Graph(
                figure={
                    'data': traces,
                    'layout': go.Layout(
                        title=col_name[col],
                        xaxis_title='Time',
                        yaxis_title='Angular Velocity (deg/s)' if 'Velocity' in col_name[col] else 'Angle (deg)',
                        hovermode='closest',
                        margin={'r': 50},
                        showlegend=False,
                        paper_bgcolor='#2B303D',  # Main plot background color
                        plot_bgcolor='#2B303D',  # Plot area background color
                        font=dict(color='white')
                    )
                },
                style={'height': '350px', 'width': '70%'}
            ), 
        ], style={'display': 'flex', 'alignItems': 'center', 'justifyContent': 'start', 'marginBottom': '30px'})

    # If "Kinematic Sequence" is selected, generate a single graph for all kinematic columns
    if col_name['Kinematic Sequence'] in columns:
        columns.remove(col_name['Kinematic Sequence'])
        traces = []

        # Determine the y-axis range to span the entire y-axis for the max value lines
        y_min = df_all[kinematic_columns].min().min()
        y_max = df_all[kinematic_columns].max().max()
        
        # If "Mean" is selected, show average of all trials
        if graph_type == 'mean':
            avg_df = df_all.groupby('TIME').mean().reset_index()
            for k_col in kinematic_columns:
                traces.append(go.Scatter(x=avg_df['TIME'], y=avg_df[k_col], mode='lines', name=f'Average {col_name[k_col]}', line=dict(color=kinematic_colors[k_col])))
                
                # Dashed line for max value
                max_val = avg_df[k_col].max()
                max_time = avg_df[avg_df[k_col] == max_val]['TIME'].iloc[0]
                traces.append(go.Scatter(
                    x=[max_time, max_time],
                    y=[y_min, y_max],
                    mode='lines',
                    line=dict(color=kinematic_colors[k_col], dash='dot'),
                    showlegend=False
                ))
        else:
            for k_col in kinematic_columns:
                for trial in trials:
                    trial_df = df_all[df_all['TRIAL'] == trial]
                    traces.append(go.Scatter(x=trial_df['TIME'], y=trial_df[k_col], mode='lines', name=f'Trial {trial} {col_name[k_col]}', line=dict(color=kinematic_colors[k_col])))
                    
                    # Dashed line for max value
                    max_val = trial_df[k_col].max()
                    max_time = trial_df[trial_df[k_col] == max_val]['TIME'].iloc[0]
                    traces.append(go.Scatter(
                        x=[max_time, max_time],
                        y=[y_min, y_max],
                        mode='lines',
                        line=dict(color=kinematic_colors[k_col], dash='dot'),
                        showlegend=False
                    ))
        
        graphs.append(generate_graph_and_image('Kinematic Sequence', traces))

    # For other columns, plot them as separate graphs with their corresponding images
    for col in columns:
        traces = []
        yaxis_label = 'Angular Velocity (deg/s)' if 'Velocity' in col_name[col] else 'Angle (deg)'
        
        # If "Mean" is selected, show average of all trials
        if graph_type == 'mean':
            avg_df = df_all.groupby('TIME').mean().reset_index()
            traces.append(go.Scatter(x=avg_df['TIME'], y=avg_df[col], mode='lines', name=f'Average {col_name[col]}'))
            
            # Dashed line for max value
            max_val = avg_df[col].max()
            max_time = avg_df[avg_df[col] == max_val]['TIME'].iloc[0]
            traces.append(go.Scatter(
                x=[max_time, max_time],
                y=[0, max_val],
                mode='lines',
                line=dict(color='red', dash='dot'),
                showlegend=False
            ))
        else:
            for trial in trials:
                trial_df = df_all[df_all['TRIAL'] == trial]
                traces.append(go.Scatter(x=trial_df['TIME'], y=trial_df[col], mode='lines', name=f'Trial {trial}'))
                
                # Dashed line for max value
                max_val = trial_df[col].max()
                max_time = trial_df[trial_df[col] == max_val]['TIME'].iloc[0]
                traces.append(go.Scatter(
                    x=[max_time, max_time],
                    y=[0, max_val],
                    mode='lines',
                    line=dict(color='red', dash='dot'),
                    showlegend=False
                ))
        
        graphs.append(generate_graph_and_image(col, traces))
    
    return graphs




if __name__ == '__main__':
    app.run_server(debug=True)