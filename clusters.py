#Assigning clusters to form a portfolio for each new month 
def clusters(cl):
  cl['cluster'] = KMeans(n_clusters = 5, random_state=0, init = 'random').fit(cl).labels_
  return cl

