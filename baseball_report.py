import dash
from dash import dcc
from dash import html
import dash.dependencies as dd
import plotly.graph_objs as go
import pandas as pd
import os

folder_path = 'Data/'

pit_path = folder_path + 'Processed Data/Pitching Data'
pit_all_files = [f for f in os.listdir(pit_path) if f.endswith('.csv')]
pit_players = list(set([f.split('_')[0] for f in pit_all_files]))

hit_path = folder_path + 'Processed Data/Hitting Data'
hit_all_files = [f for f in os.listdir(hit_path) if f.endswith('.csv')]
hit_players = list(set([f.split('_')[0] for f in hit_all_files]))

pit_avg = pd.read_csv(folder_path + 'Driveline_Pitching_Timenormalize_avg.csv')
pit_std = pd.read_csv(folder_path + 'Driveline_Pitching_Timenormalize_std.csv')

hit_avg = pd.read_csv(folder_path + 'Driveline_Hitting_Timenormalize_avg.csv')
hit_std = pd.read_csv(folder_path + 'Driveline_Hitting_Timenormalize_std.csv')

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

pit_col_name = {'Hip/Shoulder Separation' : "엉덩이/어깨 분리 각도",
            'Elbow Flexion' : "팔꿈치 굽힘 각도",
            'Shoulder External Rotaion' : "어깨 외회전 각도",
            'Shoulder Horizontal Abduction' : "어깨 수평 벌림 각도",
            'Shoulder Abduction' : "어깨 벌림 각도",
            'Lead Leg Knee Flexion' : "무릎 굽힘 각도",
            'Lead Leg Knee Extension Angular Velocity' : "무릎 폄속도",
            'Trunk Forward Tilt' : "앞쪽 몸통 기울기",
            'Trunk Lateral Tilt' : "옆쪽 몸통 기울기",
            'Kinematic Sequence' : "키네마틱 시퀀스"}

pit_kinematic_columns = ['Pelvis Angular Velocity',
                     'Torso Angular Velocity',
                     'Elbow Angular Velocity',
                     'Shoulder Angular Velocity']

pit_kinematic_colors = {'Pelvis Angular Velocity': '#e63946',
                    'Torso Angular Velocity': '#2a9d8f',
                    'Elbow Angular Velocity': '#e9c46a',
                    'Shoulder Angular Velocity': '#3a86ff'}

hit_src_name = {'Hip/Shoulder Separation' : "https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2Fbyb824%2FbtsyV1Stif0%2FiEXEHXjrkcKNNoPltvHAIK%2Fimg.png",
            'Shoulder Horizontal Abduction' : "https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FF1hNM%2FbtsyXZNSsG0%2FqHcaFPr3U5IqKBP8enGdlk%2Fimg.png",
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

hit_col_name = {'Hip/Shoulder Separation' : "엉덩이/어깨 분리 각도",
            'Shoulder Horizontal Abduction' : "어깨 수평 벌림 각도",
            'Shoulder Abduction' : "어깨 벌림 각도",
            'Elbow Flexion' : "팔꿈치 굽힘 각도",
            'Torso Lateral Tilt' : "옆쪽 몸통 기울기",
            'Torso Forward Tilt' : "앞쪽 몸통 기울기",
            'Torso Rotation' : "몸통 회전 각도",
            'Pelvis Lateral Tilt' : "옆쪽 골반 기울기",
            'Pelvis Forward Tilt' : "앞쪽 골반 기울기",
            'Pelvis Rotation' : "골반 회전 각도",
            'Kinematic Sequence' : "키네마틱 시퀀스",
            'GRF' : "지면 반력",
            'COP Velocity' : '압력 중심점 이동 속도'}


hit_kinematic_columns = ['Pelvis Angular Velocity',
                         'Torso Angular Velocity',
                         'Arm Angular Velocity']

hit_kinematic_colors = {'Pelvis Angular Velocity': '#e63946',
                        'Torso Angular Velocity': '#2a9d8f',
                        'Arm Angular Velocity': '#3a86ff'}

hit_GRF_columns = ['Front Vertical Force',
                         'Back Vertical Force',
                         'Total Vertical Force']

hit_GRF_colors = {'Front Vertical Force': '#e63946',
                        'Back Vertical Force': '#2a9d8f',
                        'Total Vertical Force': '#3a86ff'}

# Initialization
app = dash.Dash(__name__)
app.title = ("KMU Baseball Report")
server = app.server

USER_LOGGED_IN = False

# 2. Layout
login_layout = html.Div([
    dcc.Location(id='url-login', refresh=True),
    html.Div([
        html.Div([
            html.Div([
                dcc.Input(
                    placeholder='Enter your username',
                    type='text',
                    id='uname-box',
                    className='uname_box'
                ),
                dcc.Input(
                    placeholder='Enter your password',
                    type='password',
                    id='pwd-box',
                    className='pwd_box'
                ),
                html.Button(
                    children='Login',
                    n_clicks=0,
                    type='submit',
                    id='login-button',
                    className='login_button'
                ),
                html.Div(children='', id='output-state')
            ], className='form_container'),
        ], className='login_container'),
    ], className='login_page')
])

report_layout = html.Div([
    dcc.Location(id='url-report', refresh=True),
    html.Div(id='report-selection', children=[
        html.H1("레포트 유형 선택", style={'color': 'white', 'fontFamily': 'Verdana'}),
    
        dcc.RadioItems(
            id='report-type-radioitems',
            options=[
                {'label': "타자 레포트", 'value': 'hitter'},
                {'label': "투수 레포트", 'value': 'pitcher'}
            ],
            style={'color': 'white', 'fontFamily': 'Verdana'},
            labelStyle={'display': 'inline-block', 'marginRight': '30px'}
        ),
        html.Button("레포트 보기", id="go-button-report", style={'marginTop': '30px'}),
        html.Button("뒤로 가기", id="back-button", style={'display': 'none'})
        ]),
    
    html.Div(id='report-dashboard'),
    html.Button('Logout', id='logout-button', n_clicks=0)
    ], style={'padding' : '20px', 'backgroundColor': '#313746'})

app.layout = html.Div([
    html.Div(id='page-content', children=login_layout)
])

# 3. Callbacks
@app.callback(Output('page-content', 'children'),
              [Input('login-button', 'n_clicks')],
              [State('uname-box', 'value'),
               State('pwd-box', 'value')])
def login(n_clicks, username, password):
    if n_clicks > 0:
        if username == 'id' and password == 'password':  # Replace with your own validation logic
            return report_layout
        else:
            return login_layout
    else:
        return login_layout

# 로그아웃 콜백
@app.callback(Output('url-report', 'pathname'),
              [Input('logout-button', 'n_clicks')])
def logout(n_clicks):
    if n_clicks > 0:
        return '/login'
    return '/report'

@app.callback(
    [dd.Output('report-dashboard', 'children'),
     dd.Output('report-selection', 'style'),
     dd.Output('report-type-radioitems', 'value')],  # 값 초기화를 위해 Output 추가
    [dd.Input('go-button-report', 'n_clicks'),
     dd.Input('back-button', 'n_clicks')],
    [dd.State('report-type-radioitems', 'value')]
)

def combined_callback(go_button_clicks, back_button_clicks, selected_report):
    ctx = dash.callback_context
    if not ctx.triggered:
        # 'report-type-radioitems'의 Output을 추가로 반환해야 하므로, None 대신 dash.no_update를 추가합니다.
        return None, {}, dash.no_update
    
    triggered_id = ctx.triggered[0]['prop_id'].split('.')[0]

    if triggered_id == 'go-button-report' and go_button_clicks:
        if selected_report == 'pitcher':
            return html.Div([html.Div([
                    html.Span("투수 레포트", style={'float': 'left', 'marginBottom': '20px', 'marginLeft': '10px', 'lineHeight': '30px', 'fontSize': '30px', 'color': 'white'}),
                    html.Button("뒤로 가기", id="back-button", style={'float': 'right'})
                    ], style={'textAlign': 'right', 'display': 'block'}),
                dcc.Dropdown(
                    id='player-dropdown',
                    options=[{'label': player, 'value': player} for player in pit_players],
                    placeholder="선수 선택",
                    style={'marginTop': '30px', 'marginBottom': '30px', 'fontFamily': 'Verdana'}
                ),

                dcc.RadioItems(
                    id='consistency-mean-radioitems',
                    options=[
                        {'label': "개별 그래프", 'value': 'consistency'},
                        {'label': "평균 그래프", 'value': 'mean'}
                    ],
                    value='consistency',
                    style={'color': 'white', 'fontFamily': 'Verdana', 'marginBottom': '30px'},
                    labelStyle={'display': 'inline-block', 'marginRight': '30px'}
                ),

                html.Div(id='player-checklists'),
                html.Div(id='player-graph')
            ], style={'padding': '10px', 'backgroundColor': '#2B303D'}), {'display': 'none'}, dash.no_update

        elif selected_report == 'hitter':
            return html.Div([html.Div([
                    html.Span("타자 레포트", style={'float': 'left', 'marginBottom': '20px', 'marginLeft': '10px', 'lineHeight': '30px', 'fontSize': '30px', 'color': 'white'}),
                    html.Button("뒤로 가기", id="back-button", style={'float': 'right'})
                    ], style={'textAlign': 'right', 'display': 'block'}),
                dcc.Dropdown(
                    id='player-dropdown',
                    options=[{'label': player, 'value': player} for player in hit_players],
                    placeholder="선수 선택",
                    style={'marginTop': '30px', 'marginBottom': '30px', 'fontFamily': 'Verdana'}
                ),

                dcc.RadioItems(
                    id='consistency-mean-radioitems',
                    options=[
                        {'label': "개별 그래프", 'value': 'consistency'},
                        {'label': "평균 그래프", 'value': 'mean'}
                    ],
                    value='consistency',
                    style={'color': 'white', 'fontFamily': 'Verdana', 'marginBottom': '30px'},
                    labelStyle={'display': 'inline-block', 'marginRight': '30px'}
                ),

                html.Div(id='player-checklists'),
                html.Div(id='player-graph')
            ], style={'padding': '10px', 'backgroundColor': '#2B303D'}), {'display': 'none'}, dash.no_update

    elif triggered_id == 'back-button' and back_button_clicks:
        return None, {'display': 'block'}, ''
    
    return dash.no_update, dash.no_update, dash.no_update

@app.callback(
    dd.Output('player-checklists', 'children'),
    [dd.Input('player-dropdown', 'value')],
    [dd.State('report-type-radioitems', 'value')]
    )

def update_checklists(selected_player, selected_report):
    if not selected_player:
        return None

    if selected_report == 'pitcher':
        player_data = pit_all_data[pit_all_data['Name'] == selected_player]

        trial_buttons = html.Div([
            html.Button("전체 선택", id="select-all-trials", style={'marginTop': '15px', 'marginBottom': '10px', 'marginRight': '10px'}),
            html.Button("전체 해제", id="clear-all-trials")
        ])

        trials_checklist = dcc.Checklist(
            id='trial-checklist',
            options=[{'label': f'{i}번째', 'value': i} for i in player_data['Trial'].unique()],
            value=[],
            inline=True,
            style={'color': 'white', 'fontFamily': 'Verdana'},
            labelStyle={'marginRight': '30px', 'marginBottom': '10px'}
        )

        variables_buttons = html.Div([
            html.Button("전체 선택", id="select-all-variables", style={'marginTop': '15px', 'marginBottom': '10px', 'marginRight': '10px'}),
            html.Button("전체 해제", id="clear-all-variables")
        ])

        columns_to_exclude = ['Time', 'Trial', 'Name', 'Pelvis Angular Velocity', 'Torso Angular Velocity', 'Elbow Angular Velocity', 'Shoulder Angular Velocity']
        variable_options = [col for col in player_data.columns if col not in columns_to_exclude]
        variable_options.append('Kinematic Sequence')

        variables_checklist = dcc.Checklist(
            id='variables-checklist',
            options=[{'label': pit_col_name.get(col, ""), 'value': col} for col in variable_options],
            value=[],
            inline=True,
            style={'color': 'white', 'fontFamily': 'Verdana'},
            labelStyle={'marginRight': '30px'}
        )

    elif selected_report == 'hitter':
        player_data = hit_all_data[hit_all_data['Name'] == selected_player]

        trial_buttons = html.Div([
            html.Button("전체 선택", id="select-all-trials", style={'marginTop': '15px', 'marginBottom': '10px', 'marginRight': '10px'}),
            html.Button("전체 해제", id="clear-all-trials")
        ])

        trials_checklist = dcc.Checklist(
            id='trial-checklist',
            options=[{'label': f'{i}번째', 'value': i} for i in player_data['Trial'].unique()],
            value=[],
            inline=True,
            style={'color': 'white', 'fontFamily': 'Verdana'},
            labelStyle={'marginRight': '30px', 'marginBottom': '10px'}
        )

        variables_buttons = html.Div([
            html.Button("전체 선택", id="select-all-variables", style={'marginTop': '15px', 'marginBottom': '10px', 'marginRight': '10px'}),
            html.Button("전체 해제", id="clear-all-variables")
        ])
 
        columns_to_exclude = ['Time', 'Trial', 'Name', 'Torso Angular Velocity', 'Pelvis Angular Velocity', 'Arm Angular Velocity', 'Front Vertical Force', 'Back Vertical Force', 'Total Vertical Force']
        variable_options = [col for col in player_data.columns if col not in columns_to_exclude]
        variable_options.append('Kinematic Sequence')
        variable_options.append('GRF')

        variables_checklist = dcc.Checklist(
            id='variables-checklist',
            options=[{'label': hit_col_name.get(col, ""), 'value': col} for col in variable_options],
            value=[],
            inline=True,
            style={'color': 'white', 'fontFamily': 'Verdana'},
            labelStyle={'marginRight': '30px'}
        )

    return html.Div([
        html.Label("Trial 선택", style={'color': 'white', 'fontFamily': 'Verdana'}),
        trial_buttons,
        trials_checklist,
        html.Div(style={'height': '30px', 'backgroundColor': '#2B303D'}),
        html.Label("변수 선택", style={'color': 'white', 'fontFamily': 'Verdana', 'marginTop': '20px'}),
        variables_buttons,
        variables_checklist,
        html.Div(style={'height': '50px', 'backgroundColor': '#2B303D'})
        ])

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
    [dd.State('report-type-radioitems', 'value')]
)

def update_graph(selected_player, selected_trials, selected_vars, consistency_mean, selected_report):
    if not selected_player or not selected_trials or not selected_vars:
        return None

    if selected_report == 'pitcher':
        filtered_data = pit_all_data[(pit_all_data['Name'] == selected_player) & (pit_all_data['Trial'].isin(selected_trials))].reset_index(drop=True)
    elif selected_report == 'hitter':
        filtered_data = hit_all_data[(hit_all_data['Name'] == selected_player) & (hit_all_data['Trial'].isin(selected_trials))].reset_index(drop=True)
            
    graphs = []

    if "Kinematic Sequence" in selected_vars:
        traces = []
        min_values = []
        max_values = []

        if selected_report == 'pitcher':
            if consistency_mean == 'mean':
                mean_data = filtered_data.groupby('Time').mean(numeric_only=True).reset_index()
                for col in pit_kinematic_columns:
                    traces.append(go.Scatter(x=mean_data['Time'], y=mean_data[col], mode='lines', name=f'평균 {col}', line=dict(color=pit_kinematic_colors[col])))
                    min_values.append(mean_data[col].min())
                    max_values.append(mean_data[col].max())

                min_of_mins = min(min_values)
                max_of_maxes = max(max_values)
                for col in pit_kinematic_columns:
                    max_time = mean_data.loc[mean_data.index[mean_data[col] == mean_data[col].max()][0], 'Time']
                    traces.append(go.Scatter(
                        x=[max_time, max_time],
                        y=[min_of_mins, max_of_maxes],
                        mode='lines',
                        line=dict(color=pit_kinematic_colors[col], dash='dot'),
                        showlegend=False
                    ))

                traces.append(go.Scatter(
                    x=[375, 375],
                    y=[min_of_mins, max_of_maxes],
                    mode='lines',
                    line=dict(color='#FFFFFF'),
                    hoverinfo='text',
                    hovertext=f'FC',
                    showlegend=False
                ))
            else:
                for idx, trial in enumerate(selected_trials):
                    trial_data = filtered_data[filtered_data['Trial'] == trial]
                    for col in pit_kinematic_columns:
                        max_time = trial_data.index[trial_data[col] == trial_data[col].max()][0]
                        max_value = trial_data[col].max()
                        min_value = trial_data[col].min()
                        min_values.append(min_value)
                        max_values.append(max_value)
                        traces.append(go.Scatter(
                            x=[trial_data.loc[max_time, 'Time'], trial_data.loc[max_time, 'Time']],
                            y=[trial_data['Shoulder Angular Velocity'].min(), trial_data['Shoulder Angular Velocity'].max()],
                            mode='lines',
                            line=dict(color=pit_kinematic_colors[col], dash='dot'),
                            name=f'{trial}번째',
                            showlegend=False
                        ))

                        traces.append(go.Scatter(x=trial_data['Time'], y=trial_data[col], mode='lines', name=f'{trial}번째', line=dict(color=pit_kinematic_colors[col])))

                traces.append(go.Scatter(
                    x=[375, 375],
                    y=[trial_data[col].min(), trial_data[col].max()],
                    mode='lines',
                    line=dict(color='#FFFFFF'),
                    hoverinfo='text',
                    hovertext=f'FC',
                    showlegend=False
                ))

            graphs.append(html.Div([
                html.Div(
                    style={'display': 'flex', 'alignItems': 'center', 'backgroundColor': '#2B303D'},
                    children=[
                        html.Div(
                            html.Img(src=pit_src_name["Kinematic Sequence"], style={'padding' : '1%', 'width': '100%'}),
                            style={'width': '13%', 'backgroundColor': '#2B303D'}
                        ),
                dcc.Graph(figure={
                        'data': traces,
                        'layout': go.Layout(
                            title="키네마틱 시퀀스",
                            xaxis={
                                'title': '시간',
                                'tickvals': [0, 375, 500],
                                'ticktext': ['0s', '1.5s (FC)', '2s'],
                                'showline': True,
                                'showgrid': False,
                                'showticklabels': True,
                                'color': 'white',
                                'linecolor': 'white',
                            },
                            yaxis={
                                'title': '각속도',
                                'zeroline': True,
                                'zerolinecolor': '#808080',
                                'showline': True,
                                'showgrid': True,
                                'showticklabels': True,
                                'color': 'white',
                                'linecolor': 'white',
                            },
                            hovermode='closest',
                            showlegend=False,
                            paper_bgcolor='#2B303D',
                            plot_bgcolor='#2B303D',
                            font=dict(color='white')
                        )
                    },
                    style={'width': '85%'}
                )
                    ]
                )], style={'backgroundColor': '#252934'}
            ))

        elif selected_report == 'hitter':
            if consistency_mean == 'mean':
                mean_data = filtered_data.groupby('Time').mean(numeric_only=True).reset_index()
                for col in hit_kinematic_columns:
                    traces.append(go.Scatter(x=mean_data['Time'], y=mean_data[col], mode='lines', name=f'평균 {col}', line=dict(color=hit_kinematic_colors[col])))
                    min_values.append(mean_data[col].min())
                    max_values.append(mean_data[col].max())

                min_of_mins = min(min_values)
                max_of_maxes = max(max_values)
                for col in hit_kinematic_columns:
                    max_time = mean_data.loc[mean_data.index[mean_data[col] == mean_data[col].max()][0], 'Time']
                    traces.append(go.Scatter(
                        x=[max_time, max_time],
                        y=[min_of_mins, max_of_maxes],
                        mode='lines',
                        line=dict(color=hit_kinematic_colors[col], dash='dot'),
                        showlegend=False
                    ))

                traces.append(go.Scatter(
                    x=[1500, 1500],
                    y=[min_of_mins, max_of_maxes],
                    mode='lines',
                    line=dict(color='#FFFFFF'),
                    hoverinfo='text',
                    hovertext=f'FC',
                    showlegend=False
                ))
            else:
                for idx, trial in enumerate(selected_trials):
                    trial_data = filtered_data[filtered_data['Trial'] == trial]
                    for col in hit_kinematic_columns:
                        max_time = trial_data.index[trial_data[col] == trial_data[col].max()][0]
                        max_value = trial_data[col].max()
                        min_value = trial_data[col].min()
                        min_values.append(min_value)
                        max_values.append(max_value)
                        traces.append(go.Scatter(
                            x=[trial_data.loc[max_time, 'Time'], trial_data.loc[max_time, 'Time']],
                            y=[trial_data['Arm Angular Velocity'].min(), trial_data['Arm Angular Velocity'].max()],
                            mode='lines',
                            line=dict(color=hit_kinematic_colors[col], dash='dot'),
                            name=f'{trial}번째',
                            showlegend=False
                        ))

                        traces.append(go.Scatter(x=trial_data['Time'], y=trial_data[col], mode='lines', name=f'{trial}번째', line=dict(color=hit_kinematic_colors[col])))

                traces.append(go.Scatter(
                    x=[1500, 1500],
                    y=[trial_data[col].min(), trial_data[col].max()],
                    mode='lines',
                    line=dict(color='#FFFFFF'),
                    hoverinfo='text',
                    hovertext=f'FC',
                    showlegend=False
                ))

            graphs.append(html.Div([
                html.Div(
                    style={'display': 'flex', 'alignItems': 'center', 'backgroundColor': '#2B303D'},
                    children=[
                        html.Div(
                            html.Img(src=hit_src_name["Kinematic Sequence"], style={'padding' : '1%', 'width': '100%'}),
                            style={'width': '13%', 'backgroundColor': '#2B303D'}
                        ),
                dcc.Graph(figure={
                        'data': traces,
                        'layout': go.Layout(
                            title="키네마틱 시퀀스",
                            xaxis={
                                'title': '시간',
                                'tickvals': [0, 1500, 2000],
                                'ticktext': ['0s', '1.5s (FC)', '2s'],
                                'showline': True,
                                'showgrid': False,
                                'showticklabels': True,
                                'color': 'white',
                                'linecolor': 'white',
                            },
                            yaxis={
                                'title': '각속도',
                                'zeroline': True,
                                'zerolinecolor': '#808080',
                                'showline': True,
                                'showgrid': True,
                                'showticklabels': True,
                                'color': 'white',
                                'linecolor': 'white',
                            },
                            hovermode='closest',
                            showlegend=False,
                            paper_bgcolor='#2B303D',
                            plot_bgcolor='#2B303D',
                            font=dict(color='white')
                        )
                    },
                    style={'width': '85%'}
                )
                    ]
                )], style={'backgroundColor': '#252934'}
            ))
        selected_vars.remove("Kinematic Sequence")
    
    if "GRF" in selected_vars:
        traces = []

        if consistency_mean == 'mean':
            mean_data = filtered_data.groupby('Time').mean(numeric_only=True).reset_index()
            for col in hit_GRF_columns:
                traces.append(go.Scatter(x=mean_data['Time'], y=mean_data[col], mode='lines', name=f'평균 {col}', line=dict(color=hit_GRF_colors[col])))
                traces.append(go.Scatter(
                    x=[1500, 1500],
                    y=[mean_data[col].min(), mean_data[col].max()],
                    mode='lines',
                    line=dict(color='#FFFFFF'),
                    hoverinfo='text',
                    hovertext=f'FC',
                    showlegend=False
                ))
        else:
            for col in hit_GRF_columns:
                for idx, trial in enumerate(selected_trials):
                    trial_data = filtered_data[filtered_data['Trial'] == trial]
                    traces.append(go.Scatter(x=trial_data['Time'], y=trial_data[col], mode='lines', name=f'{trial}번째', line=dict(color=hit_GRF_colors[col])))
                    traces.append(go.Scatter(
                        x=[1500, 1500],
                        y=[trial_data[col].min(), trial_data[col].max()],
                        mode='lines',
                        line=dict(color='#FFFFFF'),
                        hoverinfo='text',
                        hovertext=f'FC',
                        showlegend=False
                    ))

        graphs.append(html.Div([
            html.Div(
                style={'display': 'flex', 'alignItems': 'center', 'backgroundColor': '#2B303D'},
                children=[
                    html.Div(
                        html.Img(src=hit_src_name["GRF"], style={'padding': '1%', 'width': '100%'}),
                        style={'width': '13%', 'backgroundColor': '#2B303D'}
                    ),
            dcc.Graph(
                figure={
                    'data': traces,
                    'layout': go.Layout(
                            title="지면 반력",
                            xaxis={
                                'title': '시간',
                                'tickvals': [0, 1500, 2000],
                                'ticktext': ['0s', '1.5s (FC)', '2s'],
                                'showline': True,
                                'showgrid': False,
                                'showticklabels': True,
                                'color': 'white',
                                'linecolor': 'white',
                            },
                            yaxis={
                                'title': 'N',
                                'zeroline': True,
                                'zerolinecolor': '#808080',
                                'showline': True,
                                'showgrid': True,
                                'showticklabels': True,
                                'color': 'white',
                                'linecolor': 'white',
                            },
                            hovermode='closest',
                            showlegend=False,
                            paper_bgcolor='#2B303D',
                            plot_bgcolor='#2B303D',
                            font=dict(color='white')
                        )
                }, style={'width': '85%'}
            )])
        ], style={'backgroundColor': '#252934', 'marginTop': '80px'}))

        selected_vars.remove("GRF")
    
    for col in selected_vars:
        traces = []

        if consistency_mean == 'consistency':
            if selected_report == 'pitcher':
                traces.append(go.Scatter(x=pit_avg['Time'], y=pit_avg[col] + pit_std[col], mode='lines', fill=None, line_color='rgba(0,100,80,0.2)', showlegend=False))
                traces.append(go.Scatter(x=pit_avg['Time'], y=pit_avg[col] - pit_std[col], mode='lines', fill='tonexty', line_color='rgba(0,100,80,0.2)', showlegend=False))

                for idx, trial in enumerate(selected_trials):
                    trial_data = filtered_data[filtered_data['Trial'] == trial]
                    color = custom_palette[idx % len(custom_palette)]
                    traces.append(go.Scatter(x=trial_data['Time'], y=trial_data[col], mode='lines', name=f'{trial}번째', line=dict(color=color)))

                traces.append(go.Scatter(
                    x=[377, 377],
                    y=[trial_data[col].min(), trial_data[col].max()],
                    mode='lines',
                    line=dict(color='#FFFFFF'),
                    hoverinfo='text',
                    hovertext=f'FC',
                    showlegend=False
                ))
                
            elif selected_report == 'hitter':
                traces.append(go.Scatter(x=hit_avg['Time'], y=hit_avg[col] + hit_std[col], mode='lines', fill=None, line_color='rgba(0,100,80,0.2)', showlegend=False))
                traces.append(go.Scatter(x=hit_avg['Time'], y=hit_avg[col] - hit_std[col], mode='lines', fill='tonexty', line_color='rgba(0,100,80,0.2)', showlegend=False))

                for idx, trial in enumerate(selected_trials):
                    trial_data = filtered_data[filtered_data['Trial'] == trial]
                    color = custom_palette[idx % len(custom_palette)]
                    traces.append(go.Scatter(x=trial_data['Time'], y=trial_data[col], mode='lines', name=f'{trial}번째', line=dict(color=color)))

                traces.append(go.Scatter(
                    x=[1500, 1500],
                    y=[trial_data[col].min(), trial_data[col].max()],
                    mode='lines',
                    line=dict(color='#FFFFFF'),
                    hoverinfo='text',
                    hovertext=f'FC',
                    showlegend=False
                ))
                
        elif consistency_mean == 'mean':
            if selected_report == 'pitcher':
                tmp_k = [377, 377]
            elif selected_report == 'hitter':
                tmp_k = [1500, 1500]

            mean_data = filtered_data.groupby('Time').mean(numeric_only=True).reset_index()
            traces.append(go.Scatter(x=mean_data['Time'], y=mean_data[col], mode='lines', name=f'평균값', line=dict(color='#9CAFDE')))
            traces.append(go.Scatter(
                    x=tmp_k,
                    y=[mean_data[col].min(), mean_data[col].max()],
                    mode='lines',
                    line=dict(color='#FFFFFF'),
                    hoverinfo='text',
                    hovertext=f'FC',
                    showlegend=False
                ))
        
        if selected_report == 'pitcher':
            tmp_src = pit_src_name.get(col, "")
            graph_title = pit_col_name.get(col, "")
            tv = [0, 375, 500]
            tt = ['0s', '1.5s (FC)', '2s']
        elif selected_report == 'hitter':
            tmp_src = hit_src_name.get(col, "")
            graph_title = hit_col_name.get(col, "")
            tv = [0, 1500, 2000]
            tt = ['0s', '1.5s (FC)', '2s']

        graphs.append(html.Div([
            html.Div(
                style={'display': 'flex', 'alignItems': 'center', 'backgroundColor': '#2B303D'},
                children=[
                    html.Div(
                        html.Img(src=tmp_src, style={'padding': '1%', 'width': '100%'}),
                        style={'width': '13%', 'backgroundColor': '#2B303D'}
                    ),
            dcc.Graph(
                figure={
                    'data': traces,
                    'layout': go.Layout(
                        title=graph_title,
                        xaxis={
                            'title': '시간',
                            'tickvals': tv,
                            'ticktext': tt,
                            'showline': True,
                            'showgrid': False,
                            'showticklabels': True,
                            'color': 'white',
                            'linecolor': 'white',
                        },
                        yaxis={
                            'title': '각도',
                            'zeroline': True,
                            'zerolinecolor': '#808080',
                            'showline': True,
                            'showgrid': True,
                            'showticklabels': True,
                            'color': 'white',
                            'linecolor': 'white',
                        },
                        hovermode='closest',
                        showlegend=False,
                        paper_bgcolor='#2B303D',
                        plot_bgcolor='#2B303D',
                        font=dict(color='white')
                    )
                },
                style={'width': '85%'}
            )
                ]
            )], style={'backgroundColor': '#252934', 'marginTop': '80px'}
        ))

    return graphs


# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)