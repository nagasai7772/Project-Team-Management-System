from fastapi import FastAPI

app=FastAPI(title="Project & Team Management API",version="1.0.0",description="API for managing workspaces, projects, teams, and tasks.")


@app.get("/")
def root():
    return {"message":"Project & Team Management API is running"}
@app.get("/health")
def health():
    return {"status":"Server API is Healthy"}
