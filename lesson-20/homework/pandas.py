import pandas as pd
import numpy as np
import sqlite3

try:
    
    conn = sqlite3.connect('Chinook_Sqlite.sqlite')
    # Create SQL Queries 
    query = 'Select * from Customer'
    query_invoice = 'Select * from Invoice'
    # query_invoice_line = 'Select * from InvoiceLine'
except:
    print("Database Error")    


customer_df = pd.read_sql(query, conn)
invoice = pd.read_sql(query_invoice, conn)
# invoice_line = pd.read_sql(query_invoice_line, conn)   


customer_df = pd.read_sql(query, conn)
invoice = pd.read_sql(query_invoice, conn)
# invoice_line = pd.read_sql(query_invoice_line, conn)


# Merging tables invoice and Customer
merged_df = pd.merge(invoice, customer_df, on='CustomerId')
# Grouping and summing total 
customer_total_amount = merged_df.groupby('CustomerId')['Total'].sum().reset_index()
print(customer_total_amount)

# Task 1-2
top_customers = customer_total_amount.sort_values(by='Total', ascending= False).head()
top_5_customer = pd.merge(customer_df, top_customers, on='CustomerId')
print(top_5_customer)

# Task 1-3 Display the customer ID, name, and the total amount spent for the top 5 customers.
result = pd.merge(customer_df, top_customers, on='CustomerId', how='right')
result['name'] = result['FirstName'] + ' ' + result['LastName']
final_result = result[['CustomerId', 'name', 'Total']]
print(final_result)

# Task 2-1 Album vs. Individual Track Purchases:
# Determine the percentage of customers who prefer to buy individual tracks instead of full albums

# Merge invoice_line with track to get AlbumId for each purchased track
line_with_album = pd.merge(invoice_line, track[['TrackId', 'AlbumId']], on='TrackId')

# Count total tracks per album
tracks_per_album = track.groupby('AlbumId')['TrackId'].count().reset_index()
tracks_per_album.rename(columns={'TrackId': 'TotalTracks'}, inplace= True)

# Counts tracks bought per invoice per album
purchased_per_invoice = line_with_album.groupby(['InvoiceId', 'AlbumId'])['TrackId'].count().reset_index()
purchased_per_invoice.rename(columns={'TrackId': 'PurchasedTracks'}, inplace=True)

# Merge to get total available tracks for that album
merged = pd.merge(purchased_per_invoice, tracks_per_album, on='AlbumId')

# Determine if full album was bought
merged['IsFullAlbum'] = merged['PurchasedTracks'] == merged['TotalTracks']

# If any album on an invoice is a full album, we consider the invoice a full album purchase
album_vs_track = merged.groupby('InvoiceId')['IsFullAlbum'].any().reset_index()

# Now, join with invoice to get CustomerId
album_vs_track = pd.merge(album_vs_track, invoice[['InvoiceId', 'CustomerId']], on='InvoiceId')

# Determine customer preference: if a customer has **only individual track invoices**
pref_type = album_vs_track.groupby('CustomerId')['IsFullAlbum'].any().reset_index()
pref_type['PrefersIndividualTracks'] = ~pref_type['IsFullAlbum']

# Calculate percentage
total_customers = pref_type.shape[0]
individual_pref_customers = pref_type['PrefersIndividualTracks'].sum()
percentage = (individual_pref_customers / total_customers) * 100

print(f"Percentage of customers who prefer individual tracks: {percentage:.2f}%")

# Task 2-2 A customer is considered to prefer individual tracks if they have purchased only a subset of tracks from an album.
# Get AlbumId with each purchase
line_with_album = pd.merge(invoice_line, track[['TrackId', 'AlbumId']], on='TrackId')

# Total track per in album
album_track_counts = track.groupby('AlbumId')['TrackId'].nunique().reset_index()
album_track_counts.rename(columns={'TrackId': 'TotalTracks'}, inplace=True)

# Tracks bought per invoice per album
invoice_album_counts = line_with_album.groupby(['InvoiceId', 'AlbumId'])['TrackId'].nunique().reset_index()
invoice_album_counts.rename(columns={'TrackId': 'PurchasedTracks'}, inplace=True)

# Compare to find if its a full album purchase
merged_counts = pd.merge(invoice_album_counts, album_track_counts, on='AlbumId')
merged_counts['IsFullAlbumPurchase'] = merged_counts['PurchasedTracks'] == merged_counts['TotalTracks']

# link invoices to customer
invoice_customer = invoice[['InvoiceId', 'CustomerId']]
merged_counts = pd.merge(merged_counts, invoice_customer, on='InvoiceId')

# For each customer, Check if they ever made a full album purchase
customer_album_pref = merged_counts.groupby('CustomerId')['IsFullAlbumPurchase'].any().reset_index()
customer_album_pref['PrefersIndividualTracks'] = ~customer_album_pref['IsFullAlbumPurchase']

# Calculate percentage
total_customers = customer_album_pref.shape[0]
individual_only_customers = customer_album_pref['PrefersIndividualTracks'].sum()
percentage = (individual_only_customers / total_customers) * 100

print(f"Percentage of customers who prefer individual tracks: {percentage:.2f}%")


# Task 2-3 Provide a summary of the percentage of customers who fall into each category (individual tracks vs. full albums).
# Count number of customers in each category
summary_counts = customer_album_pref['PrefersIndividualTracks'].value_counts().rename(index={True: 'Individual Tracks', False: 'Full Albums'})

# Convert to DataFrame
summary_df = summary_counts.reset_index()
summary_df.columns = ['PurchasePreference', 'CustomerCount']

# Calculate percentage
total_customers = summary_df['CustomerCount'].sum()
summary_df['Percentage'] = (summary_df['CustomerCount'] / total_customers * 100).round(2)

# Display summary
print(summary_df)
