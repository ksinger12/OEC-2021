import plotly.graph_objects as go
import numpy as np
import networkx as nx
from itertools import product
import random
from math import cos, sin, sqrt

from algorithm import Person
from algorithm import getDataForVisualization
from algorithm import PType


fig = go.Figure()

def parseAllPeriods(interactions): 
    graphs = []
    for period in interactions: 
        graphs.append(parsePeriod(period))
    return graphs

def positionByGroup(groupName):
    switcher = {
        "Physics A": (0, 1),
        "Biology A": (0, 2),
        "Functions A": (0, 3),
        "Calculus A": (0, 4),
        "Philosophy A": (0, 5),
        "Art A": (1, 1),
        "Drama A": (1, 2),
        "Computer Science A":  (1, 3),
        "Computer Engineering A":  (1, 4),
        "Humanities A": (1, 5), 
        "Physics B":  (2, 1),
        "Biology B":  (2, 2),
        "Functions B":  (2, 3),
        "Calculus B": (2, 4),
        "Philosophy B":  (2, 5),
        "Art B": (3, 1),
        "Drama B": (3, 2),
        "Computer Science B": (3, 3),
        "Computer Engineering B": (3, 4),
        "Humanities B": (3, 5),

        "Grade9": (0, 0),
        "Grade10": (0, 1),
        "Grade11": (1, 0),
        "Grade12": (1, 1),
        "Workers": (0.5, 0.5),

        "Board Game Club":(0, 1),
        "Football":(0, 2),
        "Soccer":(0, 3),
        "Band":(0, 4),
        "Video Game Club": (1, 1),
        "Computer Science Club": (1, 2),
        "Basketball":(1, 3),
        "Choir": (1, 4),
        "Baseball":(2, 1.5),
        "Drama Club":(2, 2.5),
        "Badminton": (2, 3.5)
    }

    pos = switcher[groupName]

    r = 0.5 * sqrt(random.uniform(0, 1))
    theta = random.uniform(0, 1) * 2 * 3.14
    return (pos[0] + r * cos(theta), pos[1] + r * sin(theta))
 

def parsePeriod(period):
    G_graphs = []
    for class_ in period.keys():
        G_ = nx.Graph()
        x = 0
        for person in period[class_]:
            G_.add_node(x, data=person, pos=positionByGroup(class_))
            x += 1
        G_.add_edges_from((a,b) for a,b in product(range(len(period[class_])), range(len(period[class_]))) if a != b)
        

        G_graphs.append(G_)
    G = nx.disjoint_union_all(G_graphs)

    # print(G.nodes(data=True))
    # print(G.nodes)
    # print(G.edges())

    # print(G.nodes[3]['pos'])
    return G




def displayGraph(list_of_graphs):
        
    for G in list_of_graphs:

        edge_x = []
        edge_y = []
        for edge in G.edges():
            x0, y0 = G.nodes(data=True)[edge[0]]['pos']
            x1, y1 = G.nodes[edge[1]]['pos']
            edge_x.append(x0)
            edge_x.append(x1)
            edge_x.append(None)
            edge_y.append(y0)
            edge_y.append(y1)
            edge_y.append(None)

        edge_trace = go.Scatter(
            x=edge_x, y=edge_y,
            line=dict(width=0.5, color='#888'),
            hoverinfo='none',
            mode='lines')

        node_x = []
        node_y = []
        for node in G.nodes():
            x, y = G.nodes[node]['pos']
            node_x.append(x)
            node_y.append(y)

        node_trace = go.Scatter(
            x=node_x, y=node_y,
            mode='markers',
            hoverinfo='text',
            marker=dict(
                showscale=True,
                # colorscale options
                #'Greys' | 'YlGnBu' | 'Greens' | 'YlOrRd' | 'Bluered' | 'RdBu' |
                #'Reds' | 'Blues' | 'Picnic' | 'Rainbow' | 'Portland' | 'Jet' |
                #'Hot' | 'Blackbody' | 'Earth' | 'Electric' | 'Viridis' |
                colorscale='Picnic',
                reversescale=False,
                color=[],
                size=10,
                colorbar=dict(
                    thickness=15,
                    title='% Chance of Infection',
                    xanchor='left',
                    titleside='right'
                ),
                line_width=2))


        node_adjacencies = []
        node_text = []
        node_infection_prob = []

        for node in G.nodes(data=True):
            person = node[1]['data']
            desc = ''
            desc += person.fname + " " + person.lname + "<br>"
            
            desc += person.ptype.name + "<br>"

            infection_chance = person.infected
            node_infection_prob.append(infection_chance)

            if infection_chance == 1:
                desc = "<b>Patient Zero!</b><br>" + desc
            else:
                desc += f"Chance of Infection: {infection_chance}<br>"
            node_text.append(desc)



        node_connections = []
        for node, adjacencies in enumerate(G.adjacency()):
            node_text[node] += 'Close contacts: '+str(len(adjacencies[1]))

        node_trace.marker.color = node_infection_prob
        node_trace.text = node_text + node_adjacencies




        fig.add_traces([edge_trace, node_trace])



    # Make 1st trace visible
    for dataset in fig.data[2:]:
        dataset.visible = False

    
    print(G)
    # Create and add slider
    steps = []
    periods = ["Period 1 + Movement", "Period 2 + Movement", "Lunch Period + Movement", "Period 3 + Movement", "Period 4 + Movement", "Extracurriculars"]
    for i in range(int(len(fig.data)/2)):
        step = dict(
            method="update",
            args=[{"visible": [False] * len(fig.data)},
                {"title": periods[i]}, 
                {"layout":go.Layout(
                        title="Percent Chance of Infection by Period of Day",
                        titlefont_size=16,
                        showlegend=True,
                        hovermode='closest',
                        margin=dict(b=20,l=5,r=5,t=40),
                        annotations=[ dict(
                            text="Python code: <a href='https://plotly.com/ipython-notebooks/network-graphs/'> https://plotly.com/ipython-notebooks/network-graphs/</a>",
                            showarrow=False,
                            xref="paper", yref="paper",
                            x=0.005, y=-0.002 ) ],
                        xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
                        yaxis=dict(showgrid=False, zeroline=False, showticklabels=False))}
                        ],  # layout attribute
        )
        step["args"][0]["visible"][i*2] = True  # Toggle i*2'th trace to "visible"
        step["args"][0]["visible"][i*2 + 1] = True  # Toggle i*2+1'th trace to "visible"

        steps.append(step)

    sliders = [dict(
        active=0,
        currentvalue={"prefix": "Current Time Period: "},
        pad={"t": 50},
        steps=steps
    )]

    fig.update_layout(
        sliders=sliders,
        title="Percent Chance of Infection by Period of Day"
    )

    fig.add_layout_image(dict(
            source="./classes.png",
            xref="x",
            yref="y",
            x=0,
            y=3,
            sizex=2,
            sizey=2,
            sizing="stretch",
            opacity=0.75,
            layer="below")
    )



    fig.show()




displayGraph(parseAllPeriods(getDataForVisualization()))