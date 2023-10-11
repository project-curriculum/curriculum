import pandas as pd
import numpy as np
import os
import math

import matplotlib.pyplot as plt
import seaborn as sns


def johns_barplot(x, y, data, title, xlabel, hue=None, hue_order=None, hue_palette=None, single_color=None, sort_data=True, x_label_rotation=0, bar_font_size=12, figsize=(10, 6)):
    if sort_data:
        data_to_plot = data.sort_values(y, ascending=False)
    else:
        data_to_plot = data
    
    plt.figure(figsize=figsize)
    
    if single_color:
        ax = sns.barplot(x=x, y=y, hue=hue, hue_order=hue_order, data=data_to_plot, color=single_color)
    else:
        ax = sns.barplot(x=x, y=y, hue=hue, hue_order=hue_order, palette=hue_palette, data=data_to_plot)
    
    ax.set(yticklabels=[])
    ax.yaxis.set_ticks_position('none')
    sns.despine(left=True, bottom=True)
    
    y_axis_height = ax.get_ylim()[1]
    
    for p in ax.patches:
        if p.get_height() < 1:
            ax.annotate(f'{p.get_height():.2f}', (p.get_x() + p.get_width() / 2., p.get_height() + (y_axis_height * 0.01)),
                        ha='center', va='baseline', fontsize=bar_font_size)
        elif p.get_height() < 1000:
            ax.annotate(f'{p.get_height():.0f}', (p.get_x() + p.get_width() / 2., p.get_height() + (y_axis_height * 0.01)),
                        ha='center', va='baseline', fontsize=bar_font_size)
        else:
            ax.annotate(f'{p.get_height()/1000:.1f}K', (p.get_x() + p.get_width() / 2., p.get_height() + (y_axis_height * 0.01)),
                        ha='center', va='baseline', fontsize=bar_font_size)
    
    plt.title(title, fontsize=12)
    plt.xlabel(xlabel, labelpad=20, fontsize=12)
    plt.ylabel('')
    plt.xticks(rotation=x_label_rotation)
    
    plt.show()


# Define the johns_barsubplot function for creating the bar subplot
def johns_barsubplot(ax, x, y, data, title, xlabel, hue=None, hue_order=None, hue_palette=None, single_color=None, sort_data=True, x_label_rotation=0, bar_font_size=12):
    if sort_data:
        data_to_plot = data.sort_values(y, ascending=False)
    else:
        data_to_plot = data
    
    if single_color:
        sns.barplot(x=x, y=y, hue=hue, hue_order=hue_order, data=data_to_plot, ax=ax, color=single_color)
    else:
        sns.barplot(x=x, y=y, hue=hue, hue_order=hue_order, palette=hue_palette, data=data_to_plot, ax=ax)
    
    ax.set(yticklabels=[])
    ax.yaxis.set_ticks_position('none')
    sns.despine(left=True, bottom=True)
    
    y_axis_height = ax.get_ylim()[1]
    
    for p in ax.patches:
        if p.get_height() < 1:
            ax.annotate(f'{p.get_height():.2f}', (p.get_x() + p.get_width() / 2., p.get_height() + (y_axis_height * 0.01)),
                        ha='center', va='baseline', fontsize=bar_font_size)
        elif p.get_height() < 1000:
            ax.annotate(f'{p.get_height():.0f}', (p.get_x() + p.get_width() / 2., p.get_height() + (y_axis_height * 0.01)),
                        ha='center', va='baseline', fontsize=bar_font_size)
        else:
            ax.annotate(f'{p.get_height()/1000:.1f}K', (p.get_x() + p.get_width() / 2., p.get_height() + (y_axis_height * 0.01)),
                        ha='center', va='baseline', fontsize=bar_font_size)
    
    ax.set_title(title, fontsize=12)
    ax.set_xlabel(xlabel, labelpad=20, fontsize=12)
    ax.set_ylabel('')
    ax.set_xticklabels(ax.get_xticklabels(), rotation=x_label_rotation)