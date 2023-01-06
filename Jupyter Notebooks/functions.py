import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation
import cv2
import os
from tqdm import tqdm
import matplotlib.style as mplstyle
mplstyle.use('fast')

from mplsoccer.pitch import Pitch

def save_match_clip_old(ball,hometeam,awayteam, fpath, fname='clip_test', figax=None, frames_per_second=25, team_colors=('r','b'), field_dimen = (105.0,68.0), PlayerMarkerSize=10, PlayerAlpha=0.7):
    """
    Generate a movie clip of a soccer match based on tracking data.
    
    Parameters
    ----------
    ball: pandas DataFrame
        Tracking data for the ball.
    hometeam: pandas DataFrame
        Tracking data for the home team.
    awayteam: pandas DataFrame
        Tracking data for the away team.
    fpath: str
        Directory to save the movie clip.
    fname: str
        Filename for the movie clip (default is 'clip_test').
    figax: tuple of matplotlib Figure and Axes
        Figure and axes to use for plotting (default is None, in which case a new figure and axes will be created).
    frames_per_second: int
        Frame rate for the movie clip (default is 25).
    team_colors: tuple of str
        Colors to use for the home and away teams (default is ('r','b')).
    field_dimen: tuple of float
        Length and width of the soccer pitch in meters (default is (105.0,68.0)).
    PlayerMarkerSize: float
        Size of the markers for the player positions (default is 10).
    PlayerAlpha: float
        Transparency of the markers
    """
    
    # Set index variable to index of hometeam DataFrame
    index = hometeam.index
    # Import FFMpegWriter and initialize with specified frame rate
    FFMpegWriter = animation.writers['ffmpeg']
    # Initialize metadata dictionary with information about movie clip
    metadata = dict(title='Tracking Data', artist='Matplotlib', comment='Tracking data clip')
    # Initialize writer with FFMpegWriter and metadata
    writer = FFMpegWriter(fps=frames_per_second, metadata=metadata)
    # Initialize fname with file path and filename for movie clip
    fname = fpath + '/' +  fname + '.mp4'
    # Create pitch
    if figax is None:
        pitch = Pitch(pitch_type='secondspectrum', # Using second spectrum to fit with tracking data
              pitch_width=68, pitch_length=105, # Setting pitch size to danish standard
              goal_type='box', # Add "nets" to goals
              pitch_color='grass', # Setting the color to be grass 
              line_color='white',  # Setting the lines on the pitch to be white
              stripe=True, # Add stripes to the grass color
              corner_arcs=True, # Add corner arcs
             )

        fig, ax = pitch.draw(figsize=(105/6.562,68/6.562))
    else:
    # Set fig and ax to figax tuple
        fig,ax = figax
    # Adjust subplot parameters to give specified padding
    fig.set_tight_layout(True)
    # Generate movie
    print("Generating movie...",end='')
    with writer.saving(fig, fname, 100):
        for i in ball.frameIdx:
            figobjs = [] # this is used to collect up all the axis objects so that they can be deleted after each iteration
            hobjs = pitch.scatter(hometeam.loc[hometeam["frameIdx"]==i].x,
                                  hometeam.loc[hometeam["frameIdx"]==i].y, 
                                  ax=ax, 
                                  edgecolor='black', # Edge color of the point
                                  c=hometeam.loc[hometeam["frameIdx"]==i].GK, # Color of the point
                                  s=250, # Size of the points
                                  cmap='autumn' #Color map - field players will be green and keeper grey
                                 ) # plot player positions
            figobjs.append(hobjs)
            aobjs = pitch.scatter(awayteam.loc[awayteam["frameIdx"]==i].x,
                                  awayteam.loc[awayteam["frameIdx"]==i].y, 
                                  ax=ax, # What plot to add them to 
                                  edgecolor='black', # Edge color of the point
                                  c=awayteam.loc[awayteam["frameIdx"]==i].GK, # Color of the point
                                  s=250, # Size of the points
                                  cmap='Set2' #Color map - field players will be green and keeper grey
                                 ) # plot player positions
            figobjs.append(aobjs)
            # plot ball
            bobjs = pitch.scatter(ball.loc[ball["frameIdx"]==i].xBall,
                                  ball.loc[ball["frameIdx"]==i].yBall, 
                                  ax=ax, # What plot to add them to 
                                  edgecolor='black', # Edge color of the point
                                  c='black', # Color of the point
                                  s=100 # Size of the points
                                 ) # plot player positions
            figobjs.append(bobjs)
            writer.grab_frame()
            # Delete all axis objects (other than pitch lines) in preperation for next frame
            for figobj in figobjs:
                figobj.remove()
    print("done")
    plt.clf()
    plt.close(fig)    

    
def save_match_clip(ball,hometeam,awayteam, fpath, fname='clip_test', figax=None, frames_per_second=25, team_colors=('r','b'), field_dimen = (105.0,68.0), PlayerMarkerSize=10, PlayerAlpha=0.7):
    """
    Generate a movie clip of a soccer match based on tracking data.
    
    Parameters
    ----------
    ball: pandas DataFrame
        Tracking data for the ball.
    hometeam: pandas DataFrame
        Tracking data for the home team.
    awayteam: pandas DataFrame
        Tracking data for the away team.
    fpath: str
        Directory to save the movie clip.
    fname: str
        Filename for the movie clip (default is 'clip_test').
    figax: tuple of matplotlib Figure and Axes
        Figure and axes to use for plotting (default is None, in which case a new figure and axes will be created).
    frames_per_second: int
        Frame rate for the movie clip (default is 25).
    team_colors: tuple of str
        Colors to use for the home and away teams (default is ('r','b')).
    field_dimen: tuple of float
        Length and width of the soccer pitch in meters (default is (105.0,68.0)).
    PlayerMarkerSize: float
        Size of the markers for the player positions (default is 10).
    PlayerAlpha: float
        Transparency of the markers
    """
    
    # Set index variable to index of hometeam DataFrame
    index = hometeam.index
    
    # Initialize fname with file path and filename for movie clip
    fname = fpath + '/' +  fname + '.mp4'
    # Create pitch
    if figax is None:
        pitch = Pitch(pitch_type='secondspectrum', # Using second spectrum to fit with tracking data
              pitch_width=68, pitch_length=105, # Setting pitch size to danish standard
              goal_type='box', # Add "nets" to goals
              pitch_color='grass', # Setting the color to be grass 
              line_color='white',  # Setting the lines on the pitch to be white
              stripe=True, # Add stripes to the grass color
              corner_arcs=True, # Add corner arcs
             )

        fig, ax = pitch.draw(figsize=(105/6.562,68/6.562))
    else:
    # Set fig and ax to figax tuple
        fig, ax = figax
    
    # Adjust subplot parameters to give specified padding
    fig.set_tight_layout(True)
    
    hobjs = pitch.scatter([],
                      [], 
                      ax=ax, 
                      edgecolor='black', # Edge color of the point
                      c=hometeam.loc[hometeam["frameIdx"]==0].GK, # Color of the point
                      s=250, # Size of the points
                      cmap='autumn' #Color map - field players will be green and keeper grey
                     ) # plot player positions
    
    aobjs = pitch.scatter([],
                      [], 
                      ax=ax, # What plot to add them to 
                      edgecolor='black', # Edge color of the point
                      c=awayteam.loc[awayteam["frameIdx"]==0].GK, # Color of the point
                      s=250, # Size of the points
                      cmap='Set2' #Color map - field players will be green and keeper grey
                     ) # plot player positions
    
    # plot ball
    bobjs = pitch.scatter([],
                          [], 
                          ax=ax, # What plot to add them to 
                          edgecolor='black', # Edge color of the point
                          c='black', # Color of the point
                          s=100 # Size of the points
                         ) # plot player positions
    
    # Generate movie
    print("Generating movie...",end='')
    files = []
    for i in tqdm(ball.frameIdx):
       
        figobjs = [] # this is used to collect up all the axis objects so that they can be deleted after each iteration
        
        hobjs = pitch.scatter(hometeam.loc[hometeam["frameIdx"]==i].x,
                    hometeam.loc[hometeam["frameIdx"]==i].y, 
                    ax=ax, 
                    edgecolor='black', # Edge color of the point
                    c=hometeam.loc[hometeam["frameIdx"]==i].GK, # Color of the point
                    s=250, # Size of the points
                    cmap='autumn' #Color map - field players will be green and keeper grey
                    ) # plot player positions
        # hobjs.set_offsets(np.array([hometeam.loc[hometeam["frameIdx"]==i].x, hometeam.loc[hometeam["frameIdx"]==i].y]))
        figobjs.append(hobjs)
        
        aobjs = pitch.scatter(awayteam.loc[awayteam["frameIdx"]==i].x,
                    awayteam.loc[awayteam["frameIdx"]==i].y, 
                    ax=ax, # What plot to add them to 
                    edgecolor='black', # Edge color of the point
                    c=awayteam.loc[awayteam["frameIdx"]==i].GK, # Color of the point
                    s=250, # Size of the points
                    cmap='Set2' #Color map - field players will be green and keeper grey
                    ) # plot player positions

        # aobjs.set_offsets([awayteam.loc[awayteam["frameIdx"]==i].x, awayteam.loc[awayteam["frameIdx"]==i].y])
        figobjs.append(aobjs)
        
        bobjs = pitch.scatter(ball.loc[ball["frameIdx"]==i].xBall,
                        ball.loc[ball["frameIdx"]==i].yBall, 
                        ax=ax, # What plot to add them to 
                        edgecolor='black', # Edge color of the point
                        c='black', # Color of the point
                        s=100 # Size of the points
                        ) # plot player positions
        # bobjs.set_offsets([ball.loc[ball["frameIdx"]==i].xBall, ball.loc[ball["frameIdx"]==i].yBall])
        figobjs.append(bobjs)
        
        fname_temp = '_temp%03d.png' % i
#         print(fname_temp)
        plt.savefig(fname_temp, bbox_inches='tight')
        files.append(fname_temp)
        
        # Delete all axis objects (other than pitch lines) in preperation for next frame
        for figobj in figobjs:
            figobj.remove()
    
    plt.clf()
    plt.close(fig)   
    
    image = cv2.imread(fname_temp)
    (h, w) = image.shape[:2]
    fourcc = cv2.VideoWriter_fourcc('M', 'J', 'P', 'G')
    writer = cv2.VideoWriter(fname, fourcc, frames_per_second, (w, h), True)
    for fname in files:
        image = cv2.imread(fname)
        writer.write(image)

    # cleanup
    for fname in files:
        os.remove(fname)
    print("done") 


def save_match_clip_new(ball,hometeam,awayteam, fpath, fname='clip_test', figax=None, frames_per_second=25, team_colors=('r','b'), field_dimen = (105.0,68.0), PlayerMarkerSize=10, PlayerAlpha=0.7):
    """
    Generate a movie clip of a soccer match based on tracking data.
    
    Parameters
    ----------
    ball: pandas DataFrame
        Tracking data for the ball.
    hometeam: pandas DataFrame
        Tracking data for the home team.
    awayteam: pandas DataFrame
        Tracking data for the away team.
    fpath: str
        Directory to save the movie clip.
    fname: str
        Filename for the movie clip (default is 'clip_test').
    figax: tuple of matplotlib Figure and Axes
        Figure and axes to use for plotting (default is None, in which case a new figure and axes will be created).
    frames_per_second: int
        Frame rate for the movie clip (default is 25).
    team_colors: tuple of str
        Colors to use for the home and away teams (default is ('r','b')).
    field_dimen: tuple of float
        Length and width of the soccer pitch in meters (default is (105.0,68.0)).
    PlayerMarkerSize: float
        Size of the markers for the player positions (default is 10).
    PlayerAlpha: float
        Transparency of the markers
    """
    
    # Set index variable to index of hometeam DataFrame
    index = hometeam.index
    
    # Initialize fname with file path and filename for movie clip
    fname = fpath + '/' +  fname + '.mp4'
    # Create pitch
    if figax is None:
        pitch = Pitch(pitch_type='secondspectrum', # Using second spectrum to fit with tracking data
              pitch_width=68, pitch_length=105, # Setting pitch size to danish standard
              goal_type='box', # Add "nets" to goals
              pitch_color='grass', # Setting the color to be grass 
              line_color='white',  # Setting the lines on the pitch to be white
              stripe=True, # Add stripes to the grass color
              corner_arcs=True, # Add corner arcs
             )

        fig, ax = pitch.draw(figsize=(105/6.562,68/6.562))
    else:
    # Set fig and ax to figax tuple
        fig, ax = figax
    
    # Adjust subplot parameters to give specified padding
    fig.set_tight_layout(True)
    
    hobjs = pitch.scatter([],
                      [], 
                      ax=ax, 
                      edgecolor='black', # Edge color of the point
                      c=hometeam.loc[hometeam["frameIdx"]==0].GK, # Color of the point
                      s=250, # Size of the points
                      cmap='autumn' #Color map - field players will be green and keeper grey
                     ) # plot player positions
    
    aobjs = pitch.scatter([],
                      [], 
                      ax=ax, # What plot to add them to 
                      edgecolor='black', # Edge color of the point
                      c=awayteam.loc[awayteam["frameIdx"]==0].GK, # Color of the point
                      s=250, # Size of the points
                      cmap='Set2' #Color map - field players will be green and keeper grey
                     ) # plot player positions
    
    # plot ball
    bobjs = pitch.scatter([],
                          [], 
                          ax=ax, # What plot to add them to 
                          edgecolor='black', # Edge color of the point
                          c='black', # Color of the point
                          s=100 # Size of the points
                         ) # plot player positions

    # Set up formatting for the movie files
    away = np.array(hometeam[['x', 'y']]).reshape(-1, 11, 2)
    home = np.array(awayteam[['x', 'y']]).reshape(-1, 11, 2)
    ball = np.array(ball[['xBall', 'yBall']]).reshape(-1, 1, 2)
    
    # Generate movie
    print("Generating movie...",end='')
    files = []
    for count, (a, h, b) in tqdm(enumerate(zip(away, home, ball)), total=len(away)):
       
        figobjs = [] # this is used to collect up all the axis objects so that they can be deleted after each iteration
        
        # hobjs = pitch.scatter(hometeam.loc[hometeam["frameIdx"]==i].x,
        #             hometeam.loc[hometeam["frameIdx"]==i].y, 
        #             ax=ax, 
        #             edgecolor='black', # Edge color of the point
        #             c=hometeam.loc[hometeam["frameIdx"]==i].GK, # Color of the point
        #             s=250, # Size of the points
        #             cmap='autumn' #Color map - field players will be green and keeper grey
        #             ) # plot player positions
        hobjs.set_offsets(h)
        figobjs.append(hobjs)
        
        # aobjs = pitch.scatter(awayteam.loc[awayteam["frameIdx"]==i].x,
        #             awayteam.loc[awayteam["frameIdx"]==i].y, 
        #             ax=ax, # What plot to add them to 
        #             edgecolor='black', # Edge color of the point
        #             c=awayteam.loc[awayteam["frameIdx"]==i].GK, # Color of the point
        #             s=250, # Size of the points
        #             cmap='Set2' #Color map - field players will be green and keeper grey
        #             ) # plot player positions

        aobjs.set_offsets(a)
        figobjs.append(aobjs)
        
        # bobjs = pitch.scatter(ball.loc[ball["frameIdx"]==i].xBall,
        #                 ball.loc[ball["frameIdx"]==i].yBall, 
        #                 ax=ax, # What plot to add them to 
        #                 edgecolor='black', # Edge color of the point
        #                 c='black', # Color of the point
        #                 s=100 # Size of the points
        #                 ) # plot player positions
        bobjs.set_offsets(b)
        figobjs.append(bobjs)
        
        fname_temp = '_temp%03d.png' % count
#         print(fname_temp)
        plt.savefig(fname_temp, bbox_inches='tight')
        files.append(fname_temp)
        
        # Delete all axis objects (other than pitch lines) in preperation for next frame
        # for figobj in figobjs:
        #     figobj.remove()
    
    plt.clf()
    plt.close(fig)   
    
    image = cv2.imread(fname_temp)
    (h, w) = image.shape[:2]
    fourcc = cv2.VideoWriter_fourcc('M', 'J', 'P', 'G')
    writer = cv2.VideoWriter(fname, fourcc, frames_per_second, (w, h), True)
    for fname in files:
        image = cv2.imread(fname)
        writer.write(image)

    # cleanup
    for fname in files:
        os.remove(fname)
    print("done") 
