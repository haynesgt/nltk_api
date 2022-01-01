# Note that to set a default region you can do:
# gcloud set config builds/region $REGION
# gcloud set config run/region $REGION
gcloud run deploy --source=./ nltk-api --allow-unauthenticated
