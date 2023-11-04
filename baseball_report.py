import dash
from dash import dcc
from dash import html
import dash.dependencies as dd
import plotly.graph_objs as go
import pandas as pd
import os

folder_path = 'Data/Processed Data/'

pit_path = folder_path + 'Pitching Data'
pit_all_files = [f for f in os.listdir(pit_path) if f.endswith('.csv')]
pit_players = list(set([f.split('_')[0] for f in pit_all_files]))

hit_path = folder_path + 'Hitting Data'
hit_all_files = [f for f in os.listdir(hit_path) if f.endswith('.csv')]
hit_players = list(set([f.split('_')[0] for f in hit_all_files]))

pit_avg = pd.read_csv('C:/Users/user/Desktop/Samsung Report/Data/Driveline_Pitching_Timenormalize_avg.csv')
pit_std = pd.read_csv('C:/Users/user/Desktop/Samsung Report/Data/Driveline_Pitching_Timenormalize_std.csv')

hit_avg = pd.read_csv('C:/Users/user/Desktop/Samsung Report/Data/Driveline_Hitting_Timenormalize_avg.csv')
hit_std = pd.read_csv('C:/Users/user/Desktop/Samsung Report/Data/Driveline_Hitting_Timenormalize_std.csv')

pit_data = []
for idx, file in enumerate(pit_all_files, 1):
    new_data = pd.read_csv(pit_path + f'/{file}')

    new_data['Trial'] = int(file.split('_')[-1].split('.')[0])
    new_data['Name'] = file.split('_')[0]
    pit_data.append(new_data)

pit_all_data = pd.concat(pit_data, ignore_index=True)

hit_data = []
for idx, file in enumerate(hit_all_files, 1):
    new_data = pd.read_csv(hit_path + f'/{file}')

    new_data['Trial'] = int(file.split('_')[-1].split('.')[0])
    new_data['Name'] = file.split('_')[0]
    hit_data.append(new_data)

hit_all_data = pd.concat(hit_data, ignore_index=True)

custom_palette = ['#e95d00', '#c60004', '#7fca00', '#fadf00', '#f1438e', '#26c9dd', '#d5f1f6', '#7f1832', '#40a347', '#c4507c', '#6435e8', '#a7e149', '#b0d1ed', '#b2ff66', '#ebf96a']

pit_src_name = {'Hip/Shoulder Separation' : "https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FF1hNM%2FbtsyXZNSsG0%2FqHcaFPr3U5IqKBP8enGdlk%2Fimg.png",
            'Elbow Flexion' : "https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FYPj8D%2Fbtsy4b0PjGT%2FacxybeGX01XUgjOW3KzTuk%2Fimg.png",
            'Shoulder External Rotaion' : "https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FcA5uIp%2FbtsyTXXzk3H%2F3gvShC3j2W5dpkP6oSn6qK%2Fimg.png",
            'Shoulder Horizontal Abduction' : "https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FbMNU1k%2FbtsyTxEQCGe%2FazjHlTudjOQJdjkMd45RBK%2Fimg.png",
            'Shoulder Abduction' : "https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FZ68RV%2FbtsyU4h6MxZ%2FLMfDEMRO2rtfncrGKPkiE1%2Fimg.png",
            'Lead Leg Knee Flexion' : "https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FAISc3%2FbtsyViAqe0j%2FqkKnVXFoxKbWz5maT1McHK%2Fimg.png",
            'Lead Leg Knee Extension Angular Velocity' : "https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2Fc8xB5Z%2Fbtsy4i6t7rz%2F6PbsxYYtYkrS1Y1lzxKMnk%2Fimg.png",
            'Trunk Forward Tilt' : "https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FbbxkIS%2FbtsyYpFwfBU%2FNGGK8ebdS8iVWTmUxwNKr0%2Fimg.png",
            'Trunk Lateral Tilt' : "https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2Fb4GH1Z%2Fbtsy3OSltlF%2FqGNLUkvxLZfIeupKkjoox1%2Fimg.png",
            'Kinematic Sequence' : "https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2Fbyb824%2FbtsyV1Stif0%2FiEXEHXjrkcKNNoPltvHAIK%2Fimg.png"}

pit_kinematic_columns = ['Pelvis Angular Velocity',
                     'Torso Angular Velocity',
                     'Elbow Angular Velocity',
                     'Shoulder Angular Velocity']

pit_kinematic_colors = {'Pelvis Angular Velocity': 'red',
                    'Torso Angular Velocity': 'orange',
                    'Elbow Angular Velocity': 'green',
                    'Shoulder Angular Velocity': 'blue'}

hit_src_name = {'Hip/Shoulder Separation' : "https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2Fbyb824%2FbtsyV1Stif0%2FiEXEHXjrkcKNNoPltvHAIK%2Fimg.png",
            'Shoulder External Rotaion' : "https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FF1hNM%2FbtsyXZNSsG0%2FqHcaFPr3U5IqKBP8enGdlk%2Fimg.png",
            'Shoulder Abduction' : "https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FYPj8D%2Fbtsy4b0PjGT%2FacxybeGX01XUgjOW3KzTuk%2Fimg.png",
            'Elbow Flexion' : "https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FcA5uIp%2FbtsyTXXzk3H%2F3gvShC3j2W5dpkP6oSn6qK%2Fimg.png",
            'Torso Lateral Tilt' : "https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FbMNU1k%2FbtsyTxEQCGe%2FazjHlTudjOQJdjkMd45RBK%2Fimg.png",
            'Torso Forward Tilt' : "https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FZ68RV%2FbtsyU4h6MxZ%2FLMfDEMRO2rtfncrGKPkiE1%2Fimg.png",
            'Torso Rotation' : "https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FAISc3%2FbtsyViAqe0j%2FqkKnVXFoxKbWz5maT1McHK%2Fimg.png",
            'Pelvis Lateral Tilt' : "https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2Fc8xB5Z%2Fbtsy4i6t7rz%2F6PbsxYYtYkrS1Y1lzxKMnk%2Fimg.png",
            'Pelvis Forward Tilt' : "https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2Fc8xB5Z%2Fbtsy4i6t7rz%2F6PbsxYYtYkrS1Y1lzxKMnk%2Fimg.png",
            'Pelvis Rotation' : "https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2Fc8xB5Z%2Fbtsy4i6t7rz%2F6PbsxYYtYkrS1Y1lzxKMnk%2Fimg.png",
            'Kinematic Sequence' : "https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2Fbyb824%2FbtsyV1Stif0%2FiEXEHXjrkcKNNoPltvHAIK%2Fimg.png",
            'GRF' : "https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2Fbyb824%2FbtsyV1Stif0%2FiEXEHXjrkcKNNoPltvHAIK%2Fimg.png"}

hit_kinematic_columns = ['Pelvis Angular Velocity',
                         'Torso Angular Velocity',
                         'Arm Angular Velocity']

hit_kinematic_colors = {'Pelvis Angular Velocity': 'red',
                        'Torso Angular Velocity': 'green',
                        'Arm Angular Velocity': 'blue'}

hit_GRF_columns = ['Front Vertical Force',
                         'Back Vertical Force',
                         'Total Vertical Force']

hit_GRF_colors = {'Front Vertical Force': 'red',
                        'Back Vertical Force': 'green',
                        'Total Vertical Force': 'blue'}

# Initialization
app = dash.Dash(__name__)
app.title = ("KMU Baseball Report")
server = app.server

# 2. Layout
app.layout = html.Div([
    html.Div(id='report-selection', children=[
        html.H1("Select Report Type", style={'color': 'white', 'fontFamily': 'Verdana'}),
    
        dcc.RadioItems(
            id='report-type-radioitems',
            options=[
                {'label': "Batter's Report", 'value': 'batter'},
                {'label': "Pitcher's Report", 'value': 'pitcher'}
            ],
            style={'color': 'white', 'fontFamily': 'Verdana'},
            labelStyle={'display': 'inline-block', 'marginRight': '20px'}
        ),
        html.Button("Go", id="go-button-report", style={'marginTop': '20px'}),
        html.Button("Back to Report Selection", id="back-button", style={'marginBottom': '20px', 'display': 'none'})
        ]),
    
    # Report-specific layout
    html.Div(id='report-dashboard')
    ], style={'backgroundColor': '#074CA1'})

# 3. Callbacks
@app.callback(
    [dd.Output('report-dashboard', 'children'),
     dd.Output('report-selection', 'style')],
    [dd.Input('go-button-report', 'n_clicks'),
     dd.Input('back-button', 'n_clicks')],
    [dd.State('report-type-radioitems', 'value')]
)

def combined_callback(go_button_clicks, back_button_clicks, selected_report):
    ctx = dash.callback_context
    if not ctx.triggered:
        return None, {}
    
    # Identify which component was triggered
    triggered_id = ctx.triggered[0]['prop_id'].split('.')[0]

    # If "Go" button was clicked
    if triggered_id == 'go-button-report' and go_button_clicks and selected_report == 'pitcher':
        return html.Div([
            html.Button("Back to Report Selection", id="back-button", style={'marginBottom': '20px'}),
            dcc.Dropdown(
                id='player-dropdown',
                options=[{'label': player, 'value': player} for player in pit_players],
                placeholder="Select a player"
            ),

            dcc.RadioItems(
                id='consistency-mean-radioitems',
                options=[
                    {'label': "Consistency", 'value': 'consistency'},
                    {'label': "Mean", 'value': 'mean'}
                ],
                value='consistency',
                style={'color': 'white', 'fontFamily': 'Verdana'},
                labelStyle={'display': 'inline-block', 'marginRight': '20px'}
            ),

            html.Div(id='player-checklists'),
            html.Div(id='player-graph')
        ], style={'marginLeft': '30px', 'padding': '10px', 'marginBottom': '30px', 'backgroundColor': '#2B303D'}), {'display': 'none'}
    
    elif triggered_id == 'go-button-report' and go_button_clicks and selected_report == 'batter':
        return html.Div([
            html.Button("Back to Report Selection", id="back-button", style={'marginBottom': '20px'}),
            dcc.Dropdown(
                id='player-dropdown',
                options=[{'label': player, 'value': player} for player in hit_players],
                placeholder="Select a player..."
            ),

            dcc.RadioItems(
                id='consistency-mean-radioitems',
                options=[
                    {'label': "Consistency", 'value': 'consistency'},
                    {'label': "Mean", 'value': 'mean'}
                ],
                value='consistency',
                style={'color': 'white', 'fontFamily': 'Verdana', 'display': 'none'},  # Initially hidden
                labelStyle={'display': 'inline-block', 'marginRight': '20px'}
            ),

            html.Div(id='player-checklists'),
            html.Div(id='player-graph')
        ], style={'marginLeft': '30px', 'padding': '10px', 'marginBottom': '30px', 'backgroundColor': '#074CA1'}), {'display': 'none'}

    # If "Back to Report Selection" button was clicked
    elif triggered_id == 'back-button' and back_button_clicks:
        return None, {}
    
    return dash.no_update, dash.no_update

# Callback for player dropdown to update checklists and graph
@app.callback(
    dd.Output('player-checklists', 'children'),
    [dd.Input('player-dropdown', 'value')],
    [dd.State('report-type-radioitems', 'value')]
    )

def update_checklists(selected_player, selected_report):
    if not selected_player:
        return None

    if selected_report == 'pitcher':
        # Extract data for the selected player
        player_data = pit_all_data[pit_all_data['Name'] == selected_player]

        trial_buttons = html.Div([
            html.Button("Select All", id="select-all-trials", style={'marginRight': '10px'}),
            html.Button("Clear All", id="clear-all-trials")
        ])

        # Create Trials Checklist
        trials_checklist = dcc.Checklist(
            id='trial-checklist',
            options=[{'label': f'Trial {i}', 'value': i} for i in player_data['Trial'].unique()],
            value=[],
            inline=True,
            style={'color': 'white', 'fontFamily': 'Verdana'},
            labelStyle={'marginRight': '20px'}
        )

        # Buttons for "Select All" and "Clear All" for Variables
        variables_buttons = html.Div([
            html.Button("Select All", id="select-all-variables", style={'marginRight': '10px'}),
            html.Button("Clear All", id="clear-all-variables")
        ])

        # Create Variables Checklist
        columns_to_exclude = ['Time', 'Trial', 'Name', 'Pelvis Angular Velocity', 'Torso Angular Velocity', 'Elbow Angular Velocity', 'Shoulder Angular Velocity']
        variable_options = [col for col in player_data.columns if col not in columns_to_exclude]
        variable_options.append('Kinematic Sequence')

        variables_checklist = dcc.Checklist(
            id='variables-checklist',
            options=[{'label': col, 'value': col} for col in variable_options],
            value=[],
            inline=True,
            style={'color': 'white', 'fontFamily': 'Verdana'},
            labelStyle={'marginRight': '20px'}
        )

    elif selected_report == 'batter':
        # Extract data for the selected player
        player_data = hit_all_data[hit_all_data['Name'] == selected_player]

        trial_buttons = html.Div([
            html.Button("Select All", id="select-all-trials", style={'marginRight': '10px'}),
            html.Button("Clear All", id="clear-all-trials")
        ])

        # Create Trials Checklist
        trials_checklist = dcc.Checklist(
            id='trial-checklist',
            options=[{'label': f'Trial {i}', 'value': i} for i in player_data['Trial'].unique()],
            value=[],
            inline=True,
            style={'color': 'white', 'fontFamily': 'Verdana'},
            labelStyle={'marginRight': '20px'}
        )

        # Buttons for "Select All" and "Clear All" for Variables
        variables_buttons = html.Div([
            html.Button("Select All", id="select-all-variables", style={'marginRight': '10px'}),
            html.Button("Clear All", id="clear-all-variables")
        ])

        # Create Variables Checklist   
        columns_to_exclude = ['Time', 'Trial', 'Name', 'Torso Angular Velocity', 'Pelvis Angular Velocity', 'Arm Angular Velocity', 'Front Vertical Force', 'Back Vertical Force', 'Total Vertical Force']
        variable_options = [col for col in player_data.columns if col not in columns_to_exclude]
        variable_options.append('Kinematic Sequence')
        variable_options.append('GRF')

        variables_checklist = dcc.Checklist(
            id='variables-checklist',
            options=[{'label': col, 'value': col} for col in variable_options],
            value=[],
            inline=True,
            style={'color': 'white', 'fontFamily': 'Verdana'},
            labelStyle={'marginRight': '20px'}
        )

    return html.Div([
        html.Label("Select Trials:", style={'color': 'white'}),
        trial_buttons,
        trials_checklist,
        html.Label("Select Variables:", style={'color': 'white'}),
        variables_buttons,
        variables_checklist
    ])

# Callbacks for the new buttons
@app.callback(
    dd.Output('trial-checklist', 'value'),
    [dd.Input('select-all-trials', 'n_clicks'),
     dd.Input('clear-all-trials', 'n_clicks')],
    [dd.State('trial-checklist', 'options')]
)
def update_trial_selection(select_all, clear_all, options):
    ctx = dash.callback_context
    if not ctx.triggered:
        return dash.no_update

    button_id = ctx.triggered[0]['prop_id'].split('.')[0]
    
    if button_id == 'select-all-trials':
        return [option['value'] for option in options]
    elif button_id == 'clear-all-trials':
        return []

    return dash.no_update

@app.callback(
    dd.Output('variables-checklist', 'value'),
    [dd.Input('select-all-variables', 'n_clicks'),
     dd.Input('clear-all-variables', 'n_clicks')],
    [dd.State('variables-checklist', 'options')]
)
def update_variable_selection(select_all, clear_all, options):
    ctx = dash.callback_context
    if not ctx.triggered:
        return dash.no_update

    button_id = ctx.triggered[0]['prop_id'].split('.')[0]
    
    if button_id == 'select-all-variables':
        return [option['value'] for option in options]
    elif button_id == 'clear-all-variables':
        return []

    return dash.no_update

@app.callback(
    dd.Output('player-graph', 'children'),
    [dd.Input('player-dropdown', 'value'),
     dd.Input('trial-checklist', 'value'),
     dd.Input('variables-checklist', 'value'),
     dd.Input('consistency-mean-radioitems', 'value')],
    [dd.State('report-type-radioitems', 'value')]  # Added this input
)

def update_graph(selected_player, selected_trials, selected_vars, consistency_mean, selected_report):
    if not selected_player or not selected_trials or not selected_vars:
        return None

    # Filter data based on selected player and trials
    if selected_report == 'pitcher':
        filtered_data = pit_all_data[(pit_all_data['Name'] == selected_player) & (pit_all_data['Trial'].isin(selected_trials))].reset_index(drop=True)
    elif selected_report == 'batter':
        filtered_data = hit_all_data[(hit_all_data['Name'] == selected_player) & (hit_all_data['Trial'].isin(selected_trials))].reset_index(drop=True)
            
    graphs = []

    if "Kinematic Sequence" in selected_vars:
        traces = []

        if selected_report == 'pitcher':
            if consistency_mean == 'mean':
                mean_data = filtered_data.groupby('Time').mean().reset_index()
                print(mean_data)
                for col in pit_kinematic_columns:
                    traces.append(go.Scatter(x=mean_data['Time'], y=mean_data[col], mode='lines', name=f'Mean {col}', line=dict(color=pit_kinematic_colors[col])))
            else:
                for col in pit_kinematic_columns:
                    for idx, trial in enumerate(selected_trials):
                        trial_data = filtered_data[filtered_data['Trial'] == trial]
                        color = pit_kinematic_colors[col]
                        traces.append(go.Scatter(x=trial_data['Time'], y=trial_data[col], mode='lines', name=f'{col} - Trial {trial}', line=dict(color=color)))

            # Create a graph for the Kinematic Sequence
            graphs.append(html.Div([
                html.Div(html.Img(src=pit_src_name["Kinematic Sequence"], style={'width': '15%', 'float': 'left', 'marginTop': '95px'}), style={'backgroundColor': '#074CA1'}),
                html.Div(dcc.Graph(
                    figure={
                        'data': traces,
                        'layout': go.Layout(
                            title="Kinematic Sequence",
                            xaxis_title='Time',
                            yaxis_title='Value',
                            hovermode='closest',
                            showlegend=False,
                            paper_bgcolor='#074CA1',
                            plot_bgcolor='#C0C0C0',
                            font=dict(color='white')
                        )
                    }
                ), style={'width': '85%', 'float': 'right'})
            ], style={'clear': 'both', 'backgroundColor': '#074CA1'}))

        elif selected_report == 'batter':
            if consistency_mean == 'mean':
                mean_data = filtered_data.groupby('Time').mean().reset_index()
                for col in hit_kinematic_columns:
                    traces.append(go.Scatter(x=mean_data['Time'], y=mean_data[col], mode='lines', name=f'Mean {col}', line=dict(color=hit_kinematic_colors[col])))
            else:
                for col in hit_kinematic_columns:
                    for idx, trial in enumerate(selected_trials):
                        trial_data = filtered_data[filtered_data['Trial'] == trial]
                        color = hit_kinematic_colors[col]
                        traces.append(go.Scatter(x=trial_data['Time'], y=trial_data[col], mode='lines', name=f'{col} - Trial {trial}', line=dict(color=color)))

            # Create a graph for the Kinematic Sequence
            graphs.append(html.Div([
                html.Div(html.Img(src=hit_src_name["Kinematic Sequence"], style={'width': '15%', 'float': 'left', 'marginTop': '95px'}), style={'backgroundColor': '#074CA1'}),
                html.Div(dcc.Graph(
                    figure={
                        'data': traces,
                        'layout': go.Layout(
                            title="Kinematic Sequence",
                            xaxis_title='Time',
                            yaxis_title='Value',
                            hovermode='closest',
                            showlegend=False,
                            paper_bgcolor='#074CA1',
                            plot_bgcolor='#C0C0C0',
                            font=dict(color='white')
                        )
                    }
                ), style={'width': '85%', 'float': 'right'})
            ], style={'clear': 'both', 'backgroundColor': '#074CA1'}))

        selected_vars.remove("Kinematic Sequence")
    
    if "GRF" in selected_vars:
        traces = []

        if selected_report == 'batter':
            if consistency_mean == 'mean':
                # Compute mean for each of the kinematic columns
                mean_data = filtered_data.groupby('Time').mean().reset_index()
                for col in hit_GRF_columns:
                    traces.append(go.Scatter(x=mean_data['Time'], y=mean_data[col], mode='lines', name=f'Mean {col}', line=dict(color=hit_GRF_colors[col])))
            else:
                for col in hit_GRF_columns:
                    for idx, trial in enumerate(selected_trials):
                        trial_data = filtered_data[filtered_data['Trial'] == trial]
                        color = hit_GRF_colors[col]
                        traces.append(go.Scatter(x=trial_data['Time'], y=trial_data[col], mode='lines', name=f'{col} - Trial {trial}', line=dict(color=color)))

            # Create a graph for the Kinematic Sequence
            graphs.append(html.Div([
                html.Div(html.Img(src=hit_src_name["GRF"], style={'width': '15%', 'float': 'left', 'marginTop': '95px'}), style={'backgroundColor': '#2B303D'}),
                html.Div(dcc.Graph(
                    figure={
                        'data': traces,
                        'layout': go.Layout(
                            title="GRF",
                            xaxis_title='Time',
                            yaxis_title='Value',
                            hovermode='closest',
                            showlegend=False,
                            paper_bgcolor='#074CA1',
                            plot_bgcolor='#C0C0C0',
                            font=dict(color='white')
                        )
                    }
                ), style={'width': '85%', 'float': 'right'})
            ], style={'clear': 'both', 'backgroundColor': '#074CA1'}))

        selected_vars.remove("GRF")
    
    for col in selected_vars:
        traces = []

        # If "consistency" is selected, plot each trial separately
        if consistency_mean == 'consistency':
            if selected_report == 'pitcher':
                traces.append(go.Scatter(x=pit_avg['Time'], y=pit_avg[col] + pit_std[col], mode='lines', fill=None, line_color='rgba(0,100,80,0.2)', showlegend=False))
                traces.append(go.Scatter(x=pit_avg['Time'], y=pit_avg[col] - pit_std[col], mode='lines', fill='tonexty', line_color='rgba(0,100,80,0.2)', showlegend=False))
                
            elif selected_report == 'batter':
                traces.append(go.Scatter(x=hit_avg['Time'], y=hit_avg[col] + hit_std[col], mode='lines', fill=None, line_color='rgba(0,100,80,0.2)', showlegend=False))
                traces.append(go.Scatter(x=hit_avg['Time'], y=hit_avg[col] - hit_std[col], mode='lines', fill='tonexty', line_color='rgba(0,100,80,0.2)', showlegend=False))

            for idx, trial in enumerate(selected_trials):
                trial_data = filtered_data[filtered_data['Trial'] == trial]
                color = custom_palette[idx % len(custom_palette)]
                traces.append(go.Scatter(x=trial_data['Time'], y=trial_data[col], mode='lines', name=f'Trial {trial}', line=dict(color=color)))
                
                fc_time = trial_data['FC'].iloc[0]
                traces.append(go.Scatter(
                    x=[fc_time, fc_time],
                    y=[trial_data[col].min(), trial_data[col].max()],
                    mode='lines',
                    line=dict(color='#fffcc3'),
                    hoverinfo='text',  # Display custom hover text
                    hovertext=f'Trial {trial} FC',  # Custom hover text
                    showlegend=False
                ))

        elif consistency_mean == 'mean':
            mean_data = filtered_data.groupby('Time').mean().reset_index()
            traces.append(go.Scatter(x=mean_data['Time'], y=mean_data[col], mode='lines', name=f'Mean {col}', line=dict(color='#ffff99')))
        
        if selected_report == 'pitcher':
            tmp_src = pit_src_name.get(col, "")
        elif selected_report == 'batter':
            tmp_src = hit_src_name.get(col, "")

        graphs.append(html.Div([
            html.Img(src=tmp_src, style={'width': '15%', 'float': 'left', 'marginTop': '90px'}),
            html.Div(dcc.Graph(
                figure={
                    'data': traces,
                    'layout': go.Layout(
                        title=col,
                        xaxis_title='Time',
                        yaxis_title='Value',
                        hovermode='closest',
                        showlegend=False,
                        paper_bgcolor='#074CA1',
                        plot_bgcolor='#C0C0C0',
                        font=dict(color='white')
                    )
                }
            ), style={'width': '85%', 'float': 'right'})
        ], style={'clear': 'both', 'backgroundColor': '#074CA1'}))
 
    return graphs


# Run the app
if __name__ == '__main__':

    app.run_server(debug=True)