import os
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from adjustText import adjust_text
import pandas as pd
from scipy.stats import fisher_exact
from IPython.display import display
from matplotlib.legend import Legend
from matplotlib.transforms import Bbox
from brokenaxes import brokenaxes


from matplotlib.gridspec import GridSpec


def custom_volcano_plot(data_path, metadata_path, metadata_column='tagm_location',
                        point_size=50, figsize=20, threshold=0,
                        save_path=None, x_lim=[-0.5, 0.5], y_lims=[[0, 6], [9, 15]]):
    
    markers = [
        'o',  # Circle
        'X',  # X-shaped marker
        '^',  # Upward triangle
        's',  # Square
        'v',  # Downward triangle
        'P',  # Plus-filled pentagon
        '*',  # Star
        '+',  # Plus
        'x',  # Cross
        '.',  # Point
        ',',  # Pixel
        'd',  # Diamond
        'D',  # Thin diamond
        'h',  # Hexagon 1
        'H',  # Hexagon 2
        'p',  # Pentagon
        '|',  # Vertical line
        '_',  # Horizontal line
    ]
    
    plt.rcParams.update({'font.size': 14})

    # Load data
    if isinstance(data_path, pd.DataFrame):
        data = data_path
    else:
        data = pd.read_csv(data_path)

    fontsize = 18

    plt.rcParams.update({'font.size': fontsize})
    data['variable'] = data['feature'].str.extract(r'\[(.*?)\]')
    data['variable'].fillna(data['feature'], inplace=True)
    data['gene_nr'] = data['variable'].str.split('_').str[0]
    data = data[data['variable'] != 'Intercept']

    # Load metadata
    if isinstance(metadata_path, pd.DataFrame):
        metadata = metadata_path
    else:
        metadata = pd.read_csv(metadata_path)
    metadata['gene_nr'] = metadata['gene_nr'].astype(str)
    data['gene_nr'] = data['gene_nr'].astype(str)

    merged_data = pd.merge(data, metadata[['gene_nr', metadata_column]], on='gene_nr', how='left')
    merged_data[metadata_column].fillna('unknown', inplace=True)

    # Define palette and markers
    palette = {'pc': 'red', 'nc': 'green', 'control': 'white', 'other': 'gray'}
    marker_dict = {val: marker for val, marker in zip(
        merged_data[metadata_column].unique(), markers)}

    # Create the figure with custom spacing
    fig = plt.figure(figsize=(figsize,figsize))
    gs = GridSpec(2, 1, height_ratios=[1, 3], hspace=0.05)

    ax_upper = fig.add_subplot(gs[0])
    ax_lower = fig.add_subplot(gs[1], sharex=ax_upper)

    # Hide x-axis labels on the upper plot
    ax_upper.tick_params(axis='x', which='both', bottom=False, labelbottom=False)

    hit_list = []

    # Scatter plot on both axes
    for _, row in merged_data.iterrows():
        y_val = -np.log10(row['p_value'])
        ax = ax_upper if y_val > y_lims[1][0] else ax_lower

        ax.scatter(
            row['coefficient'], y_val,
            color=palette.get(row['condition'], 'gray'),
            marker=marker_dict.get(row[metadata_column], 'o'),
            s=point_size, edgecolor='black', alpha=0.6
        )

        if row['p_value'] <= 0.05 and abs(row['coefficient']) >= abs(threshold):
            hit_list.append(row['variable'])

    # Set axis limits
    ax_upper.set_ylim(y_lims[1])
    ax_lower.set_ylim(y_lims[0])
    ax_lower.set_xlim(x_lim)

    ax_lower.spines['top'].set_visible(False)
    ax_upper.spines['top'].set_visible(False)
    ax_upper.spines['bottom'].set_visible(False)

    # Set x-axis and y-axis titles
    ax_lower.set_xlabel('Coefficient')  # X-axis title on the lower graph
    ax_lower.set_ylabel('-log10(p-value)')  # Y-axis title on the lower graph
    ax_upper.set_ylabel('-log10(p-value)')  # Y-axis title on the upper graph
    
    for ax in [ax_upper, ax_lower]:
        ax.spines['right'].set_visible(False)

    # Add threshold lines to both axes
    for ax in [ax_upper, ax_lower]:
        ax.axvline(x=-abs(threshold), linestyle='--', color='black')
        ax.axvline(x=abs(threshold), linestyle='--', color='black')

    ax_lower.axhline(y=-np.log10(0.05), linestyle='--', color='black')

    # Annotate significant points
    texts_upper, texts_lower = [], []  # Collect text annotations separately

    for _, row in merged_data.iterrows():
        y_val = -np.log10(row['p_value'])
        if row['p_value'] > 0.05 or abs(row['coefficient']) < abs(threshold):
            continue

        ax = ax_upper if y_val > y_lims[1][0] else ax_lower
        text = ax.text(row['coefficient'], y_val, row['variable'], 
                       fontsize=fontsize, ha='center', va='bottom')

        if ax == ax_upper:
            texts_upper.append(text)
        else:
            texts_lower.append(text)

    # Adjust text positions to avoid overlap
    adjust_text(texts_upper, ax=ax_upper, arrowprops=dict(arrowstyle='-', color='black'))
    adjust_text(texts_lower, ax=ax_lower, arrowprops=dict(arrowstyle='-', color='black'))

    # Add a single legend on the lower axis
    handles = [plt.Line2D([0], [0], marker=m, color='w', markerfacecolor='gray', markersize=10)
               for m in marker_dict.values()]
    labels = marker_dict.keys()
    ax_lower.legend(handles, 
                    labels, 
                    bbox_to_anchor=(1.05, 1), 
                    loc='upper left',
                    borderaxespad=0.25, 
                    labelspacing=2, 
                    handletextpad=0.25, 
                    markerscale=2, 
                    prop={'size': fontsize})


    # Save and show the plot
    if save_path:
        plt.savefig(save_path, format='pdf', bbox_inches='tight')
    plt.show()
    
    return hit_list

def go_term_enrichment_by_column(significant_df, metadata_path, go_term_columns=['Computed GO Processes', 'Curated GO Components', 'Curated GO Functions', 'Curated GO Processes']):
    """
    Perform GO term enrichment analysis for each GO term column and generate plots.

    Parameters:
    - significant_df: DataFrame containing the significant genes from the screen.
    - metadata_path: Path to the metadata file containing GO terms.
    - go_term_columns: List of columns in the metadata corresponding to GO terms.

    For each GO term column, this function will:
    - Split the GO terms by semicolons.
    - Count the occurrences of GO terms in the hits and in the background.
    - Perform Fisher's exact test for enrichment.
    - Plot the enrichment score vs -log10(p-value).
    """
    
    #significant_df['variable'].fillna(significant_df['feature'], inplace=True)
    #split_columns = significant_df['variable'].str.split('_', expand=True)
    #significant_df['gene_nr'] = split_columns[0]
    #gene_list = significant_df['gene_nr'].to_list()

    significant_df = significant_df.dropna(subset=['n_gene'])
    significant_df = significant_df[significant_df['n_gene'] != None]

    gene_list = significant_df['n_gene'].to_list()

    # Load metadata
    metadata = pd.read_csv(metadata_path)
    split_columns = metadata['Gene ID'].str.split('_', expand=True)
    metadata['gene_nr'] = split_columns[1]

    # Create a subset of metadata with only the rows that contain genes in gene_list (hits)
    hits_metadata = metadata[metadata['gene_nr'].isin(gene_list)]

    # Create a list to hold results from all columns
    combined_results = []

    for go_term_column in go_term_columns:
        # Initialize lists to store results
        go_terms = []
        enrichment_scores = []
        p_values = []

        # Split the GO terms in the entire metadata and hits
        metadata[go_term_column] = metadata[go_term_column].fillna('')
        hits_metadata[go_term_column] = hits_metadata[go_term_column].fillna('')

        all_go_terms = metadata[go_term_column].str.split(';').explode()
        hit_go_terms = hits_metadata[go_term_column].str.split(';').explode()

        # Count occurrences of each GO term in hits and total metadata
        all_go_term_counts = all_go_terms.value_counts()
        hit_go_term_counts = hit_go_terms.value_counts()

        # Perform enrichment analysis for each GO term
        for go_term in all_go_term_counts.index:
            total_with_go_term = all_go_term_counts.get(go_term, 0)
            hits_with_go_term = hit_go_term_counts.get(go_term, 0)

            # Calculate the total number of genes and hits
            total_genes = len(metadata)
            total_hits = len(hits_metadata)

            # Perform Fisher's exact test
            contingency_table = [[hits_with_go_term, total_hits - hits_with_go_term],
                                 [total_with_go_term - hits_with_go_term, total_genes - total_hits - (total_with_go_term - hits_with_go_term)]]
            
            _, p_value = fisher_exact(contingency_table)
            
            # Calculate enrichment score (hits with GO term / total hits with GO term)
            if total_with_go_term > 0 and total_hits > 0:
                enrichment_score = (hits_with_go_term / total_hits) / (total_with_go_term / total_genes)
            else:
                enrichment_score = 0.0

            # Store the results only if enrichment score is non-zero
            if enrichment_score > 0.0:
                go_terms.append(go_term)
                enrichment_scores.append(enrichment_score)
                p_values.append(p_value)

        # Create a results DataFrame for this GO term column
        results_df = pd.DataFrame({
            'GO Term': go_terms,
            'Enrichment Score': enrichment_scores,
            'P-value': p_values,
            'GO Column': go_term_column  # Track the GO term column for final combined plot
        })

        # Sort by enrichment score
        results_df = results_df.sort_values(by='Enrichment Score', ascending=False)

        # Append this DataFrame to the combined list
        combined_results.append(results_df)

        # Plot the enrichment results for each individual column
        plt.figure(figsize=(10, 6))
        
        # Create a scatter plot of Enrichment Score vs -log10(p-value)
        sns.scatterplot(data=results_df, x='Enrichment Score', y=-np.log10(results_df['P-value']), hue='GO Term', size='Enrichment Score', sizes=(50, 200))
        
        # Set plot labels and title
        plt.title(f'GO Term Enrichment Analysis for {go_term_column}')
        plt.xlabel('Enrichment Score')
        plt.ylabel('-log10(P-value)')
        
        # Move the legend to the right of the plot
        plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.)
        
        # Show the plot
        plt.tight_layout()  # Ensure everything fits in the figure area
        plt.show()

        # Optionally return or save the results for each column
        print(f'Results for {go_term_column}')

    # Combine results from all columns into a single DataFrame
    combined_df = pd.concat(combined_results)

    # Plot the combined results with text labels
    plt.figure(figsize=(12, 8))
    sns.scatterplot(data=combined_df, x='Enrichment Score', y=-np.log10(combined_df['P-value']),
                    style='GO Column', size='Enrichment Score', sizes=(50, 200))

    # Set plot labels and title for the combined graph
    plt.title('Combined GO Term Enrichment Analysis')
    plt.xlabel('Enrichment Score')
    plt.ylabel('-log10(P-value)')
    
    # Annotate the points with labels and connecting lines
    texts = []
    for i, row in combined_df.iterrows():
        texts.append(plt.text(row['Enrichment Score'], -np.log10(row['P-value']), row['GO Term'], fontsize=9))
    
    # Adjust text to avoid overlap
    adjust_text(texts, arrowprops=dict(arrowstyle='-', color='black'))
    
    # Show the combined plot
    plt.tight_layout()
    plt.show()

def plot_gene_phenotypes(data, gene_list, x_column='Gene ID', data_column='T.gondii GT1 CRISPR Phenotype - Mean Phenotype',error_column='T.gondii GT1 CRISPR Phenotype - Standard Error', save_path=None):
    """
    Plot a line graph for the mean phenotype with standard error shading and highlighted genes.
    
    Args:
        data (pd.DataFrame): The input DataFrame containing gene data.
        gene_list (list): A list of gene names to highlight on the plot.
    """
    # Ensure x_column is properly processed
    def extract_gene_id(gene):
        if isinstance(gene, str) and '_' in gene:
            return gene.split('_')[1]
        return str(gene)

    data.loc[:, data_column] = pd.to_numeric(data[data_column], errors='coerce')
    data = data.dropna(subset=[data_column])
    data.loc[:, error_column] = pd.to_numeric(data[error_column], errors='coerce')
    data = data.dropna(subset=[error_column])

    data['x'] = data[x_column].apply(extract_gene_id)
    
    # Sort by the data_column and assign ranks
    data = data.sort_values(by=data_column).reset_index(drop=True)
    data['rank'] = range(1, len(data) + 1)

    # Prepare the x, y, and error values for plotting
    x = data['rank']
    y = data[data_column]
    yerr = data[error_column]

    # Create the plot
    plt.figure(figsize=(10, 10))

    # Plot the mean phenotype with standard error shading
    plt.plot(x, y, label='Mean Phenotype', color=(0/255, 155/255, 155/255), linewidth=2)
    plt.fill_between(
        x, y - yerr, y + yerr, 
        color=(0/255, 155/255, 155/255), alpha=0.1, label='Standard Error'
    )

    # Prepare for adjustText
    texts = []  # Store text objects for adjustment

    # Highlight the genes in the gene_list
    for gene in gene_list:
        gene_id = extract_gene_id(gene)
        gene_data = data[data['x'] == gene_id]
        if not gene_data.empty:
            # Scatter the highlighted points in purple and add labels for adjustment
            plt.scatter(
                gene_data['rank'], 
                gene_data[data_column], 
                color=(155/255, 55/255, 155/255), 
                s=200,
                alpha=0.6,
                label=f'Highlighted Gene: {gene}',
                zorder=3  # Ensure the points are on top
            )
            # Add the text label next to the highlighted gene
            texts.append(
                plt.text(
                    gene_data['rank'].values[0], 
                    gene_data[data_column].values[0], 
                    gene, 
                    fontsize=18, 
                    ha='right'
                )
            )

    # Adjust text to avoid overlap with lines drawn from points to text
    adjust_text(texts, arrowprops=dict(arrowstyle='-', color='gray'))

    # Label the plot
    plt.xlabel('Rank')
    plt.ylabel('Mean Phenotype')
    #plt.xticks(rotation=90)  # Rotate x-axis labels for readability
    plt.legend().remove()  # Remove the legend if not needed
    plt.tight_layout()

    # Save the plot if a path is provided
    if save_path:
        plt.savefig(save_path, format='pdf', dpi=600, bbox_inches='tight')
        print(f"Figure saved to {save_path}")
    
    plt.show()

def plot_gene_heatmaps(data, gene_list, columns, x_column='Gene ID', normalize=False, save_path=None):
    """
    Generate a teal-to-white heatmap with the specified columns and genes.

    Args:
        data (pd.DataFrame): The input DataFrame containing gene data.
        gene_list (list): A list of genes to include in the heatmap.
        columns (list): A list of column names to visualize as heatmaps.
        normalize (bool): If True, normalize the values for each gene between 0 and 1.
        save_path (str): Optional. If provided, the plot will be saved to this path.
    """
    # Ensure x_column is properly processed
    def extract_gene_id(gene):
        if isinstance(gene, str) and '_' in gene:
            return gene.split('_')[1]
        return str(gene)

    data['x'] = data[x_column].apply(extract_gene_id)

    # Filter the data to only include the specified genes
    filtered_data = data[data['x'].isin(gene_list)].set_index('x')[columns]

    # Normalize each gene's values between 0 and 1 if normalize=True
    if normalize:
        filtered_data = filtered_data.apply(lambda x: (x - x.min()) / (x.max() - x.min()), axis=1)

    # Define the figure size dynamically based on the number of genes and columns
    width = len(columns) * 4
    height = len(gene_list) * 1

    # Create the heatmap
    plt.figure(figsize=(width, height))
    cmap = sns.color_palette("viridis", as_cmap=True)

    # Plot the heatmap with genes on the y-axis and columns on the x-axis
    sns.heatmap(
        filtered_data, 
        cmap=cmap, 
        cbar=True, 
        annot=False, 
        linewidths=0.5, 
        square=True
    )

    # Set the labels
    plt.xticks(rotation=90, ha='center')  # Rotate x-axis labels for better readability
    plt.yticks(rotation=0)  # Keep y-axis labels horizontal
    plt.xlabel('')
    plt.ylabel('')

    # Adjust layout to ensure the plot fits well
    plt.tight_layout()

    # Save the plot if a path is provided
    if save_path:
        plt.savefig(save_path, format='pdf', dpi=600, bbox_inches='tight')
        print(f"Figure saved to {save_path}")

    plt.show()