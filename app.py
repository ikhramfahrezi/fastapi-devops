   import os
   import time
   import psycopg2
   from fastapi import FastAPI

   app = FastAPI()

   @app.get("/")
   def read_root():
       return {"message": "Halo dari DevOps Mini Project!"}

   @app.get("/db-check")
   def db_check():
       # Sleep 3 detik biar pasti database udah siap (Trik klasik DevOps!)
       time.sleep(3) 
       try:
           # Ambil konfigurasi database dari Environment Variables
           conn = psycopg2.connect(
               dbname=os.getenv("POSTGRES_DB"),
               user=os.getenv("POSTGRES_USER"),
               password=os.getenv("POSTGRES_PASSWORD"),
               host=os.getenv("POSTGRES_HOST"),
               port=os.getenv("POSTGRES_PORT")
           )
           cur = conn.cursor()
           cur.execute("SELECT version();")
           db_version = cur.fetchone()[0]
           cur.close()
           conn.close()
           return {"status": "Connected to Database!", "db_version": db_version}
       except Exception as e:
           return {"status": "Failed to connect", "error": str(e)}